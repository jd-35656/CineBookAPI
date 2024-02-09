"""
Module for defining a schema to represent owners with email,
phone, and password fields.

This module contains the `OwnerSchema` and `OwnerUpdateSchema` class,
which is a Marshmallow schema used for validating and serializing/
deserializing owner data.

Example
-------
Define an `OwnerSchema` instance:

    >>> owner_schema = OwnerSchema()

Define an `OwnerUpdateSchema` instance:

    >>> owner_update_schema = OwnerUpdateSchema()

Classes
-------
OwnerSchema : class
    A schema for representing owners with email, phone, and
    password fields.

OwnerUpdateSchema : class
    A schema for updating owner information with email, phone,
    and password fields.

"""

import hashlib

from marshmallow import (
    Schema,
    ValidationError,
    fields,
    pre_load,
    validate,
    validates_schema,
)


class OwnerSchema(Schema):
    """
    Schema for representing an owner with email, phone, and
    password fields.

    Attributes
    ----------
    id : marshmallow.fields.UUID
        UUID field for unique identifier (dump only).
    email : marshmallow.fields.Email
        Email field for owner's email address (required).
    phone : marshmallow.fields.Number
        Numeric field for owner's phone number (required).
        Must be within the range of 10 digits.
    password : marshmallow.fields.Str
        String field for owner's password (load only).
        Must be between 8 and 16 characters long (required).

    Methods
    -------
    process_input(data, **kwargs)
        Pre-processing method to hash the password before
        loading into the schema.
    """

    id = fields.UUID(
        dump_only=True,
    )
    email = fields.Email(
        required=True,
    )
    phone = fields.Number(
        validate=validate.Range(
            min=1000000000,
            max=9999999999,
        ),
        required=True,
    )
    password = fields.Str(
        load_only=True,
        validate=validate.Length(
            min=8,
            max=16,
        ),
        required=True,
    )

    @pre_load
    def process_input(self, data, **kwargs):  # pylint: disable=unused-argument
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


class OwnerUpdateSchema(Schema):
    """
    Schema for updating owner information with email, phone, and
    password fields.

    Attributes
    ----------
    email : marshmallow.fields.Email
        Email field for owner's email address (optional).
    phone : marshmallow.fields.Int
        Numeric field for owner's phone number (optional).
        Must be within the range of 10 digits.
    password : marshmallow.fields.Str
        String field for owner's password (optional).
        Must be between 8 and 16 characters long.

    Methods
    -------
    validate_at_least_one_field(data, **kwargs)
        Method to validate that at least one field (email, phone, password)
        is provided.
    process_input(data, **kwargs)
        Pre-processing method to hash the password before loading into
        the schema.
    """

    email = fields.Email()
    phone = fields.Int(
        validate=validate.Range(
            min=1000000000,
            max=9999999999,
        ),
    )
    password = fields.Str(
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
            If none of the fields (email, phone, password) is provided.
        """
        if not any(field in data for field in ["email", "phone", "password"]):
            raise ValidationError(
                "At least one field (email, phone, password) must be provided."
            )

    @pre_load
    def process_input(self, data, **kwargs):  # pylint: disable=unused-argument
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
