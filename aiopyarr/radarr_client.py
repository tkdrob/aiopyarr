"""Radarr API."""
from __future__ import annotations

from datetime import datetime

from aiohttp.client import ClientSession

from .const import HTTPMethod, HTTPResponse
from .decorator import api_command
from .models.common import Diskspace
from .models.host_configuration import PyArrHostConfiguration
from .request_client import RequestClient

from .models.radarr import (  # isort:skip
    RadarrBlocklist,
    RadarrBlocklistMovie,
    RadarrCalendar,
    RadarrCommand,
    RadarrCustomFilter,
    RadarrDownloadClient,
    RadarrHealth,
    RadarrHostConfig,
    RadarrImportList,
    RadarrIndexer,
    RadarrMetadataConfig,
    RadarrMovie,
    RadarrMovieEditor,
    RadarrMovieFile,
    RadarrMovieHistory,
    RadarrNamingConfig,
    RadarrNotification,
    RadarrQualityProfile,
    RadarrQueue,
    RadarrQueueDetail,
    RadarrQueueStatus,
    RadarrRemotePathMapping,
    RadarrRootFolder,
    RadarrSystemStatus,
    RadarrTag,
    RadarrTagDetails,
    RadarrUIConfig,
    RadarrUpdate,
)


class RadarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Radarr endpoints."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        port: int = 7878,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 10,
        raw_response: bool = False,
        redact: bool = True,
    ) -> None:
        """Initialize Radarr API."""
        super().__init__(
            host_configuration,
            session,
            hostname,
            ipaddress,
            url,
            api_token,
            port,
            ssl,
            verify_ssl,
            base_api_path,
            request_timeout,
            raw_response,
            redact,
        )

    async def async_get_movies(
        self,
        movieid: int | None = None,
        raw: bool = False,
    ) -> RadarrCalendar | list[RadarrCalendar]: #TODO fix name
        """Get information about movies.

        Include a TMDB id for a specific movie or leave black for all.
        """
        datatype = None
        if raw is False:
            datatype = RadarrCalendar
        return await self._async_request(
            "movie",
            params={"tmdbId": movieid} if movieid is not None else None,
            datatype=datatype,
        )

    async def async_add_movie(  # pylint: disable=too-many-arguments
        self,
        db_id: str,
        quality_profile_id: int,
        root_dir: str,
        monitored: bool = True,
        search_for_movie: bool = True,
        tmdb: bool = True,
    ) -> HTTPResponse:
        """Add a movie to the database.

        Args:
            db_id: IMDB or TMDB ID
            quality_profile_id: ID of the quality profile the movie will use
            root_dir: location of the root DIR
            monitored: should the movie be monitored.
            search_for_movie: Should we search for the movie.
            tmdb: Use TMDB IDs. Set to False to use IMDB.
        """
        movie_json = await self._async_construct_movie_json(
            db_id, quality_profile_id, root_dir, monitored, search_for_movie, tmdb
        )
        return await self._async_request(
            "movie",
            params=movie_json,
            datatype=RadarrMovie,
            method=HTTPMethod.POST,
        )

    async def async_update_movies(
        self, data: RadarrMovie | RadarrMovieEditor, move_files: bool = False
    ) -> RadarrMovie | list[RadarrMovie]:
        """Edit movie properties of multiple movies at once."""
        return await self._async_request(
            "movie/editor" if hasattr(data, "movieIds") else "movie",
            params=None if hasattr(data, "movieIds") else {"moveFiles": move_files},
            data=data,
            datatype=RadarrMovieEditor,
            method=HTTPMethod.PUT,
        )

    async def async_delete_movies(
        self,
        ids: int | list[int],
        delete_files: bool = False,
        add_exclusion: bool = False,
    ) -> HTTPResponse:
        """Delete movies (and optionally files).

        ids: include an integer to delete one movie or a list for mass deletion
        """
        data = {
            "movieIds": ids,
            "deleteFiles": delete_files,
            "addImportExclusion": add_exclusion,
        }
        return await self._async_request(
            "movie/editor" if isinstance(ids, list) else f"movie/{ids}",
            data=data,
            method=HTTPMethod.DELETE,
        )

    async def async_import_movies(self, data: list[RadarrMovie]) -> list[RadarrMovie]:
        """Import movies in bulk.

        It allows movies to be bulk added to the Radarr database.
        """
        return await self._async_request(
            "movie/import",
            data=data,
            datatype=RadarrMovie,
            method=HTTPMethod.POST,
        )

    async def async_get_movie_files_by_movie_id(self, movieid: int) -> RadarrMovieFile:
        """Get a movie file object by Movie database id."""
        return await self._async_request(
            "moviefile",
            params={"movieid": movieid},
            datatype=RadarrMovieFile,
        )

    async def async_delete_movie_file(self, movieid: int) -> HTTPResponse:
        """Delete a moviefile by its database id."""
        return await self._async_request(
            f"moviefile/{movieid}",
            method=HTTPMethod.DELETE,
        )

    async def async_lookup_movie(
        self, term: str, tmdb: bool = True
    ) -> list[RadarrMovie]:
        """Lookup information about movie.

        tmdb: Use TMDB IDs. Set to False to use IMDB.
        """
        return await self._async_request(
            "movie/lookup",
            params={"term": f"{'tmdb' if tmdb is True else 'imdb'} :{term}"},
            datatype=RadarrMovie,
        )

    async def async_lookup_movie_files(self, ids: list[int]) -> list[RadarrMovieFile]:
        """Get movie file information for multiple movie files."""
        return await self._async_request(
            "moviefile", params={"moviefileids": ids}, datatype=RadarrMovieFile
        )

    async def async_get_history(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_direction: str = "descending",
        sort_key: str = "date",
    ) -> list[RadarrMovieHistory]:
        """Return a json object list of items in your history.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_direction: Direction to sort items.
            sort_key: Field to sort by.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": sort_direction,
            "sortKey": sort_key,
        }
        return await self._async_request(
            "history",
            params=params,
            datatype=RadarrMovieHistory,
        )

    async def async_get_movie_history(
        self, recordid: int, event_type: int | None = None
    ) -> list[RadarrMovieHistory]:
        """Get history for a given movie in database by its database id.

        Args:
            id: Database id of movie
            event_type: History event type to retrieve.
        """
        params = {"movieId": recordid}
        if event_type:
            params["eventType"] = event_type
        return await self._async_request(
            "history/movie",
            params=params,
            datatype=RadarrMovieHistory,
        )

    async def async_get_download_clients(
        self, clientid: int | None = None
    ) -> RadarrDownloadClient | list[RadarrDownloadClient]:
        """Get information about download client.

        id: Get downloadclient matching id. Leave blank for all.
        """
        return await self._async_request(
            f"downloadclient{f'/{clientid}' if clientid is not None else ''}",
            datatype=RadarrDownloadClient,
        )

    async def async_get_import_lists(
        self, listid: int | None = None
    ) -> RadarrImportList | list[RadarrImportList]:
        """Get information about import list.

        id: Get import list matching id. Leave blank for all.
        """
        return await self._async_request(
            f"importlist{f'/{listid}' if listid is not None else ''}",
            datatype=RadarrImportList,
        )

    @api_command("diskspace", datatype=Diskspace)
    async def async_get_diskspace(self) -> list[Diskspace]:
        """Get information about diskspace."""

    @api_command("config/ui", datatype=RadarrUIConfig)
    async def async_get_ui_config(self) -> RadarrUIConfig:
        """Get information about UI configuration."""

    async def async_update_ui_config(self, data: RadarrUIConfig) -> HTTPResponse:
        """Edit one or many UI settings and save to to the database."""
        return await self._async_request(
            "config/ui",
            data=data,
            datatype=RadarrUIConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("config/host", datatype=RadarrHostConfig)
    async def async_get_host_config(self) -> RadarrHostConfig:
        """Get information about host configuration."""

    async def async_update_host_config(self, data: RadarrHostConfig) -> HTTPResponse:
        """Edit General/Host settings for Radarr."""
        return await self._async_request(
            "config/host",
            data=data,
            datatype=RadarrHostConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("config/naming", datatype=RadarrNamingConfig)
    async def async_get_naming_config(self) -> RadarrNamingConfig:
        """Get information about naming configuration."""

    async def async_update_naming_config(
        self, data: RadarrNamingConfig
    ) -> HTTPResponse:
        """Edit Settings for movie file and folder naming."""
        return await self._async_request(
            "config/naming",
            data=data,
            datatype=RadarrNamingConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("metadata", datatype=RadarrMetadataConfig)
    async def async_get_metadata_config(self) -> RadarrMetadataConfig:
        """Get information about metadata configuration."""

    async def async_get_tags_details(
        self, tagid: int | None = None
    ) -> RadarrTagDetails | list[RadarrTagDetails]:
        """Get information about tag details.

        id: Get tag details matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag/detail{f'/{tagid}' if tagid is not None else ''}",
            datatype=RadarrTagDetails,
        )

    async def async_get_tags(
        self, tagid: int | None = None
    ) -> RadarrTag | list[RadarrTag]:
        """Get information about tag.

        id: Get tag matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag{f'/{tagid}' if tagid is not None else ''}",
            datatype=RadarrTag,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_direction: str = "descending",
        sort_key: str = "date",
    ) -> RadarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_direction: Direction to sort items.
            sort_key: Field to sort by.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": sort_direction,
            "sortKey": sort_key,
        }
        return await self._async_request(
            "blocklist",
            params=params,
            datatype=RadarrBlocklist,
        )

    async def async_delete_blocklist(self, bocklistid: int) -> HTTPResponse:
        """Remove a specific release (the id provided) from the blocklist."""
        return await self._async_request(
            "blocklist",
            params={"id": bocklistid},
            method=HTTPMethod.DELETE,
        )

    async def async_get_blocklist_movie(
        self,
        bocklistid: int,
    ) -> list[RadarrBlocklistMovie]:
        """Retrieve blocklisted releases that are tied to a given movie in the database."""
        return await self._async_request(
            "blocklist/movie",
            params={"movieId": bocklistid},
            datatype=RadarrBlocklistMovie,
        )

    async def async_delete_blocklist_bulk(self, data: list[int]) -> HTTPResponse:
        """Delete blocklisted releases in bulk."""
        return await self._async_request(
            "blocklist/bulk",
            data=data,
            method=HTTPMethod.DELETE,
        )

    @api_command("queue/status", datatype=RadarrQueueStatus)
    async def async_get_queue_status(self) -> RadarrQueueStatus:
        """Get information about download queue status."""

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        sort_direction: str = "ascending",
        sort_key: str = "timeLeft",
        include_unknown_movie_items: bool = True,
    ) -> list[RadarrQueue]:
        """Return a json object list of items in the queue.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_direction: Direction to sort items.
            sort_key: Field to sort by.
            include_unknown_movie_items: Include unknown movie items.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": sort_direction,
            "sortKey": sort_key,
            "includeUnknownMovieItems": include_unknown_movie_items,
        }
        return await self._async_request("queue", params=params, datatype=RadarrQueue)

    async def async_get_queue_details(
        self,
        include_movie: bool = True,
    ) -> list[RadarrQueueDetail]:
        """Get details of all items in queue."""
        return await self._async_request(
            "queue/details",
            params={"includeMovie": str(include_movie)},
            datatype=RadarrQueueDetail,
        )

    async def async_force_grab_queue_item(self, queueid: int) -> HTTPResponse:
        """Perform a Radarr "force grab" on a pending queue item by its ID."""
        return await self._async_request(
            f"queue/grab/{queueid}", method=HTTPMethod.POST
        )

    async def async_delete_queue(
        self,
        ids: int | list[int],
        remove_from_client: bool = True,
        blocklist: bool = True,
    ) -> HTTPResponse:
        """Remove an item from the queue and optionally blocklist it.

        Args:
            ids: id of the item to be removed or mass deletion with a list
            remove_from_client: Remove the item from the client.
            blocklist: Add the item to the blocklist.
        """
        return await self._async_request(
            "queue/bulk" if isinstance(ids, list) else f"queue/{ids}",
            params={"removeFromClient": remove_from_client, "blocklist": blocklist},
            data=ids if isinstance(ids, list) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_get_indexers(
        self, indexerid: int | None = None
    ) -> RadarrIndexer | list[RadarrIndexer]:
        """Get all indexers or a single indexer by its database id.

        id: Get indexer matching id. Leave blank for all.
        """
        return await self._async_request(
            f"indexer{f'/{indexerid}' if indexerid is not None else ''}",
            datatype=RadarrIndexer,
        )

    async def async_update_indexer(
        self, indexerid: int, data: RadarrIndexer
    ) -> HTTPResponse:
        """Edit an indexer."""
        return await self._async_request(
            f"indexer/{indexerid}",
            data=data,
            method=HTTPMethod.PUT,
        )

    async def async_delete_indexer(self, indexerid: int) -> HTTPResponse:
        """Delete indexer by database id."""
        return await self._async_request(
            f"indexer/{indexerid}", method=HTTPMethod.DELETE
        )

    async def async_update_download_client(
        self, clientid: int, data: RadarrDownloadClient
    ) -> HTTPResponse:
        """Edit a download client by database id.

        Args:
            id: Download client database id
            data: data to be updated within download client
        """
        return await self._async_request(
            f"downloadclient/{clientid}",
            data=data,
            datatype=RadarrDownloadClient,
            method=HTTPMethod.PUT,
        )

    async def async_delete_download_client(self, clientid: int) -> HTTPResponse:
        """Delete a download client."""
        return await self._async_request(
            f"downloadclient/{clientid}", method=HTTPMethod.DELETE
        )

    async def async_update_import_list(
        self, listid: int, data: RadarrImportList
    ) -> HTTPResponse:
        """Edit an importlist."""
        return await self._async_request(
            f"importlist/{listid}",
            data=data,
            datatype=RadarrImportList,
            method=HTTPMethod.PUT,
        )

    async def async_delete_import_list(self, listid: int) -> HTTPResponse:
        """Delete an import list."""
        return await self._async_request(
            f"importlist/{listid}",
            datatype=RadarrIndexer,
            method=HTTPMethod.DELETE,
        )

    async def async_get_notifications(
        self, notifyid: int | None = None
    ) -> RadarrNotification | list[RadarrNotification]:
        """Get information about notification.

        id: Get notification matching id. Leave blank for all.
        """
        return await self._async_request(
            f"notification{f'/{notifyid}' if notifyid is not None else ''}",
            datatype=RadarrNotification,
        )

    async def async_update_notification(
        self, notifyid: int, data: RadarrNotification
    ) -> HTTPResponse:
        """Edit a notification."""
        return await self._async_request(
            f"notification/{notifyid}",
            data=data,
            datatype=RadarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_delete_notification(self, notifyid: int) -> HTTPResponse:
        """Delete a notification."""
        return await self._async_request(
            f"notification/{notifyid}",
            datatype=RadarrNotification,
            method=HTTPMethod.DELETE,
        )

    async def async_create_tag(self, label: str) -> HTTPResponse:
        """Create a new tag.

        Can be assigned to a movie, list, delay profile, notification, or restriction.
        """
        return await self._async_request(
            "tag",
            data={"id": 0, "label": label},
            datatype=RadarrTag,
            method=HTTPMethod.POST,
        )

    async def async_update_tag(self, tagid: int, label: str) -> HTTPResponse:
        """Edit a tag by its database id."""
        return await self._async_request(
            f"tag/{tagid}",
            data={"id": tagid, "label": label},
            datatype=RadarrTag,
            method=HTTPMethod.PUT,
        )

    async def async_delete_tag(self, tagid: int) -> HTTPResponse:
        """Delete a tag."""
        return await self._async_request(
            f"tag/{tagid}",
            datatype=RadarrTag,
            method=HTTPMethod.DELETE,
        )

    @api_command("command", datatype=RadarrCommand)
    async def async_get_command(self) -> list[RadarrCommand]:
        """Get status of recently run commands/tasks."""

    async def async_command_app_update(self) -> HTTPResponse:
        """Trigger Radarr software update."""
        return await self._async_request(
            "command",
            data={"name": "ApplicationUpdate"},
            method=HTTPMethod.POST,
        )

    async def async_command_backup(self) -> HTTPResponse:
        """Trigger a backup routine."""
        return await self._async_request(
            "command",
            data={"name": "Backup"},
            method=HTTPMethod.POST,
        )

    async def async_command_check_health(self) -> HTTPResponse:
        """Trigger a system health check."""
        return await self._async_request(
            "command",
            data={"name": "CheckHealth"},
            method=HTTPMethod.POST,
        )

    async def async_command_clear_blocklist(self) -> HTTPResponse:
        """Trigger the removal of all blocklisted movies."""
        return await self._async_request(
            "command",
            data={"name": "ClearBlocklist"},
            method=HTTPMethod.POST,
        )

    async def async_command_clean_recycle_bin(self) -> HTTPResponse:
        """Trigger a recycle bin cleanup check."""
        return await self._async_request(
            "command",
            data={"name": "CleanUpRecycleBin"},
            method=HTTPMethod.POST,
        )

    async def async_command_delete_log_files(self) -> HTTPResponse:
        """Trigger the removal of all Info/Debug/Trace log files."""
        return await self._async_request(
            "command",
            data={"name": "DeleteLogFiles"},
            method=HTTPMethod.POST,
        )

    async def async_command_delete_update_log_files(self) -> HTTPResponse:
        """Trigger the removal of all Update log files."""
        return await self._async_request(
            "command",
            data={"name": "DeleteUpdateLogFiles"},
            method=HTTPMethod.POST,
        )

    async def async_command_downloaded_movies_scan(self) -> HTTPResponse:
        """Trigger the scan of downloaded movies."""
        return await self._async_request(
            "command",
            data={"name": "DownloadedMoviesScan"},
            method=HTTPMethod.POST,
        )

    async def async_command_missing_movies_search(self) -> HTTPResponse:
        """Trigger a search of all missing movies."""
        return await self._async_request(
            "command",
            data={"name": "MissingMoviesSearch"},
            method=HTTPMethod.POST,
        )

    async def async_command_refresh_monitored_downloads(self) -> HTTPResponse:
        """Trigger the scan of monitored downloads."""
        return await self._async_request(
            "command",
            data={"name": "RefreshMonitoredDownloads"},
            method=HTTPMethod.POST,
        )

    async def async_command_refresh_movies(self, movieids: list[int]) -> HTTPResponse:
        """Trigger a refresh / scan of movies."""
        return await self._async_request(
            "command",
            data={"name": "RefreshMovie", "movieIds": movieids},
            method=HTTPMethod.POST,
        )

    async def async_get_calendar(
        self, start_date: datetime, end_date: datetime, unmonitored: bool = True
    ) -> list[RadarrCalendar]:
        """Get a list of movies based on calendar parameters."""
        params = {
            "start": start_date.strftime("%Y-%m-%d"),
            "end": end_date.strftime("%Y-%m-%d"),
            "unmonitored": str(unmonitored),
        }
        return await self._async_request(
            "calendar",
            params=params,
            datatype=RadarrCalendar,
        )

    @api_command("system/status", datatype=RadarrSystemStatus)
    async def async_get_system_status(self) -> RadarrSystemStatus:
        """Get information about system status."""

    @api_command("health", datatype=RadarrHealth)
    async def async_get_failed_health_checks(self) -> RadarrHealth:
        """Get information about failed health checks."""

    @api_command("update", datatype=RadarrUpdate)
    async def async_get_software_update_info(self) -> RadarrUpdate:
        """Get information about software updates."""

    @api_command("qualityProfile", datatype=RadarrQualityProfile)
    async def async_get_quality_profiles(self) -> list[RadarrQualityProfile]:
        """Get information about quality profiles."""

    @api_command("customfilter", datatype=RadarrCustomFilter)
    async def async_get_custom_filters(self) -> list[RadarrCustomFilter]:
        """Get information about custom filters."""

    @api_command("remotePathMapping", datatype=RadarrRemotePathMapping)
    async def async_get_remote_path_mappings(self) -> list[RadarrRemotePathMapping]:
        """Get information about remote path mappings."""

    @api_command("rootfolder", datatype=RadarrRootFolder)
    async def async_get_root_folders(self) -> list[RadarrRootFolder]:
        """Get information about root folders."""

    async def _async_construct_movie_json(  # pylint: disable=too-many-arguments
        self,
        db_id: str,
        quality_profile_id: int,
        root_dir: str,
        monitored: bool = True,
        search_for_movie: bool = True,
        tmdb: bool = True,
    ) -> dict[str, str | int | dict[str, bool]]:
        """Search for movie on tmdb and returns Movie json to add.

        Args:
            db_id: imdb or tmdb id
            quality_profile_id: ID of the quality profile the movie will use
            root_dir: location of the root DIR
            monitored: should the movie be monitored.
            search_for_movie: Should we search for the movie.
            tmdb: Use TMDB IDs. Set to False to use IMDB.
        """
        if not (movie := await self.async_lookup_movie(db_id, tmdb=tmdb)[0]):
            raise Exception("Movie Doesn't Exist")

        return {
            "title": movie["title"],
            "rootFolderPath": root_dir,
            "qualityProfileId": quality_profile_id,
            "year": movie["year"],
            "tmdbId": movie["tmdbId"],
            "images": movie["images"],
            "titleSlug": movie["titleSlug"],
            "monitored": monitored,
            "addOptions": {"searchForMovie": search_for_movie},
        }
