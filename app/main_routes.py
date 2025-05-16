from flask import Blueprint, render_template, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash
from .data import db_session
from .data.product import Product
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user
from .forms import RegisterForm
from .data.users import User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cart')
def cart():
    return render_template('cart.html')


@main.route('/profile_options')
def profile():
    return render_template('profile_options.html')

@main.route('/profile')
def profile_main():
    return render_template('profile.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.username == form.username.data).first()
        if user and check_password_hash(user.hashed_password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.profile_main'))
        else:
            return render_template('login.html', form=form, error="Неверные данные")
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        existing_user = session.query(User).filter(User.email == form.mail.data).first()
        if existing_user:
            flash("Email уже зарегистрирован!")
            return redirect(url_for('main.register'))
        user = User(
            username=form.username.data,
            email=form.mail.data,
            phone=form.phone.data,
            hashed_password=generate_password_hash(form.password.data)
        )
        session.add(user)
        session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)
