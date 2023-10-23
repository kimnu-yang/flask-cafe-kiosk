from flask import Blueprint, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Menu, Order, Cart

bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/')
def index():
    order_id = Order.query.order_by(desc(Order.id))[0].id
    order_id += 1
        
    cnt = 0
    total_price = 0
    data = Cart.query.filter(Cart.order_id == order_id).all()
    for i in data:
        menu_data = Menu.query.filter(Menu.id == i.menu_id)[0]
        i.name = menu_data.name
        i.image = menu_data.image
        i.price = format(menu_data.price, ',d')
        
        cnt+=1
        total_price+=menu_data.price
    
    return render_template('cart.html', cart_list=data, order_id=order_id, cnt=cnt, total_price=format(total_price, ',d'))

@bp.route('/add',methods=['POST'])
def add():

    order_id = Order.query.order_by(desc(Order.id))[0].id
    order_id += 1
        
    menu_id = request.form['menu']
    data = Cart(order_id=order_id, menu_id=menu_id)
    
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('main.index'))

@bp.route('/del',methods=['POST'])
def delete():
    data = Cart.query.get_or_404(request.form['cart'])
    db.session.delete(data)
    db.session.commit()
    
    return redirect(url_for('cart.index'))