"""
Logger Package
==============

This package provides a centralized logger for the main application.

Usage
-----
To use the logger in your application, you can import it as follows:

    >>> from your_package import init_app, logger
    >>> from flask import Flask

    Initialize the logger with a Flask app:

    >>> app = Flask(__name__)
    >>> logger.init_app(app)

    Now, you can use the logger to log messages:

    >>> logger.info("Your log message")
"""
from src.main.logger.logger_manager import Logger

logger = Logger()
