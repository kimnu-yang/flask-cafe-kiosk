"""empty message

Revision ID: c8b98e88f5a8
Revises: 978b0e26bbae
Create Date: 2023-10-05 16:24:24.917988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8b98e88f5a8'
down_revision = '978b0e26bbae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredient', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('state', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_column('state')
        batch_op.drop_column('ingredient')

    op.drop_table('inventory')
    # ### end Alembic commands ###