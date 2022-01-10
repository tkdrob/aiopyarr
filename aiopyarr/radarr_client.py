"""Radarr API."""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from .const import HTTPMethod
from .decorator import api_command
from .request_client import RequestClient

from .models.radarr import (  # isort:skip
    RadarrBlocklist,
    RadarrBlocklistMovie,
    RadarrCalendar,
    RadarrImportList,
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
    RadarrTagDetails,
)

if TYPE_CHECKING:
    from aiohttp.client import ClientSession

    from .const import HTTPResponse
    from .models.host_configuration import PyArrHostConfiguration
    from .models.radarr_common import _RadarrMovieImages


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
        request_timeout: float = 60,
        raw_response: bool = False,
        redact: bool = True,
        api_ver: str | None = None,
    ) -> None:
        """Initialize Radarr API."""
        super().__init__(
            port,
            request_timeout,
            raw_response,
            redact,
            host_configuration,
            session,
            hostname,
            ipaddress,
            url,
            api_token,
            ssl,
            verify_ssl,
            base_api_path,
            api_ver,
        )

    async def async_get_movies(
        self, movieid: int | None = None
    ) -> RadarrMovie | list[RadarrMovie]:
        """Get information about movies.

        Include a TMDB id for a specific movie or leave black for all.
        """
        return await self._async_request(
            f"movie{f'/{movieid}' if movieid is not None else ''}",
            datatype=RadarrMovie,
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
            method=HTTPMethod.POST,
        )

    async def async_edit_movies(
        self, data: RadarrMovieEditor, move_files: bool = False
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

    async def async_edit_import_list(
        self, listid: int, data: RadarrImportList
    ) -> RadarrImportList:
        """Edit an importlist."""
        return await self._async_request(
            f"importlist/{listid}",
            data=data,
            datatype=RadarrImportList,
            method=HTTPMethod.PUT,
        )

    async def async_add_import_list(self, data: RadarrImportList) -> RadarrImportList:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=RadarrImportList, method=HTTPMethod.POST
        )

    @api_command("config/naming", datatype=RadarrNamingConfig)
    async def async_get_naming_config(self) -> RadarrNamingConfig:
        """Get information about naming configuration."""

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
            f"tag/detail{f'/{tagid}' if tagid is not None else ''}",
            datatype=RadarrTagDetails,
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

    async def async_delete_blocklist(self, bocklistid: int) -> HTTPResponse:
        """Remove a specific release (the id provided) from the blocklist."""
        return await self._async_request(
            "blocklist",
            params={"id": bocklistid},
            method=HTTPMethod.DELETE,
        )

    async def async_delete_blocklist_bulk(self, data: list[int]) -> HTTPResponse:
        """Delete blocklisted releases in bulk."""
        return await self._async_request(
            "blocklist/bulk",
            data=data,
            method=HTTPMethod.DELETE,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        sort_direction: str = "ascending",
        sort_key: str = "timeLeft",
        include_unknown_movie_items: bool = False,
        include_movie: bool = False,
    ) -> RadarrQueue:
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
            "includeUnknownMovieItems": str(include_unknown_movie_items),  # Unverified
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
            "includeUnknownMovieItems": str(include_unknown_movie_items),  # Unverified
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
            f"notification{f'/{notifyid}' if notifyid is not None else ''}",
            datatype=RadarrNotification,
        )

    async def async_edit_notification(
        self, data: RadarrNotification
    ) -> RadarrNotification:
        """Edit a notification."""
        return await self._async_request(
            f"notification/{data.id}",
            data=data,
            datatype=RadarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_add_notification(
        self, data: RadarrNotification
    ) -> RadarrNotification:
        """Add a notification."""
        return await self._async_request(
            "notification",
            data=data,
            datatype=RadarrNotification,
            method=HTTPMethod.POST,
        )

    async def async_test_notification(self, data: RadarrNotification) -> HTTPResponse:
        """Test a notification configuration."""
        return await self._async_request(
            "notification/test",
            data=data,
            method=HTTPMethod.POST,
        )

    async def async_parse(self, title: str) -> RadarrParse:
        """Return the movie with matching file name."""
        params = {"title": title}
        return await self._async_request("parse", params=params, datatype=RadarrParse)

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

    async def async_get_release(
        self, movieid: int | None = None
    ) -> list[RadarrRelease]:
        """Search indexers for specified fields."""
        return await self._async_request(
            "release",
            params={"movieId": movieid} if movieid is not None else None,
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
            params={"movieId": movieid},
            datatype=RadarrRename,
        )

    async def _async_construct_movie_json(  # pylint: disable=too-many-arguments
        self,
        db_id: str,
        quality_profile_id: int,
        root_dir: str,
        monitored: bool = True,
        search_for_movie: bool = True,
        tmdb: bool = True,
    ) -> dict[str, str | int | dict[str, bool] | list[_RadarrMovieImages]] | None:
        """Search for movie on tmdb and returns Movie json to add.

        Args:
            db_id: imdb or tmdb id
            quality_profile_id: ID of the quality profile the movie will use
            root_dir: location of the root DIR
            monitored: should the movie be monitored.
            search_for_movie: Should we search for the movie.
            tmdb: Use TMDB IDs. Set to False to use IMDB.
        """
        if not (movie := await self.async_lookup_movie(db_id, tmdb=tmdb)):
            raise Exception("Movie Doesn't Exist")

        return {
            "title": movie[0].title or "",
            "rootFolderPath": root_dir,
            "qualityProfileId": quality_profile_id,
            "year": movie[0].year or "",
            "tmdbId": movie[0].tmdbId or "",
            "images": movie[0].images or [],
            "titleSlug": movie[0].titleSlug or "",
            "monitored": monitored,
            "addOptions": {"searchForMovie": search_for_movie},
        }

    async def async_get_import_list_exclusions(
        self, clientid: int | None = None
    ) -> Any:
        """Get import list exclusions."""
        raise NotImplementedError()

    async def async_delete_import_list_exclusion(self, clientid: int) -> Any:
        """Delete import list exclusion."""
        raise NotImplementedError()

    async def async_add_import_list_exclusion(self, data: Any) -> Any:
        """Add import list exclusion."""
        raise NotImplementedError()

    async def async_get_release_profiles(self, profileid: int | None = None) -> Any:
        """Get release profiles."""
        raise NotImplementedError()

    async def async_edit_release_profile(self, data: Any) -> Any:
        """Edit release profile."""
        raise NotImplementedError()

    async def async_delete_release_profile(self, profileid: int) -> Any:
        """Delete release profiles."""
        raise NotImplementedError()

    async def async_add_release_profiles(self, data: Any) -> Any:
        """Add release profile."""
        raise NotImplementedError()

    async def async_edit_import_list_exclusion(self, data: Any) -> Any:
        """Edit import list exclusion."""
        raise NotImplementedError()
