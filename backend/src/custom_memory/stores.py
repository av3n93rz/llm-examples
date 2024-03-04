from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa
import uuid
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector


# declarative base class
class Base(DeclarativeBase):
    pass


# Conversation table mapping using the base
class ConversationStore(Base):
    __tablename__ = "conversation"

    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.TEXT)
    user_id = sa.Column(sa.VARCHAR)
    created_at = sa.Column(sa.TIMESTAMP, server_default=sa.text("now()"))

    @classmethod
    def get_by_id_and_user_id(
        cls, session: Session, id: uuid.UUID, user_id: str
    ) -> Optional["ConversationStore"]:
        return (
            session.query(cls)
            .filter(sa.and_(cls.id == id, cls.user_id == user_id))
            .first()
        )

    @classmethod
    def get_by_id(
        cls, session: Session, id: uuid.UUID
    ) -> Optional["ConversationStore"]:
        return session.query(cls).filter(cls.id == id).first()


# Message table mapping using the base
class MessageStore(Base):
    __tablename__ = "message"

    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = sa.Column(sa.ForeignKey(f"{ConversationStore.__tablename__}.id"))
    embedding = sa.Column(Vector(None), nullable=False)
    input = sa.Column(sa.TEXT)
    output = sa.Column(sa.TEXT)
    created_at = sa.Column(sa.TIMESTAMP, server_default=sa.text("now()"))
