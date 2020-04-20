#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def pythonrt(text):
    str = text.replace('_', ' ')
    return 'Python {}'.format(escape(str))


@app.route('/number/<int:n>', strict_slashes=False)
def numberrt(n):
    return 'n is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templatert(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_evenrt(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run()
