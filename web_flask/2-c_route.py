#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def ctxt(text):
    str = text.replace("_", " ")
    return 'C {}'.format(str)

if __name__ == "__main__":
    app.run()
