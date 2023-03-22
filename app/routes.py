from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-phone')
def add_phone():
    return 'Add Phone'
