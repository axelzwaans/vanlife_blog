"""Update user model

Revision ID: c7015d309d37
Revises: 14e9b4f3cc10
Create Date: 2022-12-23 15:41:28.912689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7015d309d37'
down_revision = '14e9b4f3cc10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstname', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('lastname', sa.String(length=150), nullable=True))
        batch_op.drop_column('firstName')
        batch_op.drop_column('lastName')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastName', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('firstName', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')

    # ### end Alembic commands ###
