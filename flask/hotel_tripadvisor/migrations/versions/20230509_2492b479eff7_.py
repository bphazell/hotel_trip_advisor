"""empty message

Revision ID: 2492b479eff7
Revises: 01340b70acd3
Create Date: 2023-05-09 08:28:35.169455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2492b479eff7'
down_revision = '01340b70acd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('members', 'username',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('members', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('members', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('members', 'username',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###
