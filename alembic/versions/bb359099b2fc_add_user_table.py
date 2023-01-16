"""add user table

Revision ID: bb359099b2fc
Revises: 7ce98a58ed5f
Create Date: 2023-01-16 07:23:32.388768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb359099b2fc'
down_revision = '7ce98a58ed5f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(50),nullable=False),
                    sa.Column('password',sa.String(50),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')

    pass
