"""Readarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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
class ReadarrBook(_ReadarrBookCommon):
    """Readarr book attributes."""

    author: ReadarrAuthor | None = None
    authorId: int | None = None
    authorTitle: str | None = None
    disambiguation: str | None = None
    editions: list[_ReadarrEditionsValue] | None = None
    grabbed: bool | None = None
    images: list[_ReadarrImage] | None = None
    overview: str | None = None
    pageCount: int | None = None
    remoteCover: str | None = None
    seriesTitle: str | None = None
    statistics: _ReadarrAuthorStatistics | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author) or {}
        self.editions = [_ReadarrEditionsValue(x) for x in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class ReadarrAuthor(_ReadarrAuthorBase):
    """Readarr author attributes."""


@dataclass(init=False)
class ReadarrAuthorLookup(ReadarrAuthor):
    """Readarr author attributes."""

    monitorNewItems: str | None = None


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

    authorIds: list[int] | None = None
    metadataProfileId: int | None = None


@dataclass(init=False)
class ReadarrBookFile(_QualityCommon):
    """Readarr book file attributes."""

    audioTags: _ReadarrAudioTags | None = None
    authorId: int | None = None
    bookId: int | None = None
    dateAdded: datetime | None = None
    id: int | None = None
    mediaInfo: _ReadarrBookFileMediaInfo | None = None
    path: str | None = None
    qualityWeight: int | None = None
    size: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags) or {}
        self.mediaInfo = _ReadarrBookFileMediaInfo(self.mediaInfo) or {}


@dataclass(init=False)
class ReadarrBookFileEditor(BaseModel):
    """Readarr book file attributes."""

    bookFileIds: list[int] | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookLookup(_Common6):
    """Readarr book lookup attributes."""

    added: datetime | None = None
    anyEditionOk: bool | None = None
    author: ReadarrAuthor | None = None
    authorId: int | None = None
    authorTitle: str | None = None
    disambiguation: str | None = None
    editions: list[_ReadarrEditionsValue] | None = None
    foreignBookId: str | None = None
    genres: list[str] | None = None
    grabbed: bool | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    pageCount: int | None = None
    ratings: _ReadarrRating | None = None
    releaseDate: datetime | None = None
    remoteCover: str | None = None
    seriesTitle: str | None = None
    title: str | None = None
    titleSlug: int | None = None

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

    addOptions: _ReadarrAddOptions | None = None
    id: int | None = None
    statistics: _ReadarrAuthorStatistics | None = None

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
    id: int | None = None
    monitored: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.books = [ReadarrBookshelfAuthorBook(book) for book in self.books or []]


@dataclass(init=False)
class ReadarrBookshelf(BaseModel):
    """Readarr bookshelf attributes."""

    authors: list[ReadarrBookshelfAuthor] | None = None
    monitoringOptions: _ReadarrAuthorAddOptions | None = None

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

    consoleLogLevel: str | None = None
    filterSentryEvents: bool | None = None
    id: int | None = None
    logRotate: int | None = None
    logSql: bool | None = None
    metadataSource: str | None = None


@dataclass(init=False)
class ReadarrBookHistory(_Common2, _QualityCommon):
    """Readarr history record attributes."""

    authorId: int | None = None
    bookId: int | None = None
    data: _HistoryData | None = None
    date: datetime | None = None
    id: int | None = None
    sourceTitle: str | None = None

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

    enableAutomaticAdd: bool | None = None
    fields: list[_Fields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    listType: str | None = None
    metadataProfileId: int | None = None
    monitorNewItems: str | None = None
    qualityProfileId: int | None = None
    shouldMonitor: str | None = None
    shouldMonitorExisting: bool | None = None
    shouldSearch: bool | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrMetadataProvider(BaseModel):
    """Readarr metadata provider attributes."""

    embedMetadata: bool | None = None
    id: int | None = None
    scrubAudioTags: bool | None = None
    updateCovers: bool | None = None
    writeAudioTags: str | None = None
    writeBookTags: str | None = None


@dataclass(init=False)
class ReadarrNamingConfig(BaseModel):
    """Readarr naming config attributes."""

    authorFolderFormat: str | None = None
    id: int | None = None
    includeAuthorName: bool | None = None
    includeBookTitle: bool | None = None
    includeQuality: bool | None = None
    renameBooks: bool | None = None
    replaceIllegalCharacters: bool | None = None
    replaceSpaces: bool | None = None
    standardBookFormat: str | None = None


@dataclass(init=False)
class ReadarrNotification(_Common3, _Notification):
    """Readarr notification attributes."""

    fields: list[_Fields] | None = None
    onBookRetag: bool | None = None
    onDownloadFailure: bool | None = None
    onImportFailure: bool | None = None
    onReleaseImport: bool | None = None
    supportsOnBookRetag: bool | None = None
    supportsOnDownloadFailure: bool | None = None
    supportsOnImportFailure: bool | None = None
    supportsOnReleaseImport: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrParse(BaseModel):
    """Readarr parse attributes."""

    author: ReadarrAuthor | None = None
    books: list[ReadarrBook] | None = None
    id: int | None = None
    parsedBookInfo: _ReadarrParsedBookInfo | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.author = ReadarrAuthor(self.author) or {}
        self.books = [ReadarrBook(book) for book in self.books or []]
        self.parsedBookInfo = _ReadarrParsedBookInfo(self.parsedBookInfo) or {}


@dataclass(init=False)
class ReadarrQueueDetail(_Common4, _Common8):
    """Readarr queue detail attributes."""

    author: ReadarrAuthor | None = None
    authorId: int | None = None
    book: ReadarrBook | None = None
    bookId: int | None = None
    downloadForced: bool | None = None

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

    authorName: str | None = None
    bookTitle: str | None = None
    discography: bool | None = None
    preferredWordScore: int | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrRename(_Rename):
    """Readarr rename attributes."""

    authorId: int | None = None
    bookFileId: int | None = None
    bookId: int | None = None


@dataclass(init=False)
class ReadarrRetag(ReadarrRename):
    """Readarr retag attributes."""

    changes: list[_RetagChange] | None = None
    path: str | None = None
    trackNumbers: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        self.changes = [_RetagChange(change) for change in self.changes or []]


@dataclass(init=False)
class ReadarrSearch(BaseModel):
    """Readarr search attributes."""

    author: _ReadarrSearchAuthor | None = None
    foreignId: str | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrSearchAuthor(self.author) or {}


@dataclass(init=False)
class ReadarrSeries(BaseModel):
    """Readarr series attributes."""

    description: str | None = None
    id: int | None = None
    links: list[_ReadarrSeriesLinks2] | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.links = [_ReadarrSeriesLinks2(link) for link in self.links or []]


@dataclass(init=False)
class ReadarrTagDetails(_TagDetails):
    """Readarr tag details attributes."""

    authorIds: list[int] | None = None


@dataclass(init=False)
class ReadarrManualImport(_ManualImport):
    """Readarr manual import attributes."""

    additionalFile: bool | None = None
    audioTags: _ReadarrAudioTags | None = None
    author: ReadarrAuthor | None = None
    book: ReadarrBook | None = None
    disableReleaseSwitching: bool | None = None
    foreignEditionId: int | None = None
    replaceExistingFiles: bool | None = None

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
