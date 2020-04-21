#!/usr/bin/python3
"""Script that starts a Flask web app"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(response_or_exc):
    """restarts session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Returns a template that displays cities by states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states_list=states)


if __name__ == '__main__':
    app.run()
