"""
Provides a Flask Blueprint for managing owners authorizations.

Attributes
----------
blp : flask.Blueprint
    The Blueprint object for managing owners in the application.

Examples
--------
>>> from flask import Flask
>>> from .owner_auth import blp
>>>
>>> app = Flask(__name__)
>>> app.register_blueprint(blp)
"""

from flask import Blueprint

blp: Blueprint = Blueprint("owner_auth", __name__)
