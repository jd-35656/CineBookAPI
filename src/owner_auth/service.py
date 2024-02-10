"""
Module defining the OwnerSessionService class for handling owner auth.

This module contains the OwnerSessionService class, which provides methods for
handling the registration of owners and their details.

Classes
-------
OwnerSessionService
    Service class for handling owner auth.

"""

from typing import Any, Dict

from src.main.database import db
from src.owner.model import OwnerModel
from src.owner.schema import OwnerSchema
from src.owner_detail.model import OwnerDetailModel
from src.owner_detail.schema import OwnerDetailSchema


class OwnerSessionService:
    """
    Service class for handling owner registration.

    Provides methods to handle the registration of owners and their details.

    Methods
    -------
    register_service(data: Dict[str, Any])
        Handles the registration of an owner and their details.

        Parameters
        ----------
        data : Dict[str, Any]
            Data containing owner and owner detail information.

        Raises
        ------
        Exception
            If an error occurs during registration.
    """

    @staticmethod
    def register_service(data: Dict[str, Any]) -> None:
        """
        Handles the registration of an owner and their details.

        Parameters
        ----------
        data : Dict[str, Any]
            Data containing owner and owner detail information.

        Raises
        ------
        Exception
            If an error occurs during registration.
        """

        with db.transaction() as session:

            owner_schema = OwnerSchema()
            raw_owner_data = data.get("owner", {})
            serialize_owner_data = owner_schema.load(raw_owner_data)
            owner_data = OwnerModel(**serialize_owner_data)  # type: ignore
            session.add(owner_data)

            session.flush()

            owner_detail_schema = OwnerDetailSchema()
            raw_owner_detail_data = data.get("owner_detail", {})
            raw_owner_detail_data["owner_id"] = owner_data.id
            serialize_owner_detail_data = owner_detail_schema.load(
                raw_owner_detail_data
            )
            owner_detail_data = OwnerDetailModel(
                **serialize_owner_detail_data,  # type: ignore
            )
            session.add(owner_detail_data)
