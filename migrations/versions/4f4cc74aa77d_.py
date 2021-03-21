"""is super column
Revision ID: 3b94ee806d38
Revises: eeb328b2a8cf
Create Date: 2021-03-20 13:15:03.446182
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision = '3b94ee806d38'
down_revision = 'eeb328b2a8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('limited', sa.Boolean(), nullable=False, server_default=expression.false()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'limited')
    # ### end Alembic commands ###