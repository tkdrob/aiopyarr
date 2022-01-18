"""Lidarr API."""
from __future__ import annotations

from datetime import datetime

from aiohttp.client import ClientSession

from aiopyarr.exceptions import ArrException

from .const import (
    ALBUM_ID,
    ALL,
    ARTIST_ID,
    ASCENDING,
    DESCENDING,
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
    LidarrArtist,
    LidarrArtistEditor,
    LidarrBlocklist,
    LidarrCalendar,
    LidarrCommands,
    LidarrEventType,
    LidarrHistory,
    LidarrImportList,
    LidarrMetadataProfile,
    LidarrParse,
    LidarrQueue,
    LidarrQueueDetail,
    LidarrRelease,
    LidarrRename,
    LidarrRetag,
    LidarrSearch,
    LidarrTagDetails,
    LidarrTrack,
    LidarrTrackDetails,
    LidarrTrackFile,
    LidarrTrackFileDetails as FileDetails,
    LidarrTrackFileEditor,
    LidarrWantedCutoff,
)
from .models.request import Command
from .request_client import RequestClient


class LidarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Lidarr endpoints."""

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
        user_agent: str | None = None,
    ) -> None:
        """Initialize Lidarr API."""
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

    async def async_album_studio(self, data: dict) -> list[LidarrAlbum]:
        """Edit database with album studio."""
        return await self._async_request(
            "albumstudio",
            data=data,
            datatype=LidarrAlbum,
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

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 10,
        ascending: bool = False,
        sort_key: str = "date",
    ) -> LidarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Direction to sort items.
            sort_key: date, id, artistid, sourcetitle, quality,
            indexer, path, or message.
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_DIRECTION: ASCENDING if ascending else DESCENDING,
            SORT_KEY: sort_key,
        }
        return await self._async_request(
            "blacklist",
            params=params,
            datatype=LidarrBlocklist,
        )

    async def async_get_calendar(  # pylint: disable=too-many-arguments
        self,
        start_date: datetime,
        end_date: datetime,
        calendarid: int | None = None,
        unmonitored: bool = False,
    ) -> LidarrCalendar | list[LidarrCalendar]:
        """Get calendar items."""
        params = {
            "start": start_date.strftime("%Y-%m-%d"),
            "end": end_date.strftime("%Y-%m-%d"),
            "unmonitored": str(unmonitored),
        }
        return await self._async_request(
            f"calendar{'' if calendarid is None else f'/{calendarid}'}",
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
        sortkey: str = TITLE,
        page: int = 1,
        page_size: int = 10,
        missing: bool = True,
    ) -> LidarrWantedCutoff | LidarrAlbum:
        """Get wanted albums not meeting cutoff or missing.

        Args:
            sortkey: id, title, ratings, or quality".
            page: Page number to return.
            page_size: Number of items per page.
            missing: Search for missing or cutoff not met
        """
        params = {
            SORT_KEY: sortkey,
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
        sortkey: str = "date",
        ascending: bool = True,
        artist: int | bool = False,
        album: int | bool = False,
        event_type: LidarrEventType | None = None,  # not working
        date: datetime | None = None,
    ) -> LidarrHistory | list[LidarrAlbumHistory]:
        """Get history.

        sortkey: date, quality
        artist: True, include artist info in response
                int, search history by artist
        album: True, include album info in response
                int, specify album when artist: int is specified
        date: Specify a datetime object to get history since that date
        """
        params = {
            PAGE: page,
            PAGE_SIZE: pagesize,
            SORT_KEY: sortkey,
            SORT_DIRECTION: ASCENDING if ascending else DESCENDING,
        }
        if event_type and event_type in LidarrEventType:
            params["eventType"] = event_type.value
        if isinstance(artist, bool):
            params["includeArtist"] = str(artist)
            command = f"history{'/since' if isinstance(date, datetime) else ''}"
            if isinstance(album, bool):
                params["includeAlbum"] = str(album)
        else:
            params[ARTIST_ID] = artist
            if not isinstance(album, bool):
                params[ALBUM_ID] = album
            command = "history/artist"
        if isinstance(date, datetime):
            params["date"] = date.strftime("%Y-%m-%d")
        _type = date is None and isinstance(artist, bool)
        return await self._async_request(
            command,
            params=params,
            datatype=LidarrHistory if _type else LidarrAlbumHistory,
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

    # {name} not yet confirmed
    async def async_importlist_action(self, data: LidarrImportList) -> LidarrImportList:
        """Perform import list action."""
        return await self._async_request(
            f"importlist/action/{data.name}",
            data=data,
            datatype=LidarrImportList,
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

    # metadataprovider not working, 404

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: str = "timeleft",
        unknown_artists: bool = False,
        include_artist: bool = False,
        include_album: bool = False,
    ) -> LidarrQueue:
        """Get current download information.

        Args:
            page: page number
            page_size: number of results per page_size
            sort_key: timeleft, title, id, or date
            unknown_artists: Include items with an unknown artist
            include_artist: Include the artist
            include_album: Include the album
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_KEY: sort_key,
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
    ) -> list[LidarrQueueDetail]:
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
            datatype=LidarrQueueDetail,
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
    ) -> LidarrTrackDetails | list[LidarrTrack]:
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
            datatype=LidarrTrackDetails if isinstance(trackids, int) else LidarrTrack,
        )

    async def async_get_track_files(
        self,
        artistid: int | None = None,
        albumid: int | None = None,
        trackfileids: int | list[int] | None = None,
        unmapped: bool = False,  # Not sure what this does
    ) -> FileDetails | list[LidarrTrackFile]:
        """Get track files based on specified ids.

        trackfileids: specify one integer to include audioTags for that id
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
            datatype=FileDetails if isinstance(trackfileids, int) else LidarrTrackFile,
        )

    # documented, but may throw code 500
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
