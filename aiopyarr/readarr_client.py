"""Readarr API."""
from __future__ import annotations

import json
from datetime import datetime
from typing import TYPE_CHECKING

from .const import HTTPMethod, HTTPResponse
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
    ReadarrBookshelf,
    ReadarrCalendar,
    ReadarrDelayProfile,
    ReadarrDevelopmentConfig,
    ReadarrHistory,
    ReadarrImportlist,
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
        redact: bool = True,
        api_ver: str = "v1",
    ) -> None:
        """Initialize Readarr API."""
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

    async def async_author(
        self, authorid: int | None = None
    ) -> ReadarrAuthor | list[ReadarrAuthor]:
        """Get info about specified author by id or using a term for lookup."""
        command = f"author{f'/{authorid}' if authorid is not None else ''}"
        return await self._async_request(command, datatype=ReadarrAuthor)

    async def async_author_lookup(self, term: str) -> list[ReadarrAuthorLookup]:
        """Search for new authors using a term."""
        return await self._async_request(
            "author/lookup", params={"term": term}, datatype=ReadarrAuthorLookup
        )

    async def async_author_add(self, data: ReadarrAuthor) -> ReadarrAuthor:
        """Add author to database."""
        return await self._async_request(
            "author", data=data, datatype=ReadarrAuthor, method=HTTPMethod.POST
        )

    async def async_author_edit(self, data: ReadarrAuthorEditor) -> ReadarrAuthorEditor:
        """Add author database info."""
        return await self._async_request(
            "author/editor",
            data=data,
            datatype=ReadarrAuthorEditor,
            method=HTTPMethod.PUT,
        )

    # add author editor delete
    async def async_delete_author(
        self,
        authorid: int,
        delete_files: bool = False,
        import_list_exclusion: bool = True,
    ) -> HTTPResponse:
        """Delete the author with the given id.

        Args:
            authorid: Database id for author
            delete_files: If true author folder and files will be deleted
            import_list_exclusion: Add an exclusion so author doesn't get re-added
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(
            f"author/{authorid}", params=params, method=HTTPMethod.DELETE
        )

    async def _async_construct_book_json(  # pylint: disable=too-many-arguments
        self,
        db_id: int,
        book_id_type: str,
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
        book_id_types = ["goodreads", "isbn", "asin"]
        if book_id_type not in book_id_types:
            raise ValueError(f"Invalid book id type. Expected one of: {book_id_types}")

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

    async def async_command_check_updates(self) -> HTTPResponse:
        """Trigger checking application updates."""
        return await self._async_request(
            "command",
            data={"name": "ApplicationUpdateCheck"},
            method=HTTPMethod.POST,
        )

    async def async_command_backup(self) -> HTTPResponse:
        """Trigger application backup."""
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

    async def async_command_refresh_author(self) -> HTTPResponse:
        """Trigger author refresh."""
        return await self._async_request(
            "command",
            data={"name": "RefreshAuthor"},
            method=HTTPMethod.POST,
        )

    async def async_command_rescan_folders(self) -> HTTPResponse:
        """Trigger folder rescan."""
        return await self._async_request(
            "command",
            data={"name": "RescanFolders"},
            method=HTTPMethod.POST,
        )

    async def async_get_blocklist(
        self,
        page: int = 1,
        page_size: int = 20,
        sort_direction: str = "descending",
        sort_key: str = "date",
    ) -> ReadarrBlocklist:
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
            sortkey: id, title, ratings, or others".
            page: Page number to return.
            page_size: Number of items per page.
        """
        params = {
            "sortKey": sortkey,
            "page": page,
            "pageSize": page_size,
        }
        return await self._async_request(
            f"wanted/missing{f'/{recordid}' if recordid is not None else ''}",
            params=params,
            datatype=ReadarrBook if recordid is not None else ReadarrWantedMissing,
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
            sortkey: id, title, ratings, or others".
            page: Page number to return.
            page_size: Number of items per page.
            sort_asc: Sort items in ascending order.
        """
        params = {
            "sortKey": sortkey,
            "page": page,
            "pageSize": page_size,
        }
        return await self._async_request(
            f"wanted/cutoff{f'/{recordid}' if recordid is not None else ''}",
            params=params,
            datatype=ReadarrBook if recordid is not None else ReadarrWantedCutoff,
        )

    async def async_get_queue(  # pylint: disable=too-many-arguments
        self,
        page: int = 1,
        page_size: int = 10,
        sort_dir: str = "ascending",
        sort_key: str = "timeleft",
        unknown_authors: bool = False,
        include_author: bool = False,
        include_book: bool = False,
    ) -> ReadarrQueue:
        """Get current download information.

        Args:
            page: page number
            page_size: number of results per page_size
            sort_dir: direction to sort
            sort_key: field to sort by
            unknown_authors: Include items with an unknown author
            include_author: Include the author
            include_book: Include the book
        """

        params = {
            "page": page,
            "pageSize": page_size,
            "sortDirection": sort_dir,
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
        path = f"book/{bookid}" if bookid is not None else "book"
        return await self._async_request(path, datatype=ReadarrBook)

    async def async_add_book(self, data: ReadarrBook) -> ReadarrBook:
        """Add a new book and its associated author (if not already added)."""
        return await self._async_request(
            "book", data=json.dumps(data), method=HTTPMethod.POST
        )

    async def async_edit_book(self, data: ReadarrBook) -> ReadarrBook:
        """Edit an existing book (if not already added)."""
        return await self._async_request(
            f"book/{data.id}", data=data, datatype=ReadarrBook, method=HTTPMethod.PUT
        )

    async def async_delete_book(
        self,
        bookid: int,
        delete_files: bool = False,
        import_list_exclusion: bool = True,
    ) -> HTTPResponse:
        """Delete the book with the given id.

        Args:
            bookid: Database id for book
            delete_files: If true book folder and files will be deleted
            import_list_exclusion: Add an exclusion so book doesn't get re-added
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(
            f"book/{bookid}", params=params, method=HTTPMethod.DELETE
        )

    async def async_get_book_file(
        self,
        authorid: int | None = None,
        fileid: int | list[int] | None = None,
        bookid: list[int] | None = None,
        unmapped: bool = False,
    ) -> ReadarrBookFile:
        """Return all books in your collection or book with matching book ID."""
        params = {"unmapped": str(unmapped)}
        if not isinstance(fileid, int):
            if authorid is not None:
                params["authorId"] = str(authorid)
            if fileid is not None:
                params["bookFileIds"] = str(fileid)
            if bookid is not None:
                params["bookId"] = str(bookid)
        if isinstance(fileid, list):
            path = "bookfile"
        else:
            path = f"bookfile/{fileid}" if fileid is not None else "bookfile"
        return await self._async_request(path, params=params, datatype=ReadarrBookFile)

    async def async_edit_book_file(self, data: ReadarrBookFile) -> ReadarrBookFile:
        """Edit book file attributes."""
        return await self._async_request(
            f"bookfile/{data.id}",
            data=data,
            datatype=ReadarrBookFile,
            method=HTTPMethod.PUT,
        )

    async def async_edit_book_file_bulk(
        self, data: ReadarrBookFileEditor
    ) -> HTTPResponse:
        """Epdate book file attributes in bulk."""
        return await self._async_request(
            "bookfile/editor",
            data=data,
            method=HTTPMethod.PUT,
        )

    async def async_delete_book_file(
        self, fileid: int | None = None, data: ReadarrBookFileEditor | None = None
    ) -> HTTPResponse:
        """Delete book files. Use fileid for one file or data for mass deletion."""
        command = f"bookfile/{f'{fileid}' if fileid is not None else 'bulk'}"
        return await self._async_request(command, data=data, method=HTTPMethod.DELETE)

    async def async_lookup_book(
        self, term: str, booktype: str = "isbn"
    ) -> list[ReadarrBookLookup]:
        """Search for new books using a term, goodreads ID, isbn or asin."""
        book_id_types = ["goodreads", "isbn", "asin"]
        if booktype not in book_id_types:
            raise ValueError(f"Invalid book id type. Expected one of: {book_id_types}")
        return await self._async_request(
            "book/lookup",
            params={"term": f"{booktype}:{term}"},
            datatype=ReadarrBookLookup,
        )

    async def async_add_bookself(self, data: ReadarrBookshelf) -> HTTPResponse:
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
            f"calendar{f'/{calendarid}' if calendarid is not None else ''}",
            params=params,
            datatype=ReadarrCalendar,
        )

    # /api/v1/calendar/readarr.ics not working

    async def async_get_delay_profiles(
        self, profileid: int | None = None
    ) -> list[ReadarrDelayProfile]:
        """Get all delay profiles."""
        return await self._async_request(
            f"delayprofile{f'/{profileid}' if profileid is not None else ''}",
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
            f"delayprofile/{data.id}",
            data=data,
            datatype=ReadarrDelayProfile,
            method=HTTPMethod.PUT,
        )

    async def async_delete_delay_profile(self, profileid: int) -> HTTPResponse:
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
            params={"afterId": afterid},
            datatype=ReadarrDelayProfile,
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
            f"config/development/{data.id}",
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
    ) -> ReadarrImportlist | list[ReadarrImportlist]:
        """Get import lists."""
        return await self._async_request(
            f"importlist{f'/{listid}' if listid is not None else ''}",
            datatype=ReadarrImportlist,
        )

    async def async_edit_import_list(
        self, data: ReadarrImportlist
    ) -> ReadarrImportlist:
        """Edit import list."""
        return await self._async_request(
            f"importlist{data.id}",
            data=data,
            datatype=ReadarrImportlist,
            method=HTTPMethod.PUT,
        )

    async def async_add_import_list(self, data: ReadarrImportlist) -> ReadarrImportlist:
        """Add import list."""
        return await self._async_request(
            "importlist", data=data, datatype=ReadarrImportlist, method=HTTPMethod.POST
        )

    async def async_get_metadata_profiles(
        self, profileid: int | None = None
    ) -> ReadarrMetadataProfile | list[ReadarrMetadataProfile]:
        """Get metadata profiles."""
        return await self._async_request(
            f"metadataprofile{f'/{profileid}' if profileid is not None else ''}",
            datatype=ReadarrMetadataProfile,
        )

    async def async_delete_metadata_profile(
        self, profileid: int | None = None
    ) -> HTTPResponse:
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
            f"metadataprofile/{data.id}",
            data=data,
            datatype=ReadarrMetadataProfile,
            method=HTTPMethod.PUT,
        )

    # metadataprofile/schema, not that useful

    async def async_get_metadata_provider_configs(
        self, providerid: int | None = None
    ) -> ReadarrMetadataProviderConfig | list[ReadarrMetadataProviderConfig]:
        """Get metadata provider configs."""
        return await self._async_request(
            f"metadataprovider{f'/{providerid}' if providerid is not None else ''}",
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
            f"notification{f'/{notifyid}' if notifyid is not None else ''}",
            datatype=ReadarrNotification,
        )

    async def async_edit_notification(
        self, data: ReadarrNotification
    ) -> ReadarrNotification:
        """Edit a notification."""
        return await self._async_request(
            f"notification/{data.id}",
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

    async def async_test_notification(self, data: ReadarrNotification) -> HTTPResponse:
        """Test a notification configuration."""
        return await self._async_request(
            "notification/test",
            data=data,
            method=HTTPMethod.POST,
        )

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
            f"tag/detail{f'/{tagid}' if tagid is not None else ''}",
            datatype=ReadarrTagDetails,
        )
