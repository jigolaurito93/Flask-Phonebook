from app import app

@app.route('/')
def index():
    return 'Hello World'


@app.route('/add-phone')
def add_phone():
    return 'Add Phone'
