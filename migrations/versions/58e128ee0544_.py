"""empty message

Revision ID: 58e128ee0544
Revises: 41a42b3dbc64
Create Date: 2021-02-21 21:24:57.920771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58e128ee0544'
down_revision = '41a42b3dbc64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agendamiento',
    sa.Column('agendamiento_id', sa.Integer(), nullable=False),
    sa.Column('f_horarios_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['f_horarios_id'], ['horarios.horarios_id'], ),
    sa.PrimaryKeyConstraint('agendamiento_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agendamiento')
    # ### end Alembic commands ###
