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

Functions
---------
register() : JSON
    Route handler for registering a new owner. It expects a JSON payload
    containing owner data. It catches and handles different types of
    errors that might occur during the registration process, including
    validation errors, integrity errors, data errors, connection errors,
    SQLAlchemy errors, and general exceptions.
"""

from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError

from src.owner_auth import blp
from src.owner_auth.service import OwnerSessionService


@blp.post("/register")
def register():
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
