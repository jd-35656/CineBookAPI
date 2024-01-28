"""
Dev Config Module
===================

Classes
-------
DevConfig: BaseConfig
    Dev configuration class.
"""
from src.main.config.base_config import BaseConfig


class DevConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """
    Dev configuration class.
    """

    DEBUG: int = 1
