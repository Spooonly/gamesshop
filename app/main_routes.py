from flask import Blueprint, render_template
from .forms import LoginForm
import sqlalchemy as sa
from flask_login import current_user, login_user, logout_user
from .forms import RegisterForm
from .data.users import User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def test():
    return render_template('index.html')


@main.route('/cart')
def test2():
    return render_template('cart.html')


@main.route('/profile')
def test3():
    return render_template('profile.html')


@main.route('/product')
def test4():
    return render_template('product.html', data=data)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # проверка данных
        return 'ok'  # может быть небезопасно
        # return redirect(url_for('main.home')) пример кода с перенаправлением после входа
        # user = db_sess.session.scalar(
        # sa.select(User).where(User.name == form.username.data))
        # if user is None or not user.hashed_password != form.password.data:
        #     print('не работает')
        #     return redirect(url_for('login'))
        # login_user(user)
        # print('Вошёл')
        return redirect(url_for('index'))
