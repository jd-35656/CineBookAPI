"""
Provides a Flask Blueprint for managing owners.

Attributes
----------
blp : flask.Blueprint
    The Blueprint object for managing owners in the application.

Examples
--------
>>> from flask import Flask
>>> from .owners import blp
>>>
>>> app = Flask(__name__)
>>> app.register_blueprint(blp)
"""

from flask import Blueprint

blp = Blueprint("owners", __name__)
