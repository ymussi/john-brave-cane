"""alter-table-partner

Revision ID: c8e326afd587
Revises: 359f9af686ae
Create Date: 2020-06-06 01:54:53.843784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e326afd587'
down_revision = '359f9af686ae'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE `partner` MODIFY COLUMN ownerName varchar(244)')


def downgrade():
    op.execute('ALTER TABLE `partner` MODIFY COLUMN ownerName integer')
