"""
Defines the OwnerModel class representing owners in the system.

This module provides the OwnerModel class, which represents owners in
the system. It includes attributes such as id, email, phone number,
password, creation date, and last update date.

Attributes
----------
id : Mapped[UUID]
    The unique identifier for the owner, generated using UUID version 1.
email : Mapped[str]
    The email address of the owner.
phone : Mapped[int]
    The phone number of the owner.
password : Mapped[str]
    The password associated with the owner's account.
created : Mapped[datetime]
    The datetime when the owner's account was created.
updated : Mapped[datetime]
    The datetime when the owner's account was last updated.
"""

from datetime import datetime
from uuid import UUID, uuid1

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from src.main.database.base import Base


class OwnerModel(Base):  # pylint: disable= too-few-public-methods
    """
    Represents an owner in the system.

    Attributes
    ----------
    id : Mapped[UUID]
        The unique identifier for the owner, generated using UUID version 1.
    email : Mapped[str]
        The email address of the owner.
    phone : Mapped[int]
        The phone number of the owner.
    password : Mapped[str]
        The password associated with the owner's account.
    created : Mapped[datetime]
        The datetime when the owner's account was created.
    updated : Mapped[datetime]
        The datetime when the owner's account was last updated.
    """

    __tablename__ = "owners"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid1(),
    )
    email: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
    )
    phone: Mapped[int] = mapped_column(
        unique=True,
    )
    password: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    created: Mapped[datetime] = mapped_column(
        default=datetime.now().isoformat(),
    )
    updated: Mapped[datetime] = mapped_column(
        default=datetime.now().isoformat(),
        onupdate=datetime.now().isoformat(),
    )
