"""
Module for defining a schema to represent owners with email,
phone, and password fields.

This module contains the `OwnerSchema` class, which is a
Marshmallow schema used for validating and serializing/
deserializing owner data.

Example
-------
Define an `OwnerSchema` instance:

    >>> owner_schema = OwnerSchema()

Attributes
----------
hashlib : module
    Provides cryptographic hash functions.
marshmallow : module
    A library for object serialization and deserialization.

Classes
-------
OwnerSchema : class
    A schema for representing owners with email, phone, and
    password fields.
"""

import hashlib

from marshmallow import Schema, fields, pre_load, validate


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
