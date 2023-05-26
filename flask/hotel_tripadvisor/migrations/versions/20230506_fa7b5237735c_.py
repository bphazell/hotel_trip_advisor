"""empty message

Revision ID: fa7b5237735c
Revises: 48a2deecc61b
Create Date: 2023-05-06 11:04:20.461048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa7b5237735c'
down_revision = '48a2deecc61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('member_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('guest_id', sa.Integer(), nullable=False),
    sa.Column('join_date', sa.DateTime(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['guest_id'], ['guests.guest_id'], ),
    sa.PrimaryKeyConstraint('member_id'),
    sa.UniqueConstraint('guest_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    # ### end Alembic commands ###
