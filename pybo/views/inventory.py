from flask import Blueprint, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from werkzeug.utils import redirect
from datetime import datetime

from pybo import db
from pybo.models import Menu, Order, Cart, Inventory

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/')
def index():
    data = Inventory.query.order_by(desc(Inventory.id))
    
    return render_template('inventory.html', inventory_list=data)

@bp.route('/add',methods=['POST'])
def add():
    data = Inventory(name=request.form['name'], price=request.form['price'], amount=request.form['amount'])
    
    db.session.add(data)
    db.session.commit()
    
    data = Inventory.query.order_by(desc(Inventory.id))
    
    return render_template('inventory.html', inventory_list=data)

@bp.route('/update',methods=['POST'])
def update():
    data = Inventory.query.get(request.form['id'])
    data.amount = request.form['amount']
    
    db.session.commit()
    
    data = Inventory.query.order_by(desc(Inventory.id))
    
    return render_template('inventory.html', inventory_list=data)