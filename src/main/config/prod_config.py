"""
Prod Config Module
===================

Classes
-------
ProdConfig: BaseConfig
    Prod configuration class.
"""
from src.main.config.base_config import BaseConfig


class ProdConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """
    Prod configuration class.
    """

    DEBUG: int = 1
