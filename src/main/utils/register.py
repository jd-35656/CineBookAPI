"""Utility function for registering Flask blueprints."""

from typing import Dict, Union

from flask import Blueprint


# pylint: disable=unused-argument
def register(
    blueprint: Blueprint,
    url_prefix: str,
    name: str,
) -> Dict[str, Union[str, Blueprint]]:
    """
    Register a Flask blueprint with additional metadata.

    Parameters:
        blueprint (Blueprint): The Flask blueprint to register.
        endpoint (str): The endpoint at which the blueprint will be accessible.
        name (str): The name of the blueprint.

    Returns:
        dict: A dictionary containing metadata about the registered blueprint.
            - 'blueprint': The Flask blueprint object.
            - 'endpoint': The endpoint at which the blueprint is accessible.
            - 'name': The name of the blueprint.
    """
    return {
        "blueprint": blueprint,
        "url_prefix": url_prefix,
        "name": name,
    }
