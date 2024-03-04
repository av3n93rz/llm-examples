from .db_connection import DB
import logging
from typing import Any, Optional, List
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
import uuid
import datetime


class CustomCombinedMemory:
    def __init__(
        self,
        connection_string: str,
        embedding_function: Embeddings,
        logger: Optional[logging.Logger] = None,
        *,
        engine_args: Optional[dict[str, Any]] = None,
    ) -> None:
        self.connection_string = connection_string
        self.embedding_function = embedding_function
        self.logger = logger or logging.getLogger(__name__)
        self.engine_args = engine_args or {}
        self._store = DB(
            connection_string=self.connection_string,
            embedding_function=self.embedding_function,
            engine_args=self.engine_args,
            logger=self.logger,
        )

    def concat_documents(self, documents: List[Document]) -> str:
        return "\n".join([document.page_content for document in documents])

    def _create_document(
        self, input: str, output: str, created_at: datetime.datetime
    ) -> Document:
        return Document(
            page_content="Human: "
            + input
            + "\n"
            + "AI: "
            + output
            + "\n"
            + "date of conversation: "
            + created_at.strftime("%Y-%m-%d %H:%M:%S")
        )

    def get_relevant_documents(
        self, query: str, conversation_id: str, k: int = 5
    ) -> List[Document]:
        relevant_docs = self._store.get_relevant_documents(
            query=query, conversation_id=conversation_id
        )
        return [
            self._create_document(
                input=doc.MessageStore.input,
                output=doc.MessageStore.output,
                created_at=doc.MessageStore.created_at,
            )
            for doc in relevant_docs
        ]

    def get_short_term_memory(self, conversation_id: str, k: int = 5) -> List[Document]:
        last_messages = self._store.get_short_term_memory(
            conversation_id=conversation_id, k=k
        )

        docs = [
            self._create_document(
                input=message.input,
                output=message.output,
                created_at=message.created_at,
            )
            for message in last_messages
        ]

        docs.reverse()

        return docs

    def save_conversation(
        self, user_id: str, conversation_id: uuid.UUID, input: str, output: str
    ) -> None:
        self._store.add_message(
            user_id=user_id, conversation_id=conversation_id, input=input, output=output
        )

    def check_user_access(self, user_id: str, conversation_id: uuid.UUID) -> bool:
        conversation = self._store.get_conversation_by_id(
            conversation_id=conversation_id
        )

        # If the conversation exists and belongs to a different user we return False
        if conversation is not None and conversation.user_id != user_id:
            return False
        else:
            return True
