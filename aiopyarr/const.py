"""PyArr constants."""
from enum import Enum
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

ALBUM_ID = "albumId"
ALL = "all"
ARTIST_ID = "artistId"
ATTR_DATA = "basedata"
AUTHOR_ID = "authorId"
BOOK_ID = "bookId"
DATE = "date"
EPISODE_ID = "episodeId"
EVENT_TYPE = "eventType"
HEADERS = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}
HEADERS_JS = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/javascript",
    "Content-Type": "application/javascript",
}
IS_VALID = "isValid"
MOVIE_ID = "movieId"
NOTIFICATION = "notification"
PAGE = "page"
PAGE_SIZE = "pageSize"
PATH = "path"
SERIES_ID = "seriesId"
SORT_DIRECTION = "sortDirection"
SORT_KEY = "sortKey"
TERM = "term"
TITLE = "title"


class HTTPMethod(Enum):
    """HTTPMethod Enum."""

    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
