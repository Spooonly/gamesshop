import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class OrderDetails(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'orderdetail'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'))
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'))
    count = sa.Column(sa.Integer, nullable=True)
    price = sa.Column(sa.Integer, nullable=False)

    product = orm.relationship('Product')
    order = orm.relationship('Order')

