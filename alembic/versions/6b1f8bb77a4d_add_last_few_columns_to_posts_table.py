"""add last few columns to posts table

Revision ID: 6b1f8bb77a4d
Revises: 84581ef0268f
Create Date: 2025-09-20 12:16:40.823875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b1f8bb77a4d'
down_revision: Union[str, Sequence[str], None] = '84581ef0268f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'publshed', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
