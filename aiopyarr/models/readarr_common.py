"""Readarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import attr

from .base import BaseModel
from .request_common import (
    _Common3,
    _Common5,
    _Common6,
    _Common7,
    _IsLoaded,
    _Link,
    _Quality,
    _Ratings,
    _SelectOption,
    _TitleInfo,
)


@dataclass(init=False)
class _ReadarrCommon(BaseModel):
    """Readarr Common attributes."""

    authorMetadataId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    links: list[_Link] | None = None
    titleSlug: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.links = [_Link(link) for link in self.links or []]


@dataclass(init=False)
class _ReadarrCommon2(BaseModel):
    """Readarr Common attributes."""

    foreignAuthorId: str = attr.ib(type=str)
    genres: list[str] = attr.ib(list[str])
    overview: str = attr.ib(type=str)
    sortName: str = attr.ib(type=str)
    sortNameLastFirst: str = attr.ib(type=str)
    status: str = attr.ib(type=str)


@dataclass(init=False)
class _ReadarrRating(_Ratings):
    """Readarr ratings attributes."""

    popularity: float = attr.ib(type=float)


@dataclass(init=False)
class _ReadarrAddOptions(BaseModel):
    """Readarr add options attributes."""

    addType: str = attr.ib(type=str)
    searchForNewBook: bool = attr.ib(type=bool)


@dataclass(init=False)
class _ReadarrImage(_Common5):
    """readarr metadata value attributes."""

    extension: str = attr.ib(type=str)


@dataclass(init=False)
class _ReadarrMetadataValue(_ReadarrCommon2, _Common3):
    """Readarr metadata value attributes."""

    aliases: list[str] = attr.ib(list[str])
    born: datetime = attr.ib(type=datetime)
    died: datetime = attr.ib(type=datetime)
    disambiguation: str = attr.ib(type=str)
    gender: str = attr.ib(type=str)
    hometown: str = attr.ib(type=str)
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    nameLastFirst: str = attr.ib(type=str)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    titleSlug: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrAuthorMetadata(_IsLoaded):
    """Readarr author Metadata attributes."""

    value: _ReadarrMetadataValue = attr.ib(type=_ReadarrMetadataValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrMetadataValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorAddOptions(BaseModel):
    """Readarr author add options attributes."""

    booksToMonitor: list[str] = attr.ib(list[str])
    monitor: str = attr.ib(type=str)
    monitored: bool = attr.ib(type=bool)
    searchForMissingBooks: bool = attr.ib(type=bool)


@dataclass(init=False)
class _ReadarrQualityItem(_Common3):
    """Readarr quality item attributes."""

    allowed: bool = attr.ib(type=bool)
    items: list = attr.ib(list)  # Currently unknown contents
    quality: _Common3 = attr.ib(type=_Common3)

    def __post_init__(self):
        """Post init."""
        self.quality = _Common3(self.quality) or {}


@dataclass(init=False)
class _ReadarrQualityProfileValue(_Common3):
    """Readarr quality profile value attributes."""

    cutoff: int = attr.ib(type=int)
    items: list[_ReadarrQualityItem] | None = None
    upgradeAllowed: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.items = [_ReadarrQualityItem(item) for item in self.items or []]


@dataclass(init=False)
class _ReadarrQualityProfile(_IsLoaded):
    """Readarr quality profile attributes."""

    value: _ReadarrQualityProfileValue = attr.ib(type=_ReadarrQualityProfileValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrQualityProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrMetadataProfileValue(_Common3):
    """Readarr metadata profile value attributes."""

    allowedLanguages: str = attr.ib(type=str)
    ignored: str = attr.ib(type=str)
    minPages: int = attr.ib(type=int)
    minPopularity: float = attr.ib(type=float)
    skipMissingDate: bool = attr.ib(type=bool)
    skipMissingIsbn: bool = attr.ib(type=bool)
    skipPartsAndSets: bool = attr.ib(type=bool)
    skipSeriesSecondary: bool = attr.ib(type=bool)


@dataclass(init=False)
class _ReadarrMetadataProfile(_IsLoaded):
    """Readarr metadata profile attributes."""

    value: _ReadarrMetadataProfileValue = attr.ib(type=_ReadarrMetadataProfileValue)

    def __post_init__(self):
        self.value = _ReadarrMetadataProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueBooks(_IsLoaded):
    """Readarr author value books attributes."""

    value: list = attr.ib(list)  # Currently unknown contents


@dataclass(init=False)
class _ReadarrAuthorValueSeriesValue(BaseModel):
    """Readarr author value series value attributes."""

    books: _ReadarrAuthorValueBooks = attr.ib(type=_ReadarrAuthorValueBooks)
    description: str = attr.ib(type=str)
    foreignAuthorId: str = attr.ib(type=str)
    foreignSeriesId: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    numbered: bool = attr.ib(type=bool)
    primaryWorkCount: int = attr.ib(type=int)
    title: str = attr.ib(type=str)
    workCount: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.books = _ReadarrAuthorValueBooks(self.books) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeriesLinks(_IsLoaded):
    """Readarr author value series links attributes."""

    value: _ReadarrAuthorValueSeriesValue = attr.ib(type=_ReadarrAuthorValueSeriesValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValueSeriesValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeries(_IsLoaded):
    """Readarr author value series attributes."""

    value: list[_ReadarrAuthorValueSeriesValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrAuthorValueSeriesValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrCommon3(BaseModel):
    """Readarr common attributes."""

    added: datetime = attr.ib(type=datetime)
    cleanName: str = attr.ib(type=str)
    metadataProfileId: int = attr.ib(type=int)
    monitored: bool = attr.ib(type=bool)
    path: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    tags: list[int] = attr.ib(type=list[int])


@dataclass(init=False)
class _ReadarrAuthorValue(_Common3, _ReadarrCommon3):
    """Readarr author value attributes."""

    addOptions: _ReadarrAuthorAddOptions = attr.ib(type=_ReadarrAuthorAddOptions)
    authorMetadataId: int = attr.ib(type=int)
    books: _ReadarrAuthorValueBooks = attr.ib(type=_ReadarrAuthorValueBooks)
    foreignAuthorId: str = attr.ib(type=str)
    lastInfoSync: datetime = attr.ib(type=datetime)
    metadata: _ReadarrAuthorMetadata = attr.ib(type=_ReadarrAuthorMetadata)
    metadataProfile: _ReadarrMetadataProfile = attr.ib(type=_ReadarrMetadataProfile)
    qualityProfile: _ReadarrQualityProfile = attr.ib(type=_ReadarrQualityProfile)
    rootFolderPath: str = attr.ib(type=str)
    series: _ReadarrAuthorValueSeries = attr.ib(type=_ReadarrAuthorValueSeries)

    def __post_init__(self):
        super().__post_init__()
        self.addOptions = _ReadarrAuthorAddOptions(self.addOptions) or {}
        self.books = _ReadarrAuthorValueBooks(self.books) or {}
        self.metadata = _ReadarrAuthorMetadata(self.metadata) or {}
        self.metadataProfile = _ReadarrMetadataProfile(self.metadataProfile) or {}
        self.qualityProfile = _ReadarrQualityProfile(self.qualityProfile) or {}
        self.series = _ReadarrAuthorValueSeries(self.series) or {}


@dataclass(init=False)
class _ReadarrAuthor(_IsLoaded):
    """Readarr author attributes."""

    value: _ReadarrAuthorValue = attr.ib(type=_ReadarrAuthorValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValue(self.value) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValueMediaInfo(BaseModel):
    """Reaarr editions value book files value media info attributes."""

    audioBitrate: str = attr.ib(type=str)
    audioBitRate: str = attr.ib(type=str)
    audioBits: int = attr.ib(type=int)
    audioChannels: float = attr.ib(type=float)
    audioCodec: str = attr.ib(type=str)
    audioFormat: str = attr.ib(type=str)
    audioSampleRate: str = attr.ib(type=str)


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValue(BaseModel):
    """Readarr editions value book files value attributes."""

    author: _ReadarrAuthor = attr.ib(type=_ReadarrAuthor)
    calibreId: int = attr.ib(type=int)
    dateAdded: datetime = attr.ib(type=datetime)
    edition: _IsLoaded = attr.ib(type=_IsLoaded)
    editionId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo = attr.ib(
        type=_ReadarrEditionsValueBookFilesValueMediaInfo
    )
    modified: datetime = attr.ib(type=datetime)
    part: int = attr.ib(type=int)
    partCount: int = attr.ib(type=int)
    path: str = attr.ib(type=str)
    quality: _Quality = attr.ib(type=_Quality)
    releaseGroup: str = attr.ib(type=str)
    sceneName: str = attr.ib(type=str)
    size: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.edition = _IsLoaded(self.edition) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFiles(_IsLoaded):
    """Readarr editions value book files attributes."""

    value: list[_ReadarrEditionsValueBookFilesValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [
            _ReadarrEditionsValueBookFilesValue(item) for item in self.value or []
        ]


@dataclass(init=False)
class _ReadarrEditionsValue(_Common6):
    """Readarr editions value attributes."""

    asin: str = attr.ib(type=str)
    book: _IsLoaded = attr.ib(type=_IsLoaded)
    bookFiles: _ReadarrEditionsValueBookFiles = attr.ib(
        type=_ReadarrEditionsValueBookFiles
    )
    bookId: int = attr.ib(type=int)
    disambiguation: str = attr.ib(type=str)
    foreignEditionId: str = attr.ib(type=str)
    format: str = attr.ib(type=str)
    grabbed: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    images: list[_ReadarrImage] | None = None
    isbn13: str = attr.ib(type=str)
    isEbook: bool = attr.ib(type=bool)
    language: str = attr.ib(type=str)
    links: list[_Link] | None = None
    manualAdd: bool = attr.ib(type=bool)
    pageCount: int = attr.ib(type=int)
    publisher: str = attr.ib(type=str)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    releaseDate: datetime = attr.ib(type=datetime)
    remoteCover: str = attr.ib(type=str)
    title: str = attr.ib(type=str)
    titleSlug: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.book = _IsLoaded(self.book) or {}
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles) or {}
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrEditions(_IsLoaded):
    """Readarr editions attributes."""

    value: list[_ReadarrEditionsValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrEditionsValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrSeriesLinksValue(BaseModel):
    """Readarr series links value attributes."""

    book: _IsLoaded = attr.ib(type=_IsLoaded)
    bookId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    isPrimary: bool = attr.ib(type=bool)
    position: str = attr.ib(type=str)
    series: _ReadarrAuthorValueSeriesLinks = attr.ib(
        type=_ReadarrAuthorValueSeriesLinks
    )
    seriesId: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.book = _IsLoaded(self.book) or {}
        self.series = _ReadarrAuthorValueSeriesLinks(self.series) or {}


@dataclass(init=False)
class _ReadarrSeriesLinks(_IsLoaded):
    """Readarr series links attributes."""

    value: list[_ReadarrSeriesLinksValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrSeriesLinksValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrSeriesLinks2(BaseModel):
    """Readarr series links attributes."""

    bookId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    position: str = attr.ib(type=str)
    seriesId: int = attr.ib(type=int)
    seriesPosition: int = attr.ib(type=int)


@dataclass(init=False)
class _ReadarrBookCommon(_ReadarrCommon):
    """Readarr book base common attributes."""

    added: datetime = attr.ib(type=datetime)
    addOptions: _ReadarrAddOptions = attr.ib(type=_ReadarrAddOptions)
    anyEditionOk: bool = attr.ib(type=bool)
    authorMetadata: _ReadarrAuthorMetadata = attr.ib(type=_ReadarrAuthorMetadata)
    bookFiles: _ReadarrEditionsValueBookFiles = attr.ib(
        type=_ReadarrEditionsValueBookFiles
    )
    cleanTitle: str = attr.ib(type=str)
    foreignBookId: str = attr.ib(type=str)
    genres: list[str] = attr.ib(list[str])
    lastInfoSync: datetime = attr.ib(type=datetime)
    monitored: bool = attr.ib(type=bool)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    releaseDate: datetime = attr.ib(type=datetime)
    seriesLinks: _ReadarrSeriesLinks = attr.ib(type=_ReadarrSeriesLinks)
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAddOptions(self.addOptions) or {}
        self.authorMetadata = _ReadarrAuthorMetadata(self.authorMetadata) or {}
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles) or {}
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.seriesLinks = _ReadarrSeriesLinks(self.seriesLinks) or {}


@dataclass(init=False)
class _ReadarrAuthorStatistics(BaseModel):
    """Readarr author statistics attributes."""

    availableBookCount: int = attr.ib(type=int)
    bookCount: int = attr.ib(type=int)
    bookFileCount: int = attr.ib(type=int)
    percentOfBooks: float = attr.ib(type=float)
    sizeOnDisk: int = attr.ib(type=int)
    totalBookCount: int = attr.ib(type=int)


@dataclass(init=False)
class _ReadarrAuthorBook(_ReadarrBookCommon):
    """Readarr author book attributes."""

    author: _ReadarrAuthor = attr.ib(type=_ReadarrAuthor)
    editions: _ReadarrEditions = attr.ib(type=_ReadarrEditions)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.editions = _ReadarrEditions(self.editions) or {}


@dataclass(init=False)
class _ReadarrBlocklistFilter(BaseModel):
    """Readarr blocklist attributes."""

    key: str = attr.ib(type=str)
    value: str = attr.ib(type=str)


@dataclass(init=False)
class _ReadarrAuthorBase(_ReadarrCommon2, _ReadarrCommon, _ReadarrCommon3):
    """Readarr author attributes."""

    addOptions: _ReadarrAuthorAddOptions = attr.ib(type=_ReadarrAuthorAddOptions)
    authorName: str = attr.ib(type=str)
    authorNameLastFirst: str = attr.ib(type=str)
    disambiguation: str = attr.ib(type=str)
    ended: bool = attr.ib(type=bool)
    images: list[_ReadarrImage] | None = None
    lastBook: _ReadarrAuthorBook = attr.ib(type=_ReadarrAuthorBook)
    monitorNewItems: str = attr.ib(type=str)
    nextBook: _ReadarrAuthorBook = attr.ib(type=_ReadarrAuthorBook)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    remotePoster: str = attr.ib(type=str)
    rootFolderPath: str = attr.ib(type=str)
    statistics: _ReadarrAuthorStatistics = attr.ib(type=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAuthorAddOptions(self.addOptions) or {}
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.lastBook = _ReadarrAuthorBook(self.lastBook) or {}
        self.nextBook = _ReadarrAuthorBook(self.nextBook) or {}
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class _ReadarrBlocklistRecord(_Common7):
    """Readarr blocklist record attributes."""

    author: _ReadarrAuthorBase = attr.ib(type=_ReadarrAuthorBase)
    authorId: int = attr.ib(type=int)
    bookIds: list[int] = attr.ib(type=list[int])
    date: datetime = attr.ib(type=datetime)
    message: str = attr.ib(type=str)
    quality: _Quality = attr.ib(type=_Quality)
    sourceTitle: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthorBase(self.author) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrCountry(BaseModel):
    """Readarr country attributes."""

    name: str = attr.ib(type=str)
    twoLetterCode: str = attr.ib(type=str)


@dataclass(init=False)
class _ReadarrAudioTags(BaseModel):
    """Readarr audio tags attributes."""

    asin: str = attr.ib(type=str)
    authorMBId: str = attr.ib(type=str)
    authors: list[str] = attr.ib(list[str])
    authorTitle: str = attr.ib(type=str)
    bookMBId: str = attr.ib(type=str)
    bookTitle: str = attr.ib(type=str)
    catalogNumber: str = attr.ib(type=str)
    cleanTitle: str = attr.ib(type=str)
    country: _ReadarrCountry = attr.ib(type=_ReadarrCountry)
    disambiguation: str = attr.ib(type=str)
    discCount: int = attr.ib(type=int)
    discNumber: int = attr.ib(type=int)
    duration: str = attr.ib(type=str)
    goodreadsId: str = attr.ib(type=str)
    isbn: str = attr.ib(type=str)
    label: str = attr.ib(type=str)
    language: str = attr.ib(type=str)
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo = attr.ib(
        type=_ReadarrEditionsValueBookFilesValueMediaInfo
    )
    publisher: str = attr.ib(type=str)
    quality: _Quality = attr.ib(type=_Quality)
    recordingMBId: str = attr.ib(type=str)
    releaseGroup: str = attr.ib(type=str)
    releaseHash: str = attr.ib(type=str)
    releaseMBId: str = attr.ib(type=str)
    seriesIndex: str = attr.ib(type=str)
    seriesTitle: str = attr.ib(type=str)
    source: str = attr.ib(type=str)
    title: str = attr.ib(type=str)
    trackMBId: str = attr.ib(type=str)
    trackNumbers: list[int] = attr.ib(type=list[int])
    year: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.country = _ReadarrCountry(self.country) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrBookFileMediaInfo(_ReadarrEditionsValueBookFilesValueMediaInfo):
    """Readarr book file media info attributes."""

    id: int = attr.ib(type=int)


@dataclass(init=False)
class _ReadarrParsedBookInfo(BaseModel):
    """Readarr parsed book info attributes."""

    authorName: str = attr.ib(type=str)
    authorTitleInfo: _TitleInfo = attr.ib(type=_TitleInfo)
    bookTitle: str = attr.ib(type=str)
    discography: bool = attr.ib(type=bool)
    discographyEnd: int = attr.ib(type=int)
    discographyStart: int = attr.ib(type=int)
    quality: _Quality = attr.ib(type=_Quality)
    releaseDate: datetime = attr.ib(type=datetime)
    releaseGroup: str = attr.ib(type=str)
    releaseHash: str = attr.ib(type=str)
    releaseVersion: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.authorTitleInfo = _TitleInfo(self.authorTitleInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrSearchAuthor(_ReadarrCommon2, _ReadarrCommon3):
    """Readarr search author attributes."""

    authorMetadataId: int = attr.ib(type=int)
    authorName: str = attr.ib(type=str)
    authorNameLastFirst: str = attr.ib(type=str)
    ended: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    monitorNewItems: str = attr.ib(type=str)
    ratings: _ReadarrRating = attr.ib(type=_ReadarrRating)
    remotePoster: str = attr.ib(type=str)
    statistics: _ReadarrAuthorStatistics = attr.ib(type=_ReadarrAuthorStatistics)
    titleSlug: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class _ReadarrCategory(_SelectOption):
    """Readarr category attributes."""

    hint: str = attr.ib(type=str)
    parentValue: int = attr.ib(type=int)
