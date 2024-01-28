"""
Config Package
==============

Attributes
----------
config: BaseConfig
    Returns the config for flask app.

Example
-------
>>>from flask import Flask
>>>from config import config
>>>app = Flask(__name__)
>>>app.config.from_object(config)
>>># Other codes goes here.
"""

from src.main.config.app_config import get_config
from src.main.config.base_config import BaseConfig

config: BaseConfig = get_config()
