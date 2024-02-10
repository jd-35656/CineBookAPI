"""
Module defining a Marshmallow schema for owner login details.

This module defines a schema using the Marshmallow library for handling
owner login details. The schema validates email, phone, and password
fields, and provides methods for pre-processing the data and validating
that at least one field (email or phone) is provided.

Classes
-------
OwnerLoginSchema : Schema class
    Schema for validating owner login details.

SessionSchema : Schema class
    Schema for managing session details.

"""

import hashlib
from typing import Any, Dict

from marshmallow import (
    Schema,
    ValidationError,
    fields,
    post_load,
    validate,
    validates_schema,
)


class OwnerLoginSchema(Schema):
    """
    Schema for validating owner login details.

    Attributes
    ----------
    email : Email field
        Field for validating email.
    phone : Integer field
        Field for validating phone number.
    password : String field
        Field for validating password.

    Methods
    -------
    validate_at_least_one_field(data, **kwargs)
        Validates that at least one of the fields (email or phone) is provided.
    hash_password(data, **kwargs)
        Pre-processing method to hash the password before loading into the
        schema.
    """

    email = fields.Email()
    phone = fields.Int(
        validate=validate.Range(
            min=1000000000,
            max=9999999999,
        ),
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(
            min=8,
            max=16,
        ),
    )

    @validates_schema
    def validate_at_least_one_field(
        self, data, **kwargs
    ):  # pylint: disable=unused-argument
        """
        Validate that at least one field (email, phone, password) is provided.

        Parameters
        ----------
        data : dict
            Input data containing owner information.

        Raises
        ------
        ValidationError
            If none of the fields (email, phone) is provided.
        """
        if not any(field in data for field in ["email", "phone"]):
            raise ValidationError(
                "At least one field (email, phone) must be provided."
            )

    @post_load
    # pylint: disable=unused-argument
    def hash_password(self, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Pre-processing method to hash the password before
        loading into the schema.

        Parameters
        ----------
        data : dict
            Input data containing password.

        Returns
        -------
        dict
            Processed data with hashed password.
        """

        if "password" in data:
            password_bytes = data["password"].encode("utf-8")
            hashed_password = hashlib.sha256(password_bytes).hexdigest()
            data["password"] = hashed_password
        return data


class SessionSchema(Schema):
    """
    Schema for managing session details.

    Attributes
    ----------
    session_id : UUID field
        Field for session identifier. Only used for dumping.
    owner_id : UUID field
        Field for owner identifier. Only used for loading.
    """

    session_id = fields.UUID(
        dump_only=True,
    )
    owner_id = fields.UUID(
        required=True,
        load_only=True,
    )
