"""adding cc_judgment_modifications table

Revision ID: b279918a6f75
Revises: 233cfe62cd05
Create Date: 2018-05-21 06:21:55.476908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b279918a6f75'
down_revision = '233cfe62cd05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cc_judgment_modifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judgment_id', sa.Integer(), nullable=True),
    sa.Column('judgment_against', sa.String(), nullable=True),
    sa.Column('judgment_for', sa.String(), nullable=True),
    sa.Column('entered_date', sa.Date(), nullable=True),
    sa.Column('entered_date_str', sa.String(), nullable=True),
    sa.Column('amount', sa.Numeric(), nullable=True),
    sa.Column('status_date', sa.Date(), nullable=True),
    sa.Column('status_date_str', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['judgment_id'], ['cc_judgments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('cc_judgments', sa.Column('judgment_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cc_judgments', 'judgment_type')
    op.drop_table('cc_judgment_modifications')
    # ### end Alembic commands ###
