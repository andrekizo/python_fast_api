"""Add content column to posts table.

Revision ID: 7ce98a58ed5f
Revises: 317d0716198d
Create Date: 2023-01-16 07:17:12.370954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ce98a58ed5f'
down_revision = '317d0716198d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.add_column('posts',sa.Column('content',sa.String(200),nullable=False))
    pass


def downgrade() -> None:
    # op.drop_column('posts','content')
    pass
