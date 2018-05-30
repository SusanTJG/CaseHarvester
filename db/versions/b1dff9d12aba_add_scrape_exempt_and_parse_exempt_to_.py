"""add scrape_exempt and parse_exempt to cases table

Revision ID: b1dff9d12aba
Revises: eee1ab2826c0
Create Date: 2018-05-21 15:26:29.131748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1dff9d12aba'
down_revision = 'eee1ab2826c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases', sa.Column('parse_exempt', sa.Boolean(), nullable=True))
    op.add_column('cases', sa.Column('scrape_exempt', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cases', 'scrape_exempt')
    op.drop_column('cases', 'parse_exempt')
    # ### end Alembic commands ###