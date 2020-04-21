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
    states = storage.all(State)
    states_list = []
    for v in states.items():
        vdct = v[1].to_dict()
        states_list.append((vdct['id'], vdct['name']))
    states_list.sort(key = itemgetter(1))
    print(states_list)
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == '__main__':
    app.run()
