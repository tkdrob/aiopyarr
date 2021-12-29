"""Sonarr API."""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

from .const import HTTPMethod
from .decorator import api_command
from .exceptions import ArrInvalidCommand, ArrResourceNotFound
from .models.common import Command, Tag
from .request_client import RequestClient

from .models.sonarr import (  # isort:skip
    SonarrBlocklist,
    SonarrCalendar,
    SonarrEpisode,
    SonarrEpisodeFile,
    SonarrEpisodeFileQuailty,
    SonarrHistory,
    SonarrParse,
    SonarrQualityProfile,
    SonarrQueue,
    SonarrRelease,
    SonarrSeries,
    SonarrSeriesLookup,
    SonarrSeriesUpdateParams,
    SonarrWantedMissing,
)

if TYPE_CHECKING:
    from aiohttp.client import ClientSession

    from .const import HTTPResponse
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
        redact: bool = True,
        api_ver: str | None = None,
    ) -> None:
        """Initialize Sonarr API."""
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

    async def async_get_episode_files(
        self, seriesid: int, episodeid: int | None = None
    ) -> SonarrEpisodeFile | list[SonarrEpisodeFile]:
        """Get information about episode files from series.

        episodeId: Get episode files matching series. Leave blank for all episodes.
        """
        return await self._async_request(
            f"episodefile{f'/{episodeid}' if episodeid is not None else ''}",
            params={"seriesId": seriesid},
            datatype=SonarrEpisodeFile,
        )

    async def async_get_image(
        self, imageid: int, imagetype: str = "poster", size: str = "large"
    ) -> bytes:
        """Get image from Sonarr.

        type: poster, banner, or fanart
        size: large, medium, small
              pixel size: None for full size (500, 250), (70, 35), (360, 180)
        """
        value = [
            value * factor
            for key, factor in {"small": 1, "medium": 2, "large": 0}.items()
            if key == size
            for key, value in {"poster": 250, "banner": 35, "fanart": 180}.items()
            if imagetype == key
        ]

        cmd = f"MediaCover/{imageid}/{imagetype}{f'-{value}' if size != 'large' else ''}.jpg"
        response = await self._async_request(cmd)
        if isinstance(response, dict):
            raise ArrResourceNotFound
        return response

    @api_command("queue", datatype=SonarrQueue)
    async def async_get_queue(self) -> list[SonarrQueue]:
        """Get information about download queue."""

    async def async_delete_queue(
        self, queueid: int, blacklist: bool = False
    ) -> HTTPResponse:
        """Delete an item from the queue and download client."""
        return await self._async_request(
            "queue",
            params={"id": queueid, "blacklist": blacklist},
            method=HTTPMethod.DELETE,
        )

    @api_command("profile", datatype=SonarrQualityProfile)
    async def async_get_profiles(self) -> list[SonarrQualityProfile]:
        """Get information about configured quality profiles."""

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

    async def async_command_refresh_series(
        self, seriesid: int | None = None
    ) -> Command:
        """Send refresh series command."""
        data = {"name": "RefreshSeries"}
        if seriesid is not None:
            data["seriesId"] = str(seriesid)
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_rescan_series(
        self, seriesid: int | None = None
    ) -> Command:
        """Send rescan series command."""
        data = {"name": "RefreshSeries"}
        if seriesid is not None:
            data["seriesId"] = str(seriesid)
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_episode_search(self, episodeids: int) -> Command:
        """Send episode search command."""
        return await self._async_request(
            "command",
            data={"name": "EpisodeSearch", "episodeIds": episodeids},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_season_search(
        self, seriesid: int, seasonnumber: int
    ) -> Command:
        """Send season search command."""
        return await self._async_request(
            "command",
            data={
                "name": "SeasonSearch",
                "seriesId": seriesid,
                "seasonNumber": seasonnumber,
            },
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_series_search(self, seriesid: int) -> Command:
        """Send series search command."""
        return await self._async_request(
            "command",
            data={"name": "SeriesSearch", "seriesId": seriesid},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_downloaded_episode_scan(
        self,
        path: str,
        clientid: str | None = None,
        importmode: str = "Copy",
    ) -> Command:
        """Send series search command.

        importMode: Copy or Hardlink depending on Sonarr configuration
        """
        data = {"name": "DownloadedEpisodesScan", "path": path}
        data["importMode"] = importmode
        if clientid is not None:
            data["downloadClientId"] = clientid
        return await self._async_request(
            "command",
            data=data,
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_rss_sync(self) -> Command:
        """Send rss sync command."""
        return await self._async_request(
            "command",
            data={"name": "RssSync"},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_rename_files(self, files: list[int]) -> Command:
        """Send rename files command."""
        return await self._async_request(
            "command",
            data={"name": "RenameFiles", "files": files},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_rename_series(self, seriesids: list[int]) -> Command:
        """Send rename series command."""
        return await self._async_request(
            "command",
            data={"name": "RenameSeries", "seriesIds": seriesids},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_backup(self) -> Command:
        """Send backup command."""
        return await self._async_request(
            "command",
            data={"name": "Backup"},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_command_missing_search(self) -> Command:
        """Send missing episode search command."""
        return await self._async_request(
            "command",
            data={"name": "missingEpisodeSearch"},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_episodes_by_series_id(self, seriesid: int) -> SonarrEpisode:
        """Get all episodes from a given series ID."""
        return await self._async_request("episode", params={"seriesId": seriesid})

    async def async_get_episode_by_id(self, episodeid: int) -> SonarrEpisode:
        """Get a specific episode by database id."""
        return await self._async_request(f"episode/{episodeid}", datatype=SonarrEpisode)

    async def async_update_episode(self, data: SonarrEpisode) -> SonarrEpisode:
        """Update given episodes, currently only monitored is changed."""
        return await self._async_request("episode", data=data, method=HTTPMethod.PUT)

    async def async_update_episode_file_quality(
        self, fileid: int, data: SonarrEpisodeFileQuailty
    ) -> SonarrEpisodeFile:
        """Update the quality of the episode file and returns the episode file."""
        return await self._async_request(
            f"episodefile/{fileid}", data=data, method=HTTPMethod.PUT
        )

    async def async_delete_episode_file(self, fileid: int) -> dict:
        """Delete the episode file with corresponding id."""
        return await self._async_request(
            f"episodefile/{fileid}", method=HTTPMethod.DELETE
        )

    async def async_get_history(  # pylint: disable=too-many-arguments
        self,
        sort_date: bool = True,
        page: int = 1,
        page_size: int = 10,
        sort_asc: bool = False,
        recordid: int | None = None,
    ) -> SonarrHistory:
        """Get history (grabs/failures/completed).

        Args:
            sort_date: date or series.title.
            page: Page number to return.
            page_size: Number of items per page.
            sort_asc: Sort items in ascending order.
            id: Filter to a specific episode ID.
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortDir": "asc" if sort_asc is True else "desc",
            "sortKey": "date" if sort_date is True else "series.title",
        }
        if recordid:
            params["episodeId"] = recordid
        return await self._async_request(
            "history", datatype=SonarrHistory, params=params
        )

    async def async_get_wanted(
        self,
        sort_date: bool = True,
        page: int = 1,
        page_size: int = 10,
        sort_asc: bool = True,
    ) -> SonarrWantedMissing:
        """Get missing episode (episodes without files).

        Args:
            sort_date: airDateUtc or series.title.
            page: Page number to return.
            page_size: Number of items per page.
            sort_asc: Sort items in ascending order.
        """
        params = {
            "sortKey": "airDateUtc" if sort_date is True else "series.title",
            "page": page,
            "pageSize": page_size,
            "sortDir": "asc" if sort_asc is True else "desc",
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

    async def async_get_release(self, releaseid: int) -> list[SonarrRelease]:
        """Get a release with a specific episode ID."""
        return await self._async_request(
            "release",
            params={"episodeId": releaseid},
            datatype=SonarrRelease,
        )

    async def async_download_release(
        self, guid: str, indexerid: int
    ) -> list[SonarrRelease]:
        """Add a previously searched release to the download client.

        If the release is
        still in Sonarr's search cache (30 minute cache). If the release is not found
        in the cache Sonarr will return a 404.

        guid: Recently searched result guid
        """
        return await self._async_request(
            "release",
            data={"guid": guid, "indexerId": indexerid},
            datatype=SonarrRelease,
            method=HTTPMethod.POST,
        )

    async def async_push_release(
        self,
        title: str,
        download_url: str,
        protocol: str,
        publish_date: str,
    ) -> list[SonarrRelease]:
        """If the title is wanted, Sonarr will grab it.

        Args:
            title: Release name
            download_url: .torrent file URL
            protocol: "Usenet" or "Torrent
            publish_date: ISO8601 date string
        """
        data = {
            "title": title,
            "downloadUrl": download_url,
            "protocol": protocol,
            "publishDate": publish_date,
        }
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
            f"series{f'/{seriesid}' if seriesid is not None else ''}",
            datatype=SonarrSeries,
        )

    async def async_get_series_episodes(
        self, seriesid: int, episodeid: int | None = None
    ) -> list[SonarrEpisode]:
        """Get information about episodes from series."""
        response = await self._async_request(
            f"episode{f'/{episodeid}' if episodeid is not None else ''}",
            params={"seriesId": seriesid},
            datatype=SonarrEpisode,
        )
        if "message" in response and response["message"] == "NotFound":
            raise ArrResourceNotFound
        if "seriesId" in response and response["seriesId"] != seriesid:
            raise ArrResourceNotFound
        return response

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

    async def async_update_series(self, data: SonarrSeriesUpdateParams) -> SonarrSeries:
        """Update an existing series."""
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
            params={"id": seriesid, "deleteFiles": str(delete_files)},
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

    async def async_create_tag(self, label: str) -> Tag:
        """Add a new tag.

        label: Tag name / label
        """
        return await self._async_request(
            "tag",
            data={"label": label},
            datatype=Tag,
            method=HTTPMethod.POST,
        )

    async def async_update_tag(self, data: Tag) -> Tag:
        """Update an existing tag."""
        return await self._async_request("tag", data=data, method=HTTPMethod.PUT)

    async def async_delete_tag(self, tagid: int) -> dict:
        """Delete the tag with the given ID."""
        return await self._async_request(f"tag/{tagid}", method=HTTPMethod.DELETE)

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_direction: str = "descending",
        sort_key: str = "date",
    ) -> SonarrBlocklist:
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
            datatype=SonarrBlocklist,
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
