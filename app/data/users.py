import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    name = sa.Column(sa.String, nullable=False)
    surname = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    phone = sa.Column(sa.String, unique=True, nullable=False)

    role_id = sa.Column(sa.Integer, sa.ForeignKey('roles.id'))

    card_data = sa.Column(sa.String, nullable=True)

    hashed_password = sa.Column(sa.String, nullable=False)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    role = orm.relationship('Role')
    basket = orm.relationship('Basket', back_populates='user')
    order = orm.relationship('Order', back_populates='user')
