from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello-from-the-other-side'

from app import routes
