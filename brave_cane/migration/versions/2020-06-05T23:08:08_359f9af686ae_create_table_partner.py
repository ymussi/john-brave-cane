"""create-table-partner

Revision ID: 359f9af686ae
Revises: 
Create Date: 2020-06-05 23:08:26.633464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359f9af686ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # CREATE TABLE PARTNER
    op.create_table('partner',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('tradingName', sa.String(244)),
                    sa.Column('ownerName', sa.Integer()),
                    sa.Column('document', sa.Integer()),
                    sa.Column('document', sa.JSON()))


def downgrade():
    # DROP TABLE PARTNER
    op.drop_table('partner')
