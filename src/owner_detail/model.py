"""
Module containing SQLAlchemy model for Owner details.

This module defines the SQLAlchemy model `OwnerModel` to
represent details of owners, including their identification,
personal information, and timestamps.

Classes:
    OwnerDetailModel: SQLAlchemy model representing owner details.
"""

from datetime import datetime
from typing import Dict, Union
from uuid import UUID, uuid1

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.main.database.base import Base


class OwnerDetailModel(Base):  # pylint: disable= too-few-public-methods
    """
    SQLAlchemy model for representing owner details.

    Attributes:
        id (Mapped[UUID]): Unique identifier for the owner.
        name (Mapped[str]): Name of the owner.
        dob (Mapped[datetime]): Date of birth of the owner.
        gender (Mapped[str]): Gender of the owner.
        address (Mapped[Dict[str, Union[str, int]]]): Address
            details of the owner.
        created (Mapped[datetime]): Timestamp indicating when
            the record was created.
        updated (Mapped[datetime]): Timestamp indicating when
            the record was last updated.

    """

    __tablename__ = "owner_details"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid1(),
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
    )
    dob: Mapped[datetime] = mapped_column(
        nullable=False,
    )
    gender: Mapped[str] = mapped_column(
        nullable=False,
    )
    address: Mapped[Dict[str, Union[str, int]]] = mapped_column(
        JSON,
        nullable=False,
    )
    created: Mapped[datetime] = mapped_column(
        default=datetime.now().isoformat(),
    )
    updated: Mapped[datetime] = mapped_column(
        default=datetime.now().isoformat(),
        onupdate=datetime.now().isoformat(),
    )
    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey("owners.id"),
        nullable=False,
        unique=True,
    )
