"""PyArr constants."""
from enum import Enum
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

ATTR_DATA = "data"

HEADERS = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}


class HTTPMethod(Enum):
    """HTTPMethod Enum."""

    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
