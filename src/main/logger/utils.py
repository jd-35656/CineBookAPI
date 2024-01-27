"""
Logger Utils Module
===================

This module provides utility functions for working with logging
in Flask applications.

Functions
---------
parse_body(
    request_response: Union[Request, Response]
    ) -> Optional[Dict[str, Any]]:
    Parse the body of a Flask Request or Response object based on
    the Content-Type.

    Parameters
    ----------
    request_response : Union[Request, Response]
        The Flask Request or Response object.

    Returns
    -------
    Optional[Dict[str, Any]]
        Parsed JSON content of the body if Content-Type is
        'application/json', else None.

"""

import json
from typing import Any, Dict, Optional, Union

from flask import Request, Response


def parse_body(
    request_response: Union[Request, Response]
) -> Optional[Dict[str, Any]]:
    """
    Parse the body of a Flask Request or Response object based on
    the Content-Type.

    Parameters
    ----------
    request_response : Union[Request, Response]
        The Flask Request or Response object.

    Returns
    -------
    Optional[Dict[str, Any]]
        Parsed JSON content of the body if Content-Type is
        'application/json', else None.
    """
    content_type: str = request_response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        try:
            return json.loads(request_response.data.decode("utf-8"))
        except json.JSONDecodeError:
            return None
    return None
