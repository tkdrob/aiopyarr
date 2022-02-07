"""Readarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

import attr

from ..const import AUTHOR_ID, PATH, TITLE
from .base import BaseModel
from .readarr_common import (
    _ReadarrAddOptions,
    _ReadarrAudioTags,
    _ReadarrAuthorAddOptions,
    _ReadarrAuthorBase,
    _ReadarrAuthorStatistics,
    _ReadarrBlocklistFilter,
    _ReadarrBlocklistRecord,
    _ReadarrBookCommon,
    _ReadarrBookFileMediaInfo,
    _ReadarrCategory,
    _ReadarrEditionsValue,
    _ReadarrImage,
    _ReadarrMetadataProfileValue,
    _ReadarrParsedBookInfo,
    _ReadarrRating,
    _ReadarrSearchAuthor,
    _ReadarrSeriesLinks2,
)
from .request_common import (
    _Common2,
    _Common3,
    _Common4,
    _Common6,
    _Common8,
    _Editor,
    _Fields,
    _HistoryData,
    _ImportListCommon,
    _Link,
    _ManualImport,
    _Notification,
    _Quality,
    _QualityCommon,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _RetagChange,
    _StatusMessage,
    _TagDetails,
)


class ReadarrBookTypes(str, Enum):
    """Readarr book types."""

    ASIN = "asin"
    GOODREADS = "goodreads"
    ISBN = "isbn"


class ReadarrCommands(str, Enum):
    """Readarr commands."""

    APP_UPDATE_CHECK = "ApplicationUpdateCheck"
    AUTHOR_SEARCH = "AuthorSearch"
    BOOK_SEARCH = "BookSearch"
    REFRESH_AUTHOR = "RefreshAuthor"
    REFRESH_BOOK = "RefreshBook"
    RENAME_AUTHOR = "RenameAuthor"
    RESCAN_FOLDERS = "RescanFolders"


class ReadarrEventType(Enum):
    """Readarr event types."""

    BOOK_IMPORTED = 3
    DELETED = 5
    DOWNLOAD_FAILED = 4
    DOWNLOAD_IMPORTED = 8
    GRABBED = 1
    IGNORED = 7
    IMPORT_FAILED = 7
    RENAMED = 6
    RETAGGED = 9


class ReadarrImportListType(str, Enum):
    """Readarr import list types."""

    PROGRAM = "program"
    GOODREADS = "goodreads"
    OTHER = "other"


class ReadarrSortKeys(str, Enum):
    """Readarr sort keys."""

    AUTHOR_ID = AUTHOR_ID
    BOOK_ID = "Books.Id"
    DATE = "books.releaseDate"
    DOWNLOAD_CLIENT = "downloadClient"
    ID = "id"
    INDEXER = "indexer"
    MESSAGE = "message"
    PATH = PATH
    PROGRESS = "progress"
    PROTOCOL = "protocol"
    QUALITY = "quality"
    RATINGS = "ratings"
    SIZE = "size"
    SOURCE_TITLE = "sourcetitle"
    STATUS = "status"
    TIMELEFT = "timeleft"
    TITLE = TITLE


@dataclass(init=False)
class ReadarrAuthor(_ReadarrAuthorBase):
    """Readarr author attributes."""


@dataclass(init=False)
class ReadarrBook(_ReadarrBookCommon):
    """Readarr book attributes."""

    author: ReadarrAuthor = attr.ib(type=ReadarrAuthor)
    authorId: int = attr.ib(type=int)
    authorTitle: str = attr.ib(type=str)
    disambiguation: str = attr.ib(type=str)
    editions: list[_ReadarrEditionsValue] | None = None
    grabbed: bool = attr.ib(type=bool)
    images: list[_ReadarrImage] | None = None
    overview: str = attr.ib(type=str)
    pageCount: int = attr.ib(type=int)
    remoteCover: str = attr.ib(type=str)
    seriesTitle: str = attr.ib(type=str)
    statistics: _ReadarrAuthorStatistics = attr.ib(type=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author) or {}
        self.editions = [_ReadarrEditionsValue(x) for x in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class ReadarrAuthorLookup(ReadarrAuthor):
    """Readarr author attributes."""

    monitorNewItems: str = attr.ib(type=str)


@dataclass(init=False)
class ReadarrBlocklist(_RecordCommon):
    """Readarr blocklist attributes."""

    filters: list[_ReadarrBlocklistFilter] | None = None
    records: list[_ReadarrBlocklistRecord] | None = None

    def __post_init__(self):
        """Post init."""
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]
        self.records = [
            _ReadarrBlocklistRecord(record) for record in self.records or []
        ]


@dataclass(init=False)
class ReadarrAuthorEditor(_Editor):
    """Readarr author editor attributes."""

    authorIds: list[int] = attr.ib(type='list[int]')
    metadataProfileId: int = attr.ib(type=int)


@dataclass(init=False)
class ReadarrBookFile(_QualityCommon):
    """Readarr book file attributes."""

    audioTags: _ReadarrAudioTags = attr.ib(type=_ReadarrAudioTags)
    authorId: int = attr.ib(type=int)
    bookId: int = attr.ib(type=int)
    dateAdded: datetime = attr.ib(type=datetime)
    id: int = attr.ib(type=int)
    mediaInfo: _ReadarrBookFileMediaInfo = attr.ib(type=_ReadarrBookFileMediaInfo)
    path: str = attr.ib(type=str)
    qualityWeight: int = attr.ib(type=int)
    size: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags) or {}
        self.mediaInfo = _ReadarrBookFileMediaInfo(self.mediaInfo) or {}


@dataclass(init=False)
class ReadarrBookFileEditor(BaseModel):
    """Readarr book file attributes."""

    bookFileIds: list[int] = attr.ib(type='list[int]')
    quality: _Quality = attr.ib(type=_Quality)

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookLookup(_Common6):
    """Readarr book lookup attributes."""

    added: datetime = attr.ib(type=datetime)
    anyEditionOk: bool = attr.ib(type=bool)
    author: ReadarrAuthor = attr.ib(type=ReadarrAuthor)
    authorId: int = attr.ib(type=int)
    authorTitle: str = attr.ib(type=str)
    disambiguation: str = attr.ib(type=str)
    editions: list[_ReadarrEditionsValue] | None = None
    foreignBookId: str = attr.ib(type=str)
    genres: list[str] = attr.ib(type='list[str]')
    grabbed: bool = attr.ib(type=bool)
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    pageCount: int = attr.ib(type=int)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    releaseDate: datetime = attr.ib(type=datetime)
    remoteCover: str = attr.ib(type=str)
    seriesTitle: str = attr.ib(type=str)
    title: str = attr.ib(type=str)
    titleSlug: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author) or {}
        self.editions = [_ReadarrEditionsValue(editn) for editn in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class ReadarrBookshelfAuthorBook(ReadarrBookLookup):
    """Readarr bookshelf author Book attributes."""

    addOptions: _ReadarrAddOptions = attr.ib(type=_ReadarrAddOptions)
    id: int = attr.ib(type=int)
    statistics: _ReadarrAuthorStatistics = attr.ib(type=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAddOptions(self.addOptions) or {}
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class ReadarrCalendar(ReadarrBookshelfAuthorBook):
    """Readarr calendar attributes."""


@dataclass(init=False)
class ReadarrBookshelfAuthor(BaseModel):
    """Readarr bookshelf author attributes."""

    books: list[ReadarrBookshelfAuthorBook] | None = None
    id: int = attr.ib(type=int)
    monitored: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.books = [ReadarrBookshelfAuthorBook(book) for book in self.books or []]


@dataclass(init=False)
class ReadarrBookshelf(BaseModel):
    """Readarr bookshelf attributes."""

    authors: list[ReadarrBookshelfAuthor] | None = None
    monitoringOptions: _ReadarrAuthorAddOptions = attr.ib(type=_ReadarrAuthorAddOptions)

    def __post_init__(self):
        """Post init."""
        self.authors = [ReadarrBookshelfAuthor(author) for author in self.authors or []]
        self.monitoringOptions = _ReadarrAuthorAddOptions(self.monitoringOptions) or {}


@dataclass(init=False)
class ReadarrWantedMissing(_RecordCommon):
    """Readarr wanted missing attributes."""

    records: list[ReadarrBook] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrBook(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrWantedCutoff(ReadarrWantedMissing):
    """Readarr wanted cutoff attributes."""

    filters: list[_ReadarrBlocklistFilter] | None = None

    def __post_init__(self):
        """Post init."""
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]


@dataclass(init=False)
class ReadarrMetadataProfile(_ReadarrMetadataProfileValue):
    """Readarr metadata profile attributes."""


@dataclass(init=False)
class ReadarrDevelopmentConfig(BaseModel):
    """Readarr development config attributes."""

    consoleLogLevel: str = attr.ib(type=str)
    filterSentryEvents: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    logRotate: int = attr.ib(type=int)
    logSql: bool = attr.ib(type=bool)
    metadataSource: str = attr.ib(type=str)


@dataclass(init=False)
class ReadarrBookHistory(_Common2, _QualityCommon):
    """Readarr history record attributes."""

    authorId: int = attr.ib(type=int)
    bookId: int = attr.ib(type=int)
    data: _HistoryData = attr.ib(type=_HistoryData)
    date: datetime = attr.ib(type=datetime)
    id: int = attr.ib(type=int)
    sourceTitle: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _HistoryData(self.data) or {}


@dataclass(init=False)
class ReadarrHistory(_RecordCommon):
    """Readarr history attributes."""

    records: list[ReadarrBookHistory] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrBookHistory(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrImportList(_ImportListCommon, _Common3):
    """Readarr importlist attributes."""

    enableAutomaticAdd: bool = attr.ib(type=bool)
    fields: list[_Fields] | None = None
    implementation: str = attr.ib(type=str)
    implementationName: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    listType: str = attr.ib(type=str)
    metadataProfileId: int = attr.ib(type=int)
    monitorNewItems: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    shouldMonitor: str = attr.ib(type=str)
    shouldMonitorExisting: bool = attr.ib(type=bool)
    shouldSearch: bool = attr.ib(type=bool)
    tags: list[int] = attr.ib(type='list[int]')

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrMetadataProvider(BaseModel):
    """Readarr metadata provider attributes."""

    embedMetadata: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    scrubAudioTags: bool = attr.ib(type=bool)
    updateCovers: bool = attr.ib(type=bool)
    writeAudioTags: str = attr.ib(type=str)
    writeBookTags: str = attr.ib(type=str)


@dataclass(init=False)
class ReadarrNamingConfig(BaseModel):
    """Readarr naming config attributes."""

    authorFolderFormat: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    includeAuthorName: bool = attr.ib(type=bool)
    includeBookTitle: bool = attr.ib(type=bool)
    includeQuality: bool = attr.ib(type=bool)
    renameBooks: bool = attr.ib(type=bool)
    replaceIllegalCharacters: bool = attr.ib(type=bool)
    replaceSpaces: bool = attr.ib(type=bool)
    standardBookFormat: str = attr.ib(type=str)


@dataclass(init=False)
class ReadarrNotification(_Common3, _Notification):
    """Readarr notification attributes."""

    fields: list[_Fields] | None = None
    onBookRetag: bool = attr.ib(type=bool)
    onDownloadFailure: bool = attr.ib(type=bool)
    onImportFailure: bool = attr.ib(type=bool)
    onReleaseImport: bool = attr.ib(type=bool)
    supportsOnBookRetag: bool = attr.ib(type=bool)
    supportsOnDownloadFailure: bool = attr.ib(type=bool)
    supportsOnImportFailure: bool = attr.ib(type=bool)
    supportsOnReleaseImport: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrParse(BaseModel):
    """Readarr parse attributes."""

    author: ReadarrAuthor = attr.ib(type=ReadarrAuthor)
    books: list[ReadarrBook] | None = None
    id: int = attr.ib(type=int)
    parsedBookInfo: _ReadarrParsedBookInfo = attr.ib(type=_ReadarrParsedBookInfo)
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.author = ReadarrAuthor(self.author) or {}
        self.books = [ReadarrBook(book) for book in self.books or []]
        self.parsedBookInfo = _ReadarrParsedBookInfo(self.parsedBookInfo) or {}


@dataclass(init=False)
class ReadarrQueueDetail(_Common4, _Common8):
    """Readarr queue detail attributes."""

    author: ReadarrAuthor = attr.ib(type=ReadarrAuthor)
    authorId: int = attr.ib(type=int)
    book: ReadarrBook = attr.ib(type=ReadarrBook)
    bookId: int = attr.ib(type=int)
    downloadForced: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.authorId) or {}
        self.book = ReadarrBook(self.book) or {}
        self.quality = _Quality(self.quality) or {}
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class ReadarrQueue(_RecordCommon):
    """Readarr queue attributes."""

    records: list[ReadarrQueueDetail] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrQueueDetail(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrRelease(_ReleaseCommon):
    """Readarr release attributes."""

    authorName: str = attr.ib(type=str)
    bookTitle: str = attr.ib(type=str)
    discography: bool = attr.ib(type=bool)
    preferredWordScore: int = attr.ib(type=int)
    quality: _Quality = attr.ib(type=_Quality)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrRename(_Rename):
    """Readarr rename attributes."""

    authorId: int = attr.ib(type=int)
    bookFileId: int = attr.ib(type=int)
    bookId: int = attr.ib(type=int)


@dataclass(init=False)
class ReadarrRetag(ReadarrRename):
    """Readarr retag attributes."""

    changes: list[_RetagChange] | None = None
    path: str = attr.ib(type=str)
    trackNumbers: list[int] = attr.ib(type='list[int]')

    def __post_init__(self):
        """Post init."""
        self.changes = [_RetagChange(change) for change in self.changes or []]


@dataclass(init=False)
class ReadarrSearch(BaseModel):
    """Readarr search attributes."""

    author: _ReadarrSearchAuthor = attr.ib(type=_ReadarrSearchAuthor)
    foreignId: str = attr.ib(type=str)
    id: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrSearchAuthor(self.author) or {}


@dataclass(init=False)
class ReadarrSeries(BaseModel):
    """Readarr series attributes."""

    description: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    links: list[_ReadarrSeriesLinks2] | None = None
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.links = [_ReadarrSeriesLinks2(link) for link in self.links or []]


@dataclass(init=False)
class ReadarrTagDetails(_TagDetails):
    """Readarr tag details attributes."""

    authorIds: list[int] = attr.ib(type='list[int]')


@dataclass(init=False)
class ReadarrManualImport(_ManualImport):
    """Readarr manual import attributes."""

    additionalFile: bool = attr.ib(type=bool)
    audioTags: _ReadarrAudioTags = attr.ib(type=_ReadarrAudioTags)
    author: ReadarrAuthor = attr.ib(type=ReadarrAuthor)
    book: ReadarrBook = attr.ib(type=ReadarrBook)
    disableReleaseSwitching: bool = attr.ib(type=bool)
    foreignEditionId: int = attr.ib(type=int)
    replaceExistingFiles: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags) or {}
        self.author = ReadarrAuthor(self.author) or {}
        self.book = ReadarrBook(self.book) or {}


@dataclass(init=False)
class ReadarrImportListOptions(BaseModel):
    """Readarr import list options attributes."""

    options: list[_ReadarrCategory] | None = None

    def __post_init__(self):
        """Post init."""
        self.options = [_ReadarrCategory(option) for option in self.options or []]
