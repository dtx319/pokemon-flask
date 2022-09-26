"""empty message

Revision ID: 8d56d8f70604
Revises: 0e1d1663b8dd
Create Date: 2022-09-25 18:15:49.195858

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8d56d8f70604'
down_revision = '0e1d1663b8dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=1200), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('car')
    op.add_column('user', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'date_created')
    op.create_table('car',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('selling_price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='car_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='car_pkey')
    )
    op.drop_table('pokemon')
    # ### end Alembic commands ###