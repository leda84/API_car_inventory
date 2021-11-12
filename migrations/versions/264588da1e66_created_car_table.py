"""Created Car table

Revision ID: 264588da1e66
Revises: 3144b1855fe9
Create Date: 2021-11-10 23:02:14.276992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264588da1e66'
down_revision = '3144b1855fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('make', sa.String(length=150), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('max_speed', sa.String(length=100), nullable=True),
    sa.Column('series', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('car')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.Column('make', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('max_speed', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('series', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='car_user_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='car_pkey')
    )
    op.drop_table('car')
    # ### end Alembic commands ###
