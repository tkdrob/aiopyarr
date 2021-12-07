"""PyArrHostConfiguration."""
from __future__ import annotations

from dataclasses import dataclass

from .. import ArrException


@dataclass
class PyArrHostConfiguration:  # pylint: disable=too-many-instance-attributes
    """PyArrHostConfiguration."""

    api_token: str | None = None
    hostname: str | None = None
    ipaddress: str | None = None
    port: int | None = None
    ssl: bool = False
    verify_ssl: bool = True
    base_api_path: str | None = None
    url: str | None = None
    api_ver: str = "v3"

    def __post_init__(self) -> None:
        """Post init."""
        if self.api_token is None:
            raise ArrException(message="No api token to the server was provided")
        if self.hostname is None and self.ipaddress is None and self.url is None:
            raise ArrException(
                message="No url, hostname or ipaddress to the server was provided"
            )

    def api_url(self, command: str) -> str:
        """Return the generated base URL based on host configuration."""
        return f"{self.base_url}/api/{self.api_ver}/{command}?apikey={self.api_token}"

    @property
    def base_url(self) -> str:
        """Return the base URL for the configured service."""
        if self.url is not None:
            return self.url
        protocol = f"http{'s' if self.ssl else ''}"
        host = self.hostname or self.ipaddress
        if self.port:
            host = f"{host}:{self.port}"
        return f"{protocol}://{host}{self.base_api_path or ''}"
