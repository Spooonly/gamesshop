import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class Order(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'orders'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    all_price = sa.Column(sa.Integer, nullable=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = orm.relationship('User')
    order_derails = orm.relationship('OrderDetails', back_populates='order')
