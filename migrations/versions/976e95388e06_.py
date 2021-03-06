"""empty message

Revision ID: 976e95388e06
Revises: 88d5354c22ec
Create Date: 2020-12-20 07:23:12.930070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '976e95388e06'
down_revision = '88d5354c22ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Venue', sa.Column('area_state_city', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Venue', 'area', ['area_state_city'], ['id'])
    op.drop_column('Venue', 'city')
    op.drop_column('Venue', 'state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'area_state_city')
    op.drop_table('area')
    # ### end Alembic commands ###
