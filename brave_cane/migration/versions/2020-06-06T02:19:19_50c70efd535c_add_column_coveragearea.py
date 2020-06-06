"""add-column-coverageArea

Revision ID: 50c70efd535c
Revises: 13d70cd06edc
Create Date: 2020-06-06 02:19:53.868724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50c70efd535c'
down_revision = '13d70cd06edc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('partner', sa.Column('coverageArea', sa.JSON()))


def downgrade():
    op.drop_column('partner', 'coverageArea')
