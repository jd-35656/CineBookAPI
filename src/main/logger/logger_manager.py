"""
Logger Manager Module
====================

This module defines the main application class for CineBookAPI using Flask.

Classes
-------
Logger:
    Represents the logger class for logging.

Example
-------
Create an instance of Logger to initialize the CineBookAPI Flask application:

    >>> from logger_manager import Logger
    >>> logger_instance = Logger()
    >>> # You now have a Logger instance for managing logs in the CineBookAPI.

Initialize Logger with a Flask app (e.g., wit) for customized configurations:

    >>> from logger_manager import Logger
    >>> from flask import Flask
    >>> wit = Flask(__name__)
    >>> logger_instance = Logger(app=wit)
    >>> # You now have a Logger instance configured to work with the 'wit'
        Flask app.
"""
import logging
from typing import Optional

from flask import Flask


class Logger:
    """
    Represents the logger class for logging.

    Args
    ----
    app : Optional[Flask]
        An optional Flask application instance. If provided, the logger will
        be configured to work with the given Flask app.

    Example
    -------
    Create an instance of Logger to initialize the CineBookAPI Flask
    application:

    >>> from logger_manager import Logger
    >>> logger_instance = Logger()
    >>> # You now have a Logger instance for managing logs in the CineBookAPI.

    Initialize Logger with a Flask app (e.g., wit) for customized
    configurations:

    >>> from logger_manager import Logger
    >>> from flask import Flask
    >>> wit = Flask(__name__)
    >>> logger_instance = Logger(app=wit)
    >>> # You now have a Logger instance configured to work with the 'wit'
    Flask app.
    """

    def __init__(self, app: Optional[Flask] = None) -> None:
        self._app: Optional[Flask] = app
        self._logger: Optional[logging.Logger] = None
        self._handler: Optional[logging.Handler] = None
        self._formatter: Optional[logging.Formatter] = None
