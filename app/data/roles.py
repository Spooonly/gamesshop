import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

class Role(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'roles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)

    users = orm.relationship('User', back_populates='role')


    def __repr__(self):
        return f'Role: {self.name}'