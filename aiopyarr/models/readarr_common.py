"""Readarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel, get_datetime
from .request_common import (
    _Common2,
    _Common3,
    _Common5,
    _Common6,
    _Common7,
    _HistoryData,
    _Link,
    _Quality,
    _QualityCommon,
    _Ratings,
    _TitleInfo,
)


@dataclass(init=False)
class _ReadarrCommon(BaseModel):
    """Readarr Common attributes."""

    authorMetadataId: int | None = None
    id: int | None = None
    links: list[_Link] | None = None
    titleSlug: str | None = None

    def __post_init__(self):
        """Post init."""
        self.links = [_Link(link) for link in self.links or []]


@dataclass(init=False)
class _ReadarrCommon2(BaseModel):
    """Readarr Common attributes."""

    foreignAuthorId: str | None = None
    genres: list[str] | None = None
    overview: str | None = None
    sortName: str | None = None
    sortNameLastFirst: str | None = None
    status: str | None = None


@dataclass(init=False)
class _ReadarrRating(_Ratings):
    """Readarr ratings attributes."""

    popularity: float | None = None


@dataclass(init=False)
class _ReadarrAddOptions(BaseModel):
    """Readarr add options attributes."""

    addType: str | None = None
    searchForNewBook: bool | None = None


@dataclass(init=False)
class _ReadarrImage(_Common5):
    """readarr metadata value attributes."""

    extension: str | None = None


@dataclass(init=False)
class _ReadarrMetadataValue(_ReadarrCommon2, _Common3):
    """Readarr metadata value attributes."""

    aliases: list[str] | None = None
    born: str | None = None
    died: str | None = None
    disambiguation: str | None = None
    gender: str | None = None
    hometown: str | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    nameLastFirst: str | None = None
    ratings: _ReadarrRating | None = None
    titleSlug: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrIsLoaded(BaseModel):
    """Readarr is loaded attribute."""

    isLoaded: bool | None = None


@dataclass(init=False)
class _ReadarrAuthorMetadata(_ReadarrIsLoaded):
    """Readarr author Metadata attributes."""

    value: _ReadarrMetadataValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrMetadataValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorAddOptions(BaseModel):
    """Readarr author add options attributes."""

    booksToMonitor: list[str] | None = None
    monitor: str | None = None
    monitored: bool | None = None
    searchForMissingBooks: bool | None = None


@dataclass(init=False)
class _ReadarrQualityItem(_Common3):
    """Readarr quality item attributes."""

    allowed: bool | None = None
    items: list | None = None  # Currently unknown contents
    quality: _Common3 | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _Common3(self.quality) or {}


@dataclass(init=False)
class _ReadarrQualityProfileValue(_Common3):
    """Readarr quality profile value attributes."""

    cutoff: int | None = None
    items: list[_ReadarrQualityItem] | None = None
    upgradeAllowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.items = [_ReadarrQualityItem(item) for item in self.items or []]


@dataclass(init=False)
class _ReadarrQualityProfile(_ReadarrIsLoaded):
    """Readarr quality profile attributes."""

    value: _ReadarrQualityProfileValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrQualityProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrMetadataProfileValue(_Common3):
    """Readarr metadata profile value attributes."""

    allowedLanguages: str | None = None
    ignored: str | None = None
    minPages: int | None = None
    minPopularity: float | None = None
    skipMissingDate: bool | None = None
    skipMissingIsbn: bool | None = None
    skipPartsAndSets: bool | None = None
    skipSeriesSecondary: bool | None = None


@dataclass(init=False)
class _ReadarrMetadataProfile(_ReadarrIsLoaded):
    """Readarr metadata profile attributes."""

    value: _ReadarrMetadataProfileValue | None = None

    def __post_init__(self):
        self.value = _ReadarrMetadataProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueBooks(_ReadarrIsLoaded):
    """Readarr author value books attributes."""

    value: list | None = None  # Currently unknown contents


@dataclass(init=False)
class _ReadarrAuthorValueSeriesValue(BaseModel):
    """Readarr author value series value attributes."""

    books: _ReadarrAuthorValueBooks | None = None
    description: str | None = None
    foreignAuthorId: str | None = None
    foreignSeriesId: str | None = None
    id: int | None = None
    numbered: bool | None = None
    primaryWorkCount: int | None = None
    title: str | None = None
    workCount: int | None = None

    def __post_init__(self):
        """Post init."""
        self.books = _ReadarrAuthorValueBooks(self.books) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeriesLinks(_ReadarrIsLoaded):
    """Readarr author value series links attributes."""

    value: _ReadarrAuthorValueSeriesValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValueSeriesValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeries(_ReadarrIsLoaded):
    """Readarr author value series attributes."""

    value: list[_ReadarrAuthorValueSeriesValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrAuthorValueSeriesValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrCommon3(BaseModel):
    """Readarr common attributes."""

    added: str | None = None
    cleanName: str | None = None
    metadataProfileId: int | None = None
    monitored: bool | None = None
    path: str | None = None
    qualityProfileId: int | None = None
    tags: list[int | None] | None = None


@dataclass(init=False)
class _ReadarrAuthorValue(_Common3, _ReadarrCommon3):
    """Readarr author value attributes."""

    addOptions: _ReadarrAuthorAddOptions | None = None
    authorMetadataId: int | None = None
    books: _ReadarrAuthorValueBooks | None = None
    foreignAuthorId: str | None = None
    lastInfoSync: str | None = None
    metadata: _ReadarrAuthorMetadata | None = None
    metadataProfile: _ReadarrMetadataProfile | None = None
    qualityProfile: _ReadarrQualityProfile | None = None
    rootFolderPath: str | None = None
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
class _ReadarrAuthor(_ReadarrIsLoaded):
    """Readarr author attributes."""

    value: _ReadarrAuthorValue | None = None

    def __post_init__(self):
        """Post init."""
        self.value = _ReadarrAuthorValue(self.value) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValueMediaInfo(BaseModel):
    """Reaarr editions value book files value media info attributes."""

    audioBitrate: str | None = None
    audioBitRate: str | None = None
    audioBits: int | None = None
    audioChannels: float | None = None
    audioCodec: str | None = None
    audioFormat: str | None = None
    audioSampleRate: str | None = None


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValue(BaseModel):
    """Readarr editions value book files value attributes."""

    author: _ReadarrAuthor | None = None
    calibreId: int | None = None
    dateAdded: str | None = None
    edition: _ReadarrIsLoaded | None = None
    editionId: int | None = None
    id: int | None = None
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    modified: str | None = None
    part: int | None = None
    partCount: int | None = None
    path: str | None = None
    quality: _Quality | None = None
    releaseGroup: str | None = None
    sceneName: str | None = None
    size: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.edition = _ReadarrIsLoaded(self.edition) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFiles(_ReadarrIsLoaded):
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

    asin: str | None = None
    book: _ReadarrIsLoaded | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    bookId: int | None = None
    disambiguation: str | None = None
    foreignEditionId: str | None = None
    format: str | None = None
    grabbed: bool | None = None
    id: int | None = None
    images: list[_ReadarrImage] | None = None
    isbn13: str | None = None
    isEbook: bool | None = None
    language: str | None = None
    links: list[_Link] | None = None
    manualAdd: bool | None = None
    pageCount: int | None = None
    publisher: str | None = None
    ratings: _ReadarrRating | None = None
    releaseDate: str | None = None
    remoteCover: str | None = None
    title: str | None = None
    titleSlug: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.book = _ReadarrIsLoaded(self.book) or {}
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles) or {}
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrEditions(_ReadarrIsLoaded):
    """Readarr editions attributes."""

    value: list[_ReadarrEditionsValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrEditionsValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrSeriesLinksValue(BaseModel):
    """Readarr series links value attributes."""

    book: _ReadarrIsLoaded | None = None
    bookId: int | None = None
    id: int | None = None
    isPrimary: bool | None = None
    position: str | None = None
    series: _ReadarrAuthorValueSeriesLinks | None = None
    seriesId: int | None = None

    def __post_init__(self):
        """Post init."""
        self.book = _ReadarrIsLoaded(self.book) or {}
        self.series = _ReadarrAuthorValueSeriesLinks(self.series) or {}


@dataclass(init=False)
class _ReadarrSeriesLinks(_ReadarrIsLoaded):
    """Readarr series links attributes."""

    value: list[_ReadarrSeriesLinksValue] | None = None

    def __post_init__(self):
        """Post init."""
        self.value = [_ReadarrSeriesLinksValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrSeriesLinks2(BaseModel):
    """Readarr series links attributes."""

    bookId: int | None = None
    id: int | None = None
    position: str | None = None
    seriesId: int | None = None
    seriesPosition: int | None = None


@dataclass(init=False)
class _ReadarrBookCommon(_ReadarrCommon):
    """Readarr book base common attributes."""

    added: str | None = None
    addOptions: _ReadarrAddOptions | None = None
    anyEditionOk: bool | None = None
    authorMetadata: _ReadarrAuthorMetadata | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    cleanTitle: str | None = None
    foreignBookId: str | None = None
    genres: list[str] | None = None
    lastInfoSync: str | None = None
    monitored: bool | None = None
    ratings: _ReadarrRating | None = None
    releaseDate: str | None = None
    seriesLinks: _ReadarrSeriesLinks | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.added = get_datetime(self.added)
        self.addOptions = _ReadarrAddOptions(self.addOptions) or {}
        self.authorMetadata = _ReadarrAuthorMetadata(self.authorMetadata) or {}
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles) or {}
        self.lastInfoSync = get_datetime(self.lastInfoSync)
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.releaseDate = get_datetime(self.releaseDate)
        self.seriesLinks = _ReadarrSeriesLinks(self.seriesLinks) or {}


@dataclass(init=False)
class _ReadarrAuthorStatistics(BaseModel):
    """Readarr author statistics attributes."""

    availableBookCount: int | None = None
    bookCount: int | None = None
    bookFileCount: int | None = None
    percentOfBooks: float | None = None
    sizeOnDisk: int | None = None
    totalBookCount: int | None = None


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

    key: str | None = None
    value: str | None = None


@dataclass(init=False)
class _ReadarrAuthorBase(_ReadarrCommon2, _ReadarrCommon, _ReadarrCommon3):
    """Readarr author attributes."""

    addOptions: _ReadarrAuthorAddOptions | None = None
    authorName: str | None = None
    authorNameLastFirst: str | None = None
    disambiguation: str | None = None
    ended: bool | None = None
    images: list[_ReadarrImage] | None = None
    lastBook: _ReadarrAuthorBook | None = None
    monitorNewItems: str | None = None
    nextBook: _ReadarrAuthorBook | None = None
    ratings: _ReadarrRating | None = None
    remotePoster: str | None = None
    rootFolderPath: str | None = None
    statistics: _ReadarrAuthorStatistics | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.added = get_datetime(self.added)
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
    authorId: int | None = None
    bookIds: list[int] | None = None
    date: str | None = None
    message: str | None = None
    quality: _Quality | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthorBase(self.author) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrCountry(BaseModel):
    """Readarr country attributes."""

    name: str | None = None
    twoLetterCode: str | None = None


@dataclass(init=False)
class _ReadarrDuration(BaseModel):
    """Readarr duration attributes."""

    days: int | None = None
    hours: int | None = None
    milliseconds: int | None = None
    minutes: int | None = None
    seconds: int | None = None
    ticks: int | None = None
    totalDays: int | None = None
    totalHours: int | None = None
    totalMilliseconds: int | None = None
    totalMinutes: int | None = None
    totalSeconds: int | None = None


@dataclass(init=False)
class _ReadarrAudioTags(BaseModel):
    """Readarr audio tags attributes."""

    asin: str | None = None
    authorMBId: str | None = None
    authors: list[str] | None = None
    authorTitle: str | None = None
    bookMBId: str | None = None
    bookTitle: str | None = None
    catalogNumber: str | None = None
    cleanTitle: str | None = None
    country: _ReadarrCountry | None = None
    disambiguation: str | None = None
    discCount: int | None = None
    discNumber: int | None = None
    duration: _ReadarrDuration | None = None
    goodreadsId: str | None = None
    isbn: str | None = None
    label: str | None = None
    language: str | None = None
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    publisher: str | None = None
    quality: _Quality | None = None
    recordingMBId: str | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    releaseMBId: str | None = None
    seriesIndex: str | None = None
    seriesTitle: str | None = None
    source: str | None = None
    title: str | None = None
    trackMBId: str | None = None
    trackNumbers: list[int] | None = None
    year: int | None = None

    def __post_init__(self):
        """Post init."""
        self.country = _ReadarrCountry(self.country) or {}
        self.duration = _ReadarrDuration(self.duration) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrBookFileMediaInfo(_ReadarrEditionsValueBookFilesValueMediaInfo):
    """Readarr book file media info attributes."""

    id: int | None = None


@dataclass(init=False)
class _ReadarrParsedBookInfo(BaseModel):
    """Readarr parsed book info attributes."""

    authorName: str | None = None
    authorTitleInfo: _TitleInfo | None = None
    bookTitle: str | None = None
    discography: bool | None = None
    discographyEnd: int | None = None
    discographyStart: int | None = None
    quality: _Quality | None = None
    releaseDate: str | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    releaseVersion: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.authorTitleInfo = _TitleInfo(self.authorTitleInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _ReadarrHistoryRecord(_Common2, _QualityCommon):
    """Readarr history record attributes."""

    authorId: int | None = None
    bookId: int | None = None
    data: _HistoryData | None = None
    date: str | None = None
    id: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _HistoryData(self.data) or {}


@dataclass(init=False)
class _ReadarrSearchAuthor(_ReadarrCommon2, _ReadarrCommon3):
    """Readarr search author attributes."""

    authorMetadataId: int | None = None
    authorName: str | None = None
    authorNameLastFirst: str | None = None
    ended: bool | None = None
    id: int | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_Link] | None = None
    monitorNewItems: str | None = None
    ratings: _ReadarrRating | None = None
    remotePoster: str | None = None
    statistics: _ReadarrAuthorStatistics | None = None
    titleSlug: str | None = None

    def __post_init__(self):
        """Post init."""
        self.added = get_datetime(self.added)
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}
        self.statistics = _ReadarrAuthorStatistics(self.statistics) or {}
