#!/usr/bin/python3
"""Starts a web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
from collections import OrderedDict
from operator import itemgetter
app = Flask(__name__)


@app.teardown_appcontext
def teardown_request(response_or_exc):
    """Refreshes storage session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """Loads all states in DB then returns a template using those states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states_list=states)


if __name__ == '__main__':
    app.run()
