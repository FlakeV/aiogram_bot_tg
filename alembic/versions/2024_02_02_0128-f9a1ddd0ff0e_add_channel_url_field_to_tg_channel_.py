"""add channel_url field to tg_channel table

Revision ID: f9a1ddd0ff0e
Revises: bb5ef8bae8ae
Create Date: 2024-02-02 01:28:04.277021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9a1ddd0ff0e'
down_revision: Union[str, None] = 'bb5ef8bae8ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tgchannels', sa.Column('channel_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tgchannels', 'channel_url')
    # ### end Alembic commands ###
