"""Readarr API."""
from __future__ import annotations
from typing import TYPE_CHECKING
from aiopyarr.const import HTTPMethod
from aiopyarr.models.readarr import ReadarrAuthor

from aiopyarr.request_client import RequestClient

if TYPE_CHECKING:
    from aiohttp.client import ClientSession
    from .models.host_configuration import PyArrHostConfiguration


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
        port: int = 8787,
        ssl: bool | None = None,
        verify_ssl: bool | None = None,
        base_api_path: str | None = None,
        request_timeout: float = 10,
        raw_response: bool = False,
        redact: bool = True,
        api_ver: str = "v1"
    ) -> None:
        """Initialize Radarr API."""
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
    async def async_get_book(self, bookid: int | None = None):
        """Returns all books in your collection or the book with the matching
        book ID if one is found.
        Args:
            bookid: Database id for book.
        Returns:
            JSON: Array
        """
        path = f"book/{bookid}" if bookid else "book"
        return await self._async_request(path)

    # POST /book

    async def async_add_book(
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
        """Adds a new book and  its associated author (if not already added)
        Args:
            db_id: goodreads, isbn, asin ID for the book
            book_id_type: goodreads / isbn / asin
            root_dir: Directory for book to be stored
            quality_profile_id: quality profile id
            metadata_profile_id: metadata profile id
            monitored: should the book be monitored
            search_for_new_book: search for the book to download now
            author_monitor: monitor the author for new books
            author_search_for_missing_books: search for missing books from this author
        Raises:
            ValueError: error raised if book_id_type is incorrect
        Returns:
            JSON: Array
        """
        book_id_types = ["goodreads", "isbn", "asin"]
        if book_id_type not in book_id_types:
            raise ValueError(f"Invalid book id type. Expected one of: {book_id_types}")

        book_json = self._construct_book_json(
            db_id,
            book_id_type,
            root_dir,
            quality_profile_id,
            metadata_profile_id,
            monitored,
            search_for_new_book,
            author_monitor,
            author_search_for_missing_books,
        )
        return await self._async_request("book", data=book_json, method=HTTPMethod.POST)

    # PUT /book
    async def async_update_book(self):
        pass

        # path = "book"
        # return await self._async_request("book", data=data)


    # DELETE /book/{id}
    async def async_delete_book(self, bookid: int, delete_files: bool = False, import_list_exclusion: bool = True):
        """Delete the book with the given id
        Args:
            bookid: Database id for book
            delete_files: If true book folder and files will be deleted
            import_list_exclusion: Add an exclusion so book doesn't get re-added
        Returns:
            JSON: {}
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(f"book/{bookid}", params=params, method=HTTPMethod.DELETE)

    async def async_lookup_book(self, term: str):
        """Searches for new books using a term, goodreads ID, isbn or asin.
        Args:
            term (str): search term
            goodreads:656
            isbn:067003469X
            asin:B00JCDK5ME
        Returns:
            JSON: Array
        """
        params = {"term": term}
        return await self._async_request("book/lookup", params=params)

    async def async_lookup_author(self, term: str) -> list[ReadarrAuthor]:
        """Searches for new authors using a term"""
        params = {"term": term}
        return await self._async_request("author/lookup", params=params)

    async def async_del_author(self, authorid: int, delete_files: bool = False, import_list_exclusion: bool = True):
        """Delete the author with the given id
        Args:
            authorid: Database id for author
            delete_files: If true author folder and files will be deleted
            import_list_exclusion: Add an exclusion so author doesn't get re-added
        Returns:
            JSON: Array
        """
        params = {
            "deleteFiles": delete_files,
            "addImportListExclusion": import_list_exclusion,
        }
        return await self._async_request(f"author/{authorid}", params=params, method=HTTPMethod.DELETE)

    ## LOG

    # GET /log/file
    async def async_get_log_file(self):
        """Get log file
        Returns:
            JSON: Array
        """
        return await self._async_request("log/file")