import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class BasketDetails(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'basketdetails'

    busket_id = sa.Column(sa.Integer, sa.ForeignKey('basket.id'))
    food_id = sa.Column(sa.Integer, sa.ForeignKey('food.id'))
    count = sa.Column(sa.Integer)  # количество товара
    price = sa.Column(sa.Integer)  # цена за все данные товары

    food = orm.relationship('Food')
    basket = orm.relationship('Basket')
