"""
Module defining schemas for representing owner details.

This module defines several schemas using the Marshmallow library
for handling owner details, including personal information, address,
and update details.

Classes
-------
Gender : Enum class
    Enum class defining gender options.
AddressSchema : Schema class
    Schema for validating address details.
OwnerDetailSchema : Schema class
    Schema for validating owner details.
OwnerDetailUpdateSchema : Schema class
    Schema for validating owner update details.
"""

from datetime import datetime
from enum import Enum

from marshmallow import Schema, ValidationError, fields, validate


class Gender(Enum):
    """
    Enumeration for representing gender options.

    Attributes
    ----------
    MALE : str
        Male gender.
    FEMALE : str
        Female gender.
    OTHER : str
        Other gender.
    """

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class AddressSchema(Schema):
    """
    Schema for validating address details.

    Attributes
    ----------
    address_line_1 : str
        First line of the address.
    address_line_2 : str
        Second line of the address.
    city : str
        City name.
    state : str
        State name.
    country : str
        Country name.
    pincode : int
        Pincode.
    """

    address_line_1 = fields.String(
        required=True,
        validate=validate.Length(
            min=10,
            max=40,
        ),
    )
    address_line_2 = fields.String(
        required=True,
        validate=validate.Length(
            min=10,
            max=40,
        ),
    )
    city = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=20,
        ),
    )
    state = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=20,
        ),
    )
    country = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=20,
        ),
    )
    pincode = fields.Integer(
        required=True,
        validate=validate.Range(
            min=100000,
            max=999999,
        ),
    )


class OwnerDetailSchema(Schema):
    """
    Schema for validating owner details.

    Attributes
    ----------
    id : UUID
        Identifier for the owner.
    name : str
        Name of the owner.
    dob : DateTime
        Date of birth of the owner.
    gender : Gender
        Gender of the owner.
    address : AddressSchema
        Address details of the owner.
    owner_id : UUID
        Identifier for the owner (load-only).
    """

    @staticmethod
    def validate_age(dob):
        """
        Validate that the owner's age is greater than 18.

        Parameters
        ----------
        dob : DateTime
            Date of birth of the owner.

        Raises
        ------
        ValidationError
            If the owner's age is less than 18.
        """
        if dob:
            age = (datetime.now() - dob).days // 365
            if age < 18:
                raise ValidationError("Age must be greater than 18.")

    id = fields.UUID(
        dump_only=True,
    )
    name = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=20,
        ),
    )
    dob = fields.DateTime(
        reqired=True,
        validate=validate_age,
    )
    gender = fields.Enum(
        Gender,
        required=True,
    )
    address = fields.Nested(
        AddressSchema,
        required=True,
    )
    owner_id = fields.UUID(
        load_only=True,
    )


class OwnerDetailUpdateSchema(Schema):
    """
    Schema for validating owner update details.

    Attributes
    ----------
    name : str
        Name of the owner.
    dob : DateTime
        Date of birth of the owner.
    gender : Gender
        Gender of the owner.
    address : AddressSchema
        Address details of the owner.
    """

    @staticmethod
    def validate_age(dob):
        """
        Validate that the owner's age is greater than 18.

        Parameters
        ----------
        dob : DateTime
            Date of birth of the owner.

        Raises
        ------
        ValidationError
            If the owner's age is less than 18.
        """
        if dob:
            age = (datetime.now() - dob).days // 365
            if age < 18:
                raise ValidationError("Age must be greater than 18.")

    name = fields.String(
        validate=validate.Length(
            min=3,
            max=20,
        ),
    )
    dob = fields.DateTime(
        validate=validate_age,
    )
    gender = fields.Enum(
        Gender,
    )
    address = fields.Nested(
        AddressSchema,
    )
