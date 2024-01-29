"""
Database Exception Module
=========================

Classes
-------
DatabaseURINotFoundError:Exception
    Exception raised when the database URI is not found in the config.

SessionCreationError:Exception
    Exception raised when there is an error creating a database session.
"""


class DatabaseURINotFoundError(Exception):
    """Exception raised when the database URI is not found in the config."""


class SessionCreationError(Exception):
    """Exception raised when there is an error creating a database session."""
