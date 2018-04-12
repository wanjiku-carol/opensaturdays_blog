"""empty message

Revision ID: 47d859b74823
Revises: cf404c3497be
Create Date: 2018-04-12 17:01:57.394405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '47d859b74823'
down_revision = 'cf404c3497be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('date_created', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.drop_column('items', 'creation_date')
    op.add_column('todos', sa.Column('date_created', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'date_created')
    op.add_column('items', sa.Column('creation_date', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.drop_column('items', 'date_created')
    # ### end Alembic commands ###
