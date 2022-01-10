"""Decorator for pyarr."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .const import HTTPMethod

if TYPE_CHECKING:
    from .request_client import RequestClient


def api_command(
    command: str,
    params: dict | None = None,
    data: dict | None = None,
    datatype: Any = None,
    method: HTTPMethod = HTTPMethod.GET,
):
    """Initialize decorator for PyArr API request."""

    def decorator(_):
        """Initialize decorator."""

        async def wrapper(*args: Any):
            """Initialize wrapper."""
            client: RequestClient = args[0]
            return await client._async_request(  # pylint: disable=protected-access
                *args,
                command,
                params=params,
                data=data,
                datatype=datatype,
                method=method
            )

        return wrapper

    return decorator
