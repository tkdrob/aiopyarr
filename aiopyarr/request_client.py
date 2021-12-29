"""Shared API."""
from __future__ import annotations

import asyncio
from copy import copy
from typing import Any

from aiohttp.client import ClientError, ClientSession, ClientTimeout

from aiopyarr.decorator import api_command

from .const import ATTR_DATA, LOGGER, HTTPMethod, HTTPResponse
from .models.host_configuration import PyArrHostConfiguration
from .models.response import PyArrResponse

from .models.common import (  # isort:skip
    Command,
    CustomFilter,
    Diskspace,
    HostConfig,
    LogFiles,
    Logs,
    RootFolder,
    SystemBackup,
    SystemStatus,
    Tag,
    UIConfig,
)

from .exceptions import (  # isort:skip
    ArrAuthenticationException,
    ArrConnectionException,
    ArrException,
    ArrResourceNotFound,
)


class RequestClient:
    """Base class for API Client."""

    _close_session = False
    _from_aenter = False

    def __init__(  # pylint: disable=too-many-arguments
        self,
        port: int,
        request_timeout: float,
        raw_response: bool,
        redact: bool,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        api_ver: str | None = None,
    ) -> None:
        """Initialize."""
        if host_configuration is None:
            host_configuration = PyArrHostConfiguration(
                hostname=hostname,
                ipaddress=ipaddress,
                url=url,
                api_token=api_token,
                api_ver=api_ver,
            )
        else:
            host_configuration = copy(host_configuration)
        host_configuration.port = port
        if ssl is not None:
            host_configuration.ssl = ssl
        if verify_ssl is not None:
            host_configuration.verify_ssl = verify_ssl
        if base_api_path is not None:
            host_configuration.base_api_path = base_api_path
        if api_ver is not None:
            host_configuration.api_ver = api_ver

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
        if not self._redact or not self._host.api_token:
            return string

        return string.replace(self._host.api_token, "[REDACTED_API_TOKEN]")

    async def _async_request(
        self,
        *args,
        params: dict | None = None,
        data: Any = None,
        datatype: Any = None,
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

        #except (Exception, BaseException) as ex:
        #    raise ArrException(self, ex) from ex

        else:
            return response.data

    @api_command("diskspace", datatype=Diskspace)
    async def async_get_diskspace(self) -> list[Diskspace]:
        """Get information about diskspace."""

    @api_command("rootfolder", datatype=RootFolder)
    async def async_get_root_folders(self) -> list[RootFolder]:
        """Get information about root folders."""

    @api_command("config/host", datatype=HostConfig)
    async def async_get_host_config(self) -> HostConfig:
        """Get information about host configuration."""

    async def async_update_host_config(self, data: HostConfig) -> HTTPResponse:
        """Edit General/Host settings for Radarr."""
        return await self._async_request(
            "config/host",
            data=data,
            datatype=HostConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("config/ui", datatype=UIConfig)
    async def async_get_ui_config(self) -> UIConfig:
        """Get information about UI configuration."""

    async def async_get_logs(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "time",
        sort_asc: bool = False,
    ) -> Logs:
        """Get logs.

        Args:
            page: Specifiy page to return.
            page_size: Number of items per page.
            sort_key: Field to sort by. id, level, logger, time
            sort_asc: Sort items in ascending order.
            filter_key: Key to filter by.
            filter_value: Value of the filter.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortKey": sort_key,
            "sortDir": "ascending" if sort_asc is True else "descending",
        }
        return await self._async_request("log", params=params, datatype=Logs)

    async def async_get_commands(
        self, cmdid: int | None = None
    ) -> Command | list[Command]:
        """Query the status of a previously started command, or all currently started commands."""
        return await self._async_request(
            f"command{f'/{cmdid}' if cmdid is not None else ''}",
            datatype=Command,
        )

    @api_command("log/file", datatype=LogFiles)
    async def async_get_log_file(self) -> list[LogFiles]:
        """Get log file."""

    @api_command("system/status", datatype=SystemStatus)
    async def async_get_system_status(self) -> SystemStatus:
        """Get information about system status."""

    @api_command("system/backup", datatype=SystemBackup)
    async def async_get_system_backup(self) -> list[SystemBackup]:
        """Get information about system backup."""

    async def async_restore_system_backup(self, backupid: int) -> HTTPResponse:
        """Restore from a system backup."""
        return await self._async_request(
            f"system/backup/restore/{backupid}", method=HTTPMethod.POST
        )

    # Upload system backup not working

    async def async_delete_system_backup(self, backupid: int) -> HTTPResponse:
        """Delete a system backup."""
        return await self._async_request(
            f"system/backup/{backupid}", method=HTTPMethod.DELETE
        )

    async def async_get_tags(self, tagid: int | None = None) -> Tag | list[Tag]:
        """Return all tags or specific tag by database id.

        id: Get tag matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag{f'/{tagid}' if tagid is not None else ''}",
            datatype=Tag,
        )

    async def async_get_custom_filters(
        self, filterid: int | None = None
    ) -> CustomFilter | list[CustomFilter]:
        """Get information about custom filters."""
        return await self._async_request(
            f"customfilter{f'/{filterid}' if filterid is not None else ''}",
            datatype=CustomFilter,
        )

    async def async_add_custom_filter(self, data: CustomFilter) -> CustomFilter:
        """Add a custom filter."""
        return await self._async_request(
            "customfilter", data=data, datatype=CustomFilter, method=HTTPMethod.POST
        )

    async def async_edit_custom_filter(
        self, filterid: int, data: CustomFilter
    ) -> CustomFilter:
        """Edit a custom filter."""
        return await self._async_request(
            f"customfilter/{filterid}",
            data=data,
            datatype=CustomFilter,
            method=HTTPMethod.PUT,
        )

    async def async_delete_custom_filter(self, filterid: int) -> HTTPResponse:
        """Delete a custom filter."""
        return await self._async_request(
            f"customfilter/{filterid}", datatype=CustomFilter, method=HTTPMethod.DELETE
        )
