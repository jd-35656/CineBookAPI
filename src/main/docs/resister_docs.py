"""
Swagger Documentation Module
===========================

This module provides functions to integrate Swagger documentation into
a Flask application using the Swagger UI library.

Functions
---------
register_documentation(app: Flask) -> None:
    Register Swagger documentation for a Flask app.

    Parameters
    ----------
    app : Flask
        The Flask application instance.

    Returns
    -------
    None

    Notes
    -----
    This function uses the `swagger_ui` library to generate Swagger
    documentation for the specified Flask app. The Swagger UI is accessible
    at the '/doc' URL prefix, and the configuration is loaded from the
    specified YAML file.

    Example
    -------
    >>> from flask import Flask
    >>> from your_module import register_documentation
    >>> app = Flask(__name__)
    >>> register_documentation(app)
"""

from flask import Flask
from swagger_ui import api_doc  # pylint: disable=import-error # type: ignore


def register_documentation(app: Flask) -> None:
    """
    Register Swagger documentation for a Flask app.

    Parameters
    ----------
    app : Flask
        The Flask application instance.

    Returns
    -------
    None

    Notes
    -----
    This function uses the `swagger_ui` library to generate Swagger
    documentation for the specified Flask app. The Swagger UI is accessible
    at the '/doc' URL prefix, and the configuration is loaded from the
    specified YAML file.

    Example
    -------
    >>> from flask import Flask
    >>> from your_module import register_documentation
    >>> app = Flask(__name__)
    >>> register_documentation(app)
    """
    api_doc(
        app,
        config_path="src/main/docs/docfiles/index.yaml",
        url_prefix="/doc",
        title="CineBookAPI Doc",
    )
