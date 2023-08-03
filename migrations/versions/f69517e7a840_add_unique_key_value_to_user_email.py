"""add unique key value to user email

Revision ID: f69517e7a840
Revises: f319815bf7d6
Create Date: 2023-02-20 10:53:35.835404

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "f69517e7a840"
down_revision = "f319815bf7d6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("user_unique_mail", "usuario", ["email"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_unique_mail", "usuario", type_="unique")
    # ### end Alembic commands ###
