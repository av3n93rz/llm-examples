"""initial

Revision ID: 3cae33950f7b
Revises: 
Create Date: 2024-03-01 14:41:47.865889

"""

import uuid
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = "3cae33950f7b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.text("CREATE EXTENSION IF NOT EXISTS vector;"))

    op.create_table(
        "conversation",
        sa.Column("id", sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column("title", sa.TEXT, nullable=False),
        sa.Column("user_id", sa.VARCHAR, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.text("now()")),
    )

    op.create_table(
        "message",
        sa.Column("id", sa.UUID, primary_key=True, default=uuid.uuid4),
        sa.Column("conversation_id", sa.UUID, sa.ForeignKey("conversation.id")),
        sa.Column("embedding", Vector(None), nullable=False),
        sa.Column("input", sa.TEXT, nullable=False),
        sa.Column("output", sa.TEXT, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, server_default=sa.text("now()")),
    )

    op.create_foreign_key(
        constraint_name="conversation_id_fk",
        source_table="message",
        referent_table="conversation",
        local_cols=["conversation_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_table("message")
    op.drop_table("conversation")
