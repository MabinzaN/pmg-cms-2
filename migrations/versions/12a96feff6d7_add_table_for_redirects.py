"""Add table for redirects.

Revision ID: 12a96feff6d7
Revises: 3fc4c97dc6bd
Create Date: 2015-01-28 08:24:32.778316

"""

# revision identifiers, used by Alembic.
revision = '12a96feff6d7'
down_revision = '3fc4c97dc6bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('redirect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('old_url', sa.String(length=250), nullable=False),
    sa.Column('new_url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_redirect_old_url', 'redirect', ['old_url'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_redirect_old_url', table_name='redirect')
    op.drop_table('redirect')
    ### end Alembic commands ###
