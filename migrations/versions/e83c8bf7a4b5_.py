"""empty message

Revision ID: e83c8bf7a4b5
Revises: 6b2ad88d0aa8
Create Date: 2023-09-27 16:52:55.173883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e83c8bf7a4b5'
down_revision = '6b2ad88d0aa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=300), nullable=True))

    # ### end Alembic commands ###
