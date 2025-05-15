from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy as sa

from sqlalchemy_serializer import SerializerMixin

from app.data.db_session import SqlAlchemyBase


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    price = sa.Column(sa.Float, nullable=False)
    image_url = sa.Column(sa.String, nullable=False)
