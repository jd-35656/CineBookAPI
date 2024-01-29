"""
Documentation Package
=====================

This package provides utilities and functions for handling documentation
in the CineBookAPI project.

Methods
-------
register_documentation : function
    Function to register Swagger documentation for a Flask app.

Examples
--------
To register Swagger documentation for a Flask app:

    >>> from flask import Flask
    >>> from docs import register_documentation
    >>> app = Flask(__name__)
    >>> register_documentation(app)
"""

from src.main.docs.resister_docs import register_documentation

__all__ = ["register_documentation"]
