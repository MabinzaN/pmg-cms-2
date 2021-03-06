"""Drop copy pasta constraint

Revision ID: 3c2b8a62b3f5
Revises: 3160b5df63b4
Create Date: 2016-08-31 15:48:46.735667

"""

# revision identifiers, used by Alembic.
revision = '3c2b8a62b3f5'
down_revision = '3160b5df63b4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'fk_soundcloud_track_file_id_file', 'soundcloud_track', type_='foreignkey')
    op.create_foreign_key(op.f('fk_soundcloud_track_file_id_file'), 'soundcloud_track', 'file', ['file_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_soundcloud_track_file_id_file'), 'soundcloud_track', type_='foreignkey')
    op.create_foreign_key(u'fk_soundcloud_track_file_id_file', 'soundcloud_track', 'file', ['file_id'], ['id'], ondelete=u'CASCADE')
    ### end Alembic commands ###
