"""Readarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel
from .request import _RecordCommon

from .request_common import (  # isort:skip
    _Common3,
    _Common4,
    _Notification,
    _Quality,
    _ReleaseCommon,
    _Rename,
    _TagDetails,
)

from .readarr_common import (  # isort:skip
    _ReadarrAddOptions,
    _ReadarrAudioTags,
    _ReadarrAuthorAddOptions,
    _ReadarrAuthorBase,
    _ReadarrAuthorStatistics,
    _ReadarrBlocklistFilter,
    _ReadarrBlocklistRecord,
    _ReadarrBookCommon,
    _ReadarrBookFileMediaInfo,
    _ReadarrEditionsValue,
    _ReadarrFields,
    _ReadarrHistoryRecord,
    _ReadarrImage,
    _ReadarrLink,
    _ReadarrMetadataProfileValue,
    _ReadarrParsedBookInfo,
    _ReadarrRating,
    _ReadarrRetagChange,
    _ReadarrSearchAuthor,
    _ReadarrSeriesLinks2,
    _ReadarrStatusMessages,
)


@dataclass(init=False)
class ReadarrBook(_ReadarrBookCommon):
    """Book attributes."""

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
        self.editions = [_ReadarrEditionsValue(editn) for editn in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class ReadarrAuthor(_ReadarrAuthorBase):
    """Author attributes."""


@dataclass(init=False)
class ReadarrAuthorLookup(ReadarrAuthor):
    """Author attributes."""

    monitorNewItems: str | None = None


@dataclass(init=False)
class ReadarrBlocklist(_RecordCommon):
    """Blocklist attributes."""

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
class ReadarrAuthorEditor(BaseModel):
    """Author editor attributes."""

    applyTags: str | None = None
    authorIds: list[int] | None = None
    deleteFiles: bool | None = None
    metadataProfileId: int | None = None
    monitored: bool | None = None
    moveFiles: bool | None = None
    qualityProfileId: int | None = None
    rootFolderPath: str | None = None
    tags: list[int | None] | None = None


@dataclass(init=False)
class ReadarrBookFile(BaseModel):
    """Book file attributes."""

    audioTags: _ReadarrAudioTags | None = None
    authorId: int | None = None
    bookId: int | None = None
    dateAdded: str | None = None
    id: int | None = None
    mediaInfo: _ReadarrBookFileMediaInfo | None = None
    path: str | None = None
    quality: _Quality | None = None
    qualityCutoffNotMet: bool | None = None
    qualityWeight: int | None = None
    size: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags) or {}
        self.mediaInfo = _ReadarrBookFileMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookFileEditor(BaseModel):
    """Book file attributes."""

    bookFileIds: list[int] | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookLookup(BaseModel):
    """Book lookup attributes."""

    added: str | None = None
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
    links: list[_ReadarrLink] | None = None
    monitored: bool | None = None
    overview: str | None = None
    pageCount: int | None = None
    ratings: _ReadarrRating | None = None
    releaseDate: str | None = None
    remoteCover: str | None = None
    seriesTitle: str | None = None
    title: str | None = None
    titleSlug: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.author) or {}
        self.editions = [_ReadarrEditionsValue(editn) for editn in self.editions or []]
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_ReadarrLink(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class ReadarrBookshelfAuthorBook(ReadarrBookLookup):
    """Bookshelf author Book attributes."""

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
    """Calendar attributes."""


@dataclass(init=False)
class ReadarrBookshelfAuthor(BaseModel):
    """Bookshelf author attributes."""

    books: list[ReadarrBookshelfAuthorBook] | None = None
    id: int | None = None
    monitored: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.books = [ReadarrBookshelfAuthorBook(book) for book in self.books or []]


@dataclass(init=False)
class ReadarrBookshelf(BaseModel):
    """Bookshelf attributes."""

    authors: list[ReadarrBookshelfAuthor] | None = None
    monitoringOptions: _ReadarrAuthorAddOptions | None = None

    def __post_init__(self):
        """Post init."""
        self.authors = [ReadarrBookshelfAuthor(author) for author in self.authors or []]
        self.monitoringOptions = _ReadarrAuthorAddOptions(self.monitoringOptions) or {}


@dataclass(init=False)
class ReadarrWantedMissing(_RecordCommon):
    """Wanted missing attributes."""

    records: list[ReadarrBook] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [ReadarrBook(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrWantedCutoff(ReadarrWantedMissing):
    """Wanted cutoff attributes."""

    filters: list[_ReadarrBlocklistFilter] | None = None

    def __post_init__(self):
        """Post init."""
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]


@dataclass(init=False)
class ReadarrMetadataProfile(_ReadarrMetadataProfileValue):
    """Metadata profile attributes."""


@dataclass(init=False)
class ReadarrDelayProfile(BaseModel):
    """Delay profile attributes."""

    enableTorrent: bool | None = None
    enableUsenet: bool | None = None
    id: int | None = None
    order: int | None = None
    preferredProtocol: str | None = None
    tags: list[int | None] | None = None
    torrentDelay: int | None = None
    usenetDelay: int | None = None


@dataclass(init=False)
class ReadarrDevelopmentConfig(BaseModel):
    """Development config attributes."""

    consoleLogLevel: str | None = None
    filterSentryEvents: bool | None = None
    id: int | None = None
    logRotate: int | None = None
    logSql: bool | None = None
    metadataSource: str | None = None


@dataclass(init=False)
class ReadarrHistory(_RecordCommon):
    """History attributes."""

    records: list[_ReadarrHistoryRecord] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [_ReadarrHistoryRecord(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrImportlist(_Common3):
    """Readarr importlist attributes."""

    configContract: str | None = None
    enableAutomaticAdd: bool | None = None
    fields: list[_ReadarrFields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    listOrder: int | None = None
    listType: str | None = None
    metadataProfileId: int | None = None
    monitorNewItems: str | None = None
    qualityProfileId: int | None = None
    rootFolderPath: str | None = None
    shouldMonitor: str | None = None
    shouldMonitorExisting: bool | None = None
    shouldSearch: bool | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_ReadarrFields(field) for field in self.fields or []]


@dataclass(init=False)
class ReadarrMetadataProviderConfig(BaseModel):
    """Metadata provider config attributes."""

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

    fields: list[_ReadarrFields] | None = None
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
        self.fields = [_ReadarrFields(field) for field in self.fields or []]


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
class ReadarrQueueDetail(_Common4):
    """Readarr queue detail attributes."""

    author: ReadarrAuthor | None = None
    authorId: int | None = None
    book: ReadarrBook | None = None
    bookId: int | None = None
    downloadForced: bool | None = None
    id: int | None = None
    protocol: str | None = None
    quality: _Quality | None = None
    size: int | None = None
    sizeleft: int | None = None
    status: str | None = None
    statusMessages: list[_ReadarrStatusMessages] | None = None
    timeleft: str | None = None
    title: str | None = None
    trackedDownloadState: str | None = None
    trackedDownloadStatus: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = ReadarrAuthor(self.authorId) or {}
        self.book = ReadarrBook(self.book) or {}
        self.quality = _Quality(self.quality) or {}
        self.statusMessages = [
            _ReadarrStatusMessages(book) for book in self.statusMessages or []
        ]


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
class ReadarrRetag(BaseModel):
    """Readarr retag attributes."""

    authorId: int | None = None
    bookFileId: int | None = None
    bookId: int | None = None
    changes: list[_ReadarrRetagChange] | None = None
    path: str | None = None
    trackNumbers: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        self.changes = [_ReadarrRetagChange(change) for change in self.changes or []]


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
