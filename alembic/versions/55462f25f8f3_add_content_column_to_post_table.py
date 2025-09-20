"""add content column to post table

Revision ID: 55462f25f8f3
Revises: 2e1e372714a5
Create Date: 2025-09-20 11:19:59.165354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55462f25f8f3'
down_revision: Union[str, Sequence[str], None] = '2e1e372714a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
