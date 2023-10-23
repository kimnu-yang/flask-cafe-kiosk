from flask import Blueprint, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from werkzeug.utils import redirect
from datetime import datetime
import json

from pybo import db
from pybo.models import Menu, Order, Cart, Inventory

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/')
def index():
    data = Order.query.order_by(desc(Order.id))
    
    for i in data:
        total_price = 0
        menu_item = {}
        
        for j in Cart.query.filter(Cart.order_id == i.id):
            for k in Menu.query.filter(Menu.id == j.menu_id):
                total_price += k.price
                if k.name in menu_item:
                    menu_item[k.name] += 1
                else:
                    menu_item[k.name] = 1
                    
        i.total_price = format(total_price, ',d')
        i.menu = str(menu_item)
    
    return render_template('order.html', order_list=data)

@bp.route('/add',methods=['POST'])
def add():
    data = Order(order_time=datetime.now(), state='order')
    
    db.session.add(data)
    db.session.commit()
    
    data = Menu.query.order_by(Menu.id)
    for i in data:
        i.price = format(i.price, ',d')
    
    return redirect(url_for('main.index'))

@bp.route('/update',methods=['POST'])
def update():
    data = Order.query.get(request.form['id'])
    data.state = request.form['state']
    
    if request.form['state'] == 'done':
        data.done_time = datetime.now()
        cart_data = Cart.query.filter(Cart.order_id == request.form['id'])
        
        for i in cart_data:
            ing_dict = json.loads(Menu.query.get(i.menu_id).ingredient)
            for ing,cnt in ing_dict.items():
                Inventory.query.get(ing).amount -= cnt
            
    elif request.form['state'] == 'cancel':
        data.cancel_time = datetime.now()
    else:
        print('올바르지 않은 요청입니다.')
        return redirect(url_for('order.index'))
    
    db.session.commit()

    data = Order.query.order_by(desc(Order.id))
    
    for i in data:
        total_price = 0
        menu_item = {}
        
        for j in Cart.query.filter(Cart.order_id == i.id):
            for k in Menu.query.filter(Menu.id == j.menu_id):
                total_price += k.price
                if k.name in menu_item:
                    menu_item[k.name] += 1
                else:
                    menu_item[k.name] = 1
                    
        i.total_price = format(total_price, ',d')
        i.menu = str(menu_item)
    
    return render_template('order.html', order_list=data)