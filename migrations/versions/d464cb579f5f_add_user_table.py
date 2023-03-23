"""Add user table

Revision ID: d464cb579f5f
Revises: 
Create Date: 2023-03-23 03:20:35.787089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd464cb579f5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
