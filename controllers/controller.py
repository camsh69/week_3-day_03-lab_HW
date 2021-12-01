from app import app
from flask import render_template
from models.order import order

@app.route('/')
def index():
    pass