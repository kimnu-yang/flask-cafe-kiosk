from flask import Blueprint, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

from pybo.models import Menu, Inventory

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    data = Menu.query.order_by(Menu.id)
    for i in data:
        i.price = format(i.price, ',d')
        
        if i.ingredient:
            i.state = 'Y'
            for key,val in json.loads(i.ingredient).items():
                if Inventory.query.get(key).amount < val:
                    i.state = 'N'
        else:
            i.state = 'N'
    
    return render_template('index.html', menu_list=data)