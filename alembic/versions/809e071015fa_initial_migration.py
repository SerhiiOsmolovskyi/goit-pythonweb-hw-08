"""Initial migration

Revision ID: 809e071015fa
Revises: 
Create Date: 2025-03-23 14:16:49.528211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '809e071015fa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_contacts_email', table_name='contacts')
    op.drop_index('ix_contacts_first_name', table_name='contacts')
    op.drop_index('ix_contacts_id', table_name='contacts')
    op.drop_index('ix_contacts_last_name', table_name='contacts')
    op.drop_index('ix_contacts_phone_number', table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birthday', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('additional_info', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contacts_pkey')
    )
    op.create_index('ix_contacts_phone_number', 'contacts', ['phone_number'], unique=False)
    op.create_index('ix_contacts_last_name', 'contacts', ['last_name'], unique=False)
    op.create_index('ix_contacts_id', 'contacts', ['id'], unique=False)
    op.create_index('ix_contacts_first_name', 'contacts', ['first_name'], unique=False)
    op.create_index('ix_contacts_email', 'contacts', ['email'], unique=True)
    # ### end Alembic commands ###
