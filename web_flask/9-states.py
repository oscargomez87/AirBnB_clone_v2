#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def end(resp_or_exep):
    """close SQLALchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    """Returns a view of all states or an specific state"""
    states = storage.all(State)
    if id:
        state_id = "State.{}".format(id)
        state = {}
        if state_id in states.keys():
            state = states[state_id]
        return render_template('9-states.html', state=state,)
    else:
        return render_template('9-states.html', states=states.values())


if __name__ == '__main__':
    app.run()
