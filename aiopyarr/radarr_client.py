"""Radarr API."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from aiohttp.client import ClientSession

from aiopyarr.exceptions import ArrException
from aiopyarr.models.request import Command, SortDirection

from .const import (
    ALL,
    DATE,
    EVENT_TYPE,
    IS_VALID,
    MOVIE_ID,
    NOTIFICATION,
    PAGE,
    PAGE_SIZE,
    PATH,
    SORT_DIRECTION,
    SORT_KEY,
    TERM,
    TITLE,
    HTTPMethod,
)
from .models.host_configuration import PyArrHostConfiguration
from .models.radarr import (
    RadarrAltTitle,
    RadarrBlocklist,
    RadarrBlocklistMovie,
    RadarrCalendar,
    RadarrCommands,
    RadarrCredit,
    RadarrEventType,
    RadarrExtraFile,
    RadarrHistory,
    RadarrImportList,
    RadarrImportListActionType,
    RadarrImportListMovie,
    RadarrIndexerFlag,
    RadarrManualImport,
    RadarrMovie,
    RadarrMovieEditor,
    RadarrMovieFile,
    RadarrMovieHistory,
    RadarrNamingConfig,
    RadarrNotification,
    RadarrParse,
    RadarrQueue,
    RadarrQueueDetail,
    RadarrRelease,
    RadarrRename,
    RadarrRestriction,
    RadarrSortKeys,
    RadarrTagDetails,
)
from .request_client import RequestClient


class RadarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Radarr endpoints."""

    __name__ = "Radarr"

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
        request_timeout: float = 60,
        raw_response: bool = False,
        api_ver: str = "v3",
    ) -> None:
        """Initialize Radarr API."""
        super().__init__(
            port,
            request_timeout,
            raw_response,
            api_ver,
            host_configuration,
            session,
            hostname,
            ipaddress,
            url,
            api_token,
            ssl,
            verify_ssl,
            base_api_path,
        )

    async def async_get_movies(
        self,
        movieid: int | None = None,
        tmdb: bool = False,
    ) -> RadarrMovie | list[RadarrMovie]:
        """Get information about movies.

        Include an id for a specific movie or leave black for all.
        tmdb: Use TMDB ID.
        """
        return await self._async_request(
            f"movie{'' if movieid is None or tmdb else f'/{movieid}'}",
            params=None if movieid is None else {"tmdbid": movieid},
            datatype=RadarrMovie,
        )

    async def async_add_movies(
        self, data: RadarrMovie | list[RadarrMovie]
    ) -> RadarrMovie | list[RadarrMovie]:
        """Add movie to the database."""
        return await self._async_request(
            f"movie{'/import' if isinstance(data, list) else ''}",
            data=data,
            datatype=RadarrMovie,
            method=HTTPMethod.POST,
        )

    async def async_edit_movies(
        self, data: RadarrMovie | RadarrMovieEditor, move_files: bool = False
    ) -> RadarrMovie | list[RadarrMovie]:
        """Edit movie properties of multiple movies at once."""
        params = {"moveFiles": str(move_files)}
        return await self._async_request(
            f"movie{'' if isinstance(data, RadarrMovie) else '/editor'}",
            params=params if isinstance(data, RadarrMovie) else None,
            data=data,
            datatype=RadarrMovie,
            method=HTTPMethod.PUT,
        )

    async def async_delete_movies(
        self,
        ids: int | list[int],
        delete_files: bool = False,
        add_exclusion: bool = False,
    ) -> None:
        """Delete movies (and optionally files).

        ids: include an integer to delete one movie or a list for mass deletion
        """
        data: dict[str, str | list[int]] = {
            "deleteFiles": str(delete_files),
            "addImportExclusion": str(add_exclusion),
        }
        if isinstance(ids, list):
            data["movieIds"] = ids
        return await self._async_request(
            "movie/editor" if isinstance(ids, list) else f"movie/{ids}",
            params=None if isinstance(ids, list) else data,
            data=data if isinstance(ids, list) else None,
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

    async def async_delete_movie_file(self, movieid: int) -> None:
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
            params={TERM: f"{'tmdb' if tmdb else 'imdb'}:{term}"},
            datatype=RadarrMovie,
        )

    async def async_lookup_movie_files(
        self, ids: list[int]
    ) -> RadarrMovieFile | list[RadarrMovieFile]:
        """Get movie file information for multiple movie files."""
        return await self._async_request(
            f"moviefile{'' if isinstance(ids, list) else f'/{ids}'}",
            params={"movieFileIds": ids} if isinstance(ids, list) else None,
            datatype=RadarrMovieFile,
        )

    async def async_get_history(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_key: RadarrSortKeys = RadarrSortKeys.DATE,
        event_type: RadarrEventType | None = None,
    ) -> RadarrHistory:
        """Get movie history.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_key: date, id, movieid, title, sourcetitle, path, ratings, or quality
                    (Others do not apply)
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_KEY: sort_key.value,
        }
        if event_type and event_type in RadarrEventType:
            params[EVENT_TYPE] = event_type.value
        return await self._async_request(
            "history",
            params=params,
            datatype=RadarrHistory,
        )

    async def async_get_history_since(
        self,
        date: datetime | None = None,
        movieid: int | None = None,
        event_type: RadarrEventType | None = None,
    ) -> list[RadarrMovieHistory]:
        """Get history since specified date.

        movieid: include to search history by movie id (date will not apply)
        Radarr permits a naked query but its required here to avoid excessively large
        data sets where filtering should be used instead
        """
        if date is None and movieid is None:
            raise ArrException(self, "Either date or movieid is required")
        params: dict[str, int | str] = {}
        if isinstance(date, datetime):
            params[DATE] = date.strftime("%Y-%m-%d")
        elif movieid is not None:
            params[MOVIE_ID] = movieid
        if event_type and event_type in RadarrEventType:
            params[EVENT_TYPE] = event_type.value
        return await self._async_request(
            f"history/{'since' if isinstance(date, datetime) else 'movie'}",
            params=params,
            datatype=RadarrMovieHistory,
        )

    async def async_get_import_lists(
        self, listid: int | None = None
    ) -> RadarrImportList | list[RadarrImportList]:
        """Get information about import lists."""
        return await self._async_request(
            f"importlist{'' if listid is None else f'/{listid}'}",
            datatype=RadarrImportList,
        )

    async def async_edit_import_list(self, data: RadarrImportList) -> RadarrImportList:
        """Edit an importlist."""
        return await self._async_request(
            "importlist",
            data=data,
            datatype=RadarrImportList,
            method=HTTPMethod.PUT,
        )

    async def async_add_import_list(self, data: RadarrImportList) -> RadarrImportList:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=RadarrImportList, method=HTTPMethod.POST
        )

    async def async_test_import_lists(
        self, data: RadarrImportList | None = None
    ) -> bool:
        """Test all import lists."""
        _res = await self._async_request(
            f"importlist/test{ALL if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item[IS_VALID] is False:
                    return False
        return True

    async def async_get_import_list_movies(self) -> list[RadarrImportListMovie]:
        """Get list of movies on configured import lists."""
        return await self._async_request(
            "importlist/movie",
            datatype=RadarrImportListMovie,
        )

    async def async_get_extra_file(self, movieid: int) -> list[RadarrExtraFile]:
        """Get extra files info from specified movie id."""
        return await self._async_request(
            "extrafile",
            params={MOVIE_ID: movieid},
            datatype=RadarrExtraFile,
        )

    async def async_get_restrictions(
        self, restrictionid: int | None = None
    ) -> RadarrRestriction | list[RadarrRestriction]:
        """Get indexer restrictions."""
        return await self._async_request(
            f"restriction{'' if restrictionid is None else f'/{restrictionid}'}",
            datatype=RadarrRestriction,
        )

    async def async_edit_restriction(
        self, data: RadarrRestriction
    ) -> RadarrRestriction:
        """Edit indexer restriction."""
        return await self._async_request(
            "restriction",
            data=data,
            datatype=RadarrRestriction,
            method=HTTPMethod.PUT,
        )

    async def async_add_restriction(self, data: RadarrRestriction) -> RadarrRestriction:
        """Add indexer restriction."""
        return await self._async_request(
            "restriction",
            data=data,
            datatype=RadarrRestriction,
            method=HTTPMethod.POST,
        )

    async def async_delete_restriction(self, restrictionid: int) -> None:
        """Delete indexer restriction."""
        return await self._async_request(
            f"restriction/{restrictionid}",
            datatype=RadarrRestriction,
            method=HTTPMethod.DELETE,
        )

    async def async_get_credits(
        self, creditid: int | None = None, movieid: int | None = None
    ) -> RadarrCredit | list[RadarrCredit]:
        """Get credits."""
        return await self._async_request(
            f"credit{'' if creditid is None else f'/{creditid}'}",
            params=None if movieid is None else {MOVIE_ID: movieid},
            datatype=RadarrCredit,
        )

    async def async_get_alt_titles(
        self, alttitleid: int | None = None, movieid: int | None = None
    ) -> RadarrAltTitle | list[RadarrAltTitle]:
        """Get alternate movie titles."""
        return await self._async_request(
            f"alttitle{'' if alttitleid is None else f'/{alttitleid}'}",
            params=None if movieid is None else {MOVIE_ID: movieid},
            datatype=RadarrAltTitle,
        )

    # GET altyear

    async def async_get_indexer_flags(self) -> list[RadarrIndexerFlag]:
        """Get indexer flags."""
        return await self._async_request(
            "indexerflag",
            datatype=RadarrIndexerFlag,
        )

    async def async_importlist_action(
        self, action: RadarrImportListActionType
    ) -> dict[str, Any]:
        """Perform import list action."""
        return await self._async_request(
            f"importlist/action/{action.value}",
            method=HTTPMethod.POST,
        )

    async def async_get_naming_config(self) -> RadarrNamingConfig:
        """Get information about naming configuration."""
        return await self._async_request("config/naming", datatype=RadarrNamingConfig)

    async def async_edit_naming_config(
        self, data: RadarrNamingConfig
    ) -> RadarrNamingConfig:
        """Edit Settings for file and folder naming."""
        return await self._async_request(
            "config/naming",
            data=data,
            datatype=RadarrNamingConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_tags_details(
        self, tagid: int | None = None
    ) -> RadarrTagDetails | list[RadarrTagDetails]:
        """Get information about tag details.

        id: Get tag details matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag/detail{'' if tagid is None else f'/{tagid}'}",
            datatype=RadarrTagDetails,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        sort_key: RadarrSortKeys = RadarrSortKeys.DATE,
    ) -> RadarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_key: date, id, movieid, title, path, sourcetitle, ratings, or quality
                    (Others do not apply)
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_DIRECTION: sort_dir.value,
            SORT_KEY: sort_key.value,
        }
        return await self._async_request(
            "blocklist",
            params=params,
            datatype=RadarrBlocklist,
        )

    async def async_get_blocklist_movie(
        self,
        bocklistid: int,
    ) -> list[RadarrBlocklistMovie]:
        """Retrieve blocklisted releases that are tied to a given movie in the database."""
        return await self._async_request(
            "blocklist/movie",
            params={MOVIE_ID: bocklistid},
            datatype=RadarrBlocklistMovie,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        sort_key: RadarrSortKeys = RadarrSortKeys.TIMELEFT,
        include_unknown_movie_items: bool = False,
        include_movie: bool = False,
    ) -> RadarrQueue:
        """Return a json object list of items in the queue.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            include_unknown_movie_items: Include unknown movie items.
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_DIRECTION: sort_dir.value,
            SORT_KEY: sort_key.value,
            "includeUnknownMovieItems": str(include_unknown_movie_items),
            "includeMovie": str(include_movie),
        }
        return await self._async_request("queue", params=params, datatype=RadarrQueue)

    async def async_get_queue_details(
        self,
        include_unknown_movie_items: bool = False,
        include_movie: bool = True,
    ) -> list[RadarrQueueDetail]:
        """Get details of all items in queue."""
        params = {
            "includeUnknownMovieItems": str(include_unknown_movie_items),
            "includeMovie": str(include_movie),
        }
        return await self._async_request(
            "queue/details",
            params=params,
            datatype=RadarrQueueDetail,
        )

    async def async_get_notifications(
        self, notifyid: int | None = None
    ) -> RadarrNotification | list[RadarrNotification]:
        """Get information about notification.

        id: Get notification matching id. Leave blank for all.
        """
        return await self._async_request(
            f"notification{'' if notifyid is None else f'/{notifyid}'}",
            datatype=RadarrNotification,
        )

    async def async_edit_notification(
        self, data: RadarrNotification
    ) -> RadarrNotification:
        """Edit a notification."""
        return await self._async_request(
            NOTIFICATION,
            data=data,
            datatype=RadarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_add_notification(
        self, data: RadarrNotification
    ) -> RadarrNotification:
        """Add a notification."""
        return await self._async_request(
            NOTIFICATION,
            data=data,
            datatype=RadarrNotification,
            method=HTTPMethod.POST,
        )

    async def async_test_notifications(
        self, data: RadarrNotification | None = None
    ) -> bool:
        """Test a notification configuration."""
        _res = await self._async_request(
            f"notification/test{ALL if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item[IS_VALID] is False:
                    return False
        return True

    async def async_parse(self, title: str) -> RadarrParse:
        """Return the movie with matching file name."""
        params = {TITLE: title}
        return await self._async_request("parse", params=params, datatype=RadarrParse)

    async def async_radarr_command(  # pylint: disable=too-many-arguments
        self,
        command: RadarrCommands,
        clientid: int | None = None,
        copymode: bool = True,
        files: list[int] | None = None,
        path: str | None = None,
        movieid: int | list[int] | None = None,
    ) -> Command:
        """Send a command to Radarr.

        Specify clientid for DownloadedMoviesScan (Optional)
        Specify files for RenameFiles
        Specify path for DownloadedMoviesScan (Optional)
        Specify movieid for:
            RefreshMovie (Optional),
            RenameMovie (list[int]),
            RescanMovie (Optional),
            MovieSearch
        """
        data: dict[str, str | int | list[int]] = {"name": command.value}
        if clientid is not None:
            data["downloadClientId"] = clientid
        if files is not None:
            data["files"] = files
        if path is not None:
            data[PATH] = path
        if movieid is not None:
            if command == RadarrCommands.RENAME_MOVIE:
                data["movieIds"] = movieid
            else:
                data[MOVIE_ID] = movieid
        if command is RadarrCommands.DOWNLOADED_MOVIES_SCAN:
            data["importMode"] = "Copy" if copymode else "Move"
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_calendar(
        self,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        unmonitored: bool = True,
    ) -> list[RadarrCalendar]:
        """Get a list of movies based on calendar parameters."""
        params = {"unmonitored": str(unmonitored)}
        if start_date:
            params["start"] = start_date.strftime("%Y-%m-%d")
        if end_date:
            params["end"] = end_date.strftime("%Y-%m-%d")
        return await self._async_request(
            "calendar",
            params=params,
            datatype=RadarrCalendar,
        )

    async def async_get_release(
        self, movieid: int | None = None
    ) -> list[RadarrRelease]:
        """Search indexers for specified fields."""
        return await self._async_request(
            "release",
            params=None if movieid is None else {MOVIE_ID: movieid},
            datatype=RadarrRelease,
        )

    async def async_download_release(
        self, guid: str, indexerid: int
    ) -> list[RadarrRelease]:
        """Add a previously searched release to the download client.

        If the release is
        still in the search cache (30 minute cache). If the release is not found
        in the cache it will return a 404.

        guid: Recently searched result guid
        """
        return await self._async_request(
            "release",
            data={"guid": guid, "indexerId": indexerid},
            datatype=RadarrRelease,
            method=HTTPMethod.POST,
        )

    # Only works if an id is associated with the release
    async def async_get_pushed_release(self, releaseid: str) -> RadarrRelease:
        """Get release previously pushed by below method."""
        return await self._async_request(
            "release/push",
            params={"id": releaseid},
            datatype=RadarrRelease,
        )

    async def async_get_rename(self, movieid: int) -> list[RadarrRename]:
        """Get files matching specified id that are not properly renamed yet."""
        return await self._async_request(
            "rename",
            params={MOVIE_ID: movieid},
            datatype=RadarrRename,
        )

    async def async_get_manual_import(
        self,
        downloadid: str,
        folder: str | None = None,
        filterexistingfiles: bool = True,
    ) -> list[RadarrManualImport]:
        """Get manual import."""
        params = {
            "downloadId": downloadid,
            "filterExistingFiles": str(filterexistingfiles),
            "folder": folder if folder is not None else "",
        }
        return await self._async_request(
            "manualimport", params=params, datatype=RadarrManualImport
        )

    async def async_edit_manual_import(
        self, data: RadarrManualImport
    ) -> list[RadarrManualImport]:
        """Get manual import."""
        return await self._async_request(
            "manualimport",
            data=data,
            datatype=RadarrManualImport,
            method=HTTPMethod.PUT,
        )

    async def async_get_release_profiles(self, profileid: int | None = None) -> Any:
        """Get release profiles."""
        raise NotImplementedError()

    async def async_edit_release_profile(self, data: Any) -> Any:
        """Edit release profile."""
        raise NotImplementedError()

    async def async_delete_release_profile(self, profileid: int) -> Any:
        """Delete release profiles."""
        raise NotImplementedError()

    async def async_add_release_profile(self, data: Any) -> Any:
        """Add release profile."""
        raise NotImplementedError()

    async def async_delete_metadata_profile(self, profileid: int) -> Any:
        """Delete a metadata profile."""
        raise NotImplementedError()
