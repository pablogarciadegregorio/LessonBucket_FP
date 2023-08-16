"""empty message

Revision ID: 8e8abe929e13
Revises: e32641b2ce91
Create Date: 2023-08-16 09:16:38.711131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8abe929e13'
down_revision = 'e32641b2ce91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text_content', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('goal', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('birth_date', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('address', sa.String(length=200), nullable=False))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('address')
        batch_op.drop_column('birth_date')
        batch_op.drop_column('name')

    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('comments')
    # ### end Alembic commands ###
