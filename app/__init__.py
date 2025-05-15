from flask import Flask
from .main_routes import main
from .data import db_session
from flask_login import LoginManager
from app.data import users, roles, basket, basket_details, product, order, order_details



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # init DB
    db_session.global_init("db/database.sqlite")

    # init login manager
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .data.users import User

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.get(User, int(user_id))

    app.register_blueprint(main, url_prefix='/')

    return app
