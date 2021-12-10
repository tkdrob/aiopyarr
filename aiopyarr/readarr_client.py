"""Readarr API."""
from __future__ import annotations
from typing import TYPE_CHECKING
import json
from .const import HTTPMethod, HTTPResponse
from .models.readarr import ReadarrAuthor, ReadarrAuthorEditor, ReadarrAuthorLookup, ReadarrBlocklist, ReadarrBook, ReadarrBookFile, ReadarrBookFileEditor, ReadarrBookLookup, ReadarrBookshelf
from .models.common import Logs
from .request_client import RequestClient

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
        api_ver: str = "v1"
    ) -> None:
        """Initialize Readarr API."""
        super().__init__(
            host_configuration,
            session,
            hostname,
            ipaddress,
            url,
            api_token,
            port,
            ssl,
            verify_ssl,
            base_api_path,
            request_timeout,
            raw_response,
            redact,
            api_ver,
        )

    async def async_author(self, authorid: int | None = None) -> ReadarrAuthor | list[ReadarrAuthor]:
        """Get info about specified author by id or using a term for lookup"""
        command = f"author{f'/{authorid}' if authorid is not None else ''}"
        return await self._async_request(command, datatype=ReadarrAuthor)

    async def async_author_lookup(self, term: str) -> list[ReadarrAuthorLookup]:
        """Searches for new authors using a term"""
        return await self._async_request("author/lookup", params={"term": term}, datatype=ReadarrAuthorLookup)

    async def async_author_add(self, data: ReadarrAuthor) -> ReadarrAuthor:
        """Add author to database"""
        return await self._async_request("author", data=data, datatype=ReadarrAuthor, method=HTTPMethod.POST)

    async def async_author_edit(self, data: ReadarrAuthorEditor) -> HTTPResponse:
        """Add author database info"""
        return await self._async_request("author/editor", data=data, method=HTTPMethod.PUT)
    # add author editor delete
    async def async_delete_author(self, authorid: int, delete_files: bool = False, import_list_exclusion: bool = True) -> HTTPResponse:
        """Delete the author with the given id
        Args:
            authorid: Database id for author
            delete_files: If true author folder and files will be deleted
            import_list_exclusion: Add an exclusion so author doesn't get re-added
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(f"author/{authorid}", params=params, method=HTTPMethod.DELETE)

    async def _async_construct_book_json(
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
    ):
        """Constructs the JSON required to add a new book to Readarr
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
        Raises:
            ValueError: error raised if book_id_type is incorrect
        Returns:
            JSON: Array
        """
        book_id_types = ["goodreads", "isbn", "asin"]
        if book_id_type not in book_id_types:
            raise ValueError(f"Invalid book id type. Expected one of: {book_id_types}")

        book = await self.async_lookup_book(book_id_type + ":" + str(db_id))[0]

        book["author"]["metadataProfileId"] = metadata_profile_id
        book["author"]["qualityProfileId"] = quality_profile_id
        book["author"]["rootFolderPath"] = root_dir
        book["author"]["addOptions"] = {
            "monitor": author_monitor,
            "searchForMissingBooks": author_search_for_missing_books,
        }
        book["monitored"] = monitored
        book["author"]["manualAdd"] = True
        book["addOptions"] = {"searchForNewBook": search_for_new_book}

        return book

    async def async_get_command(self, commandid: int | None = None):
        """Queries the status of a previously started command, or all currently started commands.
        Args:
            commandid: Database id of the command
        Returns:
            JSON: Array
        """
        path = f"command/{commandid}" if commandid else "command"
        return await self._async_request(path)

    # POST /command
    async def async_post_command(self, name: str, **kwargs):
        """Performs any of the predetermined Sonarr command routines
        Note:
            For command names and additional kwargs:
                TODO
        Args:
            name: command name that should be execured
            **kwargs: additional parameters for specific commands
        Returns:
            JSON: Array
        """
        path = "command"
        data = {
            "name": name,
            **kwargs,
        }
        return await self._async_request("command", data=data, method=HTTPMethod.POST)

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

    ## WANTED (MISSING)

    # GET /wanted/missing
    async def async_get_missing(self, sort_key: str = "releaseDate", page: int = 1, page_size: int = 10, sort_dir:str = "asc"):
        """Gets missing episode (episodes without files)
        Args:
            sort_key: Books.Id or releaseDate
            page: Page number to return
            page_size: Number of items per page
            sort_dir: Direction to sort the items
        Returns:
            JSON: Array
        """
        params = {
            "sortKey": sort_key,
            "page": page,
            "pageSize": page_size,
            "sortDir": sort_dir,
        }
        return await self._async_request("wanted/missing", params=params)

    ## QUEUE

    # GET /queue
    async def async_get_queue(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_dir: str = "ascending",
        sort_key: str = "timeleft",
        unknown_authors: bool = False,
        include_author: bool = False,
        include_book: bool = False,
    ):
        """Get current download information
        Args:
            page: page number
            page_size: number of results per page_size
            sort_dir: direction to sort
            sort_key: field to sort by
            unknown_authors: Include items with an unknown author
            include_author: Include the author
            include_book: Include the book
        Returns:
            JSON: Array
        """

        params = {
            "sortKey": sort_key,
            "page": page,
            "pageSize": page_size,
            "sortDirection": sort_dir,
            "includeUnknownAuthorItems": unknown_authors,
            "includeAuthor": include_author,
            "includeBook": include_book,
        }
        return await self._async_request("queue", params=params)

    # GET /metadataprofile
    async def async_get_metadata_profiles(self):
        """Gets all metadata profiles
        Returns:
            JSON: Array
        """
        return await self._async_request("metadataprofile")

    # GET /delayprofile
    async def async_get_delay_profiles(self):
        """Gets all delay profiles
        Returns:
            JSON: Array
        """
        return await self._async_request("delayprofile")

    # GET /releaseprofile
    async def async_get_release_profiles(self):
        """Gets all release profiles
        Returns:
            JSON: Array
        """
        return await self._async_request("releaseprofile")

    ## BOOKS
    # GET /book and /book/{id}
    async def async_get_book(self, bookid: int | None = None) -> ReadarrBook | list[ReadarrBook]:
        """Returns all books in your collection or the book with the matching
        book ID if one is found."""
        path = f"book/{bookid}" if bookid is not None else "book"
        return await self._async_request(path, datatype=ReadarrBook)

    async def async_add_book(self, data: ReadarrBook) -> ReadarrBook:
        """Add a new book and its associated author (if not already added)"""
        return await self._async_request("book", data=json.dumps(data), method=HTTPMethod.POST)

    async def async_update_book(self, data: ReadarrBook) -> ReadarrBook:
        """Edit an existing book (if not already added)"""
        return await self._async_request(f"book/{data.id}", data=json.dumps(data), method=HTTPMethod.PUT)

    async def async_delete_book(self, bookid: int, delete_files: bool = False, import_list_exclusion: bool = True) -> HTTPResponse:
        """Delete the book with the given id
        Args:
            bookid: Database id for book
            delete_files: If true book folder and files will be deleted
            import_list_exclusion: Add an exclusion so book doesn't get re-added
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(f"book/{bookid}", params=params, method=HTTPMethod.DELETE)

    async def async_get_book_file(self, authorid: int | None = None, fileid: int | list[int] | None = None, bookid: list[int] | None = None, unmapped: bool = False) -> ReadarrBookFile:
        """Return all books in your collection or the book with the matching
        book ID if one is found."""
        params = {"unmapped": str(unmapped)}
        if not isinstance(fileid, int):
            if authorid is not None:
                params["authorId"] = authorid
            if fileid is not None:
                params["bookFileIds"] = fileid
            if bookid is not None:
                params["bookId"] = bookid
        if isinstance(fileid, list):
            path = "bookfile"
        else:
            path = f"bookfile/{fileid}" if fileid is not None else "bookfile"
        return await self._async_request(path, params=params, datatype=ReadarrBookFile)

    async def async_edit_book_file(self, data: ReadarrBookFile) -> ReadarrBookFile:
        """Edit book file attributes."""
        return await self._async_request(f"bookfile/{data.id}", data=data, datatype=ReadarrBookFile, method=HTTPMethod.PUT)

    async def async_edit_book_file_bulk(self, data: ReadarrBookFileEditor) -> HTTPResponse:
        """Edit book file attributes in bulk."""
        return await self._async_request("bookfile/editor", data=data, datatype=ReadarrBookFileEditor, method=HTTPMethod.PUT)

    async def async_delete_book_file(self, fileid: int | None = None, data: ReadarrBookFileEditor | None = None) -> HTTPResponse:
        """Delete book files. Use fileid for one file or data for mass deletion"""
        command = f"bookfile/{f'{fileid}' if fileid is not None else 'bulk'}"
        return await self._async_request(command, data=data, datatype=ReadarrBookFile, method=HTTPMethod.DELETE)

    async def async_lookup_book(self, term: str, booktype: str = "isbn") -> list[ReadarrBookLookup]:
        """Searches for new books using a term, goodreads ID, isbn or asin"""
        book_id_types = ["goodreads", "isbn", "asin"]
        if booktype not in book_id_types:
            raise ValueError(f"Invalid book id type. Expected one of: {book_id_types}")
        return await self._async_request("book/lookup", params={"term": f"{booktype}:{term}"}, datatype=ReadarrBookLookup)

    async def async_add_bookself(self, data: ReadarrBookshelf) -> HTTPResponse:
        """Add a bookshelf to the database"""
        return await self._async_request("bookshelf", data=data, datatype=ReadarrBookshelf, method=HTTPMethod.POST)
