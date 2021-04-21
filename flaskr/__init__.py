# /flaskr/__init__.py: initializes the application
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcdef'