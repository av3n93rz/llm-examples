import contextlib
import logging
from typing import Any, Generator, Optional, List
import sqlalchemy as sa
from sqlalchemy.orm import Session
from .stores import ConversationStore, MessageStore
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
import uuid


class DB:
    def __init__(
        self,
        connection_string: str,
        embedding_function: Embeddings,
        logger: Optional[logging.Logger] = None,
        *,
        connection: Optional[sa.engine.Connection] = None,
        engine_args: Optional[dict[str, Any]] = None,
    ) -> None:
        self.connection_string = connection_string
        self.embedding_function = embedding_function
        self.logger = logger or logging.getLogger(__name__)
        self.engine_args = engine_args or {}
        self._bind = connection if connection else self._create_engine()

    def __del__(self) -> None:
        if isinstance(self._bind, sa.engine.Connection):
            self._bind.close()

    def _create_engine(self) -> sa.engine.Engine:
        return sa.create_engine(url=self.connection_string, **self.engine_args)

    @contextlib.contextmanager
    def _make_session(self) -> Generator[Session, None, None]:
        """Create a context manager for the session, bind to _conn string."""
        yield Session(self._bind)

    def _create_embeddings(self, docs: List[str]) -> List[float]:
        return self.embedding_function.embed_documents(docs)[0]

    def add_message(
        self, user_id: str, conversation_id: uuid.UUID, input: str, output: str
    ) -> None:
        embeddings = self._create_embeddings([input, output])
        with Session(self._bind) as session:
            message = MessageStore(
                embedding=embeddings,
                input=input,
                output=output,
                conversation_id=conversation_id,
            )

            conversation = ConversationStore.get_by_id_and_user_id(
                user_id=user_id,
                session=session,
                id=conversation_id,
            )

            if conversation is None:
                conversation = ConversationStore(
                    user_id=user_id,
                    id=conversation_id,
                    title=input,
                )
                session.add_all([conversation, message])
            else:
                session.add(message)
            session.commit()

    def get_short_term_memory(self, conversation_id: str, k: int = 5) -> List[Document]:
        with Session(self._bind) as session:
            results: List[MessageStore] = (
                session.query(MessageStore)
                .filter(MessageStore.conversation_id == conversation_id)
                .order_by(sa.desc("created_at"))
                .limit(k)
                .all()
            )

        return results

    def get_relevant_documents(
        self, query: str, conversation_id: str, k: int = 5
    ) -> List[Document]:
        embedding = self.embedding_function.embed_query(text=query)
        with Session(self._bind) as session:
            filter_by = ConversationStore.id == conversation_id
            results: List[MessageStore] = (
                session.query(
                    MessageStore,
                    MessageStore.embedding.cosine_distance(embedding).label("distance"),  # type: ignore
                )
                .filter(filter_by)
                .order_by(sa.asc("distance"))
                .join(
                    ConversationStore,
                    MessageStore.conversation_id == ConversationStore.id,
                )
                .limit(k)
                .all()
            )
        return results

    def get_conversation_by_id(self, conversation_id: str) -> ConversationStore | None:
        with Session(self._bind) as session:
            conversation = ConversationStore.get_by_id(
                session=session,
                id=conversation_id,
            )
        return conversation
