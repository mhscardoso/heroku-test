"""empty message

Revision ID: 899cc8aed09d
Revises: ecb4aaaa64ed
Create Date: 2022-08-08 16:07:36.846029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '899cc8aed09d'
down_revision = 'ecb4aaaa64ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=15), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
