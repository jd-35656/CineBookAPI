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

from src.main.config import config


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

        # Register config
        self._register_config()

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
        # Initialize extension
        self._intialize_extensions()

        return self._app

    def _demo_route(self) -> None:
        @self._app.route("/")
        def index() -> Dict[str, str]:  # type: ignore
            return {"status": "OK"}

    def _register_config(self) -> None:
        self._app.config.from_object(config)

    def _intialize_extensions(self) -> None:
        pass
