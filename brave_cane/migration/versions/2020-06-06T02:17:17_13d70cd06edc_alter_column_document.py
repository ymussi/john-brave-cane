"""alter-column-document

Revision ID: 13d70cd06edc
Revises: c8e326afd587
Create Date: 2020-06-06 02:17:37.332558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d70cd06edc'
down_revision = 'c8e326afd587'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE `partner` MODIFY COLUMN document varchar(244)')


def downgrade():
    op.execute('ALTER TABLE `partner` MODIFY COLUMN ownerName json')
