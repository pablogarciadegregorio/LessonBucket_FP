"""empty message

Revision ID: c91a9c1be012
Revises: 22b13b02c848
Create Date: 2023-09-25 09:14:38.294115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c91a9c1be012'
down_revision = '22b13b02c848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('birth_date',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('birth_date',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###
