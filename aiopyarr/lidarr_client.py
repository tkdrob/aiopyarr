"""Lidarr API."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from aiohttp.client import ClientSession

from aiopyarr.exceptions import ArrException

from .const import (
    ALBUM_ID,
    ALL,
    ARTIST_ID,
    DATE,
    EVENT_TYPE,
    IS_VALID,
    PAGE,
    PAGE_SIZE,
    SORT_DIRECTION,
    SORT_KEY,
    TERM,
    TITLE,
    HTTPMethod,
)
from .models.host_configuration import PyArrHostConfiguration
from .models.lidarr import (
    LidarrAlbum,
    LidarrAlbumEditor,
    LidarrAlbumHistory,
    LidarrAlbumLookup,
    LidarrAlbumStudio,
    LidarrArtist,
    LidarrArtistEditor,
    LidarrBlocklist,
    LidarrCalendar,
    LidarrCommands,
    LidarrEventType,
    LidarrHistory,
    LidarrImportList,
    LidarrImportListActionType,
    LidarrManualImport,
    LidarrMetadataProfile,
    LidarrMetadataProvider,
    LidarrParse,
    LidarrQueue,
    LidarrQueueItem,
    LidarrRelease,
    LidarrRename,
    LidarrRetag,
    LidarrSearch,
    LidarrSortKeys,
    LidarrTagDetails,
    LidarrTrack,
    LidarrTrackFile,
    LidarrTrackFileEditor,
    LidarrWantedCutoff,
)
from .models.request import Command, SortDirection
from .request_client import RequestClient


class LidarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Lidarr endpoints."""

    __name__ = "Lidarr"

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        port: int = 8686,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 10,
        raw_response: bool = False,
        api_ver: str = "v1",
    ) -> None:
        """Initialize Lidarr API."""
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

    async def async_get_albums(
        self,
        albumids: int | list[int] | None = None,
        artistid: int | None = None,
        foreignalbumid: int | None = None,
        allartistalbums: bool = False,
    ) -> LidarrAlbum | list[LidarrAlbum]:
        """Get info about specified album by id, leave blank for all."""
        params: dict[str, str | int | list[int]] = {}
        params["includeAllArtistAlbums"] = str(allartistalbums)
        if isinstance(albumids, list):
            params["albumids"] = albumids
        if artistid is not None:
            params[ARTIST_ID] = artistid
        if foreignalbumid is not None:
            params["foreignAlbumId"] = foreignalbumid
        cmd = "" if isinstance(albumids, list) or albumids is None else f"/{albumids}"
        return await self._async_request(
            f"album{cmd}",
            params=params,
            datatype=LidarrAlbum,
        )

    async def async_add_album(self, data: LidarrAlbum) -> LidarrAlbum:
        """Add album to database."""
        return await self._async_request(
            "album", data=data, datatype=LidarrAlbum, method=HTTPMethod.POST
        )

    async def async_edit_albums(
        self, data: LidarrAlbum | LidarrAlbumEditor
    ) -> LidarrAlbum | list[LidarrAlbum]:
        """Edit album database info."""
        return await self._async_request(
            f"album{'' if isinstance(data, LidarrAlbum) else '/monitor'}",
            data=data,
            datatype=LidarrAlbum,
            method=HTTPMethod.PUT,
        )

    async def async_delete_album(self, albumid: int) -> None:
        """Delete the album with the given id."""
        return await self._async_request(f"album/{albumid}", method=HTTPMethod.DELETE)

    async def async_album_studio(self, data: LidarrAlbumStudio) -> None:
        """Change monitoring status via album studio."""
        return await self._async_request(
            "albumstudio",
            data=data,
            method=HTTPMethod.POST,
        )

    async def async_get_artists(
        self,
        entryid: str | int | None = None,
    ) -> LidarrArtist | list[LidarrArtist]:
        """Get info about specified artists by id, leave blank for all.

        entryid: Include a string to search by MusicBrainz id.
        """
        command = "" if isinstance(entryid, str) or entryid is None else f"/{entryid}"
        return await self._async_request(
            f"artist{command}",
            params={"mbId": entryid} if isinstance(entryid, str) else None,
            datatype=LidarrArtist,
        )

    async def async_add_artist(self, data: LidarrArtist) -> LidarrArtist:
        """Add artist to database."""
        return await self._async_request(
            "artist", data=data, datatype=LidarrArtist, method=HTTPMethod.POST
        )

    async def async_edit_artists(
        self, data: LidarrArtist | LidarrArtistEditor
    ) -> LidarrArtist | list[LidarrArtist]:
        """Edit artist database info."""
        return await self._async_request(
            f"artist{'' if isinstance(data, LidarrArtist) else '/editor'}",
            data=data,
            datatype=LidarrArtist,
            method=HTTPMethod.PUT,
        )

    async def async_delete_artists(self, data: int | dict) -> None:
        """Delete the artists with the given ids."""
        return await self._async_request(
            f"artist/{data if isinstance(data, int) else 'editor'}",
            data=data if not isinstance(data, int) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_album_lookup(self, term: str) -> list[LidarrAlbumLookup]:
        """Search for new albums using a term."""
        return await self._async_request(
            "album/lookup", params={TERM: term}, datatype=LidarrAlbumLookup
        )

    # artist/import POST not confirmed

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        sort_key: LidarrSortKeys = LidarrSortKeys.DATE,
    ) -> LidarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_key: date, id, artistid, sourcetitle, quality,
            indexer, path, or message. (Others do not apply)
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_DIRECTION: sort_dir.value,
            SORT_KEY: sort_key.value,
        }
        return await self._async_request(
            "blacklist",
            params=params,
            datatype=LidarrBlocklist,
        )

    async def async_get_calendar(  # pylint: disable=too-many-arguments
        self,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        albumid: int | None = None,
        unmonitored: bool = False,
    ) -> LidarrCalendar | list[LidarrCalendar]:
        """Get calendar items.

        albumid: Specify to get calendar of releases from album id
        """
        params = {"unmonitored": str(unmonitored)}
        if start_date:
            params["start"] = start_date.strftime("%Y-%m-%d")
        if end_date:
            params["end"] = end_date.strftime("%Y-%m-%d")
        return await self._async_request(
            f"calendar{'' if albumid is None else f'/{albumid}'}",
            params=params,
            datatype=LidarrCalendar,
        )

    async def async_lidarr_command(self, command: LidarrCommands) -> Command:
        """Send a command to Lidarr."""
        return await self._async_request(
            "command",
            data={"name": command.value},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_wanted(  # pylint: disable=too-many-arguments
        self,
        recordid: int | None = None,
        sort_key: LidarrSortKeys = LidarrSortKeys.TITLE,
        page: int = 1,
        page_size: int = 10,
        missing: bool = True,
    ) -> LidarrWantedCutoff | LidarrAlbum:
        """Get wanted albums not meeting cutoff or missing.

        Args:
            sort_key: id, title, ratings, or quality". (Others do not apply)
            page: Page number to return.
            page_size: Number of items per page.
            missing: Search for missing or cutoff not met
        """
        params = {
            SORT_KEY: sort_key.value,
            PAGE: page,
            PAGE_SIZE: page_size,
        }
        _cmd = "missing" if missing else "cutoff"
        return await self._async_request(
            f"wanted/{_cmd}{'' if recordid is None else f'/{recordid}'}",
            params=params,
            datatype=LidarrWantedCutoff if recordid is None else LidarrAlbum,
        )

    async def async_parse(self, title: str) -> LidarrParse:
        """Return the movie with matching file name."""
        params = {TITLE: title}
        return await self._async_request("parse", params=params, datatype=LidarrParse)

    async def async_get_history(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        pagesize: int = 10,
        sort_key: LidarrSortKeys = LidarrSortKeys.DATE,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        event_type: LidarrEventType | None = None,
        artist: bool = False,
        album: bool = False,
    ) -> LidarrHistory:
        """Get history.

        sort_key: date, quality, title, id, artistid, path, ratings, or sourcetitle
                (Others do not apply)
        """
        params = {
            PAGE: page,
            PAGE_SIZE: pagesize,
            SORT_KEY: sort_key.value,
            SORT_DIRECTION: sort_dir.value,
        }
        if event_type and event_type in LidarrEventType:
            params[EVENT_TYPE] = event_type.value
        if artist is not None:
            params["includeArtist"] = str(artist)
        if album is not None:
            params["includeAlbum"] = str(album)
        return await self._async_request(
            "history",
            params=params,
            datatype=LidarrHistory,
        )

    async def async_get_history_since(
        self,
        date: datetime | None = None,
        artistid: int | None = None,
        event_type: LidarrEventType | None = None,
    ) -> list[LidarrAlbumHistory]:
        """Get history since specified date.

        artist: True, include artist info in response
                int, search history by artist
        album: True, include album info in response
                int, specify album when artist: int is specified
        date: Specify a datetime object to get history since that date
        """
        if date is None and artistid is None:
            raise ArrException(self, "Either date or artistid is required")
        params: dict[str, int | str] = {}
        if event_type and event_type in LidarrEventType:
            params[EVENT_TYPE] = event_type.value
        if isinstance(date, datetime):
            params[DATE] = date.strftime("%Y-%m-%d")
        elif artistid is not None:
            params[ARTIST_ID] = artistid
        return await self._async_request(
            f"history/{'since' if isinstance(date, datetime) else 'artist'}",
            params=params,
            datatype=LidarrAlbumHistory,
        )

    async def async_get_import_lists(
        self, listid: int | None = None
    ) -> LidarrImportList | list[LidarrImportList]:
        """Get import lists."""
        return await self._async_request(
            f"importlist{'' if listid is None else f'/{listid}'}",
            datatype=LidarrImportList,
        )

    async def async_edit_import_list(self, data: LidarrImportList) -> LidarrImportList:
        """Edit import list."""
        return await self._async_request(
            "importlist",
            data=data,
            datatype=LidarrImportList,
            method=HTTPMethod.PUT,
        )

    async def async_add_import_list(self, data: LidarrImportList) -> LidarrImportList:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=LidarrImportList, method=HTTPMethod.POST
        )

    async def async_test_import_lists(
        self, data: LidarrImportList | None = None
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

    async def async_importlist_action(
        self, action: LidarrImportListActionType, data: LidarrImportList | None = None
    ) -> dict[str, Any]:
        """Perform import list action."""
        if action is LidarrImportListActionType.GET_PLAYLISTS and data is None:
            raise ArrException(self, "Data is required when calling getPlaylists")
        return await self._async_request(
            f"importlist/action/{action.value}",
            data=data,
            method=HTTPMethod.POST,
        )

    async def async_get_metadata_profiles(
        self, profileid: int | None = None
    ) -> LidarrMetadataProfile | list[LidarrMetadataProfile]:
        """Get metadata profiles."""
        return await self._async_request(
            f"metadataprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=LidarrMetadataProfile,
        )

    async def async_edit_metadata_profile(
        self, data: LidarrMetadataProfile
    ) -> LidarrMetadataProfile:
        """Edit a metadata profile."""
        return await self._async_request(
            "metadataprofile",
            data=data,
            datatype=LidarrMetadataProfile,
            method=HTTPMethod.PUT,
        )

    async def async_add_metadata_profile(
        self, data: LidarrMetadataProfile
    ) -> LidarrMetadataProfile:
        """Add a metadata profile."""
        return await self._async_request(
            "metadataprofile",
            data=data,
            datatype=LidarrMetadataProfile,
            method=HTTPMethod.POST,
        )

    async def async_get_metadata_provider(self) -> LidarrMetadataProvider:
        """Get metadata provider."""
        return await self._async_request(
            "config/metadataprovider",
            datatype=LidarrMetadataProvider,
        )

    async def async_edit_metadata_provider(
        self, data: LidarrMetadataProvider
    ) -> LidarrMetadataProvider:
        """Edit metadata provider."""
        return await self._async_request(
            "config/metadataprovider",
            data=data,
            datatype=LidarrMetadataProvider,
            method=HTTPMethod.PUT,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: LidarrSortKeys = LidarrSortKeys.TIMELEFT,
        unknown_artists: bool = False,
        include_artist: bool = False,
        include_album: bool = False,
    ) -> LidarrQueue:
        """Get current download information.

        Args:
            page: page number
            page_size: number of results per page_size
            unknown_artists: Include items with an unknown artist
            include_artist: Include the artist
            include_album: Include the album
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_KEY: sort_key.value,
            "includeUnknownArtistItems": str(unknown_artists),
            "includeArtist": str(include_artist),
            "includeAlbum": str(include_album),
        }
        return await self._async_request("queue", params=params, datatype=LidarrQueue)

    async def async_get_queue_details(  # pylint: disable=too-many-arguments
        self,
        artistid: int | None = None,
        albumids: list[int] | None = None,
        include_artist: bool = False,
        include_album: bool = True,
    ) -> list[LidarrQueueItem]:
        """Get details of all items in queue."""
        params: dict = {
            "includeArtist": str(include_artist),
            "includeAlbum": str(include_album),
        }
        if artistid is not None:
            params[ARTIST_ID] = artistid
        if albumids is not None:
            params["albumIds"] = albumids
        return await self._async_request(
            "queue/details",
            params=params,
            datatype=LidarrQueueItem,
        )

    async def async_get_release(
        self, artistid: int | None = None, albumid: int | None = None
    ) -> list[LidarrRelease]:
        """Search indexers for specified fields."""
        params = {}
        if artistid is not None:
            params[ARTIST_ID] = artistid
        if albumid is not None:
            params[ALBUM_ID] = albumid
        return await self._async_request(
            "release", params=params, datatype=LidarrRelease
        )

    async def async_download_release(
        self, guid: str, indexerid: int
    ) -> list[LidarrRelease]:
        """Add a previously searched release to the download client.

        If the release is
        still in the search cache (30 minute cache). If the release is not found
        in the cache it will return a 404.

        guid: Recently searched result guid
        """
        return await self._async_request(
            "release",
            data={"guid": guid, "indexerId": indexerid},
            datatype=LidarrRelease,
            method=HTTPMethod.POST,
        )

    # Only works if an id is associated with the release
    async def async_get_pushed_release(self, releaseid: str) -> LidarrRelease:
        """Get release previously pushed by below method."""
        return await self._async_request(
            "release/push",
            params={"id": releaseid},
            datatype=LidarrRelease,
        )

    async def async_get_rename(
        self, artistid: int, albumid: int | None = None
    ) -> list[LidarrRename]:
        """Get files matching specified id that are not properly renamed yet."""
        params = {ARTIST_ID: artistid}
        if albumid is not None:
            params[ALBUM_ID] = albumid
        return await self._async_request(
            "rename",
            params=params,
            datatype=LidarrRename,
        )

    async def async_get_manual_import(  # pylint: disable=too-many-arguments
        self,
        downloadid: str,
        artistid: int = 0,
        folder: str | None = None,
        filterexistingfiles: bool = True,
        replaceexistingfiles: bool = True,
    ) -> list[LidarrManualImport]:
        """Get manual import."""
        params = {
            ARTIST_ID: artistid,
            "downloadId": downloadid,
            "filterExistingFiles": str(filterexistingfiles),
            "folder": folder if folder is not None else "",
            "replaceExistingFiles": str(replaceexistingfiles),
        }
        return await self._async_request(
            "manualimport", params=params, datatype=LidarrManualImport
        )

    async def async_edit_manual_import(
        self, data: LidarrManualImport
    ) -> list[LidarrManualImport]:
        """Get manual import."""
        return await self._async_request(
            "manualimport",
            data=data,
            datatype=LidarrManualImport,
            method=HTTPMethod.PUT,
        )

    async def async_get_retag(
        self, artistid: int, albumid: int | None = None
    ) -> list[LidarrRetag]:
        """Get retag."""
        params = {ARTIST_ID: artistid}
        if albumid is not None:
            params[ALBUM_ID] = albumid
        return await self._async_request(
            "retag",
            params=params,
            datatype=LidarrRetag,
        )

    async def async_search(self, term: str) -> list[LidarrSearch]:
        """Search for albums."""
        return await self._async_request(
            "search",
            params={TERM: term},
            datatype=LidarrSearch,
        )

    async def async_get_tags_details(
        self, tagid: int | None = None
    ) -> LidarrTagDetails | list[LidarrTagDetails]:
        """Get information about tag details.

        id: Get tag details matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag/detail{'' if tagid is None else f'/{tagid}'}",
            datatype=LidarrTagDetails,
        )

    async def async_get_tracks(
        self,
        artistid: int | None = None,
        albumid: int | None = None,
        albumreleaseid: int | None = None,
        trackids: int | list[int] | None = None,
    ) -> LidarrTrack | list[LidarrTrack]:
        """Get tracks based on specified ids.

        trackids: specify one integer to search database by track id only
        """
        if (
            artistid is None
            and albumid is None
            and albumreleaseid is None
            and trackids is None
        ):
            msg = "BadRequest: artistId, albumId, albumReleaseId or trackIds must be provided"
            raise ArrException(message=msg)
        params: dict[str, int | list[int]] = {}
        if artistid is not None:
            params[ARTIST_ID] = artistid
        if albumid is not None:
            params[ALBUM_ID] = albumid
        if albumreleaseid is not None:
            params["albumReleaseId"] = albumreleaseid
        if isinstance(trackids, list):
            params["trackIds"] = trackids
        return await self._async_request(
            f"track{f'/{trackids}' if isinstance(trackids, int) else ''}",
            params=params,
            datatype=LidarrTrack,
        )

    async def async_get_track_files(
        self,
        artistid: int | None = None,
        albumid: int | None = None,
        trackfileids: int | list[int] | None = None,
        unmapped: bool = False,
    ) -> LidarrTrackFile | list[LidarrTrackFile]:
        """Get track files based on specified ids.

        trackfileids: specify one integer to include audioTags for that id
        unmapped: True to instead get all files not matched to known albums
        """
        if artistid is None and albumid is None and trackfileids is None:
            raise ArrException(
                message="BadRequest: artistId, albumId, trackFileIds or unmapped must be provided"
            )
        params: dict[str, str | int | list[int]] = {"unmapped": str(unmapped)}
        if artistid is not None:
            params[ARTIST_ID] = artistid
        if albumid is not None:
            params[ALBUM_ID] = albumid
        if isinstance(trackfileids, list):
            params["trackFileIds"] = trackfileids
        return await self._async_request(
            f"trackfile{f'/{trackfileids}' if isinstance(trackfileids, int) else ''}",
            params=params,
            datatype=LidarrTrackFile,
        )

    async def async_edit_track_files(
        self, data: LidarrTrackFile | LidarrTrackFileEditor
    ) -> LidarrTrackFile | list[LidarrTrackFile]:
        """Edit track file attributes."""
        return await self._async_request(
            f"trackfile{'' if isinstance(data, LidarrTrackFile) else '/editor'}",
            data=data,
            datatype=LidarrTrackFile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_track_files(self, ids: int | list[int]) -> None:
        """Delete track files. Use integer for one file or list for mass deletion."""
        return await self._async_request(
            f"trackfile/{'bulk' if isinstance(ids, list) else f'{ids}'}",
            data={"trackFileIds": ids} if isinstance(ids, list) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_get_languages(self, langid: int | None = None) -> Any:
        """Get language profiles."""
        raise NotImplementedError()
