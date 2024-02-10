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
from src.owner_auth.model import OwnerSessionModel
from src.owner_auth.schema import OwnerLoginSchema, SessionSchema
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

    @staticmethod
    def login_service(data: Dict[str, Any]) -> Dict[str, Any]:
        with db.session() as session:
            schema = OwnerLoginSchema()
            serialized_data = schema.load(data)

            owner = (
                session.query(
                    OwnerModel,
                )
                .filter_by(
                    **serialized_data,  # type: ignore
                )
                .first()
            )

            if not owner:
                raise ValueError(
                    "Invalide credentials"
                )  # pylint: disable=all # type: ignore

            session_schema = SessionSchema()
            sess_data = session_schema.load({"owner_id": owner.id})
            sess = OwnerSessionModel(**sess_data)  # type: ignore
            session.add(sess)
            session.commit()

            deserialize_data = session_schema.dump(sess)

            return deserialize_data  # type: ignore

    @staticmethod
    def logout_service(header: Dict[str, Any]) -> None:
        session_id = header["Authorization"]
        with db.session() as session:
            session.query(
                OwnerSessionModel,
            ).filter_by(
                session_id=session_id,
            ).delete()
