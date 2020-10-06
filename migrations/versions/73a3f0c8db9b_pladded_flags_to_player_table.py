"""pladded flags to player table

Revision ID: 73a3f0c8db9b
Revises: 1355328f75bc
Create Date: 2020-10-06 18:12:17.528997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73a3f0c8db9b'
down_revision = '1355328f75bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('flags', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'flags')
    # ### end Alembic commands ###