"""
Module defining Flask routes for handling owner registration.

This module defines a Flask Blueprint for handling HTTP POST requests
related to owner registration. It provides a route for registering new
owners and handles various types of errors that might occur during the
registration process.

Routes
------
/register : POST
    Route for registering a new owner.
/login : POST
    Route for logging in an existing owner.
/logout : POST
    Route for logging out an existing owner.

Functions
---------
register() : JSON
    Route handler for registering a new owner. It expects a JSON payload
    containing owner data. It catches and handles different types of
    errors that might occur during the registration process, including
    validation errors, integrity errors, data errors, connection errors,
    SQLAlchemy errors, and general exceptions.

login() : JSON
    Route handler for logging in an existing owner. It expects a JSON payload
    containing owner login credentials. It catches and handles different types
    of errors that might occur during the login process, including validation
    errors, value errors, connection errors, SQLAlchemy errors, and general
    exceptions.

logout() : JSON
    Route handler for logging out an existing owner. It checks if the owner is
    logged in based on the session ID provided in the headers. It catches and
    handles different types of errors that might occur during the logout
    process, including connection errors, SQLAlchemy errors, and general
    exceptions.

"""

from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError

from src.owner_auth import blp
from src.owner_auth.service import OwnerSessionService
from src.owner_auth.utils import is_owner_loggedin


@blp.post("/register")
def register():  # pylint: disable=too-many-return-statements
    """
    Register a new owner.

    This route handler registers a new owner based on the provided JSON
    payload containing owner data. It catches and handles various types
    of errors that might occur during the registration process, including
    validation errors, integrity errors, data errors, connection errors,
    SQLAlchemy errors, and general exceptions.

    Returns
    -------
    JSON
        A JSON response containing a success message and an appropriate
        HTTP status code upon successful registration. In case of errors,
        it returns a corresponding error message along with an appropriate
        HTTP status code.

    Raises
    ------
    ValidationError
        If the provided data fails validation.
    IntegrityError
        If the phone number or email is already in use.
    DataError
        If the data format is invalid.
    ConnectionError
        If there's a connection error.
    SQLAlchemyError
        If there's a database-related error.
    Exception
        If an unexpected error occurs.
    """
    try:
        data = request.get_json()
        OwnerSessionService.register_service(data)
        return {"message": "Registered Successfully"}, 201

    except ValidationError as e:
        return {"message": f"Invalid data: {e}"}, 422

    except IntegrityError as e:
        return {"message": f"Phone number or email already in use: {e}"}, 409

    except DataError as e:
        return {"message": f"Invalid data format: {e}"}, 400

    except ConnectionError as e:
        return {"message": f"Connection error: {e}"}, 503

    except SQLAlchemyError as e:
        return {"message": f"Database error: {e}"}, 500

    except Exception as e:  # pylint: disable=broad-exception-caught
        return {"message": f"An unexpected error occurred: {e}"}, 500


@blp.post("/login")
def login():
    """
    Log in an existing owner.

    This route handler logs in an existing owner based on the provided JSON
    payload containing owner login credentials. It catches and handles various
    types of errors that might occur during the login process, including
    validation errors, value errors, connection errors, SQLAlchemy errors, and
    general exceptions.

    Returns
    -------
    JSON
        A JSON response containing a success message and an appropriate
        HTTP status code upon successful login. In case of errors, it returns
        a corresponding error message along with an appropriate HTTP status
        code.

    Raises
    ------
    ValidationError
        If the provided data fails validation.
    ValueError
        If the provided credentials are invalid.
    ConnectionError
        If there's a connection error.
    SQLAlchemyError
        If there's a database-related error.
    Exception
        If an unexpected error occurs.
    """
    try:
        data = request.get_json()
        res = OwnerSessionService.login_service(data)
        return res, 200

    except ValidationError as e:
        return {"message": f"Invalid data: {e}"}, 422

    except ValueError as e:
        return {"message": f"Invalid credential: {e}"}, 400

    except ConnectionError as e:
        return {"message": f"Connection error: {e}"}, 503

    except SQLAlchemyError as e:
        return {"message": f"Database error: {e}"}, 500

    except Exception as e:  # pylint: disable=broad-exception-caught
        return {"message": f"An unexpected error occurred: {e}"}, 500


@blp.post("/logout")
@is_owner_loggedin
def logout():
    """
    Log out an existing owner.

    This route handler logs out an existing owner based on the provided session
    ID in the headers. It checks if the owner is logged in, and if so, it logs
    them out. It catches and handles various types of errors that might occur
    during the logout process, including connection errors, SQLAlchemy errors,
    and general exceptions.

    Returns
    -------
    JSON
        A JSON response containing a success message and an appropriate
        HTTP status code upon successful logout. In case of errors, it returns
        a corresponding error message along with an appropriate HTTP status
        code.

    Raises
    ------
    ConnectionError
        If there's a connection error.
    SQLAlchemyError
        If there's a database-related error.
    Exception
        If an unexpected error occurs.
    """

    try:
        header = request.headers
        OwnerSessionService.logout_service(header)
        return {"message": "Sucessfully logged out"}, 200
    except ConnectionError as e:
        return {"message": f"Connection error: {e}"}, 503

    except SQLAlchemyError as e:
        return {"message": f"Database error: {e}"}, 500

    except Exception as e:  # pylint: disable=broad-exception-caught
        return {"message": f"An unexpected error occurred: {e}"}, 500
