"""Readarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

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

    authorMetadataId: int
    id: int
    links: list[_Link] | None = None
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        self.links = [_Link(link) for link in self.links or []]


@dataclass(init=False)
class _ReadarrCommon2(BaseModel):
    """Readarr Common attributes."""

    foreignAuthorId: str
    genres: list[str]
    overview: str
    sortName: str
    sortNameLastFirst: str
    status: str


@dataclass(init=False)
class _ReadarrRating(_Ratings):
    """Readarr ratings attributes."""

    popularity: float


@dataclass(init=False)
class _ReadarrAddOptions(BaseModel):
    """Readarr add options attributes."""

    addType: str
    searchForNewBook: bool


@dataclass(init=False)
class _ReadarrImage(_Common5):
    """readarr metadata value attributes."""

    extension: str


@dataclass(init=False)
class _ReadarrMetadataValue(_ReadarrCommon2, _Common3):
    """Readarr metadata value attributes."""

    aliases: list[str]
    born: datetime
    died: datetime
    disambiguation: str
    gender: str
    hometown: str
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    nameLastFirst: str
    ratings: _ReadarrRating | None = None
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrAuthorMetadata(_IsLoaded):
    """Readarr author Metadata attributes."""

    value: _ReadarrMetadataValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrMetadataValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorAddOptions(BaseModel):
    """Readarr author add options attributes."""

    booksToMonitor: list[str]
    monitor: str
    monitored: bool
    searchForMissingBooks: bool


@dataclass(init=False)
class _ReadarrQualityItem(_Common3):
    """Readarr quality item attributes."""

    allowed: bool
    items: list  # Currently unknown contents
    quality: _Common3 | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _Common3(self.quality) or {}


@dataclass(init=False)
class _ReadarrQualityProfileValue(_Common3):
    """Readarr quality profile value attributes."""

    cutoff: int
    items: list[_ReadarrQualityItem] | None = None
    upgradeAllowed: bool

    def __post_init__(self):
        """Post init."""
        self.items = [_ReadarrQualityItem(item) for item in self.items or []]


@dataclass(init=False)
class _ReadarrQualityProfile(_IsLoaded):
    """Readarr quality profile attributes."""

    value: _ReadarrQualityProfileValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrQualityProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrMetadataProfileValue(_Common3):
    """Readarr metadata profile value attributes."""

    allowedLanguages: str
    ignored: str
    minPages: int
    minPopularity: float
    skipMissingDate: bool
    skipMissingIsbn: bool
    skipPartsAndSets: bool
    skipSeriesSecondary: bool


@dataclass(init=False)
class _ReadarrMetadataProfile(_IsLoaded):
    """Readarr metadata profile attributes."""

    value: _ReadarrMetadataProfileValue | None = None

    def __post_init__(self):
        self.value = _ReadarrMetadataProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueBooks(_IsLoaded):
    """Readarr author value books attributes."""

    value: list  # Currently unknown contents


@dataclass(init=False)
class _ReadarrAuthorValueSeriesValue(BaseModel):
    """Readarr author value series value attributes."""

    books: _ReadarrAuthorValueBooks | None = None
    description: str
    foreignAuthorId: str
    foreignSeriesId: str
    id: int
    numbered: bool
    primaryWorkCount: int
    title: str
    workCount: int

    def __post_init__(self):
        """Post init."""
        self.books = _ReadarrAuthorValueBooks(self.books) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeriesLinks(_IsLoaded):
    """Readarr author value series links attributes."""

    value: _ReadarrAuthorValueSeriesValue | None = None

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

    added: datetime
    cleanName: str
    metadataProfileId: int
    monitored: bool
    path: str
    qualityProfileId: int
    tags: list[int]


@dataclass(init=False)
class _ReadarrAuthorValue(_Common3, _ReadarrCommon3):
    """Readarr author value attributes."""

    addOptions: _ReadarrAuthorAddOptions | None = None
    authorMetadataId: int
    books: _ReadarrAuthorValueBooks | None = None
    foreignAuthorId: str
    lastInfoSync: datetime
    metadata: _ReadarrAuthorMetadata | None = None
    metadataProfile: _ReadarrMetadataProfile | None = None
    qualityProfile: _ReadarrQualityProfile | None = None
    rootFolderPath: str
    series: _ReadarrAuthorValueSeries | None = None

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

    value: _ReadarrAuthorValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValue(self.value) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValueMediaInfo(BaseModel):
    """Reaarr editions value book files value media info attributes."""

    audioBitrate: str
    audioBitRate: str
    audioBits: int
    audioChannels: float
    audioCodec: str
    audioFormat: str
    audioSampleRate: str


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValue(BaseModel):
    """Readarr editions value book files value attributes."""

    author: _ReadarrAuthor | None = None
    calibreId: int
    dateAdded: datetime
    edition: _IsLoaded | None = None
    editionId: int
    id: int
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    modified: datetime
    part: int
    partCount: int
    path: str
    quality: _Quality | None = None
    releaseGroup: str
    sceneName: str
    size: int

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

    asin: str
    book: _IsLoaded | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    bookId: int
    disambiguation: str
    foreignEditionId: str
    format: str
    grabbed: bool
    id: int
    images: list[_ReadarrImage] | None = None
    isbn13: str
    isEbook: bool
    language: str
    links: list[_Link] | None = None
    manualAdd: bool
    pageCount: int
    publisher: str
    ratings: _ReadarrRating | None = None
    releaseDate: datetime
    remoteCover: str
    title: str
    titleSlug: int

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

    book: _IsLoaded | None = None
    bookId: int
    id: int
    isPrimary: bool
    position: str
    series: _ReadarrAuthorValueSeriesLinks | None = None
    seriesId: int

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

    bookId: int
    id: int
    position: str
    seriesId: int
    seriesPosition: int


@dataclass(init=False)
class _ReadarrBookCommon(_ReadarrCommon):
    """Readarr book base common attributes."""

    added: datetime
    addOptions: _ReadarrAddOptions | None = None
    anyEditionOk: bool
    authorMetadata: _ReadarrAuthorMetadata | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    cleanTitle: str
    foreignBookId: str
    genres: list[str]
    lastInfoSync: datetime
    monitored: bool
    ratings: _ReadarrRating | None = None
    releaseDate: datetime
    seriesLinks: _ReadarrSeriesLinks | None = None
    title: str

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

    availableBookCount: int
    bookCount: int
    bookFileCount: int
    percentOfBooks: float
    sizeOnDisk: int
    totalBookCount: int


@dataclass(init=False)
class _ReadarrAuthorBook(_ReadarrBookCommon):
    """Readarr author book attributes."""

    author: _ReadarrAuthor | None = None
    editions: _ReadarrEditions | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.editions = _ReadarrEditions(self.editions) or {}


@dataclass(init=False)
class _ReadarrBlocklistFilter(BaseModel):
    """Readarr blocklist attributes."""

    key: str
    value: str


@dataclass(init=False)
class _ReadarrAuthorBase(_ReadarrCommon2, _ReadarrCommon, _ReadarrCommon3):
    """Readarr author attributes."""

    addOptions: _ReadarrAuthorAddOptions | None = None
    authorName: str
    authorNameLastFirst: str
    disambiguation: str
    ended: bool
    images: list[_ReadarrImage] | None = None
    lastBook: _ReadarrAuthorBook | None = None
    monitorNewItems: str
    nextBook: _ReadarrAuthorBook | None = None
    ratings: _ReadarrRating | None = None
    remotePoster: str
    rootFolderPath: str
    statistics: _ReadarrAuthorStatistics | None = None

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

    author: _ReadarrAuthorBase | None = None
    authorId: int
    bookIds: list[int]
    date: datetime
    message: str
    quality: _Quality | None = None
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthorBase(self.author) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrCountry(BaseModel):
    """Readarr country attributes."""

    name: str
    twoLetterCode: str


@dataclass(init=False)
class _ReadarrAudioTags(BaseModel):
    """Readarr audio tags attributes."""

    asin: str
    authorMBId: str
    authors: list[str]
    authorTitle: str
    bookMBId: str
    bookTitle: str
    catalogNumber: str
    cleanTitle: str
    country: _ReadarrCountry | None = None
    disambiguation: str
    discCount: int
    discNumber: int
    duration: str
    goodreadsId: str
    isbn: str
    label: str
    language: str
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    publisher: str
    quality: _Quality | None = None
    recordingMBId: str
    releaseGroup: str
    releaseHash: str
    releaseMBId: str
    seriesIndex: str
    seriesTitle: str
    source: str
    title: str
    trackMBId: str
    trackNumbers: list[int]
    year: int

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

    id: int


@dataclass(init=False)
class _ReadarrParsedBookInfo(BaseModel):
    """Readarr parsed book info attributes."""

    authorName: str
    authorTitleInfo: _TitleInfo | None = None
    bookTitle: str
    discography: bool
    discographyEnd: int
    discographyStart: int
    quality: _Quality | None = None
    releaseDate: datetime
    releaseGroup: str
    releaseHash: str
    releaseVersion: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.authorTitleInfo = _TitleInfo(self.authorTitleInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrSearchAuthor(_ReadarrCommon2, _ReadarrCommon3):
    """Readarr search author attributes."""

    authorMetadataId: int
    authorName: str
    authorNameLastFirst: str
    ended: bool
    id: int
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    monitorNewItems: str
    ratings: _ReadarrRating | None = None
    remotePoster: str
    statistics: _ReadarrAuthorStatistics | None = None
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}


@dataclass(init=False)
class _ReadarrCategory(_SelectOption):
    """Readarr category attributes."""

    hint: str
    parentValue: int
