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

from datetime import datetime
from typing import Dict

from flask import Flask, Response, g, request

from src.main import routes  # noqa # pylint: disable=unused-import
from src.main.blueprints import BLUEPRINTS
from src.main.config import config
from src.main.database import db
from src.main.docs import register_documentation
from src.main.logger import logger


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

        # Register Blueprints
        self._register_blueprints()

        # Register docs
        self._register_docs()

        # Register request response logging
        self._register_request_logging()

        return self._app

    def _demo_route(self) -> None:
        @self._app.route("/")
        def index() -> Dict[str, str]:  # type: ignore
            return {"status": "OK"}

    def _register_config(self) -> None:
        self._app.config.from_object(config)

    def _intialize_extensions(self) -> None:
        logger.init_app(self._app)
        db.init_app(self._app)

    def _register_blueprints(self) -> None:
        if not BLUEPRINTS:
            return
        for blp_details in BLUEPRINTS:
            self._app.register_blueprint(**blp_details)  # type: ignore

    def _register_docs(self):
        register_documentation(self._app)

    def _register_request_logging(self) -> None:
        @self._app.before_request
        def before_request() -> None:  # type: ignore
            g.request_data = request
            g.request_data.timestamp = datetime.now()  # type: ignore

        @self._app.after_request
        def after_request(response: Response) -> Response:  # type: ignore
            g.response_data = response
            g.response_data.timestamp = datetime.now()  # type: ignore

            request_data = g.get("request_data")
            response_data = g.get("response_data")

            if request_data is not None and response_data is not None:
                logger.request_response_logging(
                    request_data=request_data, response_data=response_data
                )

            # Pop the data after logging
            g.pop("request_data", None)
            g.pop("response_data", None)

            return response
