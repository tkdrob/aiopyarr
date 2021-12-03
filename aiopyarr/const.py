"""PyArr constants."""
from enum import Enum
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

ATTR_DATA = "data"


class HTTPMethod(Enum):
    """HTTPMethod Enum."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HTTPResponse(Enum):
    """HTTPResponse Enum."""

    OK = 200
    UNAUTHORIZED = 401
    RESOURCENOTFOUND = 404
