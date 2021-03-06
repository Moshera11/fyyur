"""empty message

Revision ID: d899ff1f61b7
Revises: e577cc2e8086
Create Date: 2020-12-21 11:19:52.771050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd899ff1f61b7'
down_revision = 'e577cc2e8086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('state', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('area_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'state')
    op.drop_column('Venue', 'city')
    # ### end Alembic commands ###
