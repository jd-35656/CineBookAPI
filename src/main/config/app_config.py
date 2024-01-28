"""
Configuration Module
====================

This module provides functions to retrieve configuration objects for a
Flask app based on the current environment.

Functions
---------
get_config() -> BaseConfig:
    Returns the configuration object based on the current environment.

    The function checks the value of the "ENVIRONMENT" environment variable and
    returns the corresponding configuration object.

    Returns
    -------
    BaseConfig
        The configuration object for the Flask app.
"""
import os
from typing import Any, Dict

from src.main.config.base_config import BaseConfig
from src.main.config.dev_config import DevConfig
from src.main.config.prod_config import ProdConfig


def get_config() -> BaseConfig:
    """
    Returns the config for Flask App.

    Returns
    --------
        BaseConfig
            Returns the config for Flask App.
    """
    config_dict: Dict[str, Any] = {
        "DEV": DevConfig,
        "PROD": ProdConfig,
    }
    env: str = os.environ.get("ENVIRONMENT", "DEV")
    config: BaseConfig = config_dict[env]
    return config
