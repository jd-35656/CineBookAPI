"""
app module
==========

This module defines the main application class for CineBookAPI using Flask.

Clases
------
MyApp : class
    Represents the main application class for CineBookAPI.

Example
-------
Create an instance of MyApp to initialize the CineBookAPI Flask application:

    >>> from your_module import MyApp
    >>> my_app_instance = MyApp()
    >>> # You now have a Flask application instance named 'CineBookAPI'.
"""
from typing import Dict

from flask import Flask


class MyApp:  # pylint: disable=too-few-public-methods
    """
    Represents the main application class for CineBookAPI.

    Methods
    -------
    create_app(self)
        Returns the Flask application instance.
    """

    def __init__(self) -> None:
        self._app: Flask = Flask("CineBookAPI")

        # Incorporate demo route
        self._demo_route()

    def create_app(self) -> Flask:
        """
        Returns the Flask application instance.

        Returns
        -------
        Flask
            The Flask application instance.
        """
        return self._app

    def _demo_route(self):
        @self._app.route("/")
        def index() -> Dict[str, str]:  # type: ignore
            return {"status": "OK"}
