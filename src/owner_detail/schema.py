from datetime import datetime
from enum import Enum

from marshmallow import Schema, ValidationError, fields, validate


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class AddressSchema(Schema):
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

    @staticmethod
    def validate_age(dob):
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
        dump_only=True,
    )
