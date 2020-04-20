#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctxt(text):
    str = text.replace('_', ' ')
    return 'C {}'.format(str)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def pythonrt(text):
    str = text.replace('_', ' ')
    return 'Python {}'.format(escape(str))


if __name__ == "__main__":
    app.run()
