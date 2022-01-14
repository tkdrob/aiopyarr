"""Sonarr API."""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

from .const import HTTPMethod
from .decorator import api_command
from .exceptions import ArrInvalidCommand, ArrResourceNotFound
from .models.request import Command
from .request_client import RequestClient

from .models.sonarr import (  # isort:skip
    SonarrBlocklist,
    SonarrCalendar,
    SonarrCommands,
    SonarrEpisode,
    SonarrEpisodeFile,
    SonarrHistory,
    SonarrImportList,
    SonarrNamingConfig,
    SonarrNotification,
    SonarrParse,
    SonarrQueue,
    SonarrQueueDetail,
    SonarrRelease,
    SonarrRename,
    SonarrSeries,
    SonarrSeriesLookup,
    SonarrSeriesUpdateParams,
    SonarrTagDetails,
    SonarrWantedMissing,
)

if TYPE_CHECKING:
    from aiohttp.client import ClientSession

    from .models.host_configuration import PyArrHostConfiguration


class SonarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Sonarr endpoints."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        port: int = 8989,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 30,
        raw_response: bool = False,
        api_ver: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        """Initialize Sonarr API."""
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

    async def async_get_episode_files(
        self, entryid: int, series: bool = False
    ) -> SonarrEpisodeFile | list[SonarrEpisodeFile]:
        """Get information about an episode file.

        episodeId: Get episode files matching id.
        series: Make True to search by series.
        """
        return await self._async_request(
            f"episodefile{'' if series else f'/{entryid}'}",
            params={"seriesId": entryid} if series else None,
            datatype=SonarrEpisodeFile,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        ascending: bool = True,
        sort_key: str = "timeLeft",
        include_unknown_series_items: bool = False,
        include_series: bool = False,
        include_episode: bool = False,
    ) -> SonarrQueue:
        """Get information about download queue.

        ascending: Sort items in ascending order.
        sort_key: series.Title, id, date, airDateUtc, or title.
        page: Page number to return.
        page_size: Number of items per page.
        id: Filter to a specific episode ID.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": "ascending" if ascending else "descending",
            "sortKey": sort_key,
            "includeUnknownSeriesItems": str(
                include_unknown_series_items
            ),  # Unverified
            "includeSeries": str(include_series),
            "includeEpisode": str(include_episode),
        }
        return await self._async_request("queue", params=params, datatype=SonarrQueue)

    async def async_get_queue_details(
        self,
        include_unknown_series_items: bool = False,
        include_series: bool = True,
        include_episode: bool = True,
    ) -> list[SonarrQueueDetail]:
        """Get details of all items in queue."""
        params = {
            "includeUnknownSeriesItems": str(
                include_unknown_series_items
            ),  # Unverified
            "includeSeries": str(include_series),
            "includeEpisode": str(include_episode),
        }
        return await self._async_request(
            "queue/details",
            params=params,
            datatype=SonarrQueueDetail,
        )

    async def async_get_calendar(
        self, start_date: datetime | None = None, end_date: datetime | None = None
    ) -> list[SonarrCalendar]:
        """Get upcoming episodes, if start/end are not supplied episodes airing today.

        and tomorrow will be returned
        """
        params = {}
        if start_date:
            params["start"] = (start_date.strftime("%Y-%m-%d"),)
        if end_date:
            params["end"] = (end_date.strftime("%Y-%m-%d"),)

        return await self._async_request(
            "calendar", params=params, datatype=SonarrCalendar
        )

    async def async_sonarr_command(
        self,
        command: SonarrCommands,
        clientid: int | None = None,
        copymode: bool = True,
        episodeids: list[int] | None = None,
        files: list[int] | None = None,
        path: str | None = None,
        season: int | None = None,
        seriesid: int | list[int] | None = None,
    ) -> Command:
        """Send a command to Sonarr.

        Specify clientid for DownloadedEpisodesScan (Optional)
        Specify episodeIds for EpisodeSearch
        Specify files for RenameFiles
        Specify path for DownloadedEpisodesScan (Optional)
        Specify season for SeasonSearch
        Specify seriesId for:
            RefreshSeries (Optional),
            RenameSeries (list[int]),
            RescanSeries (Optional),
            SeasonSearch,
            SeriesSearch
        """
        data: dict[str, str | int | list[int]] = {"name": command}
        if clientid is not None:
            data["downloadClientId"] = clientid
        if episodeids is not None:
            data["episodeIds"] = episodeids
        if files is not None:
            data["files"] = files
        if path is not None:
            data["path"] = path
        if seriesid is not None:
            if command == SonarrCommands.RENAME_SERIES:
                data["seriesIds"] = seriesid
            else:
                data["seriesId"] = seriesid
        if command is SonarrCommands.DOWNLOADED_EPISODES_SCAN:
            data["importMode"] = "Copy" if copymode else "Move"
        if season is not None:
            data["seasonNumber"] = season
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_episodes(
        self, entryid: int, series: bool = False
    ) -> SonarrEpisode | list[SonarrEpisode]:
        """Get all episodes from a given series or episode id."""
        return await self._async_request(
            f"episode{'' if series else f'/{entryid}'}",
            params={"seriesId": entryid} if series else None,
            datatype=SonarrEpisode,
        )

    async def async_edit_episode(self, data: SonarrEpisode) -> SonarrEpisode:
        """Edit given episodes, currently only monitored is changed."""
        return await self._async_request(
            f"episode/{data.id}",
            data=data,
            datatype=SonarrEpisode,
            method=HTTPMethod.PUT,
        )

    async def async_edit_episode_file_quality(
        self, data: SonarrEpisodeFile
    ) -> SonarrEpisodeFile:
        """Edit an episode file quality.

        Quality only works, currently.
        Quality.id and Revision.version
        """
        return await self._async_request(
            "episodefile",
            data=data,
            datatype=SonarrEpisodeFile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_episode_file(self, fileid: int) -> None:
        """Delete the episode file with corresponding id."""
        return await self._async_request(
            f"episodefile/{fileid}", method=HTTPMethod.DELETE
        )

    async def async_get_history(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "date",
        recordid: int | None = None,
    ) -> SonarrHistory:
        """Get history (grabs/failures/completed).

        Args:
            sort_key: id, date, or series.Title.
            page: Page number to return.
            page_size: Number of items per page.
            id: Filter to a specific episode ID.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortKey": sort_key,
        }
        if recordid is not None:
            params["episodeId"] = recordid
        return await self._async_request(
            "history", datatype=SonarrHistory, params=params
        )

    async def async_get_wanted(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "airDateUtc",
        ascending: bool = True,
    ) -> SonarrWantedMissing:
        """Get missing episode (episodes without files).

        Args:
            sort_date: airDateUtc, id, series.Title, or title.
            page: Page number to return.
            page_size: Number of items per page.
            ascending: Sort items in ascending order.
        """
        params = {
            "sortKey": sort_key,
            "page": page,
            "pageSize": page_size,
            "sortDirection": "ascending" if ascending else "descending",
        }
        return await self._async_request(
            "wanted/missing",
            params=params,
            datatype=SonarrWantedMissing,
        )

    async def async_parse_title_or_path(
        self, title: str | None = None, path: str | None = None
    ) -> SonarrParse:
        """Return the result of parsing a title or path.

        series and episodes will be
        returned only if the parsing matches to a specific series and one or more
        episodes. series and episodes will be formatted the same as Series and Episode
        responses.

        title: Title of series / episode
        path: file path of series / episode
        """
        if title is None and path is None:
            raise ArrInvalidCommand(self, "A title or path must be specified")
        params = {}
        if title is not None:
            params["title"] = title
        if path is not None:
            params["path"] = path
        return await self._async_request("parse", params=params, datatype=SonarrParse)

    async def async_get_release(
        self, episodeid: int | None = None
    ) -> list[SonarrRelease]:
        """Query indexers for latest releases.

        episodeid: included in API docs but does not seem to do anything
        """
        return await self._async_request(
            "release",
            params=None if episodeid is None else {"episodeId": episodeid},
            datatype=SonarrRelease,
        )

    async def async_download_release(self, data: SonarrRelease) -> SonarrRelease:
        """Add a previously searched release to the download client.

        If the release is
        still in the search cache (30 minute cache). If the release is not found
        in the cache it will return a 404.

        Only the guid and indexerId are required
        but a full SonarrRelease object will work
        """
        return await self._async_request(
            "release",
            data=data,
            datatype=SonarrRelease,
            method=HTTPMethod.POST,
        )

    async def async_push_release(self, data: SonarrRelease) -> list[SonarrRelease]:
        """Add a release.

        If the title is wanted, Sonarr will grab it.
        """
        return await self._async_request(
            "release/push",
            data=data,
            datatype=SonarrRelease,
            method=HTTPMethod.POST,
        )

    async def async_get_series(
        self, seriesid: int | None = None
    ) -> SonarrSeries | list[SonarrSeries]:
        """Return all series in your collection or the series with the matching.

        series ID if one is found.
        """
        return await self._async_request(
            f"series{'' if seriesid is None else f'/{seriesid}'}",
            datatype=SonarrSeries,
        )

    async def async_add_series(  # pylint: disable=too-many-arguments
        self,
        tvdb_id: int,
        quality_profile_id: int,
        root_dir: str,
        season_folder: bool = True,
        monitored: bool = True,
        ignore_episodes_with_files: bool = False,
        ignore_episodes_without_files: bool = False,
        search_for_missing_episodes: bool = False,
    ) -> SonarrSeries:
        """Add a new series to your collection.

        Args:
            tvdb_id: TDDB Id
            quality_profile_id: Database id for quality profile
            root_dir: Root folder location, full path will be created from this
            season_folder: Create a folder for each season.
            monitored: Monitor this series.
            ignore_episodes_with_files: Ignore any episodes with existing files.
            ignore_episodes_without_files: Ignore any episodes without existing files.
            search_for_missing_episodes: Search for missing episodes to download.
        """
        series_json = await self._async_construct_series_json(
            tvdb_id,
            quality_profile_id,
            root_dir,
            season_folder,
            monitored,
            ignore_episodes_with_files,
            ignore_episodes_without_files,
            search_for_missing_episodes,
        )
        return await self._async_request(
            "series",
            data=series_json,
            datatype=SonarrSeries,
            method=HTTPMethod.POST,
        )

    async def async_edit_series(self, data: SonarrSeriesUpdateParams) -> SonarrSeries:
        """Edit an existing series."""
        return await self._async_request(
            "series",
            data=data,
            datatype=SonarrSeries,
            method=HTTPMethod.PUT,
        )

    async def async_delete_series(
        self, seriesid: int, delete_files: bool = False
    ) -> dict:
        """Delete the series with the given id.

        delete_files: If true series folder and files will be deleted.
        """
        return await self._async_request(
            f"series/{seriesid}",
            params={"deleteFiles": str(delete_files)},
            method=HTTPMethod.DELETE,
        )

    async def async_lookup_series(
        self, term: str | None = None, seriesid: int | None = None
    ) -> list[SonarrSeriesLookup]:
        """Search for new shows on TheTVDB.com utilizing sonarr.tv's.

        caching and augmentation proxy.
        """
        if term is None and seriesid is None:
            raise ArrResourceNotFound(self, "A term or TVDB id must be included")
        return await self._async_request(
            "series/lookup",
            datatype=SonarrSeriesLookup,
            params={"term": quote(term, safe="") if term else f"tvdb:{seriesid}"},
        )

    async def async_get_import_lists(
        self, listid: int | None = None
    ) -> SonarrImportList | list[SonarrImportList]:
        """Get information about import list.

        id: Get import list matching id. Leave blank for all.
        """
        return await self._async_request(
            f"importlist{'' if listid is None else f'/{listid}'}",
            datatype=SonarrImportList,
        )

    async def async_edit_import_list(self, data: SonarrImportList) -> SonarrImportList:
        """Edit import list."""
        return await self._async_request(
            "importlist", data=data, datatype=SonarrImportList, method=HTTPMethod.PUT
        )

    async def async_add_import_list(self, data: SonarrImportList) -> SonarrImportList:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=SonarrImportList, method=HTTPMethod.POST
        )

    async def async_test_import_lists(
        self, data: SonarrImportList | None = None
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

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 10,
        ascending: bool = False,
        sort_key: str = "date",
    ) -> SonarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Direction to sort items.
            sort_key: id, date, or series.Title.
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
            datatype=SonarrBlocklist,
        )

    @api_command("config/naming", datatype=SonarrNamingConfig)
    async def async_get_naming_config(self) -> SonarrNamingConfig:
        """Get information about naming configuration."""

    async def async_edit_naming_config(
        self, data: SonarrNamingConfig
    ) -> SonarrNamingConfig:
        """Edit Settings for file and folder naming."""
        return await self._async_request(
            "config/naming",
            data=data,
            datatype=SonarrNamingConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_notifications(
        self, notifyid: int | None = None
    ) -> SonarrNotification | list[SonarrNotification]:
        """Get information about notification.

        id: Get notification matching id. Leave blank for all.
        """
        return await self._async_request(
            f"notification{'' if notifyid is None else f'/{notifyid}'}",
            datatype=SonarrNotification,
        )

    async def async_edit_notification(
        self, data: SonarrNotification
    ) -> SonarrNotification:
        """Edit a notification."""
        return await self._async_request(
            "notification",
            data=data,
            datatype=SonarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_add_notification(
        self, data: SonarrNotification
    ) -> SonarrNotification:
        """Add a notification."""
        return await self._async_request(
            "notification",
            data=data,
            datatype=SonarrNotification,
            method=HTTPMethod.POST,
        )

    async def async_test_notifications(
        self, data: SonarrNotification | None = None
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

    async def async_get_rename(self, seriesid: int) -> list[SonarrRename]:
        """Get files matching specified id that are not properly renamed yet."""
        return await self._async_request(
            "rename",
            params={"seriesId": seriesid},
            datatype=SonarrRename,
        )

    async def async_get_tags_details(
        self, tagid: int | None = None
    ) -> SonarrTagDetails | list[SonarrTagDetails]:
        """Get information about tag details.

        id: Get tag details matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag/detail{'' if tagid is None else f'/{tagid}'}",
            datatype=SonarrTagDetails,
        )

    async def _async_construct_series_json(  # pylint: disable=too-many-arguments
        self,
        tvdb_id: int,
        quality_profile_id: int,
        root_dir: str,
        season_folder: bool = True,
        monitored: bool = True,
        ignore_episodes_with_files: bool = False,
        ignore_episodes_without_files: bool = False,
        search_for_missing_episodes: bool = False,
    ) -> dict[str, Any] | None:
        """Search for new shows on trakt and returns Series JSON to add.

        Args:
            tvdb_id: TVDB id to search
            quality_profile_id: Database id for Quality profile
            root_dir: Root directory for media
            season_folder: Specify if a season folder should be created.
            monitored: Specify if the series should be monitored.
            ignore_episodes_with_files: Ignore episodes that already have files.
            ignore_episodes_without_files: Ignore episodes that dont have any files.
            search_for_missing_episodes: Search for any missing episodes and download them.
        """
        result = await self.async_lookup_series(seriesid=tvdb_id)
        if not isinstance(result, list):
            return None
        series = result[0]
        assert isinstance(series, dict)
        if not monitored and series.get("seasons"):
            for season in series["seasons"]:
                season["monitored"] = False

        return {
            "title": series["title"],
            "seasons": series["seasons"],
            "rootFolderPath": root_dir,
            "qualityProfileId": quality_profile_id,
            "seasonFolder": season_folder,
            "monitored": monitored,
            "tvdbId": tvdb_id,
            "images": series["images"],
            "titleSlug": series["titleSlug"],
            "addOptions": {
                "ignoreEpisodesWithFiles": ignore_episodes_with_files,
                "ignoreEpisodesWithoutFiles": ignore_episodes_without_files,
                "searchForMissingEpisodes": search_for_missing_episodes,
            },
        }

    async def async_get_localization(self) -> Any:
        """Get localization strings."""
        raise NotImplementedError()

    async def async_get_languages(self, langid: int | None = None) -> Any:
        """Get import list exclusions."""
        raise NotImplementedError()
