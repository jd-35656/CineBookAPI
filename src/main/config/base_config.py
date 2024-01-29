"""
Base Config Module
===================

Classes
-------
BaseConfig: class
    Base configuration class.
"""


import os
from typing import Optional


class BaseConfig:  # pylint: disable=too-few-public-methods
    """
    Base configuration class.
    """

    DATABASE_URI: Optional[str] = os.environ.get("DATABASE_URI")
