"""empty message

Revision ID: 2217e6132010
Revises: c8b98e88f5a8
Create Date: 2023-10-05 16:29:04.377177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2217e6132010'
down_revision = 'c8b98e88f5a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredient', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('state', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('test', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_column('test')
        batch_op.drop_column('state')
        batch_op.drop_column('ingredient')

    # ### end Alembic commands ###
