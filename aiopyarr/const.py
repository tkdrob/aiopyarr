"""PyArr constants."""
from enum import Enum
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

ALL = "all"
ASCENDING = "ascending"
ATTR_DATA = "data"
DESCENDING = "descending"
IS_VALID = "isValid"

HEADERS = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}
PAGE = "page"
PAGE_SIZE = "pageSize"
SORT_DIRECTION = "sortDirection"
SORT_KEY = "sortKey"

class HTTPMethod(Enum):
    """HTTPMethod Enum."""

    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
