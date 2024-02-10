"""
Provides a Flask Blueprint for managing owners details.

Attributes
----------
blp : flask.Blueprint
    The Blueprint object for managing owners in the application.

Examples
--------
>>> from flask import Flask
>>> from .owner_detail import blp
>>>
>>> app = Flask(__name__)
>>> app.register_blueprint(blp)
"""

from flask import Blueprint

blp: Blueprint = Blueprint("owner_detail", __name__)
