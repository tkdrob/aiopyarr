"""Shared API."""
# pylint: disable=too-many-lines
from __future__ import annotations

import asyncio
from copy import copy
from json import dumps
from typing import Any, Text

from aiohttp.client import ClientError, ClientSession, ClientTimeout

from .const import ATTR_DATA, HEADERS, LOGGER, HTTPMethod
from .decorator import api_command
from .models.host_configuration import PyArrHostConfiguration
from .models.response import PyArrResponse

from .models.request import (  # isort:skip
    Command,
    Commands,
    CustomFilter,
    Diskspace,
    DownloadClient,
    DownloadClientConfig,
    Filesystem,
    Health,
    HostConfig,
    ImportListExclusion,
    Indexer,
    IndexerConfig,
    Language,
    Localization,
    LogFile,
    Logs,
    MediaManagementConfig,
    MetadataConfig,
    QualityDefinition,
    QualityProfile,
    QueueStatus,
    ReleaseProfile,
    RemotePathMapping,
    RootFolder,
    SystemBackup,
    SystemStatus,
    SystemTask,
    Tag,
    UIConfig,
    Update,
)

from .exceptions import (  # isort:skip
    ArrAuthenticationException,
    ArrConnectionException,
    ArrException,
    ArrResourceNotFound,
)


class RequestClient:  # pylint: disable=too-many-public-methods
    """Base class for API Client."""

    _close_session = False
    _from_aenter = False

    def __init__(  # pylint: disable=too-many-arguments
        self,
        port: int,
        request_timeout: float,
        raw_response: bool,
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
        user_agent: str | None = None,
    ) -> None:
        """Initialize."""
        if host_configuration is None:
            host_configuration = PyArrHostConfiguration(
                api_token=api_token,
                hostname=hostname,
                ipaddress=ipaddress,
                port=port,
                url=url,
                api_ver=api_ver,
            )
        else:
            host_configuration = copy(host_configuration)
        if host_configuration.port is None:
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
            if user_agent:
                HEADERS["User-Agent"] = user_agent
            session = ClientSession(headers=HEADERS)
            self._close_session = True

        self._host = host_configuration
        self._session = session
        self._request_timeout = request_timeout
        self._raw_response = raw_response

    async def __aenter__(self) -> RequestClient:
        """Async enter."""
        self._from_aenter = True
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        if self._session and self._close_session:
            await self._session.close()

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
        json = dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        try:
            request = await self._session.request(
                method=method.value,
                url=url,
                params=params,
                json=json,
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

            LOGGER.debug("Requesting %s returned %s", url, _result)

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

    @api_command("diskspace", datatype=Diskspace)
    async def async_get_diskspace(self) -> list[Diskspace]:
        """Get information about diskspace."""

    async def async_get_root_folders(
        self, folderid: int | None = None
    ) -> RootFolder | list[RootFolder]:
        """Get information about root folders."""
        return await self._async_request(
            f"rootfolder{'' if folderid is None else f'/{folderid}'}",
            datatype=RootFolder,
        )

    async def async_delete_root_folder(self, folderid: int) -> None:
        """Delete information about root folders."""
        return await self._async_request(
            f"rootfolder/{folderid}", method=HTTPMethod.DELETE
        )

    async def async_add_root_folder(self, data: RootFolder) -> RootFolder:
        """Add information about root folders."""
        return await self._async_request(
            "rootfolder", data=data, datatype=RootFolder, method=HTTPMethod.POST
        )

    @api_command("config/host", datatype=HostConfig)
    async def async_get_host_config(self) -> HostConfig:
        """Get information about host configuration."""

    async def async_edit_host_config(self, data: HostConfig) -> HostConfig:
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

    async def async_edit_ui_config(self, data: UIConfig) -> UIConfig:
        """Edit one or many UI settings and save to to the database."""
        return await self._async_request(
            "config/ui",
            data=data,
            datatype=UIConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_logs(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "time",
        ascending: bool = False,
    ) -> Logs:
        """Get logs.

        Args:
            page: Specifiy page to return.
            page_size: Number of items per page.
            sort_key: Field to sort by id, level, logger, time, or message
            ascending: Sort items in ascending order.
            filter_key: Key to filter by.
            filter_value: Value of the filter.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortKey": sort_key,
            "sortDir": "ascending" if ascending is True else "descending",
        }
        return await self._async_request("log", params=params, datatype=Logs)

    async def async_get_commands(
        self, cmdid: int | None = None
    ) -> Command | list[Command]:
        """Query the status of a previously started command, or all currently started commands."""
        return await self._async_request(
            f"command{'' if cmdid is None else f'/{cmdid}'}",
            datatype=Command,
        )

    async def async_command(self, command: Commands) -> Command:
        """Send a command to the API."""
        return await self._async_request(
            "command",
            data={"name": command},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_delete_command(self, commandid: int) -> None:
        """Cancel a pending command."""
        return await self._async_request(
            f"command/{commandid}", method=HTTPMethod.DELETE
        )

    @api_command("log/file", datatype=LogFile)
    async def async_get_log_file(self) -> list[LogFile]:
        """Get log file."""

    async def async_get_log_file_content(self, file: str) -> Text:
        """Get log file content."""
        return await self._async_request(f"log/file/{file}")

    @api_command("log/file/update", datatype=LogFile)
    async def async_get_log_file_updates(self) -> list[LogFile]:
        """Get log file updates."""

    async def async_get_log_file_update_content(self, file: str) -> Text:
        """Get log file update content."""
        return await self._async_request(f"log/file/update/{file}")

    @api_command("system/status", datatype=SystemStatus)
    async def async_get_system_status(self) -> SystemStatus:
        """Get information about system status."""

    @api_command("system/backup", datatype=SystemBackup)
    async def async_get_system_backup(self) -> list[SystemBackup]:
        """Get information about system backup."""

    async def async_restore_system_backup(self, backupid: int) -> None:
        """Restore from a system backup."""
        return await self._async_request(
            f"system/backup/restore/{backupid}", method=HTTPMethod.POST
        )

    # Upload system backup not working

    async def async_delete_system_backup(self, backupid: int) -> None:
        """Delete a system backup."""
        return await self._async_request(
            f"system/backup/{backupid}", method=HTTPMethod.DELETE
        )

    async def async_get_tags(self, tagid: int | None = None) -> Tag | list[Tag]:
        """Return all tags or specific tag by database id.

        id: Get tag matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag{'' if tagid is None else f'/{tagid}'}",
            datatype=Tag,
        )

    # tag PUT may not work

    async def async_edit_tag(self, data: Tag) -> Tag:
        """Edit a tag by its database id."""
        return await self._async_request(
            "tag",
            data=data,
            datatype=Tag,
            method=HTTPMethod.PUT,
        )

    async def async_delete_tag(self, tagid: int) -> None:
        """Delete a tag."""
        return await self._async_request(
            f"tag/{tagid}",
            method=HTTPMethod.DELETE,
        )

    # tag POST may not work, you can first create a tag by applying it to a movie

    async def async_add_tag(self, label: str) -> Tag:
        """Add a new tag.

        Can be assigned to a movie, list, delay profile, notification, or restriction.
        """
        return await self._async_request(
            "tag",
            data={"id": 0, "label": label},
            datatype=Tag,
            method=HTTPMethod.POST,
        )

    async def async_get_custom_filters(
        self, filterid: int | None = None
    ) -> CustomFilter | list[CustomFilter]:
        """Get information about custom filters."""
        return await self._async_request(
            f"customfilter{'' if filterid is None else f'/{filterid}'}",
            datatype=CustomFilter,
        )

    async def async_add_custom_filter(self, data: CustomFilter) -> CustomFilter:
        """Add a custom filter."""
        return await self._async_request(
            "customfilter", data=data, datatype=CustomFilter, method=HTTPMethod.POST
        )

    async def async_edit_custom_filter(self, data: CustomFilter) -> CustomFilter:
        """Edit a custom filter."""
        return await self._async_request(
            "customfilter",
            data=data,
            datatype=CustomFilter,
            method=HTTPMethod.PUT,
        )

    async def async_delete_custom_filter(self, filterid: int) -> None:
        """Delete a custom filter."""
        return await self._async_request(
            f"customfilter/{filterid}", method=HTTPMethod.DELETE
        )

    async def async_get_download_clients(
        self, clientid: int | None = None
    ) -> DownloadClient | list[DownloadClient]:
        """Get information about download client.

        clientid: Get downloadclient matching id. Leave blank for all.
        """
        return await self._async_request(
            f"downloadclient{'' if clientid is None else f'/{clientid}'}",
            datatype=DownloadClient,
        )

    async def async_add_download_client(self, data: DownloadClient) -> DownloadClient:
        """Add download client."""
        return await self._async_request(
            "downloadclient",
            data=data,
            datatype=DownloadClient,
            method=HTTPMethod.POST,
        )

    async def async_edit_download_client(self, data: DownloadClient) -> DownloadClient:
        """Edit download client."""
        return await self._async_request(
            "downloadclient",
            data=data,
            datatype=DownloadClient,
            method=HTTPMethod.PUT,
        )

    async def async_delete_download_client(self, clientid: int) -> None:
        """Delete download client."""
        return await self._async_request(
            f"downloadclient/{clientid}",
            method=HTTPMethod.DELETE,
        )

    # downloadclient/schema, not that useful

    async def async_test_download_clients(
        self, data: DownloadClient | None = None
    ) -> bool:
        """Test download client configurations."""
        _res = await self._async_request(
            f"downloadclient/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

    # downloadclient/action/{name}

    async def async_get_download_client_config(
        self, clientid: int | None = None
    ) -> DownloadClientConfig | list[DownloadClientConfig]:
        """Get download client config."""
        return await self._async_request(
            f"config/downloadclient{'' if clientid is None else f'/{clientid}'}",
            datatype=DownloadClientConfig,
        )

    async def async_edit_download_client_config(
        self, data: DownloadClientConfig
    ) -> DownloadClientConfig:
        """Edit download client config."""
        return await self._async_request(
            "config/downloadclient",
            data=data,
            datatype=DownloadClientConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("filesystem", datatype=Filesystem)
    async def async_get_filesystem(self) -> Filesystem:
        """Get filesystem attributes."""

    # filesystem/type / filesystem/mediafiles, use above method

    @api_command("health", datatype=Health)
    async def async_get_failed_health_checks(self) -> Health:
        """Get information about failed health checks."""

    async def async_delete_import_list(self, listid: int) -> None:
        """Delete an import list."""
        return await self._async_request(
            f"importlist/{listid}",
            method=HTTPMethod.DELETE,
        )

    # importlist/schema, not that useful

    # importlist/action/{name} cannot get working

    async def async_get_import_list_exclusions(
        self, clientid: int | None = None
    ) -> ImportListExclusion | list[ImportListExclusion]:
        """Get import list exclusions."""
        return await self._async_request(
            f"importlistexclusion{'' if clientid is None else f'/{clientid}'}",
            datatype=ImportListExclusion,
        )

    async def async_edit_import_list_exclusion(
        self, data: ImportListExclusion
    ) -> ImportListExclusion:
        """Edit import list exclusion."""
        return await self._async_request(
            "importlistexclusion",
            data=data,
            datatype=ImportListExclusion,
            method=HTTPMethod.PUT,
        )

    async def async_delete_import_list_exclusion(self, clientid: int) -> None:
        """Delete import list exclusion."""
        return await self._async_request(
            f"importlistexclusion/{clientid}",
            method=HTTPMethod.DELETE,
        )

    async def async_add_import_list_exclusion(
        self, data: ImportListExclusion
    ) -> ImportListExclusion:
        """Add import list exclusion."""
        return await self._async_request(
            "importlistexclusion",
            data=data,
            datatype=ImportListExclusion,
            method=HTTPMethod.POST,
        )

    async def async_get_indexers(
        self, indexerid: int | None = None
    ) -> Indexer | list[Indexer]:
        """Get all indexers or a single indexer by its database id.

        id: Get indexer matching id. Leave blank for all.
        """
        return await self._async_request(
            f"indexer{'' if indexerid is None else f'/{indexerid}'}",
            datatype=Indexer,
        )

    async def async_edit_indexer(self, data: Indexer) -> Indexer:
        """Edit an indexer."""
        return await self._async_request(
            "indexer",
            data=data,
            datatype=Indexer,
            method=HTTPMethod.PUT,
        )

    async def async_delete_indexer(self, indexerid: int) -> None:
        """Delete indexer by database id."""
        return await self._async_request(
            f"indexer/{indexerid}", method=HTTPMethod.DELETE
        )

    async def async_add_indexer(self, data: Indexer) -> Indexer:
        """Add an indexer."""
        return await self._async_request(
            "indexer",
            data=data,
            datatype=Indexer,
            method=HTTPMethod.POST,
        )

    # indexer/schema, not that useful

    async def async_test_indexers(self, data: Indexer | None = None) -> bool:
        """Test an indexer configuration."""
        _res = await self._async_request(
            f"indexer/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

    # indexer/action/{name} cannot get working

    async def async_get_indexer_configs(
        self, indexerid: int | None = None
    ) -> IndexerConfig | list[IndexerConfig]:
        """Get all indexer configs or a single config by its database id.

        id: Get indexer matching id. Leave blank for all.
        """
        return await self._async_request(
            f"config/indexer{'' if indexerid is None else f'/{indexerid}'}",
            datatype=IndexerConfig,
        )

    async def async_edit_indexer_config(self, data: IndexerConfig) -> IndexerConfig:
        """Edit an indexer config."""
        return await self._async_request(
            "config/indexer",
            data=data,
            datatype=IndexerConfig,
            method=HTTPMethod.PUT,
        )

    # initialize.js, no clue what this does

    async def async_get_languages(
        self, langid: int | None = None
    ) -> Language | list[Language]:
        """Get import list exclusions."""
        return await self._async_request(
            f"language{'' if langid is None else f'/{langid}'}",
            datatype=Language,
        )

    async def async_get_localization(self) -> Localization:
        """Get localization strings."""
        return await self._async_request("localization", datatype=Localization)

    # manualimport, cannot get working

    async def async_get_image(
        self,
        imageid: int,
        imagetype: str = "poster",
        size: str = "large",
        author: bool = False,
    ) -> bytes:
        """Get image from movie.

        imagetype: poster, banner, or fanart
        size: large, medium, small
              pixel size: None for full size (500, 250), (70, 35), (360, 180)
        authorid: Include to get author only applies to Readarr
        """
        value = [
            value * factor
            for key, factor in {"small": 1, "medium": 2, "large": 0}.items()
            if key == size
            for key, value in {"poster": 250, "banner": 35, "fanart": 180}.items()
            if imagetype == key
        ][0]
        _val = (
            "author/"
            if author
            else "book/"
            if hasattr(self, "async_get_author")
            else ""
        )
        _imgsize = f"-{value}" if size != "large" else ""

        cmd = f"mediacover/{_val}{imageid}/{imagetype}{_imgsize}.jpg"
        return await self._async_request(cmd)

    async def async_get_media_management_configs(
        self, configid: int | None = None
    ) -> MediaManagementConfig | list[MediaManagementConfig]:
        """Get media management configs."""
        return await self._async_request(
            f"config/mediamanagement{'' if configid is None else f'/{configid}'}",
            datatype=MediaManagementConfig,
        )

    async def async_edit_media_management_config(
        self, data: MediaManagementConfig
    ) -> MediaManagementConfig:
        """Edit media management config."""
        return await self._async_request(
            "config/mediamanagement",
            data=data,
            datatype=MediaManagementConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_metadata_configs(
        self, metadataid: int | None = None
    ) -> MetadataConfig | list[MetadataConfig]:
        """Get metadata configurations."""
        return await self._async_request(
            f"metadata{'' if metadataid is None else f'/{metadataid}'}",
            datatype=MetadataConfig,
        )

    async def async_edit_metadata_config(self, data: MetadataConfig) -> MetadataConfig:
        """Edit metadata configurations."""
        return await self._async_request(
            "metadata",
            data=data,
            datatype=MetadataConfig,
            method=HTTPMethod.PUT,
        )

    async def async_delete_metadata_config(self, metadataid: int) -> None:
        """Get metadata configurations."""
        return await self._async_request(
            f"metadata/{metadataid}", method=HTTPMethod.DELETE
        )

    async def async_add_metadata_config(self, data: MetadataConfig) -> MetadataConfig:
        """Add metadata configurations."""
        return await self._async_request(
            "metadata", data=data, datatype=MetadataConfig, method=HTTPMethod.POST
        )

    # metadata/schema, not that useful

    async def async_test_metadata(self, data: MetadataConfig | None = None) -> bool:
        """Test a metadata configuration."""
        _res = await self._async_request(
            f"metadata/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

    # metadata/action/{name} cannot get working

    async def async_delete_notification(self, notifyid: int) -> None:
        """Delete a notification."""
        return await self._async_request(
            f"notification/{notifyid}",
            method=HTTPMethod.DELETE,
        )

    # notification/schema, not that useful TODO try consolidating notifications

    async def async_test_all_notifications(self) -> bool:
        """Test all notification configurations."""
        _res = await self._async_request("notification/testall", method=HTTPMethod.POST)
        for item in _res:
            if item["isValid"] is False:
                return False
        return True

    # notification/action/{name} cannot get working

    async def async_get_quality_definitions(
        self, qualityid: int | None = None
    ) -> QualityDefinition | list[QualityDefinition]:
        """Get quality definitions."""
        return await self._async_request(
            f"qualitydefinition{'' if qualityid is None else f'/{qualityid}'}",
            datatype=QualityDefinition,
        )

    async def async_edit_quality_definition(
        self, data: QualityDefinition
    ) -> QualityDefinition:
        """Edit quality definition."""
        return await self._async_request(
            "qualitydefinition",
            data=data,
            datatype=QualityDefinition,
            method=HTTPMethod.PUT,
        )

    # qualitydefinition/update, no real difference from above method

    async def async_get_quality_profiles(
        self, profileid: int | None = None
    ) -> QualityProfile | list[QualityProfile]:
        """Get quality profiles."""
        return await self._async_request(
            f"qualityprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=QualityProfile,
        )

    async def async_delete_quality_profile(self, profileid: int) -> None:
        """Delete quality profile."""
        return await self._async_request(
            f"qualityprofile/{profileid}",
            method=HTTPMethod.DELETE,
        )

    async def async_edit_quality_profile(self, data: QualityProfile) -> QualityProfile:
        """Edit quality profile."""
        return await self._async_request(
            "qualityprofile",
            data=data,
            datatype=QualityProfile,
            method=HTTPMethod.PUT,
        )

    # qualityprofile/schema, not that useful

    async def async_delete_queue(
        self,
        ids: int | list[int],
        remove_from_client: bool = True,
        blocklist: bool = False,
    ) -> None:
        """Remove an item from the queue and optionally blocklist it.

        Args:
            ids: id of the item to be removed or mass deletion with a list
            remove_from_client: Remove the item from the client.
            blocklist: Add the item to the blocklist.
        """
        return await self._async_request(
            f"queue/{'bulk' if isinstance(ids, list) else ids}",
            params={
                "removeFromClient": str(remove_from_client),
                "blocklist": str(blocklist),
            },
            data={"ids": ids} if isinstance(ids, list) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_queue_grab(self, ids: int | list[int]) -> None:
        """Grab items in queue matching specified ids."""
        return await self._async_request(
            f"queue/grab/{'bulk' if isinstance(ids, list) else ids}",
            data={"ids": ids} if isinstance(ids, list) else None,
            method=HTTPMethod.POST,
        )

    @api_command("queue/status", datatype=QueueStatus)
    async def async_get_queue_status(self) -> QueueStatus:
        """Get information about download queue status."""

    async def async_delete_blocklists(self, ids: int | list[int]) -> None:
        """Delete blocklisted releases."""
        return await self._async_request(
            f"blocklist/{'bulk' if isinstance(ids, list) else ids}",
            params=None if isinstance(ids, list) else {"id": ids},
            data={"ids": ids} if isinstance(ids, list) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_get_release_profiles(
        self, profileid: int | None = None
    ) -> ReleaseProfile | list[ReleaseProfile]:
        """Get release profiles."""
        return await self._async_request(
            f"releaseprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=ReleaseProfile,
        )

    async def async_edit_release_profile(self, data: ReleaseProfile) -> ReleaseProfile:
        """Edit release profile."""
        return await self._async_request(
            "releaseprofile",
            data=data,
            datatype=ReleaseProfile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_release_profile(self, profileid: int) -> None:
        """Delete release profiles."""
        return await self._async_request(
            f"releaseprofile/{profileid}",
            method=HTTPMethod.DELETE,
        )

    async def async_add_release_profile(self, data: ReleaseProfile) -> ReleaseProfile:
        """Add release profile."""
        return await self._async_request(
            "releaseprofile",
            data=data,
            datatype=ReleaseProfile,
            method=HTTPMethod.POST,
        )

    async def async_get_remote_path_mappings(
        self, pathid: int | None = None
    ) -> RemotePathMapping | list[RemotePathMapping]:
        """Get information about remote path mappings."""
        return await self._async_request(
            f"remotepathmapping{'' if pathid is None else f'/{pathid}'}",
            datatype=RemotePathMapping,
        )

    async def async_delete_remote_path_mapping(self, pathid: int) -> None:
        """Delete information about remote path mappings."""
        return await self._async_request(
            f"remotepathmapping/{pathid}", method=HTTPMethod.DELETE
        )

    async def async_edit_remote_path_mapping(
        self, data: RemotePathMapping
    ) -> RemotePathMapping:
        """Edit information about remote path mappings."""
        return await self._async_request(
            "remotepathmapping",
            data=data,
            datatype=RemotePathMapping,
            method=HTTPMethod.PUT,
        )

    async def async_add_remote_path_mapping(
        self, data: RemotePathMapping
    ) -> RemotePathMapping:
        """Add information about remote path mappings."""
        return await self._async_request(
            "remotepathmapping",
            data=data,
            datatype=RemotePathMapping,
            method=HTTPMethod.POST,
        )

    @api_command("system/routes")
    async def async_get_system_routes(self) -> Any:
        """Get system rout information. No models, just for reference."""

    async def async_system_shutdown(self) -> bool:
        """Shutdown the system."""
        _res = await self._async_request("system/shutdown", method=HTTPMethod.POST)
        return _res["shuttingDown"] is True

    async def async_system_restart(self) -> bool:
        """Restart the system."""
        _res = await self._async_request("system/restart", method=HTTPMethod.POST)
        return _res["restarting"] is True

    async def async_get_system_tasks(
        self, taskid: int | None = None
    ) -> SystemTask | list[SystemTask]:
        """Get system tasks."""
        return await self._async_request(
            f"system/task{'' if taskid is None else f'/{taskid}'}",
            datatype=SystemTask,
        )

    @api_command("update", datatype=Update)
    async def async_get_software_update_info(self) -> list[Update]:
        """Get information about software updates."""
