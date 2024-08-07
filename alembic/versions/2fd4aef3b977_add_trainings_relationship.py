"""Rename relationship 'training' to 'trainings' in User model

Revision ID: your_revision_id
Revises: previous_revision_id
Create Date: 2024-08-06

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2fd4aef3b977'
down_revision = '77d24712686c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Since this is a change in the ORM model and not in the actual database schema,
    # no operations are needed here.
    pass


def downgrade() -> None:
    # Similarly, no operations are needed to revert the ORM change.
    pass