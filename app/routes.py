from app import app
from flask import render_template
from app.forms import PhoneForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-phone')
def add_phone():
    form = PhoneForm()
    return render_template('add_phone.html', form=form)
