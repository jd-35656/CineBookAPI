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
    >>> wit = Flask(__name__)
    >>> logger_instance.init_app(wit)
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

    Methods
    -------
    init_app(app: Flask) -> None:
        Initialize the Logger with a Flask app.

    debug(msg: str) -> None:
        Log a debug message using the configured logger.

    info(msg: str) -> None:
        Log a info message using the configured logger.

    error(msg: str) -> None:
        Log a error message using the configured logger.

    warning(msg: str) -> None:
        Log a warning message using the configured logger.

    Example
    -------
    Create an instance of Logger to initialize the CineBookAPI Flask
    application:

    >>> from logger_manager import Logger
    >>> logger_instance = Logger()
    >>> wit = Flask(__name__)
    >>> logger_instance.init_app(wit)
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

        if self._app is not None:
            self.init_app(self._app)

    def init_app(self, app: Flask) -> None:
        """
        Initialize the Logger with a Flask app.

        Parameters
        ----------
        app : Flask
            Flask application instance.
        """
        self._logger = logging.getLogger("app")
        self._logger.setLevel(logging.DEBUG)

        self._handler = logging.FileHandler("logs.log")
        self._handler.setLevel(app.config["LOG_LEVEL"])  # type: ignore

        self._formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        self._handler.setFormatter(self._formatter)

        self._logger.addHandler(self._handler)

    def debug(self, msg: str) -> None:
        """
        Log a debug message using the configured logger.

        Parameters
        ----------
        msg : str
            The debug message to be logged.

        Returns
        -------
        None
        """
        self._logger.debug(msg)  # type: ignore

    def info(self, msg: str) -> None:
        """
        Log a info message using the configured logger.

        Parameters
        ----------
        msg : str
            The info message to be logged.

        Returns
        -------
        None
        """
        self._logger.info(msg)  # type: ignore

    def error(self, msg: str) -> None:
        """
        Log a error message using the configured logger.

        Parameters
        ----------
        msg : str
            The error message to be logged.

        Returns
        -------
        None
        """
        self._logger.error(msg)  # type: ignore

    def warning(self, msg: str) -> None:
        """
        Log a warning message using the configured logger.

        Parameters
        ----------
        msg : str
            The warning message to be logged.

        Returns
        -------
        None
        """
        self._logger.warning(msg)  # type: ignore
