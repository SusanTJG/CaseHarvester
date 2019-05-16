"""Add odytraf_services table

Revision ID: 5f3daa92e736
Revises: 9d335febaed3
Create Date: 2019-05-16 16:00:51.656823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3daa92e736'
down_revision = '9d335febaed3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('odytraf_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type', sa.String(), nullable=False),
    sa.Column('requested_by', sa.String(), nullable=True),
    sa.Column('issued_date', sa.Date(), nullable=True),
    sa.Column('issued_date_str', sa.String(), nullable=True),
    sa.Column('service_status', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['odytraf.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_odytraf_services_case_number'), 'odytraf_services', ['case_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_odytraf_services_case_number'), table_name='odytraf_services')
    op.drop_table('odytraf_services')
    # ### end Alembic commands ###
