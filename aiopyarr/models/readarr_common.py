"""Readarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
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
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings)


@dataclass(init=False)
class _ReadarrAuthorMetadata(_IsLoaded):
    """Readarr author Metadata attributes."""

    value: type[_ReadarrMetadataValue] = field(default=_ReadarrMetadataValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrMetadataValue(self.value)


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
    quality: type[_Common3] = field(default=_Common3)

    def __post_init__(self):
        """Post init."""
        self.quality = _Common3(self.quality)


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

    value: type[_ReadarrQualityProfileValue] = field(
        default=_ReadarrQualityProfileValue
    )

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrQualityProfileValue(self.value)


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

    value: type[_ReadarrMetadataProfileValue] = field(
        default=_ReadarrMetadataProfileValue
    )

    def __post_init__(self):
        self.value = _ReadarrMetadataProfileValue(self.value)


@dataclass(init=False)
class _ReadarrAuthorValueBooks(_IsLoaded):
    """Readarr author value books attributes."""

    value: list  # Currently unknown contents


@dataclass(init=False)
class _ReadarrAuthorValueSeriesValue(BaseModel):
    """Readarr author value series value attributes."""

    books: type[_ReadarrAuthorValueBooks] = field(default=_ReadarrAuthorValueBooks)
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
        self.books = _ReadarrAuthorValueBooks(self.books)


@dataclass(init=False)
class _ReadarrAuthorValueSeriesLinks(_IsLoaded):
    """Readarr author value series links attributes."""

    value: type[_ReadarrAuthorValueSeriesValue] = field(
        default=_ReadarrAuthorValueSeriesValue
    )

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValueSeriesValue(self.value)


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

    addOptions: type[_ReadarrAuthorAddOptions] = field(default=_ReadarrAuthorAddOptions)
    authorMetadataId: int
    books: type[_ReadarrAuthorValueBooks] = field(default=_ReadarrAuthorValueBooks)
    foreignAuthorId: str
    lastInfoSync: datetime
    metadata: type[_ReadarrAuthorMetadata] = field(default=_ReadarrAuthorMetadata)
    metadataProfile: type[_ReadarrMetadataProfile] = field(
        default=_ReadarrMetadataProfile
    )
    qualityProfile: type[_ReadarrQualityProfile] = field(default=_ReadarrQualityProfile)
    rootFolderPath: str
    series: type[_ReadarrAuthorValueSeries] = field(default=_ReadarrAuthorValueSeries)

    def __post_init__(self):
        super().__post_init__()
        self.addOptions = _ReadarrAuthorAddOptions(self.addOptions)
        self.books = _ReadarrAuthorValueBooks(self.books)
        self.metadata = _ReadarrAuthorMetadata(self.metadata)
        self.metadataProfile = _ReadarrMetadataProfile(self.metadataProfile)
        self.qualityProfile = _ReadarrQualityProfile(self.qualityProfile)
        self.series = _ReadarrAuthorValueSeries(self.series)


@dataclass(init=False)
class _ReadarrAuthor(_IsLoaded):
    """Readarr author attributes."""

    value: type[_ReadarrAuthorValue] = field(default=_ReadarrAuthorValue)

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValue(self.value)


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

    author: type[_ReadarrAuthor] = field(default=_ReadarrAuthor)
    calibreId: int
    dateAdded: datetime
    edition: type[_IsLoaded] = field(default=_IsLoaded)
    editionId: int
    id: int
    mediaInfo: type[_ReadarrEditionsValueBookFilesValueMediaInfo] = field(
        default=_ReadarrEditionsValueBookFilesValueMediaInfo
    )
    modified: datetime
    part: int
    partCount: int
    path: str
    quality: type[_Quality] = field(default=_Quality)
    releaseGroup: str
    sceneName: str
    size: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author)
        self.edition = _IsLoaded(self.edition)
        self.mediaInfo = _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo)
        self.quality = _Quality(self.quality)


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
    book: type[_IsLoaded] = field(default=_IsLoaded)
    bookFiles: type[_ReadarrEditionsValueBookFiles] = field(
        default=_ReadarrEditionsValueBookFiles
    )
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
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    releaseDate: datetime
    remoteCover: str
    title: str
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.book = _IsLoaded(self.book)
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles)
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings)


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

    book: type[_IsLoaded] = field(default=_IsLoaded)
    bookId: int
    id: int
    isPrimary: bool
    position: str
    series: type[_ReadarrAuthorValueSeriesLinks] = field(
        default=_ReadarrAuthorValueSeriesLinks
    )
    seriesId: int

    def __post_init__(self):
        """Post init."""
        self.book = _IsLoaded(self.book)
        self.series = _ReadarrAuthorValueSeriesLinks(self.series)


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
    addOptions: type[_ReadarrAddOptions] = field(default=_ReadarrAddOptions)
    anyEditionOk: bool
    authorMetadata: type[_ReadarrAuthorMetadata] = field(default=_ReadarrAuthorMetadata)
    bookFiles: type[_ReadarrEditionsValueBookFiles] = field(
        default=_ReadarrEditionsValueBookFiles
    )
    cleanTitle: str
    foreignBookId: str
    genres: list[str]
    lastInfoSync: datetime
    monitored: bool
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    releaseDate: datetime
    seriesLinks: type[_ReadarrSeriesLinks] = field(default=_ReadarrSeriesLinks)
    title: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAddOptions(self.addOptions)
        self.authorMetadata = _ReadarrAuthorMetadata(self.authorMetadata)
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles)
        self.ratings = _ReadarrRating(self.ratings)
        self.seriesLinks = _ReadarrSeriesLinks(self.seriesLinks)


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

    author: type[_ReadarrAuthor] = field(default=_ReadarrAuthor)
    editions: type[_ReadarrEditions] = field(default=_ReadarrEditions)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author)
        self.editions = _ReadarrEditions(self.editions)


@dataclass(init=False)
class _ReadarrBlocklistFilter(BaseModel):
    """Readarr blocklist attributes."""

    key: str
    value: str


@dataclass(init=False)
class _ReadarrAuthorBase(_ReadarrCommon2, _ReadarrCommon, _ReadarrCommon3):
    """Readarr author attributes."""

    addOptions: type[_ReadarrAuthorAddOptions] = field(default=_ReadarrAuthorAddOptions)
    authorName: str
    authorNameLastFirst: str
    disambiguation: str
    ended: bool
    images: list[_ReadarrImage] | None = None
    lastBook: type[_ReadarrAuthorBook] = field(default=_ReadarrAuthorBook)
    monitorNewItems: str
    nextBook: type[_ReadarrAuthorBook] = field(default=_ReadarrAuthorBook)
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    remotePoster: str
    rootFolderPath: str
    statistics: type[_ReadarrAuthorStatistics] = field(default=_ReadarrAuthorStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAuthorAddOptions(self.addOptions)
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.lastBook = _ReadarrAuthorBook(self.lastBook)
        self.nextBook = _ReadarrAuthorBook(self.nextBook)
        self.ratings = _ReadarrRating(self.ratings)
        self.statistics = _ReadarrAuthorStatistics(self.statistics)


@dataclass(init=False)
class _ReadarrBlocklistRecord(_Common7):
    """Readarr blocklist record attributes."""

    author: type[_ReadarrAuthorBase] = field(default=_ReadarrAuthorBase)
    authorId: int
    bookIds: list[int]
    date: datetime
    message: str
    quality: type[_Quality] = field(default=_Quality)
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthorBase(self.author)
        self.quality = _Quality(self.quality)


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
    country: type[_ReadarrCountry] = field(default=_ReadarrCountry)
    disambiguation: str
    discCount: int
    discNumber: int
    duration: str
    goodreadsId: str
    isbn: str
    label: str
    language: str
    mediaInfo: type[_ReadarrEditionsValueBookFilesValueMediaInfo] = field(
        default=_ReadarrEditionsValueBookFilesValueMediaInfo
    )
    publisher: str
    quality: type[_Quality] = field(default=_Quality)
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
        self.country = _ReadarrCountry(self.country)
        self.mediaInfo = _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo)
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _ReadarrBookFileMediaInfo(_ReadarrEditionsValueBookFilesValueMediaInfo):
    """Readarr book file media info attributes."""

    id: int


@dataclass(init=False)
class _ReadarrParsedBookInfo(BaseModel):
    """Readarr parsed book info attributes."""

    authorName: str
    authorTitleInfo: type[_TitleInfo] = field(default=_TitleInfo)
    bookTitle: str
    discography: bool
    discographyEnd: int
    discographyStart: int
    quality: type[_Quality] = field(default=_Quality)
    releaseDate: datetime
    releaseGroup: str
    releaseHash: str
    releaseVersion: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.authorTitleInfo = _TitleInfo(self.authorTitleInfo)
        self.quality = _Quality(self.quality)


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
    ratings: type[_ReadarrRating] = field(default=_ReadarrRating)
    remotePoster: str
    statistics: type[_ReadarrAuthorStatistics] = field(default=_ReadarrAuthorStatistics)
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings)
        self.statistics = _ReadarrAuthorStatistics(self.statistics)


@dataclass(init=False)
class _ReadarrCategory(_SelectOption):
    """Readarr category attributes."""

    hint: str
    parentValue: int
