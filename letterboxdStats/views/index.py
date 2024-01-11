"""
Index (main) view.

"""
import flask
from flask import send_from_directory
import letterboxdStats


@letterboxdStats.app.route('/')
def show_index():
    """Display / route."""

    text = "Letterboxd Stats"
    context = {"text": text}
    return flask.render_template("index.html", **context)