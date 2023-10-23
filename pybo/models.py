from pybo import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    ingredient = db.Column(db.String(200), nullable=True)
    state = db.Column(db.String(10), nullable=True)
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu = db.Column(db.String(200), nullable=True)
    total_price = db.Column(db.Integer, nullable=True)
    order_time = db.Column(db.DateTime(), nullable=False)
    done_time = db.Column(db.DateTime(), nullable=True)
    cancel_time = db.Column(db.DateTime(), nullable=True)
    state = db.Column(db.String(10), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    menu_id = db.Column(db.Integer, nullable=False)
    
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)