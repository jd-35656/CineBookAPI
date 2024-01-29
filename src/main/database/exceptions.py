"""
Database Exception Module
=========================

Classes
-------
DatabaseURINotFoundError:Exception
    Exception raised when the database URI is not found in the config.
"""


class DatabaseURINotFoundError(Exception):
    """Exception raised when the database URI is not found in the config."""
