"""Readarr API."""
from __future__ import annotations

from datetime import datetime

from aiohttp.client import ClientSession

from .const import (
    ALL,
    AUTHOR_ID,
    BOOK_ID,
    DATE,
    EVENT_TYPE,
    IS_VALID,
    NOTIFICATION,
    PAGE,
    PAGE_SIZE,
    SORT_DIRECTION,
    SORT_KEY,
    TERM,
    TITLE,
    HTTPMethod,
)
from .exceptions import ArrException
from .models.host_configuration import PyArrHostConfiguration
from .models.readarr import (
    ReadarrAuthor,
    ReadarrAuthorEditor,
    ReadarrAuthorLookup,
    ReadarrBlocklist,
    ReadarrBook,
    ReadarrBookFile,
    ReadarrBookFileEditor,
    ReadarrBookHistory,
    ReadarrBookLookup,
    ReadarrBookshelf,
    ReadarrBookTypes,
    ReadarrCalendar,
    ReadarrCommands,
    ReadarrDevelopmentConfig,
    ReadarrEventType,
    ReadarrHistory,
    ReadarrImportList,
    ReadarrImportListOptions,
    ReadarrManualImport,
    ReadarrMetadataProfile,
    ReadarrMetadataProvider,
    ReadarrNamingConfig,
    ReadarrNotification,
    ReadarrParse,
    ReadarrQueue,
    ReadarrQueueDetail,
    ReadarrRelease,
    ReadarrRename,
    ReadarrRetag,
    ReadarrRootFolder,
    ReadarrSearch,
    ReadarrSeries,
    ReadarrSortKeys,
    ReadarrTagDetails,
    ReadarrWantedCutoff,
    ReadarrWantedMissing,
)
from .models.request import Command, Indexer, SortDirection
from .request_client import RequestClient


class ReadarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Readarr endpoints."""

    __name__ = "Readarr"

    def __init__(  # pylint: disable=too-many-arguments
        self,
        host_configuration: PyArrHostConfiguration | None = None,
        session: ClientSession | None = None,
        hostname: str | None = None,
        ipaddress: str | None = None,
        url: str | None = None,
        api_token: str | None = None,
        port: int = 8787,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 10,
        raw_response: bool = False,
        api_ver: str = "v1",
    ) -> None:
        """Initialize Readarr API."""
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

    async def async_get_authors(
        self, authorid: int | None = None
    ) -> ReadarrAuthor | list[ReadarrAuthor]:
        """Get info about specified author by id, leave blank for all."""
        command = f"author{'' if authorid is None else f'/{authorid}'}"
        return await self._async_request(command, datatype=ReadarrAuthor)

    async def async_author_lookup(self, term: str) -> list[ReadarrAuthorLookup]:
        """Search for new authors using a term."""
        return await self._async_request(
            "author/lookup", params={TERM: term}, datatype=ReadarrAuthorLookup
        )

    async def async_add_author(self, data: ReadarrAuthor) -> ReadarrAuthor:
        """Add author to database."""
        return await self._async_request(
            "author", data=data, datatype=ReadarrAuthor, method=HTTPMethod.POST
        )

    async def async_edit_authors(
        self, data: ReadarrAuthor | ReadarrAuthorEditor
    ) -> ReadarrAuthor | list[ReadarrAuthor]:
        """Edit author database info."""
        return await self._async_request(
            f"author{'' if isinstance(data, ReadarrAuthor) else '/editor'}",
            data=data,
            datatype=ReadarrAuthor,
            method=HTTPMethod.PUT,
        )

    async def async_delete_authors(
        self,
        authorids: int | list[int],
        delete_files: bool = False,
        import_list_exclusion: bool = True,
    ) -> None:
        """Delete the author with the given id.

        Args:
            authorids: Database ids for author (authorMetadataId)
            delete_files: If true author folder and files will be deleted
            import_list_exclusion: Add an exclusion so author doesn't get re-added
        """
        data = {
            "deleteFiles": str(delete_files),
            "addImportListExclusion": str(import_list_exclusion),
        }
        return await self._async_request(
            f"author/{'editor' if isinstance(authorids, list) else authorids}",
            data=data,
            method=HTTPMethod.DELETE,
        )

    async def async_readarr_command(self, command: ReadarrCommands) -> Command:
        """Send a command to Readarr."""
        return await self._async_request(
            "command",
            data={"name": command.value},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        sort_key: ReadarrSortKeys = ReadarrSortKeys.DATE,
    ) -> ReadarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_key: date, id, authorid, sourcetitle, quality,
            indexer, path, message, or ratings. (Others do not apply)
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
            datatype=ReadarrBlocklist,
        )

    async def async_get_wanted_missing(  # includeAuthor, sortDir not working
        self,
        recordid: int | None = None,
        sort_key: ReadarrSortKeys = ReadarrSortKeys.TITLE,
        page: int = 1,
        page_size: int = 10,
    ) -> ReadarrWantedMissing | ReadarrBook:
        """Get missing books.

        Args:
            sort_key: id, title, ratings, bookid, or quality. (Others do not apply)
            page: Page number to return.
            page_size: Number of items per page.
        """
        params = {
            SORT_KEY: sort_key.value,
            PAGE: page,
            PAGE_SIZE: page_size,
        }
        return await self._async_request(
            f"wanted/missing{'' if recordid is None else f'/{recordid}'}",
            params=params,
            datatype=ReadarrWantedMissing if recordid is None else ReadarrBook,
        )

    async def async_get_wanted_cutoff(  # includeAuthor, sortDir not working
        self,
        recordid: int | None = None,
        sort_key: ReadarrSortKeys = ReadarrSortKeys.TITLE,
        page: int = 1,
        page_size: int = 10,
    ) -> ReadarrWantedCutoff | ReadarrBook:
        """Get wanted books not meeting cutoff.

        Args:
            sort_key: id, title, ratings, bookid, or quality". (others do not apply)
            page: Page number to return.
            page_size: Number of items per page.
        """
        params = {
            SORT_KEY: sort_key.value,
            PAGE: page,
            PAGE_SIZE: page_size,
        }
        return await self._async_request(
            f"wanted/cutoff{'' if recordid is None else f'/{recordid}'}",
            params=params,
            datatype=ReadarrWantedCutoff if recordid is None else ReadarrBook,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_key: ReadarrSortKeys = ReadarrSortKeys.TIMELEFT,
        unknown_authors: bool = False,
        include_author: bool = False,
        include_book: bool = False,
    ) -> ReadarrQueue:
        """Get current download information.

        Args:
            page: page number
            page_size: number of results per page_size
            unknown_authors: Include items with an unknown author
            include_author: Include the author
            include_book: Include the book
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_KEY: sort_key.value,
            "includeUnknownAuthorItems": str(unknown_authors),
            "includeAuthor": str(include_author),
            "includeBook": str(include_book),
        }
        return await self._async_request("queue", params=params, datatype=ReadarrQueue)

    async def async_get_queue_details(  # pylint: disable=too-many-arguments
        self,
        authorid: int | None = None,
        bookids: list[int] | None = None,
        unknown_authors: bool = False,
        include_author: bool = False,
        include_book: bool = True,
    ) -> list[ReadarrQueueDetail]:
        """Get details of all items in queue."""
        params: dict = {
            "includeUnknownAuthorItems": str(unknown_authors),
            "includeAuthor": str(include_author),
            "includeBook": str(include_book),
        }
        if authorid is not None:
            params[AUTHOR_ID] = authorid
        if bookids is not None:
            params["bookIds"] = bookids
        return await self._async_request(
            "queue/details",
            params=params,
            datatype=ReadarrQueueDetail,
        )

    async def async_get_book(
        self, bookid: int | None = None
    ) -> ReadarrBook | list[ReadarrBook]:
        """Return all books in your collection or book with matching book ID."""
        path = f"book{'' if bookid is None else f'/{bookid}'}"
        return await self._async_request(path, datatype=ReadarrBook)

    async def async_add_book(self, data: ReadarrBook) -> ReadarrBook:
        """Add a new book and its associated author (if not already added)."""
        return await self._async_request(
            "book", data=data, datatype=ReadarrBook, method=HTTPMethod.POST
        )

    async def async_edit_book(self, data: ReadarrBook) -> ReadarrBook:
        """Edit an existing book (if not already added)."""
        return await self._async_request(
            "book", data=data, datatype=ReadarrBook, method=HTTPMethod.PUT
        )

    async def async_delete_book(
        self,
        bookid: int,
        delete_files: bool = False,
        import_list_exclusion: bool = True,
    ) -> None:
        """Delete the book with the given id.

        Args:
            bookid: Database id for book
            delete_files: If true book folder and files will be deleted
            import_list_exclusion: Add an exclusion so book doesn't get re-added
        """
        params = {
            "deleteFiles": str(delete_files),
            "addImportListExclusion": str(import_list_exclusion),
        }
        return await self._async_request(
            f"book/{bookid}", params=params, method=HTTPMethod.DELETE
        )

    async def async_get_book_file(
        self,
        authorid: int | None = None,
        bookid: list[int] | None = None,
        fileid: int | list[int] | None = None,
        unmapped: bool = False,
    ) -> ReadarrBookFile:
        """Return all books in your collection or book with matching book ID.

        unmapped: True to instead get all files not matched to known books
        """
        params: dict[str, str | int | list[int]] = {"unmapped": str(unmapped)}
        if not isinstance(fileid, int):
            if authorid is not None:
                params[AUTHOR_ID] = authorid
            if bookid is not None:
                params[BOOK_ID] = bookid
            if fileid is not None:
                params["bookFileIds"] = fileid
        if isinstance(fileid, list):
            path = "bookfile"
        else:
            path = f"bookfile{'' if fileid is None else f'/{fileid}'}"
        return await self._async_request(path, params=params, datatype=ReadarrBookFile)

    async def async_edit_book_files(
        self, data: ReadarrBookFile | ReadarrBookFileEditor
    ) -> ReadarrBookFile | list[ReadarrBookFile]:
        """Edit book file attributes."""
        return await self._async_request(
            f"bookfile{'' if isinstance(data, ReadarrBookFile) else '/editor'}",
            data=data,
            datatype=ReadarrBookFile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_book_files(self, ids: int | list[int]) -> None:
        """Delete book files. Use integer for one file or list for mass deletion."""
        return await self._async_request(
            f"bookfile/{'bulk' if isinstance(ids, list) else f'{ids}'}",
            data={"bookFileIds": ids} if isinstance(ids, list) else None,
            method=HTTPMethod.DELETE,
        )

    async def async_lookup_book(
        self, term: str, booktype: ReadarrBookTypes = ReadarrBookTypes.ISBN
    ) -> list[ReadarrBookLookup]:
        """Search for new books using a term, goodreads ID, isbn or asin."""
        return await self._async_request(
            "book/lookup",
            params={TERM: f"{booktype}:{term}"},
            datatype=ReadarrBookLookup,
        )

    async def async_add_bookshelf(
        self, data: ReadarrBookshelf
    ) -> ReadarrBookshelf:  # verify
        """Add a bookshelf to the database."""
        return await self._async_request("bookshelf", data=data, method=HTTPMethod.POST)

    async def async_get_calendar(  # pylint: disable=too-many-arguments
        self,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        bookid: int | None = None,
        unmonitored: bool = False,
        includeauthor: bool = False,
    ) -> ReadarrCalendar | list[ReadarrCalendar]:
        """Get calendar items.

        bookid: Specify to get calendar of releases from book id
        """
        params = {
            "unmonitored": str(unmonitored),
            "includeAuthor": str(includeauthor),
        }
        if start_date:
            params["start"] = start_date.strftime("%Y-%m-%d")
        if end_date:
            params["end"] = end_date.strftime("%Y-%m-%d")
        return await self._async_request(
            f"calendar{'' if bookid is None else f'/{bookid}'}",
            params=params,
            datatype=ReadarrCalendar,
        )

    # /api/v1/calendar/readarr.ics not working

    async def async_get_development_config(self) -> ReadarrDevelopmentConfig:
        """Get development config."""
        return await self._async_request(
            "config/development", datatype=ReadarrDevelopmentConfig
        )

    async def async_edit_development_config(
        self, data: ReadarrDevelopmentConfig
    ) -> ReadarrDevelopmentConfig:
        """Edit development config."""
        return await self._async_request(
            "config/development",
            data=data,
            datatype=ReadarrDevelopmentConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_history(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 20,
        sort_dir: SortDirection = SortDirection.DEFAULT,
        sort_key: ReadarrSortKeys = ReadarrSortKeys.DATE,
        event_type: ReadarrEventType | None = None,
    ) -> ReadarrHistory:
        """Get history.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            sort_key: date, id, title, sourcetitle, path, ratings, or quality
                    (Others do not apply)
        """
        params = {
            PAGE: page,
            PAGE_SIZE: page_size,
            SORT_DIRECTION: sort_dir.value,
            SORT_KEY: sort_key.value,
        }
        if event_type and event_type in ReadarrEventType:
            params[EVENT_TYPE] = event_type.value
        return await self._async_request(
            "history", params=params, datatype=ReadarrHistory
        )

    async def async_get_history_since(
        self,
        event_type: ReadarrEventType | None = None,
        date: datetime | None = None,
        authorid: int | None = None,
    ) -> list[ReadarrBookHistory]:
        """Get history since specified date.

        Args:
            authorid: include to search history by author id (date will not apply)
        Radarr permits a naked query but its required here to avoid excessively large
        data sets where filtering should be used instead
        """
        if date is None and authorid is None:
            raise ArrException(self, "Either date or authorid is required")
        params: dict[str, int | str] = {}
        if event_type and event_type in ReadarrEventType:
            params[EVENT_TYPE] = event_type.value
        if isinstance(date, datetime):
            params[DATE] = date.strftime("%Y-%m-%d")
        elif authorid is not None:
            params[AUTHOR_ID] = authorid
        return await self._async_request(
            f"history/{'since' if isinstance(date, datetime) else 'author'}",
            params=params,
            datatype=ReadarrBookHistory,
        )

    async def async_get_import_lists(
        self, listid: int | None = None
    ) -> ReadarrImportList | list[ReadarrImportList]:
        """Get import lists."""
        return await self._async_request(
            f"importlist{'' if listid is None else f'/{listid}'}",
            datatype=ReadarrImportList,
        )

    async def async_edit_import_list(
        self, data: ReadarrImportList
    ) -> ReadarrImportList:
        """Edit import list."""
        return await self._async_request(
            "importlist",
            data=data,
            datatype=ReadarrImportList,
            method=HTTPMethod.PUT,
        )

    async def async_add_import_list(self, data: ReadarrImportList) -> ReadarrImportList:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=ReadarrImportList, method=HTTPMethod.POST
        )

    async def async_test_import_lists(
        self, data: ReadarrImportList | None = None
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
        self, data: Indexer, action: str = "newznabCategories"
    ) -> ReadarrImportListOptions:
        """Perform import list action. Other actions may be possible."""
        return await self._async_request(
            f"importlist/action/{action}",
            data=data,
            datatype=ReadarrImportListOptions,
            method=HTTPMethod.POST,
        )

    async def async_get_metadata_profiles(
        self, profileid: int | None = None
    ) -> ReadarrMetadataProfile | list[ReadarrMetadataProfile]:
        """Get metadata profiles."""
        return await self._async_request(
            f"metadataprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=ReadarrMetadataProfile,
        )

    async def async_edit_metadata_profile(
        self, data: ReadarrMetadataProfile
    ) -> ReadarrMetadataProfile:
        """Edit a metadata profile."""
        return await self._async_request(
            "metadataprofile",
            data=data,
            datatype=ReadarrMetadataProfile,
            method=HTTPMethod.PUT,
        )

    async def async_add_metadata_profile(
        self, data: ReadarrMetadataProfile
    ) -> ReadarrMetadataProfile:
        """Add a metadata profile."""
        return await self._async_request(
            "metadataprofile",
            data=data,
            datatype=ReadarrMetadataProfile,
            method=HTTPMethod.POST,
        )

    async def async_get_metadata_provider(self) -> ReadarrMetadataProvider:
        """Get metadata provider."""
        return await self._async_request(
            "config/metadataprovider",
            datatype=ReadarrMetadataProvider,
        )

    async def async_edit_metadata_provider(
        self,
        data: ReadarrMetadataProvider,
    ) -> ReadarrMetadataProvider:
        """Edit metadata provider."""
        return await self._async_request(
            "config/metadataprovider",
            data=data,
            datatype=ReadarrMetadataProvider,
            method=HTTPMethod.PUT,
        )

    async def async_get_naming_config(self) -> ReadarrNamingConfig:
        """Get information about naming configuration."""
        return await self._async_request("config/naming", datatype=ReadarrNamingConfig)

    async def async_edit_naming_config(
        self, data: ReadarrNamingConfig
    ) -> ReadarrNamingConfig:
        """Edit Settings for file and folder naming."""
        return await self._async_request(
            "config/naming",
            data=data,
            datatype=ReadarrNamingConfig,
            method=HTTPMethod.PUT,
        )

    async def async_get_notifications(
        self, notifyid: int | None = None
    ) -> ReadarrNotification | list[ReadarrNotification]:
        """Get information about notification.

        id: Get notification matching id. Leave blank for all.
        """
        return await self._async_request(
            f"notification{'' if notifyid is None else f'/{notifyid}'}",
            datatype=ReadarrNotification,
        )

    async def async_edit_notification(
        self, data: ReadarrNotification
    ) -> ReadarrNotification:
        """Edit a notification."""
        return await self._async_request(
            NOTIFICATION,
            data=data,
            datatype=ReadarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_add_notification(
        self, data: ReadarrNotification
    ) -> ReadarrNotification:
        """Add a notification."""
        return await self._async_request(
            NOTIFICATION,
            data=data,
            datatype=ReadarrNotification,
            method=HTTPMethod.POST,
        )

    async def async_test_notifications(
        self, data: ReadarrNotification | None = None
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

    async def async_parse(self, title: str) -> ReadarrParse:
        """Return the movie with matching file name."""
        params = {TITLE: title}
        return await self._async_request("parse", params=params, datatype=ReadarrParse)

    async def async_get_release(
        self, authorid: int | None = None, bookid: int | None = None
    ) -> list[ReadarrRelease]:
        """Search indexers for specified fields."""
        params = {}
        if authorid is not None:
            params[AUTHOR_ID] = authorid
        if bookid is not None:
            params[BOOK_ID] = bookid
        return await self._async_request(
            "release", params=params, datatype=ReadarrRelease
        )

    async def async_download_release(
        self, guid: str, indexerid: int
    ) -> list[ReadarrRelease]:
        """Add a previously searched release to the download client.

        If the release is
        still in the search cache (30 minute cache). If the release is not found
        in the cache it will return a 404.

        guid: Recently searched result guid
        """
        return await self._async_request(
            "release",
            data={"guid": guid, "indexerId": indexerid},
            datatype=ReadarrRelease,
            method=HTTPMethod.POST,
        )

    async def async_push_release(self, data: ReadarrRelease) -> ReadarrRelease:
        """Push release."""
        return await self._async_request(
            "release/push",
            data=data,
            datatype=ReadarrRelease,
            method=HTTPMethod.POST,
        )

    async def async_get_rename(
        self, authorid: int = 0, bookid: int = 0
    ) -> list[ReadarrRename]:
        """Get files matching specified id that are not properly renamed yet."""
        return await self._async_request(
            "rename",
            params={AUTHOR_ID: authorid, BOOK_ID: bookid},
            datatype=ReadarrRename,
        )

    async def async_get_manual_import(  # pylint: disable=too-many-arguments
        self,
        downloadid: str,
        authorid: int = 0,
        folder: str | None = None,
        filterexistingfiles: bool = True,
        replaceexistingfiles: bool = True,
    ) -> list[ReadarrManualImport]:
        """Get manual import."""
        params = {
            AUTHOR_ID: authorid,
            "downloadId": downloadid,
            "filterExistingFiles": str(filterexistingfiles),
            "folder": folder if folder is not None else "",
            "replaceExistingFiles": str(replaceexistingfiles),
        }
        return await self._async_request(
            "manualimport", params=params, datatype=ReadarrManualImport
        )

    async def async_edit_manual_import(
        self, data: ReadarrManualImport
    ) -> list[ReadarrManualImport]:
        """Get manual import."""
        return await self._async_request(
            "manualimport",
            data=data,
            datatype=ReadarrManualImport,
            method=HTTPMethod.PUT,
        )

    async def async_get_retag(
        self, authorid: int = 0, bookid: int = 0
    ) -> list[ReadarrRetag]:
        """Get retag."""
        return await self._async_request(
            "retag",
            params={AUTHOR_ID: authorid, BOOK_ID: bookid},
            datatype=ReadarrRetag,
        )

    async def async_search(self, term: str) -> list[ReadarrSearch]:
        """Search for books."""
        return await self._async_request(
            "search",
            params={TERM: term},
            datatype=ReadarrSearch,
        )

    async def async_get_series(self, authorid: int) -> list[ReadarrSeries]:
        """Get series."""
        return await self._async_request(
            "series",
            params={AUTHOR_ID: authorid},
            datatype=ReadarrSeries,
        )

    async def async_get_tags_details(
        self, tagid: int | None = None
    ) -> ReadarrTagDetails | list[ReadarrTagDetails]:
        """Get information about tag details.

        id: Get tag details matching id. Leave blank for all.
        """
        return await self._async_request(
            f"tag/detail{'' if tagid is None else f'/{tagid}'}",
            datatype=ReadarrTagDetails,
        )

    async def async_get_root_folders(
        self, folderid: int | None = None
    ) -> ReadarrRootFolder | list[ReadarrRootFolder]:
        """Get information about root folders."""
        return await self._async_request(
            f"rootfolder{'' if folderid is None else f'/{folderid}'}",
            datatype=ReadarrRootFolder,
        )

    async def async_edit_root_folder(
        self, data: ReadarrRootFolder
    ) -> ReadarrRootFolder:
        """Edit information about root folders."""
        return await self._async_request(
            "rootfolder",
            data=data,
            datatype=ReadarrRootFolder,
            method=HTTPMethod.PUT,
        )
