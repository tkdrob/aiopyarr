"""Shared API."""
from __future__ import annotations

import asyncio
from copy import copy
from typing import TYPE_CHECKING

from aiohttp.client import ClientSession, ClientTimeout, ClientError

from aiopyarr.models.sonarr import Logs

from .const import ATTR_DATA, LOGGER, HTTPMethod
from .models.host_configuration import PyArrHostConfiguration
from .models.response import PyArrResponse

from .exceptions import (  # isort:skip
    ArrAuthenticationException,
    ArrConnectionException,
    ArrException,
    ArrResourceNotFound,
)

if TYPE_CHECKING:
    from aiopyarr.models.base import BaseModel


class RequestClient:
    """Base class for API Client."""

    _close_session = False
    _from_aenter = False

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        port: int | None = None,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 30,
        raw_response: bool = False,
        redact: bool = True,
    ) -> None:
        """Initialize."""
        if host_configuration is None:
            host_configuration = PyArrHostConfiguration(
                hostname=hostname, ipaddress=ipaddress, url=url, api_token=api_token
            )
        else:
            host_configuration = copy(host_configuration)
        if port is not None and host_configuration.port is None:
            host_configuration.port = port
        if ssl is not None:
            host_configuration.ssl = ssl
        if verify_ssl is not None:
            host_configuration.verify_ssl = verify_ssl
        if base_api_path is not None:
            host_configuration.base_api_path = base_api_path

        if session is None:
            session = ClientSession()
            self._close_session = True

        self._host = host_configuration
        self._session = session
        self._request_timeout = request_timeout
        self._raw_response = raw_response
        self._redact = redact

    async def __aenter__(self) -> RequestClient:
        """Async enter."""
        self._from_aenter = True
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        if self._session and self._close_session:
            await self._session.close()

    def redact_string(self, string: str) -> str:
        """Redact a api token from a string if needed."""
        if not self._redact:
            return string

        return string.replace(self._host.api_token, "[REDACTED_API_TOKEN]")

    async def _async_request(
        self,
        *args,
        params: dict | None = None,
        data: dict | None = None,
        datatype: BaseModel | None = None,
        method: HTTPMethod = HTTPMethod.GET,
    ):
        """Send API request."""
        command = args[0] if isinstance(args[0], str) else args[1]
        url = self._host.api_url(command)
        try:
            request = await self._session.request(
                method=method.value,
                url=url,
                params=params,
                json=data,
                verify_ssl=self._host.verify_ssl,
                timeout=ClientTimeout(self._request_timeout),
            )

            if request.status != 200:

                if request.status == 401:
                    raise ArrAuthenticationException(self, request)
                if request.status == 404:
                    raise ArrResourceNotFound(self, request)
                raise ArrConnectionException(
                    self,
                    f"Request for '{url}' failed with status code '{request.status}'",
                )

            _result: dict = await request.json()

            response = PyArrResponse(
                data={ATTR_DATA: _result},
                datatype=datatype,
            )

            LOGGER.debug("Requesting %s returned %s", self.redact_string(url), _result)

            if self._raw_response:
                return _result

        except ClientError as exception:
            raise ArrConnectionException(
                self,
                f"Request exception for '{url}' with - {exception}",
            ) from exception

        except asyncio.TimeoutError as ex:
            raise ArrConnectionException(self, f"Request timeout for '{url}'") from ex

        except ArrAuthenticationException as ex:
            raise ArrAuthenticationException(self, ex) from ex

        except ArrConnectionException as ex:
            raise ArrConnectionException(self, ex) from ex

        except ArrException as ex:
            raise ArrException(self, ex) from ex

        except (Exception, BaseException) as ex:
            raise ArrException(self, ex) from ex

        else:
            return response.data

    async def async_get_logs(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "time",
        sort_asc: bool = False,
        filter_key: str | None = None,
        filter_value: str = "All",
    ) -> Logs:
        """Get logs.

        Args:
            page: Specifiy page to return.
            page_size: Number of items per page.
            sort_key: Field to sort by.
            sort_asc: Sort items in ascending order.
            filter_key: Key to filter by.
            filter_value: Value of the filter.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortKey": sort_key,
            "sortDir": "asc" if sort_asc is True else "desc",
            "filterKey": str(filter_key),
            "filterValue": filter_value,
        }
        return await self._async_request("log", params=params, datatype=Logs)
