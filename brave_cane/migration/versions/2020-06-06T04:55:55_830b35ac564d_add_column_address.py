"""add-column-address

Revision ID: 830b35ac564d
Revises: 50c70efd535c
Create Date: 2020-06-06 04:55:32.972641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '830b35ac564d'
down_revision = '50c70efd535c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('partner', sa.Column('address', sa.JSON()))


def downgrade():
    op.drop_column('partner', 'address')