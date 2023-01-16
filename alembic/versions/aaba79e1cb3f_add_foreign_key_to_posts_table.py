"""add foreign key to posts table

Revision ID: aaba79e1cb3f
Revises: bb359099b2fc
Create Date: 2023-01-16 07:40:02.152995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaba79e1cb3f'
down_revision = 'bb359099b2fc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'], ondelete="NO ACTION")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts", type_="foreignkey")
    op.drop_column('posts','owner_id')
    pass
