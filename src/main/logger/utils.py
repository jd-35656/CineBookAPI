"""
Logger Utils Module
===================

This module provides utility functions for working with logging
in Flask applications.

Functions
---------
parse_request(request_data: Request) -> Dict[str, Any]:
    Parse a Flask Request object and create a dictionary representation.

    Parameters
    ----------
    request_data : Request
        The Flask Request object to be parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary representation of the parsed request.

parse_response(response_data: Response) -> Dict[str, Any]:
    Parse a Flask Response object and create a dictionary representation.

    Parameters
    ----------
    response_data : Response
        The Flask Response object to be parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary representation of the parsed response.

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

parse_header(headers: Dict[str, Any]) -> Dict[str, Any]:
    Parse headers, obfuscating sensitive information
    (e.g., authorization, cookie).

    Parameters
    ----------
    headers : Dict[str, Any]
        The headers to be parsed.

    Returns
    -------
    Dict[str, Any]
        The parsed headers with sensitive information obfuscated.
"""

import json
from typing import Any, Dict, Optional, Union

from flask import Request, Response


def parse_request(request_data: Request) -> Dict[str, Any]:
    """
    Parse a Flask Request object and create a dictionary representation.

    Parameters
    ----------
    request_data : Request
        The Flask Request object to be parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary representation of the parsed request.
    """
    return {
        "title": (
            f"{request_data.method} {request_data.path} "
            f'{request_data.environ["SERVER_PROTOCOL"]}'
        ),
        "timestamp": str(request_data.timestamp),  # type: ignore
        "body": {
            "event": "Request received",
            "details": {
                "method": request_data.method,
                "host": request_data.host,
                "path": request_data.path,
                "headers": parse_header(request_data.headers),
                "body": parse_body(request_data),
            },
        },
    }


def parse_response(response_data: Response) -> Dict[str, Any]:
    """
    Parse a Flask Response object and create a dictionary representation.

    Parameters
    ----------
    response_data : Response
        The Flask Response object to be parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary representation of the parsed response.
    """
    return {
        "title": f"{response_data.status_code}",
        "timestamp": str(response_data.timestamp),  # type: ignore
        "details": {
            "status_code": response_data.status_code,
            "headers": parse_header(response_data.headers),
            "body": parse_body(response_data),
        },
    }


def parse_header(headers: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse headers, obfuscating sensitive information
    (e.g., authorization, cookie).

    Parameters
    ----------
    headers : Dict[str, Any]
        The headers to be parsed.

    Returns
    -------
    Dict[str, Any]
        The parsed headers with sensitive information obfuscated.
    """
    res: Dict[str, Any] = {}
    for key, value in headers.items():
        if any(
            keyword in key.lower() for keyword in ["authorization", "cookie"]
        ):
            res[key] = "*****"
        else:
            res[key] = value
    return res


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
