"""Shared API."""
# pylint: disable=too-many-lines
from __future__ import annotations

import asyncio
from copy import copy
from re import search
from typing import Any, Text

from aiohttp.client import ClientError, ClientSession, ClientTimeout

from .const import (
    ALL,
    ATTR_DATA,
    HEADERS,
    HEADERS_JS,
    IS_VALID,
    LOGGER,
    PAGE,
    PAGE_SIZE,
    PATH,
    SORT_DIRECTION,
    SORT_KEY,
    HTTPMethod,
)
from .exceptions import (
    ArrAuthenticationException,
    ArrConnectionException,
    ArrException,
    ArrResourceNotFound,
)
from .models.base import todict
from .models.host_configuration import PyArrHostConfiguration
from .models.request import (
    Command,
    Commands,
    CustomFilter,
    DelayProfile,
    Diskspace,
    DownloadClient,
    DownloadClientConfig,
    Filesystem,
    FilesystemFolder,
    Health,
    HostConfig,
    ImageSize,
    ImageType,
    ImportListExclusion,
    Indexer,
    IndexerConfig,
    Language,
    Localization,
    LogFile,
    Logs,
    LogSortKeys,
    MediaManagementConfig,
    MetadataConfig,
    QualityDefinition,
    QualityProfile,
    QueueStatus,
    ReleaseProfile,
    RemotePathMapping,
    RootFolder,
    SortDirection,
    SystemBackup,
    SystemStatus,
    SystemTask,
    Tag,
    UIConfig,
    Update,
)
from .models.response import PyArrResponse


class RequestClient:  # pylint: disable=too-many-public-methods
    """Base class for API Client."""

    _close_session = False
    _from_aenter = False

    def __init__(  # pylint: disable=too-many-arguments
        self,
        port: int,
        request_timeout: float,
        raw_response: bool,
        api_ver: str,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
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

    async def _async_request(  # pylint:disable=too-many-arguments
        self,
        command: str,
        params: dict | None = None,
        data: Any = None,
        datatype: Any = None,
        method: HTTPMethod = HTTPMethod.GET,
    ) -> Any:
        """Send API request."""
        url = self._host.api_url(command)
        try:
            request = await self._session.request(
                method=method.value,
                url=url,
                params=params,
                json=todict(data),
                ssl=self._host.verify_ssl,
                timeout=ClientTimeout(self._request_timeout),
            )

            if request.status >= 400:

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

    async def async_try_zeroconf(self) -> tuple[str, str, str]:
        """Get api information if login not required."""
        try:
            async with ClientSession(headers=HEADERS_JS) as session:
                data = await (
                    await session.request(
                        method=HTTPMethod.GET.value,
                        url=self._host.api_url("initialize", True),
                        ssl=self._host.verify_ssl,
                        timeout=ClientTimeout(2),
                    )
                ).text()

            # Type ingored as we are already catching errors
            api_ver = str(search(r"apiRoot: '/api/(.*)'", data).group(1))  # type: ignore
            api_token = str(search(r"apiKey: '(.*)'", data).group(1))  # type: ignore
            base_api_path = str(search(r"urlBase: '(.*)'", data).group(1))  # type: ignore
        except (AttributeError, asyncio.exceptions.TimeoutError) as ex:
            raise ArrException(message="Failed to get api info automatically") from ex
        return api_ver, api_token, base_api_path

    async def async_get_diskspace(self) -> list[Diskspace]:
        """Get information about diskspace."""
        return await self._async_request("diskspace", datatype=Diskspace)

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

    async def async_get_host_config(self) -> HostConfig:
        """Get information about host configuration."""
        return await self._async_request("config/host", datatype=HostConfig)

    async def async_edit_host_config(self, data: HostConfig) -> HostConfig:
        """Edit General/Host settings for Radarr."""
        return await self._async_request(
            "config/host",
            data=data,
            datatype=HostConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_ui_config(self) -> UIConfig:
        """Get information about UI configuration."""
        return await self._async_request("config/ui", datatype=UIConfig)

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
        sort_key: LogSortKeys = LogSortKeys.TIME,
        sort_dir: SortDirection = SortDirection.DEFAULT,
    ) -> Logs:
        """Get logs.

        Args:
            page: Specifiy page to return.
            page_size: Number of items per page.
            filter_key: Key to filter by.
            filter_value: Value of the filter.
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_KEY: sort_key.value,
            SORT_DIRECTION: sort_dir.value,
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
        cmd = None
        if command == Commands.CLEAR_BLOCKLIST.value and hasattr(
            self, "async_get_albums"
        ):
            cmd = "ClearBlacklist"
        return await self._async_request(
            "command",
            data={"name": cmd if cmd else command.value},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_delete_command(self, commandid: int) -> None:
        """Cancel a pending command."""
        return await self._async_request(
            f"command/{commandid}", method=HTTPMethod.DELETE
        )

    async def async_get_log_file(self) -> list[LogFile]:
        """Get log file."""
        return await self._async_request("log/file", datatype=LogFile)

    async def async_get_log_file_content(self, file: str) -> Text:
        """Get log file content."""
        return await self._async_request(f"log/file/{file}")

    async def async_get_log_file_updates(self) -> list[LogFile]:
        """Get log file updates."""
        return await self._async_request("log/file/update", datatype=LogFile)

    async def async_get_log_file_update_content(self, file: str) -> Text:
        """Get log file update content."""
        return await self._async_request(f"log/file/update/{file}")

    async def async_get_system_status(self) -> SystemStatus:
        """Get information about system status."""
        return await self._async_request("system/status", datatype=SystemStatus)

    async def async_get_system_backup(self) -> list[SystemBackup]:
        """Get information about system backup."""
        return await self._async_request("system/backup", datatype=SystemBackup)

    async def async_restore_system_backup(self, backupid: int) -> None:
        """Restore from a system backup."""
        return await self._async_request(
            f"system/backup/restore/{backupid}", method=HTTPMethod.POST
        )

    # Curently not working with postman, a second request must be made
    # also requires Content-Type: multipart/form-data
    # https://stackoverflow.com/questions/57553738/how-to-aiohttp-request-post-files-list-python-requests-module
    async def async_upload_system_backup(self, data: bytes) -> None:
        """Upload a system backup."""
        return await self._async_request(
            "system/backup/restore/upload", data=data, method=HTTPMethod.POST
        )

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
            f"downloadclient/test{ALL if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item[IS_VALID] is False:
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

    async def async_get_filesystem(self, path: str) -> Filesystem:
        """Get filesystem attributes."""
        return await self._async_request(
            "filesystem",
            params={PATH: path},
            datatype=Filesystem,
        )

    async def async_get_filesystem_media_type(self, path: str) -> str:
        """Return whether queried path is a file or folder."""
        return (
            await self._async_request(
                "filesystem/type",
                params={PATH: path},
            )
        )["type"]

    async def async_get_filesystem_media(self, path: str) -> list[FilesystemFolder]:
        """Get attributes of specified mediafiles path."""
        return await self._async_request(
            "filesystem/mediafiles",
            params={PATH: path},
            datatype=FilesystemFolder,
        )

    async def async_get_failed_health_checks(self) -> list[Health]:
        """Get information about failed health checks."""
        return await self._async_request("health", datatype=Health)

    async def async_delete_import_list(self, listid: int) -> None:
        """Delete an import list."""
        return await self._async_request(
            f"importlist/{listid}",
            method=HTTPMethod.DELETE,
        )

    # importlist/schema, not that useful

    # Readarr asks for MusicBrainz id, api programming error
    # Radarr has exclusion in UI, but no endpoint implemented
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
        """Edit import list exclusion.

        foreignId must be different than existing or the call will fail
        """
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

        if data.id is not None:
            delattr(data, "id")
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
            f"indexer/test{ALL if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item[IS_VALID] is False:
                    return False
        return True

    # indexer/action/{name} not yet confirmed

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

    # initialize.js, can get api version, key(security issue), and urlbase
    # can be done unauthenticated

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

    # manualimport GET / PUT, not yet confirmed TODO

    async def async_get_image(
        self,
        imageid: int,
        imagetype: ImageType = ImageType.POSTER,
        size: ImageSize = ImageSize.LARGE,
        alt: bool = False,
    ) -> bytes:
        """Get image from application.

        imagetype: poster, banner, or fanart (logo only for Lidarr)
                (others may be possible)
        size: large, medium, small
              pixel size: None for full size (500, 250), (70, 35), (360, 180)
              Does not apply to Lidarr
        alt: True to get author (Readarr), album (Lidarr)
        """
        val = [
            val * factor
            for key, factor in {
                ImageSize.LARGE: 0,
                ImageSize.MEDIUM: 2,
                ImageSize.SMALL: 1,
            }.items()
            if key == size
            for x, val in {
                ImageType.BANNER: 35,
                ImageType.FANART: 180,
                ImageType.LOGO: 0,
                ImageType.POSTER: 250,
            }.items()
            if imagetype == x
        ][0]
        _val = ""
        if hasattr(self, "async_get_albums"):
            _val = "album/" if alt else "artist/"
        elif hasattr(self, "async_get_authors"):
            _val = "author/" if alt else "book/"
        _imgsize = f"-{val}" if size is not ImageSize.LARGE else ""
        _imgsize = "" if hasattr(self, "async_get_albums") else _imgsize

        _ext = "png" if imagetype == ImageType.LOGO else "jpg"
        cmd = f"mediacover/{_val}{imageid}/{imagetype}{_imgsize}.{_ext}"
        return await self._async_request(cmd)

    async def async_mark_failed(self, recordid: int) -> None:
        """Mark a history item as failed."""
        return await self._async_request(
            f"history/failed/{recordid}", method=HTTPMethod.POST
        )

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
            f"metadata/test{ALL if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item[IS_VALID] is False:
                    return False
        return True

    # metadata/action/{name} not yet confirmed

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
            if item[IS_VALID] is False:
                return False
        return True

    # notification/action/{name} not yet confirmed

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

    async def async_edit_quality_profile(self, data: QualityProfile) -> QualityProfile:
        """Edit quality profile."""
        return await self._async_request(
            "qualityprofile",
            data=data,
            datatype=QualityProfile,
            method=HTTPMethod.PUT,
        )

    async def async_add_quality_profile(self, data: QualityProfile) -> QualityProfile:
        """Add quality profile."""
        return await self._async_request(
            "qualityprofile",
            data=data,
            datatype=QualityProfile,
            method=HTTPMethod.POST,
        )

    async def async_delete_quality_profile(self, profileid: int) -> None:
        """Delete quality profile."""
        return await self._async_request(
            f"qualityprofile/{profileid}",
            method=HTTPMethod.DELETE,
        )

    # qualityprofile/schema, not that useful

    async def async_delete_queue(
        self,
        ids: int | list[int],
        remove_from_client: bool = True,
        blocklist: bool = False,
        skipredownload: bool = False,
    ) -> None:
        """Remove an item from the queue and optionally blocklist it.

        Args:
            ids: id of the item to be removed or mass deletion with a list
            remove_from_client: Remove the item from the client.
            blocklist: Add the item to the blocklist.
            skipredownload: Prevent application from replacing with new result
                Only documented in Readarr/Lidarr, may not work for others.
        """
        return await self._async_request(
            f"queue/{'bulk' if isinstance(ids, list) else ids}",
            params={
                "removeFromClient": str(remove_from_client),
                "blocklist": str(blocklist),
                "skipReDownload": str(skipredownload),
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

    async def async_get_queue_status(self) -> QueueStatus:
        """Get information about download queue status."""
        return await self._async_request("queue/status", datatype=QueueStatus)

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

    async def async_get_system_routes(self) -> list[list[dict[str, Any]]]:
        """Get api endpoint information. No models, just for reference."""
        return await self._async_request("system/routes")

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

    async def async_get_software_update_info(self) -> list[Update]:
        """Get information about software updates."""
        return await self._async_request("update", datatype=Update)

    async def async_get_delay_profiles(
        self, profileid: int | None = None
    ) -> DelayProfile | list[DelayProfile]:
        """Get delay profiles."""
        return await self._async_request(
            f"delayprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=DelayProfile,
        )

    async def async_add_delay_profile(self, data: DelayProfile) -> DelayProfile:
        """Add delay profile."""
        return await self._async_request(
            "delayprofile",
            data=data,
            datatype=DelayProfile,
            method=HTTPMethod.POST,
        )

    async def async_edit_delay_profile(self, data: DelayProfile) -> DelayProfile:
        """Edit delay profile."""
        return await self._async_request(
            "delayprofile",
            data=data,
            datatype=DelayProfile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_delay_profile(self, profileid: int) -> None:
        """Delete delay profile."""
        return await self._async_request(
            f"delayprofile/{profileid}", method=HTTPMethod.DELETE
        )

    async def async_delay_profile_reorder(
        self, profileid: int, afterid: int | None = None
    ) -> list[DelayProfile]:
        """Reorder delay profile."""
        return await self._async_request(
            f"delayprofile/reorder/{profileid}",
            params=None if afterid is None else {"afterId": afterid},
            method=HTTPMethod.PUT,
        )

    async def async_delete_metadata_profile(self, profileid: int) -> None:
        """Delete a metadata profile."""
        return await self._async_request(
            f"metadataprofile/{profileid}",
            method=HTTPMethod.DELETE,
        )

    async def async_command_other(
        self,
        command: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | list[dict[str, Any]] | None = None,
        method: HTTPMethod = HTTPMethod.GET,
    ) -> Any:
        """Run a command not already defined.

        Useful if new endpoints become available/known
        or if the user insists on using schema query endpoints
        """
        return await self._async_request(
            command,
            params=params,
            data=data,
            method=method,
        )
