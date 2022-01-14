"""Exceptions for Arr Api Client."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

    from .request_client import RequestClient


class ArrException(Exception):
    """Base arr exception."""

    def __init__(
        self,
        client: RequestClient | None = None,
        message: str | BaseException | ClientResponse | Exception = "",
    ) -> None:
        """Initialize."""
        super().__init__(str(message) if client is not None else message)


class ArrConnectionException(ArrException):
    """Arr connection exception."""


class ArrAuthenticationException(ArrException):
    """Arr authentication exception."""


class ArrResourceNotFound(ArrException):
    """Arr resource not found exception."""


class ArrInvalidCommand(ArrException):
    """Arr invalid command exception."""
