"""empty message

Revision ID: ee696cb49d51
Revises: d899ff1f61b7
Create Date: 2020-12-21 11:24:33.606112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee696cb49d51'
down_revision = 'd899ff1f61b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'area_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('area_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
