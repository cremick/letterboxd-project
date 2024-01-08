"""LetterboxdStats package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)

# Read settings from config module (letterboxdStats.config)
app.config.from_object('letterboxdStats.config')

# Tell app about views.
import letterboxdStats.views