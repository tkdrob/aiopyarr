"""Readarr Models."""

# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
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
    _RootFolderExended,
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

    author: type[ReadarrAuthor] = field(default=ReadarrAuthor)
    authorId: int
    authorTitle: str
    disambiguation: str
    editions: list[_ReadarrEditionsValue] | None = None
    grabbed: bool
    images: list[_ReadarrImage] | None = None
    overview: str
    pageCount: int
    remoteCover: str
    seriesTitle: str
    statistics: type[_ReadarrAuthorStatistics] = field(default=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author)
        self.editions = [_ReadarrEditionsValue(x) for x in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.statistics = _ReadarrAuthorStatistics(self.statistics)


@dataclass(init=False)
class ReadarrAuthorLookup(ReadarrAuthor):
    """Readarr author attributes."""

    monitorNewItems: str


@dataclass(init=False)
class ReadarrBlocklist(_RecordCommon):
    """Readarr blocklist attributes."""

    filters: list[_ReadarrBlocklistFilter] | None = None
    records: list[_ReadarrBlocklistRecord] = field(
        default_factory=list[_ReadarrBlocklistRecord]
    )

    def __post_init__(self):
        """Post init."""
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]
        self.records = [_ReadarrBlocklistRecord(record) for record in self.records]


@dataclass(init=False)
class ReadarrAuthorEditor(_Editor):
    """Readarr author editor attributes."""

    authorIds: list[int]
    metadataProfileId: int


@dataclass(init=False)
class ReadarrBookFile(_QualityCommon):
    """Readarr book file attributes."""

    audioTags: type[_ReadarrAudioTags] = field(default=_ReadarrAudioTags)
    authorId: int
    bookId: int
    dateAdded: datetime
    id: int
    mediaInfo: type[_ReadarrBookFileMediaInfo] = field(
        default=_ReadarrBookFileMediaInfo
    )
    path: str
    qualityWeight: int
    size: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags)
        self.mediaInfo = _ReadarrBookFileMediaInfo(self.mediaInfo)


@dataclass(init=False)
class ReadarrBookFileEditor(BaseModel):
    """Readarr book file attributes."""

    bookFileIds: list[int]
    quality: type[_Quality] = field(default=_Quality)

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class ReadarrBookLookup(_Common6):
    """Readarr book lookup attributes."""

    added: datetime
    anyEditionOk: bool
    author: type[ReadarrAuthor] = field(default=ReadarrAuthor)
    authorId: int
    authorTitle: str
    disambiguation: str
    editions: list[_ReadarrEditionsValue] | None = None
    foreignBookId: str
    genres: list[str]
    grabbed: bool
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    pageCount: int
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    releaseDate: datetime
    remoteCover: str
    seriesTitle: str
    title: str
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author)
        self.editions = [_ReadarrEditionsValue(editn) for editn in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings)


@dataclass(init=False)
class ReadarrBookshelfAuthorBook(ReadarrBookLookup):
    """Readarr bookshelf author Book attributes."""

    addOptions: type[_ReadarrAddOptions] = field(default=_ReadarrAddOptions)
    id: int
    statistics: type[_ReadarrAuthorStatistics] = field(default=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAddOptions(self.addOptions)
        self.statistics = _ReadarrAuthorStatistics(self.statistics)


@dataclass(init=False)
class ReadarrCalendar(ReadarrBookshelfAuthorBook):
    """Readarr calendar attributes."""


@dataclass(init=False)
class ReadarrBookshelfAuthor(BaseModel):
    """Readarr bookshelf author attributes."""

    books: list[ReadarrBookshelfAuthorBook] | None = None
    id: int
    monitored: bool

    def __post_init__(self):
        """Post init."""
        self.books = [ReadarrBookshelfAuthorBook(book) for book in self.books or []]


@dataclass(init=False)
class ReadarrBookshelf(BaseModel):
    """Readarr bookshelf attributes."""

    authors: list[ReadarrBookshelfAuthor] | None = None
    monitoringOptions: type[_ReadarrAuthorAddOptions] = field(
        default=_ReadarrAuthorAddOptions
    )

    def __post_init__(self):
        """Post init."""
        self.authors = [ReadarrBookshelfAuthor(author) for author in self.authors or []]
        self.monitoringOptions = _ReadarrAuthorAddOptions(self.monitoringOptions)


@dataclass(init=False)
class ReadarrWantedMissing(_RecordCommon):
    """Readarr wanted missing attributes."""

    records: list[ReadarrBook] = field(default_factory=list[ReadarrBook])

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrBook(record) for record in self.records]


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

    consoleLogLevel: str
    filterSentryEvents: bool
    id: int
    logRotate: int
    logSql: bool
    metadataSource: str


@dataclass(init=False)
class ReadarrBookHistory(_Common2, _QualityCommon):
    """Readarr history record attributes."""

    authorId: int
    bookId: int
    data: type[_HistoryData] = field(default=_HistoryData)
    date: datetime
    id: int
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _HistoryData(self.data)


@dataclass(init=False)
class ReadarrHistory(_RecordCommon):
    """Readarr history attributes."""

    records: list[ReadarrBookHistory] = field(default_factory=list[ReadarrBookHistory])

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrBookHistory(record) for record in self.records]


@dataclass(init=False)
class ReadarrImportList(_ImportListCommon, _Common3):
    """Readarr importlist attributes."""

    enableAutomaticAdd: bool
    fields: list[_Fields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    listType: str
    metadataProfileId: int
    monitorNewItems: str
    qualityProfileId: int
    shouldMonitor: str
    shouldMonitorExisting: bool
    shouldSearch: bool
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrMetadataProvider(BaseModel):
    """Readarr metadata provider attributes."""

    embedMetadata: bool
    id: int
    scrubAudioTags: bool
    updateCovers: bool
    writeAudioTags: str
    writeBookTags: str


@dataclass(init=False)
class ReadarrNamingConfig(BaseModel):
    """Readarr naming config attributes."""

    authorFolderFormat: str
    id: int
    includeAuthorName: bool
    includeBookTitle: bool
    includeQuality: bool
    renameBooks: bool
    replaceIllegalCharacters: bool
    replaceSpaces: bool
    standardBookFormat: str


@dataclass(init=False)
class ReadarrNotification(_Common3, _Notification):
    """Readarr notification attributes."""

    fields: list[_Fields] | None = None
    onBookRetag: bool
    onDownloadFailure: bool
    onImportFailure: bool
    onReleaseImport: bool
    supportsOnBookRetag: bool
    supportsOnDownloadFailure: bool
    supportsOnImportFailure: bool
    supportsOnReleaseImport: bool

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrParse(BaseModel):
    """Readarr parse attributes."""

    author: type[ReadarrAuthor] = field(default=ReadarrAuthor)
    books: list[ReadarrBook] | None = None
    id: int
    parsedBookInfo: type[_ReadarrParsedBookInfo] = field(default=_ReadarrParsedBookInfo)
    title: str

    def __post_init__(self):
        """Post init."""
        self.author = ReadarrAuthor(self.author)
        self.books = [ReadarrBook(book) for book in self.books or []]
        self.parsedBookInfo = _ReadarrParsedBookInfo(self.parsedBookInfo)


@dataclass(init=False)
class ReadarrQueueDetail(_Common4, _Common8):
    """Readarr queue detail attributes."""

    author: type[ReadarrAuthor] = field(default=ReadarrAuthor)
    authorId: int
    book: type[ReadarrBook] = field(default=ReadarrBook)
    bookId: int
    downloadForced: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.authorId)
        self.book = ReadarrBook(self.book)
        self.quality = _Quality(self.quality)
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class ReadarrQueue(_RecordCommon):
    """Readarr queue attributes."""

    records: list[ReadarrQueueDetail] = field(default_factory=list[ReadarrQueueDetail])

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrQueueDetail(record) for record in self.records]


@dataclass(init=False)
class ReadarrRelease(_ReleaseCommon):
    """Readarr release attributes."""

    authorName: str
    bookTitle: str
    discography: bool
    preferredWordScore: int
    quality: type[_Quality] = field(default=_Quality)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class ReadarrRename(_Rename):
    """Readarr rename attributes."""

    authorId: int
    bookFileId: int
    bookId: int


@dataclass(init=False)
class ReadarrRetag(ReadarrRename):
    """Readarr retag attributes."""

    changes: list[_RetagChange] | None = None
    path: str
    trackNumbers: list[int]

    def __post_init__(self):
        """Post init."""
        self.changes = [_RetagChange(change) for change in self.changes or []]


@dataclass(init=False)
class ReadarrSearch(BaseModel):
    """Readarr search attributes."""

    author: type[_ReadarrSearchAuthor] = field(default=_ReadarrSearchAuthor)
    foreignId: str
    id: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrSearchAuthor(self.author)


@dataclass(init=False)
class ReadarrSeries(BaseModel):
    """Readarr series attributes."""

    description: str
    id: int
    links: list[_ReadarrSeriesLinks2] | None = None
    title: str

    def __post_init__(self):
        """Post init."""
        self.links = [_ReadarrSeriesLinks2(link) for link in self.links or []]


@dataclass(init=False)
class ReadarrTagDetails(_TagDetails):
    """Readarr tag details attributes."""

    authorIds: list[int]


@dataclass(init=False)
class ReadarrManualImport(_ManualImport):
    """Readarr manual import attributes."""

    additionalFile: bool
    audioTags: type[_ReadarrAudioTags] = field(default=_ReadarrAudioTags)
    author: type[ReadarrAuthor] = field(default=ReadarrAuthor)
    book: type[ReadarrBook] = field(default=ReadarrBook)
    disableReleaseSwitching: bool
    foreignEditionId: int
    replaceExistingFiles: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags)
        self.author = ReadarrAuthor(self.author)
        self.book = ReadarrBook(self.book)


@dataclass(init=False)
class ReadarrImportListOptions(BaseModel):
    """Readarr import list options attributes."""

    options: list[_ReadarrCategory] | None = None

    def __post_init__(self):
        """Post init."""
        self.options = [_ReadarrCategory(option) for option in self.options or []]


@dataclass(init=False)
class ReadarrRootFolder(_RootFolderExended):
    """Readarr root folder attributes."""

    isCalibreLibrary: bool
    outputProfile: str
    port: int
    useSsl: bool
