"""Readarr API."""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from aiopyarr.models.request import Command, RootFolder

from .const import HTTPMethod
from .decorator import api_command
from .request_client import RequestClient

from .models.readarr import (  # isort:skip
    ReadarrAuthor,
    ReadarrAuthorEditor,
    ReadarrAuthorLookup,
    ReadarrBlocklist,
    ReadarrBook,
    ReadarrBookFile,
    ReadarrBookFileEditor,
    ReadarrBookLookup,
    ReadarrBookTypes,
    ReadarrBookshelf,
    ReadarrCalendar,
    ReadarrCommands,
    ReadarrDelayProfile,
    ReadarrDevelopmentConfig,
    ReadarrHistory,
    ReadarrImportList,
    ReadarrMetadataProfile,
    ReadarrMetadataProviderConfig,
    ReadarrNamingConfig,
    ReadarrNotification,
    ReadarrParse,
    ReadarrQueue,
    ReadarrQueueDetail,
    ReadarrRelease,
    ReadarrRename,
    ReadarrRetag,
    ReadarrSearch,
    ReadarrSeries,
    ReadarrTagDetails,
    ReadarrWantedCutoff,
    ReadarrWantedMissing,
)

if TYPE_CHECKING:
    from aiohttp.client import ClientSession

    from .models.host_configuration import PyArrHostConfiguration


class ReadarrClient(RequestClient):  # pylint: disable=too-many-public-methods
    """API client for Readarr endpoints."""

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
        user_agent: str | None = None,
    ) -> None:
        """Initialize Readarr API."""
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

    async def async_get_author(
        self, authorid: int | None = None
    ) -> ReadarrAuthor | list[ReadarrAuthor]:
        """Get info about specified author by id, leave blank for all."""
        command = f"author{'' if authorid is None else f'/{authorid}'}"
        return await self._async_request(command, datatype=ReadarrAuthor)

    async def async_author_lookup(self, term: str) -> list[ReadarrAuthorLookup]:
        """Search for new authors using a term."""
        return await self._async_request(
            "author/lookup", params={"term": term}, datatype=ReadarrAuthorLookup
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
            datatype=ReadarrAuthor if isinstance(data, ReadarrAuthor) else None,
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

    async def _async_construct_book_json(  # pylint: disable=too-many-arguments
        self,
        db_id: int,
        book_id_type: ReadarrBookTypes,
        root_dir: str,
        quality_profile_id: int = 1,
        metadata_profile_id: int = 0,
        monitored: bool = True,
        search_for_new_book: bool = False,
        author_monitor: str = "all",
        author_search_for_missing_books: bool = False,
    ) -> ReadarrBookLookup | dict | None:
        """Construct the JSON required to add a new book to Readarr.

        Args:
            db_id: goodreads, isbn, asin ID
            book_id_type: goodreads / isbn / asin
            root_dir: root directory for books
            quality_profile_id: quality profile id
            metadata_profile_id: metadata profile id
            monitored: should the book be monitored
            search_for_new_book : shour a search for the new book happen
            author_monitor: monitor the author.
            author_search_for_missing_books: search for other missing books by the author
        """
        books = await self.async_lookup_book(book_id_type + ":" + str(db_id))
        if not isinstance(books, list) or books[0].author is None:
            return None

        books[0].author.metadataProfileId = metadata_profile_id
        books[0].author.qualityProfileId = quality_profile_id
        books[0].author.rootFolderPath = root_dir
        if books[0].author.addOptions:
            books[0].author.addOptions.monitor = author_monitor
            books[
                0
            ].author.addOptions.searchForMissingBooks = author_search_for_missing_books
        books[0].monitored = monitored

        books[0].author.__setattr__("manualAdd", True)
        books[0].__setattr__("addOptions", {"searchForNewBook": search_for_new_book})

        return books[0]

    async def async_readarr_command(self, command: ReadarrCommands) -> Command:
        """Send a command to Readarr."""
        return await self._async_request(
            "command",
            data={"name": command},
            datatype=Command,
            method=HTTPMethod.POST,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        ascending: bool = False,
        sort_key: str = "date",
    ) -> ReadarrBlocklist:
        """Return blocklisted releases.

        Args:
            page: Page to be returned.
            page_size: Number of results per page.
            ascending: Direction to sort items.
            sort_key: date, id, authorid, sourcetitle, quality,
            indexer, path, message, or ratings.
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
            datatype=ReadarrBlocklist,
        )

    async def async_get_wanted_missing(  # includeAuthor, sortDir not working
        self,
        recordid: int | None = None,
        sortkey: str = "title",
        page: int = 1,
        page_size: int = 10,
    ) -> ReadarrWantedMissing | ReadarrBook:
        """Get missing books.

        Args:
            sortkey: id, title, ratings, or quality".
            page: Page number to return.
            page_size: Number of items per page.
        """
        params = {
            "sortKey": sortkey,
            "page": page,
            "pageSize": page_size,
        }
        return await self._async_request(
            f"wanted/missing{'' if recordid is None else f'/{recordid}'}",
            params=params,
            datatype=ReadarrWantedMissing if recordid is None else ReadarrBook,
        )

    async def async_get_wanted_cutoff(  # includeAuthor, sortDir not working
        self,
        recordid: int | None = None,
        sortkey: str = "title",
        page: int = 1,
        page_size: int = 10,
    ) -> ReadarrWantedCutoff | ReadarrBook:
        """Get wanted books not meeting cutoff.

        Args:
            sortkey: id, title, ratings, or quality".
            page: Page number to return.
            page_size: Number of items per page.
        """
        params = {
            "sortKey": sortkey,
            "page": page,
            "pageSize": page_size,
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
        sort_key: str = "timeleft",
        unknown_authors: bool = False,
        include_author: bool = False,
        include_book: bool = False,
    ) -> ReadarrQueue:
        """Get current download information.

        Args:
            page: page number
            page_size: number of results per page_size
            sort_key: timeleft, title, id, or date
            unknown_authors: Include items with an unknown author
            include_author: Include the author
            include_book: Include the book
        """
        params = {
            "page": page,
            "pageSize": page_size,
            "sortKey": sort_key,
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
            params["authorId"] = authorid
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
        """Return all books in your collection or book with matching book ID."""
        params: dict[str, str | int | list[int]] = {"unmapped": str(unmapped)}
        if not isinstance(fileid, int):
            if authorid is not None:
                params["authorId"] = authorid
            if bookid is not None:
                params["bookId"] = bookid
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
            datatype=ReadarrBookFile if isinstance(data, ReadarrBookFile) else None,
            method=HTTPMethod.PUT,
        )

    async def async_delete_book_files(self, ids: int | list[int]) -> None:
        """Delete book files. Use fileid for one file or data for mass deletion."""
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
            params={"term": f"{booktype}:{term}"},
            datatype=ReadarrBookLookup,
        )

    async def async_add_bookshelf(
        self, data: ReadarrBookshelf
    ) -> ReadarrBookshelf:  # verify
        """Add a bookshelf to the database."""
        return await self._async_request("bookshelf", data=data, method=HTTPMethod.POST)

    async def async_get_calendar(  # pylint: disable=too-many-arguments
        self,
        start_date: datetime,
        end_date: datetime,
        calendarid: int | None = None,
        unmonitored: bool = False,
        includeauthor: bool = False,
    ) -> ReadarrCalendar | list[ReadarrCalendar]:
        """Get calendar items."""
        params = {
            "start": start_date.strftime("%Y-%m-%d"),
            "end": end_date.strftime("%Y-%m-%d"),
            "unmonitored": str(unmonitored),
            "includeAuthor": str(includeauthor),
        }
        return await self._async_request(
            f"calendar{'' if calendarid is None else f'/{calendarid}'}",
            params=params,
            datatype=ReadarrCalendar,
        )

    # /api/v1/calendar/readarr.ics not working

    async def async_get_delay_profiles(
        self, profileid: int | None = None
    ) -> ReadarrDelayProfile | list[ReadarrDelayProfile]:
        """Get all delay profiles."""
        return await self._async_request(
            f"delayprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=ReadarrDelayProfile,
        )

    async def async_add_delay_profile(
        self, data: ReadarrDelayProfile
    ) -> ReadarrDelayProfile:
        """Add delay profiles."""
        return await self._async_request(
            "delayprofile",
            data=data,
            datatype=ReadarrDelayProfile,
            method=HTTPMethod.POST,
        )

    async def async_edit_delay_profile(
        self, data: ReadarrDelayProfile
    ) -> ReadarrDelayProfile:
        """Edit delay profiles."""
        return await self._async_request(
            "delayprofile",
            data=data,
            datatype=ReadarrDelayProfile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_delay_profile(self, profileid: int) -> None:
        """Delete delay profiles."""
        return await self._async_request(
            f"delayprofile/{profileid}", method=HTTPMethod.DELETE
        )

    async def async_delay_profile_reorder(
        self, profileid: int, afterid: int | None = None
    ) -> list[ReadarrDelayProfile]:
        """Reorder delay profiles."""
        return await self._async_request(
            f"delayprofile/reorder/{profileid}",
            params=None if afterid is None else {"afterId": afterid},
            method=HTTPMethod.PUT,
        )

    @api_command("config/development", datatype=ReadarrDevelopmentConfig)
    async def async_get_development_config(self) -> ReadarrDevelopmentConfig:
        """Get development config."""

    # Documented, does not seem to work.
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

    async def async_get_history(
        self,
    ) -> ReadarrHistory:
        """Get history."""
        return await self._async_request("history", datatype=ReadarrHistory)

    # history/since / history/author

    # history/failed POST does not seem to work

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
            f"importlist/test{'all' if data is None else ''}",
            data=None if data is None else data,
            method=HTTPMethod.POST,
        )
        if data is None:
            for item in _res:
                if item["isValid"] is False:
                    return False
        return True

    async def async_get_metadata_profiles(
        self, profileid: int | None = None
    ) -> ReadarrMetadataProfile | list[ReadarrMetadataProfile]:
        """Get metadata profiles."""
        return await self._async_request(
            f"metadataprofile{'' if profileid is None else f'/{profileid}'}",
            datatype=ReadarrMetadataProfile,
        )

    async def async_delete_metadata_profile(self, profileid: int | None = None) -> None:
        """Delete a metadata profile."""
        return await self._async_request(
            f"metadataprofile/{profileid}",
            method=HTTPMethod.DELETE,
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

    # metadataprofile/schema, not that useful

    # metadataprovider not working, 404
    async def async_get_metadata_provider_configs(
        self, providerid: int | None = None
    ) -> ReadarrMetadataProviderConfig | list[ReadarrMetadataProviderConfig]:
        """Get metadata provider configs."""
        return await self._async_request(
            f"metadataprovider{'' if providerid is None else f'/{providerid}'}",
            datatype=ReadarrMetadataProviderConfig,
        )

    async def async_edit_metadata_provider_config(
        self,
        data: ReadarrMetadataProviderConfig,
    ) -> ReadarrMetadataProviderConfig:
        """Edit a metadata provider config."""
        return await self._async_request(
            f"metadataprovider/{data.id}",
            data=data,
            datatype=ReadarrMetadataProviderConfig,
            method=HTTPMethod.PUT,
        )

    @api_command("config/naming", datatype=ReadarrNamingConfig)
    async def async_get_naming_config(self) -> ReadarrNamingConfig:
        """Get information about naming configuration."""

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
            "notification",
            data=data,
            datatype=ReadarrNotification,
            method=HTTPMethod.PUT,
        )

    async def async_add_notification(
        self, data: ReadarrNotification
    ) -> ReadarrNotification:
        """Add a notification."""
        return await self._async_request(
            "notification",
            data=data,
            datatype=ReadarrNotification,
            method=HTTPMethod.POST,
        )

    async def async_test_notifications(
        self, data: ReadarrNotification | None = None
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

    async def async_parse(self, title: str) -> ReadarrParse:
        """Return the movie with matching file name."""
        params = {"title": title}
        return await self._async_request("parse", params=params, datatype=ReadarrParse)

    async def async_get_release(
        self, authorid: int | None = None, bookid: int | None = None
    ) -> list[ReadarrRelease]:
        """Search indexers for specified fields."""
        params = {}
        if authorid is not None:
            params["authorId"] = authorid
        if bookid is not None:
            params["bookId"] = bookid
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

    # Only works if an id is associated with the release
    async def async_get_pushed_release(self, releaseid: str) -> ReadarrRelease:
        """Get release previously pushed by below method."""
        return await self._async_request(
            "release/push",
            params={"id": releaseid},
            datatype=ReadarrRelease,
        )

    async def async_get_rename(
        self, authorid: int = 0, bookid: int = 0
    ) -> list[ReadarrRename]:
        """Get files matching specified id that are not properly renamed yet."""
        return await self._async_request(
            "rename",
            params={"authorId": authorid, "bookId": bookid},
            datatype=ReadarrRename,
        )

    async def async_get_retag(
        self, authorid: int = 0, bookid: int = 0
    ) -> list[ReadarrRetag]:
        """Get retag."""
        return await self._async_request(
            "retag",
            params={"authorId": authorid, "bookId": bookid},
            datatype=ReadarrRetag,
        )

    async def async_search(self, term: str) -> list[ReadarrSearch]:
        """Search for books."""
        return await self._async_request(
            "search",
            params={"term": term},
            datatype=ReadarrSearch,
        )

    async def async_get_series(self, authorid: int) -> list[ReadarrSeries]:
        """Get series."""
        return await self._async_request(
            "series",
            params={"authorId": authorid},
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

    async def async_edit_root_folder(self, data: RootFolder) -> RootFolder:
        """Edit information about root folders."""
        return await self._async_request(
            "rootfolder",
            data=data,
            datatype=RootFolder,
            method=HTTPMethod.PUT,
        )
