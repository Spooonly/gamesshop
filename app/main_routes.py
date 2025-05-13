from flask import Blueprint, render_template, request

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
    data = request.args
    print(data['name'])
    return render_template('product.html', data=data)