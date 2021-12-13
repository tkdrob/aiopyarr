"""Readarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel
from .common import _RecordCommon

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
    _ReadarrCommandBody,
    _ReadarrDuration,
    _ReadarrEditionsValue,
    _ReadarrImage,
    _ReadarrLink,
    _ReadarrMetadataProfileValue,
    _ReadarrQuality,
    _ReadarrRating,
)


@dataclass(init=False)
class ReadarrBook(_ReadarrBookCommon):
    """Book attributes."""

    authorTitle: str | None = None
    seriesTitle: str | None = None
    disambiguation: str | None = None
    overview: str | None = None
    authorId: int | None = None
    pageCount: int | None = None
    author: ReadarrAuthor | None = None
    images: list[_ReadarrImage] | None = None
    statistics: _ReadarrAuthorStatistics | None = None
    remoteCover: str | None = None
    editions: list[_ReadarrEditionsValue] | None = None
    grabbed: bool | None = None

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
        super().__post_init__()
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]
        self.records = [
            _ReadarrBlocklistRecord(record) for record in self.records or []
        ]


@dataclass(init=False)
class ReadarrAuthorEditor(BaseModel):
    """Author editor attributes."""

    authorIds: list[int]
    monitored: bool
    qualityProfileId: int
    metadataProfileId: int
    rootFolderPath: str
    tags: list[int]
    applyTags: str
    moveFiles: bool
    deleteFiles: bool


@dataclass(init=False)
class ReadarrBookFile(BaseModel):
    """Book file attributes."""

    id: int | None = None
    authorId: int | None = None
    bookId: int | None = None
    path: str | None = None
    size: int | None = None
    dateAdded: str | None = None
    quality: _ReadarrQuality | None = None
    qualityWeight: int | None = None
    mediaInfo: _ReadarrBookFileMediaInfo | None = None
    qualityCutoffNotMet: bool | None = None
    audioTags: _ReadarrAudioTags | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _ReadarrAudioTags(self.audioTags) or {}
        self.mediaInfo = _ReadarrBookFileMediaInfo(self.mediaInfo) or {}
        self.quality = _ReadarrQuality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookFileEditor(BaseModel):
    """Book file attributes."""

    bookFileIds: list[int] | None = None
    quality: _ReadarrQuality | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _ReadarrQuality(self.quality) or {}


@dataclass(init=False)
class ReadarrBookLookup(BaseModel):
    """Book lookup attributes."""

    title: str | None = None
    authorTitle: str | None = None
    seriesTitle: str | None = None
    disambiguation: str | None = None
    overview: str | None = None
    authorId: int | None = None
    foreignBookId: str | None = None
    titleSlug: str | None = None
    monitored: bool | None = None
    anyEditionOk: bool | None = None
    ratings: _ReadarrRating | None = None
    releaseDate: str | None = None
    pageCount: int | None = None
    genres: list[str] | None = None
    author: ReadarrAuthor | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_ReadarrLink] | None = None
    added: str | None = None
    remoteCover: str | None = None
    editions: list[_ReadarrEditionsValue] | None = None
    grabbed: bool | None = None

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

    id: int | None = None
    statistics: _ReadarrAuthorStatistics | None = None
    addOptions: _ReadarrAddOptions | None = None

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

    id: int | None = None
    monitored: bool | None = None
    books: list[ReadarrBookshelfAuthorBook] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.books = [ReadarrBookshelfAuthorBook(book) for book in self.books or []]


@dataclass(init=False)
class ReadarrBookshelf(BaseModel):
    """Bookshelf attributes."""

    authors: list[ReadarrBookshelfAuthor] | None = None
    monitoringOptions: _ReadarrAuthorAddOptions | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.authors = [ReadarrBookshelfAuthor(author) for author in self.authors or []]
        self.monitoringOptions = _ReadarrAuthorAddOptions(self.monitoringOptions) or {}


@dataclass(init=False)
class ReadarrCommand(BaseModel):
    """Command attributes."""

    id: int | None = None
    name: str | None = None
    commandName: str | None = None
    message: str | None = None
    body: _ReadarrCommandBody | None = None
    priority: str | None = None
    status: str | None = None
    queued: str | None = None
    started: str | None = None
    ended: str | None = None
    duration: _ReadarrDuration | None = None
    exception: str | None = None
    trigger: str | None = None
    clientUserAgent: str | None = None
    stateChangeTime: str | None = None
    sendUpdatesToClient: bool | None = None
    updateScheduledTask: bool | None = None
    lastExecutionTime: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.body = _ReadarrCommandBody(self.body) or {}
        self.duration = _ReadarrDuration(self.duration) or {}


@dataclass(init=False)
class ReadarrWantedMissing(_RecordCommon):
    """Wanted missing attributes."""

    records: list[ReadarrBook] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [ReadarrBook(record) for record in self.records or []]


@dataclass(init=False)
class ReadarrWantedCutoff(ReadarrWantedMissing):
    """Wanted cutoff attributes."""

    filters: list[_ReadarrBlocklistFilter] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.filters = [
            _ReadarrBlocklistFilter(filter) for filter in self.filters or []
        ]


@dataclass(init=False)
class ReadarrMetadataProfile(_ReadarrMetadataProfileValue):
    """Metadata profile attributes."""
