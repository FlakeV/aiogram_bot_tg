"""create tg chanel table

Revision ID: bb5ef8bae8ae
Revises: 5701ac09e596
Create Date: 2024-02-01 00:47:46.055729

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bb5ef8bae8ae"
down_revision: Union[str, None] = "396fb425f633"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tgchannels",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("tg_id", sa.BigInteger(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tgchannels_id"), "tgchannels", ["id"], unique=False)
    op.create_index(op.f("ix_tgchannels_tg_id"), "tgchannels", ["tg_id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tgchannels_tg_id"), table_name="tgchannels")
    op.drop_index(op.f("ix_tgchannels_id"), table_name="tgchannels")
    op.drop_table("tgchannels")
    # ### end Alembic commands ###
