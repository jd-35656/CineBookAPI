"""
Owner Authentication Utilities

This module provides utility functions and decorators for handling owner
authentication in a Flask application.

Functions
---------
is_loggedin : decorator
    Decorator to check if the user is logged in based on the session ID
    provided in the headers.

get_owner_id : function
    Retrieve the owner ID associated with the session ID from the
    request headers.
"""

from functools import wraps

from flask import abort, request

from src.main.database import db
from src.owner_auth.model import OwnerSessionModel


def is_owner_loggedin(func):
    """
    Decorator to check if the user is logged in based on the session ID
    provided in the headers.

    Parameters
    ----------
    func : function
        The function to be decorated.

    Returns
    -------
    function
        The decorated function.

    Raises
    ------
    HTTPException
        If the session ID is missing or invalid, a 401 Unauthorized
        response is raised.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers
        if "Authorization" not in header:
            abort(401, "Unauthorized: Missing session ID in headers")

        session_id = header["Authorization"]

        with db.session() as session:
            sess = (
                session.query(OwnerSessionModel)
                .filter_by(session_id=session_id)
                .first()
            )

        if not sess:
            abort(401, "Unauthorized: Invalid session ID")

        return func(*args, **kwargs)

    return wrapper


def get_owner_id() -> str:
    """
    Retrieve the owner ID associated with the session ID from
    the request headers.

    Returns
    -------
    UUID
        Owner ID associated with the session ID.

    Raises
    ------
    HTTPException
        If the session ID is missing or invalid.
    """
    header = request.headers
    if "Authorization" not in header:
        abort(401, "Unauthorized: Missing session ID in headers")

    session_id = header["Authorization"]

    with db.session() as session:
        sess = (
            session.query(OwnerSessionModel.owner_id)
            .filter_by(session_id=session_id)
            .first()
        )

    if not sess:
        abort(401, "Unauthorized: Invalid session ID")
    owner_id = str(sess.owner_id)

    return owner_id
