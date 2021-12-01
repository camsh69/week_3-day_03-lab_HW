from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="Home", orders=orders)

@app.route('/order/<int:index_number>')
def order(index_number):
    return render_template('order.html', title="Orders", order=orders[index_number])