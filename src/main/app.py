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
from flask import Flask


class MyApp:  # pylint: disable=too-few-public-methods
    """
    Represents the main application class for CineBookAPI.
    """

    def __init__(self) -> None:
        self._app: Flask = Flask("CineBookAPI")
