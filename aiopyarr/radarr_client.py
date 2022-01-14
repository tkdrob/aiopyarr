"""Radarr API."""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from aiopyarr.models.request import Command

from .const import HTTPMethod
from .decorator import api_command
from .request_client import RequestClient

from .models.radarr import (  # isort:skip
    RadarrBlocklist,
    RadarrBlocklistMovie,
    RadarrCalendar,
    RadarrCommands,
    RadarrEventType,
    RadarrHistory,
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
        api_ver: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        """Initialize Radarr API."""
        super().__init__(
            port,
            request_timeout,
            raw_response,
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
            user_agent,
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
            f"movie{'' if movieid is None or tmdb is True else f'/{movieid}'}",
            params=None if movieid is None else {"tmdbid": movieid},
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
    ) -> RadarrMovie:
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
        self, data: RadarrMovie | RadarrMovieEditor, move_files: bool = False
    ) -> RadarrMovie | list[RadarrMovie]:
        """Edit movie properties of multiple movies at once."""
        params = {"moveFiles": str(move_files)}
        return await self._async_request(
            "movie/editor" if hasattr(data, "movieIds") else "movie",
            params=None if hasattr(data, "movieIds") else params,
            data=data if hasattr(data, "movieIds") else None,
            datatype=RadarrMovieEditor if hasattr(data, "movieIds") else RadarrMovie,
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
            params={"term": f"{'tmdb' if tmdb is True else 'imdb'}:{term}"},
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
        ascending: bool = False,
        sort_key: str = "date",
    ) -> RadarrHistory:
        """Get movie history.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Direction to sort items.
            sort_key: date, id, movieid, title, sourcetitle, or quality
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": "ascending" if ascending else "descending",
            "sortKey": sort_key,
        }
        return await self._async_request(
            "history",
            params=params,
            datatype=RadarrHistory,
        )

    async def async_get_movie_history(
        self, recordid: int, event_type: RadarrEventType | None = None
    ) -> list[RadarrMovieHistory]:
        """Get history for a given movie in database by its database id.

        Args:
            id: Database id of movie
            event_type: History event type to retrieve.
        """
        params: dict[str, str | int] = {"movieId": recordid}
        params["eventType"] = event_type if event_type else ""
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
            f"importlist/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

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
            f"tag/detail{'' if tagid is None else f'/{tagid}'}",
            datatype=RadarrTagDetails,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        ascending: bool = False,
        sort_key: str = "date",
    ) -> RadarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Direction to sort items.
            sort_key: date, id, movieid, title, sourcetitle, or quality
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": "ascending" if ascending else "descending",
            "sortKey": sort_key,
        }
        return await self._async_request(
            "blocklist",
            params=params,
            datatype=RadarrBlocklist,
        )

    # Documented, not able to make it work
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

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        ascending: bool = True,
        sort_key: str = "timeLeft",
        include_unknown_movie_items: bool = False,
        include_movie: bool = False,
    ) -> RadarrQueue:
        """Return a json object list of items in the queue.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Cort by ascending or descending.
            sort_key: date, id, movieid, title, sourcetitle, or quality.
            include_unknown_movie_items: Include unknown movie items.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": "ascending" if ascending else "descending",
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
            f"notification{'' if notifyid is None else f'/{notifyid}'}",
            datatype=RadarrNotification,
        )

    async def async_edit_notification(
        self, data: RadarrNotification
    ) -> RadarrNotification:
        """Edit a notification."""
        return await self._async_request(
            "notification",
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

    async def async_test_notifications(
        self, data: RadarrNotification | None = None
    ) -> bool:
        """Test a notification configuration."""
        _res = await self._async_request(
            f"notification/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

    async def async_parse(self, title: str) -> RadarrParse:
        """Return the movie with matching file name."""
        params = {"title": title}
        return await self._async_request("parse", params=params, datatype=RadarrParse)

    async def async_radarr_command(
        self, command: RadarrCommands, movieids: list[int] | None = None
    ) -> Command:
        """Send a command to Radarr.

        movieids: applicable to RefreshMovie
        """
        data: dict[str, str | list[int]] = {"name": command}
        if movieids is not None:
            data["movieIds"] = movieids
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
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
            params=None if movieid is None else {"movieId": movieid},
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
    ) -> dict[str, str | int | dict[str, str] | list[_RadarrMovieImages]] | None:
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
            "monitored": str(monitored),
            "addOptions": {"searchForMovie": str(search_for_movie)},
        }

    async def async_get_import_list_exclusions(
        self, clientid: int | None = None
    ) -> Any:
        """Get import list exclusions."""
        raise NotImplementedError()

    async def async_edit_import_list_exclusion(self, data: Any) -> Any:
        """Edit import list exclusion."""
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

    async def async_add_release_profile(self, data: Any) -> Any:
        """Add release profile."""
        raise NotImplementedError()
