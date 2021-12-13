"""Radarr Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel


@dataclass(init=False)
class _ReadarrLink(BaseModel):
    """Link attributes."""

    url: str | None = None
    name: str | None = None


@dataclass(init=False)
class _ReadarrCommon(BaseModel):
    """Readarr Common attributes."""

    id: int | None = None
    authorMetadataId: int | None = None
    titleSlug: str | None = None
    links: list[_ReadarrLink] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.links = [_ReadarrLink(link) for link in self.links or []]


@dataclass(init=False)
class _ReadarrRating(BaseModel):
    """Ratings attributes."""

    votes: int | None = None
    value: float | None = None
    popularity: float | None = None


@dataclass(init=False)
class _ReadarrAddOptions(BaseModel):
    """Add options attributes."""

    addType: str | None = None
    searchForNewBook: bool | None = None


@dataclass(init=False)
class _ReadarrImage(BaseModel):
    """Metadata value attributes."""

    url: str | None = None
    coverType: str | None = None
    extension: str | None = None


@dataclass(init=False)
class _ReadarrMetadataValue(BaseModel):
    """Metadata value attributes."""

    id: int | None = None
    foreignAuthorId: str | None = None
    titleSlug: str | None = None
    name: str | None = None
    sortName: str | None = None
    nameLastFirst: str | None = None
    sortNameLastFirst: str | None = None
    aliases: list[str] | None = None
    overview: str | None = None
    disambiguation: str | None = None
    gender: str | None = None
    hometown: str | None = None
    born: str | None = None
    died: str | None = None
    status: str | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_ReadarrLink] | None = None
    genres: list[str] | None = None
    ratings: _ReadarrRating | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_ReadarrLink(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrAuthorMetadata(BaseModel):
    """Author Metadata attributes."""

    isLoaded: bool | None = None
    value: _ReadarrMetadataValue | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrMetadataValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorAddOptions(BaseModel):
    """Author add options attributes."""

    monitor: str | None = None
    booksToMonitor: list[str] | None = None
    monitored: bool | None = None
    searchForMissingBooks: bool | None = None


@dataclass(init=False)
class _ReadarrIdName(BaseModel):
    """Id/name attributes."""

    id: int | None = None
    name: str | None = None


@dataclass(init=False)
class _ReadarrQualityItem(_ReadarrIdName):
    """Quality item attributes."""

    quality: _ReadarrIdName | None = None
    items: list | None = None  # Currently unknown contents
    allowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _ReadarrIdName(self.quality) or {}


@dataclass(init=False)
class _ReadarrQualityProfileValue(_ReadarrIdName):
    """Quality profile value attributes."""

    upgradeAllowed: bool | None = None
    cutoff: int | None = None
    items: list[_ReadarrQualityItem] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.items = [_ReadarrQualityItem(item) for item in self.items or []]


@dataclass(init=False)
class _ReadarrQualityProfile(BaseModel):
    """Quality profile attributes."""

    isLoaded: bool | None = None
    value: _ReadarrQualityProfileValue | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrQualityProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrMetadataProfileValue(BaseModel):
    """Metadata profile value attributes."""

    id: int | None = None
    name: str | None = None
    minPopularity: float | None = None
    skipMissingDate: bool | None = None
    skipMissingIsbn: bool | None = None
    skipPartsAndSets: bool | None = None
    skipSeriesSecondary: bool | None = None
    allowedLanguages: str | None = None
    minPages: int | None = None
    ignored: str | None = None


@dataclass(init=False)
class _ReadarrMetadataProfile(BaseModel):
    """Metadata profile attributes."""

    isLoaded: bool | None = None
    value: _ReadarrMetadataProfileValue | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrMetadataProfileValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueBooks(BaseModel):
    """Author value books attributes."""

    isLoaded: bool | None = None
    value: list | None = None  # Currently unknown contents


@dataclass(init=False)
class _ReadarrAuthorValueSeriesValue(BaseModel):
    """Author value series value attributes."""

    id: int | None = None
    foreignSeriesId: str | None = None
    title: str | None = None
    description: str | None = None
    numbered: bool | None = None
    workCount: int | None = None
    primaryWorkCount: int | None = None
    books: _ReadarrAuthorValueBooks | None = None
    foreignAuthorId: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.books = _ReadarrAuthorValueBooks(self.books) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeriesLinks(BaseModel):
    """Author value series links attributes."""

    value: _ReadarrAuthorValueSeriesValue | None = None
    isLoaded: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrAuthorValueSeriesValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValueSeries(BaseModel):
    """Author value series attributes."""

    value: list[_ReadarrAuthorValueSeriesValue] | None = None
    isLoaded: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = [_ReadarrAuthorValueSeriesValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrAuthorValueMetadata(BaseModel):
    """Author value metadata attributes."""

    value: _ReadarrMetadataValue | None = None
    isLoaded: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrMetadataValue(self.value) or {}


@dataclass(init=False)
class _ReadarrAuthorValue(BaseModel):
    """Author value attributes."""

    id: int | None = None
    authorMetadataId: int | None = None
    cleanName: str | None = None
    monitored: bool | None = None
    lastInfoSync: str | None = None
    path: str | None = None
    rootFolderPath: str | None = None
    added: str | None = None
    qualityProfileId: int | None = None
    metadataProfileId: int | None = None
    tags: list[int] | None = None
    addOptions: _ReadarrAuthorAddOptions | None = None
    metadata: _ReadarrAuthorValueMetadata | None = None
    qualityProfile: _ReadarrQualityProfile | None = None
    metadataProfile: _ReadarrMetadataProfile | None = None
    books: _ReadarrAuthorValueBooks | None = None
    series: _ReadarrAuthorValueSeries | None = None
    name: str | None = None
    foreignAuthorId: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _ReadarrAuthorAddOptions(self.addOptions) or {}
        self.books = _ReadarrAuthorValueBooks(self.books) or {}
        self.metadata = _ReadarrAuthorValueMetadata(self.metadata) or {}
        self.metadataProfile = _ReadarrMetadataProfile(self.metadataProfile) or {}
        self.qualityProfile = _ReadarrQualityProfile(self.qualityProfile) or {}
        self.series = _ReadarrAuthorValueSeries(self.series) or {}


@dataclass(init=False)
class _ReadarrAuthor(BaseModel):
    """Author attributes."""

    isLoaded: bool | None = None
    value: _ReadarrAuthorValue | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = _ReadarrAuthorValue(self.value) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBook(BaseModel):
    """Editions value book attributes."""

    isLoaded: bool | None = None


@dataclass(init=False)
class _ReadarrQualityRevision(BaseModel):
    """Quality revision attributes attributes."""

    version: int | None = None
    real: int | None = None
    isRepack: bool | None = None


@dataclass(init=False)
class _ReadarrQuality(BaseModel):
    """Quality attributes attributes."""

    quality: _ReadarrIdName | None = None
    revision: _ReadarrQualityRevision | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _ReadarrIdName(self.quality) or {}
        self.revision = _ReadarrQualityRevision(self.revision) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValueMediaInfo(BaseModel):
    """Editions value book files value media info attributes."""

    audioFormat: str | None = None
    audioBitRate: str | None = None
    audioBitrate: str | None = None
    audioChannels: float | None = None
    audioBits: int | None = None
    audioSampleRate: str | None = None
    audioCodec: str | None = None


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValueEdition(BaseModel):
    """Editions value book files value edition attributes."""

    isLoaded: bool | None = None


@dataclass(init=False)
class _ReadarrEditionsValueBookFilesValue(BaseModel):
    """Editions value book files value attributes."""

    id: int | None = None
    path: str | None = None
    size: int | None = None
    modified: str | None = None
    dateAdded: str | None = None
    sceneName: str | None = None
    releaseGroup: str | None = None
    quality: _ReadarrQuality | None = None
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    editionId: int | None = None
    calibreId: int | None = None
    part: int | None = None
    author: _ReadarrAuthor | None = None
    edition: _ReadarrEditionsValueBookFilesValueEdition | None = None
    partCount: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.edition = _ReadarrEditionsValueBookFilesValueEdition(self.edition) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _ReadarrQuality(self.quality) or {}


@dataclass(init=False)
class _ReadarrEditionsValueBookFiles(BaseModel):
    """Editions value book files attributes."""

    isLoaded: bool | None = None
    value: list[_ReadarrEditionsValueBookFilesValue] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = [
            _ReadarrEditionsValueBookFilesValue(item) for item in self.value or []
        ]


@dataclass(init=False)
class _ReadarrEditionsValue(BaseModel):
    """Editions value attributes."""

    id: int | None = None
    bookId: int | None = None
    foreignEditionId: str | None = None
    titleSlug: str | None = None
    isbn13: str | None = None
    asin: str | None = None
    title: str | None = None
    language: str | None = None
    overview: str | None = None
    format: str | None = None
    isEbook: bool | None = None
    disambiguation: str | None = None
    publisher: str | None = None
    pageCount: int | None = None
    releaseDate: str | None = None
    images: list[_ReadarrImage] | None = None
    links: list[_ReadarrLink] | None = None
    ratings: _ReadarrRating | None = None
    monitored: bool | None = None
    manualAdd: bool | None = None
    book: _ReadarrEditionsValueBook | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    remoteCover: str | None = None
    grabbed: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.book = _ReadarrEditionsValueBook(self.book) or {}
        self.bookFiles = _ReadarrEditionsValueBookFiles(self.bookFiles) or {}
        self.images = [_ReadarrImage(image) for image in self.images or []]
        self.links = [_ReadarrLink(link) for link in self.links or []]
        self.ratings = _ReadarrRating(self.ratings) or {}


@dataclass(init=False)
class _ReadarrEditions(BaseModel):
    """Editions attributes."""

    isLoaded: bool | None = None
    value: list[_ReadarrEditionsValue] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = [_ReadarrEditionsValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrSeriesLinksValue(BaseModel):
    """Series links value attributes."""

    id: int | None = None
    position: str | None = None
    seriesId: int | None = None
    bookId: int | None = None
    isPrimary: bool | None = None
    series: _ReadarrAuthorValueSeriesLinks | None = None
    book: _ReadarrEditionsValueBook | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.book = _ReadarrEditionsValueBook(self.book) or {}
        self.series = _ReadarrAuthorValueSeriesLinks(self.series) or {}


@dataclass(init=False)
class _ReadarrSeriesLinks(BaseModel):
    """Series links attributes."""

    isLoaded: bool | None = None
    value: list[_ReadarrSeriesLinksValue] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.value = [_ReadarrSeriesLinksValue(item) for item in self.value or []]


@dataclass(init=False)
class _ReadarrBookCommon(_ReadarrCommon):
    """Book base common attributes."""

    foreignBookId: str | None = None
    title: str | None = None
    releaseDate: str | None = None
    genres: list[str] | None = None
    ratings: _ReadarrRating | None = None
    cleanTitle: str | None = None
    monitored: bool | None = None
    anyEditionOk: bool | None = None
    lastInfoSync: str | None = None
    added: str | None = None
    addOptions: _ReadarrAddOptions | None = None
    authorMetadata: _ReadarrAuthorMetadata | None = None
    bookFiles: _ReadarrEditionsValueBookFiles | None = None
    seriesLinks: _ReadarrSeriesLinks | None = None

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
    """Author statistics attributes."""

    bookFileCount: int | None = None
    bookCount: int | None = None
    availableBookCount: int | None = None
    totalBookCount: int | None = None
    sizeOnDisk: int | None = None
    percentOfBooks: float | None = None


@dataclass(init=False)
class _ReadarrAuthorBook(_ReadarrBookCommon):
    """Author book attributes."""

    author: _ReadarrAuthor | None = None
    editions: _ReadarrEditions | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthor(self.author) or {}
        self.editions = _ReadarrEditions(self.editions) or {}


@dataclass(init=False)
class _ReadarrBlocklistFilter(BaseModel):
    """Blocklist attributes."""

    key: str | None = None
    value: str | None = None


@dataclass(init=False)
class _ReadarrAuthorBase(_ReadarrCommon):
    """Author attributes."""

    status: str | None = None
    ended: bool | None = None
    authorName: str | None = None
    authorNameLastFirst: str | None = None
    foreignAuthorId: str | None = None
    overview: str | None = None
    disambiguation: str | None = None
    nextBook: _ReadarrAuthorBook | None = None
    lastBook: _ReadarrAuthorBook | None = None
    images: list[_ReadarrImage] | None = None
    remotePoster: str | None = None
    path: str | None = None
    qualityProfileId: int | None = None
    metadataProfileId: int | None = None
    monitored: bool | None = None
    monitorNewItems: str | None = None
    rootFolderPath: str | None = None
    genres: list[str] | None = None
    cleanName: str | None = None
    sortName: str | None = None
    sortNameLastFirst: str | None = None
    tags: list[int] | None = None
    added: str | None = None
    addOptions: _ReadarrAuthorAddOptions | None = None
    ratings: _ReadarrRating | None = None
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
class _ReadarrBlocklistRecord(BaseModel):
    """Blocklist record attributes."""

    id: int | None = None
    authorId: int | None = None
    bookIds: list[int] | None = None
    sourceTitle: str | None = None
    quality: _ReadarrQuality | None = None
    date: str | None = None
    protocol: str | None = None
    indexer: str | None = None
    message: str | None = None
    author: _ReadarrAuthorBase | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.author = _ReadarrAuthorBase(self.author) or {}
        self.quality = _ReadarrQuality(self.quality) or {}


@dataclass(init=False)
class _ReadarrCountry(BaseModel):
    """Country attributes."""

    twoLetterCode: str | None = None
    name: str | None = None


@dataclass(init=False)
class _ReadarrDuration(BaseModel):
    """Duration attributes."""

    ticks: int | None = None
    days: int | None = None
    hours: int | None = None
    milliseconds: int | None = None
    minutes: int | None = None
    seconds: int | None = None
    totalDays: int | None = None
    totalHours: int | None = None
    totalMilliseconds: int | None = None
    totalMinutes: int | None = None
    totalSeconds: int | None = None


@dataclass(init=False)
class _ReadarrAudioTags(BaseModel):
    """Audio tags attributes."""

    title: str | None = None
    cleanTitle: str | None = None
    authors: list[str] | None = None
    authorTitle: str | None = None
    bookTitle: str | None = None
    seriesTitle: str | None = None
    seriesIndex: str | None = None
    isbn: str | None = None
    asin: str | None = None
    goodreadsId: str | None = None
    authorMBId: str | None = None
    bookMBId: str | None = None
    releaseMBId: str | None = None
    recordingMBId: str | None = None
    trackMBId: str | None = None
    discNumber: int | None = None
    discCount: int | None = None
    country: _ReadarrCountry | None = None
    year: int | None = None
    publisher: str | None = None
    label: str | None = None
    source: str | None = None
    catalogNumber: str | None = None
    disambiguation: str | None = None
    duration: _ReadarrDuration | None = None
    quality: _ReadarrQuality | None = None
    mediaInfo: _ReadarrEditionsValueBookFilesValueMediaInfo | None = None
    trackNumbers: list[int] | None = None
    language: str | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.country = _ReadarrCountry(self.country) or {}
        self.duration = _ReadarrDuration(self.duration) or {}
        self.mediaInfo = (
            _ReadarrEditionsValueBookFilesValueMediaInfo(self.mediaInfo) or {}
        )
        self.quality = _ReadarrQuality(self.quality) or {}


@dataclass(init=False)
class _ReadarrBookFileMediaInfo(_ReadarrEditionsValueBookFilesValueMediaInfo):
    """Book file media info attributes."""

    id: int | None = None


@dataclass(init=False)
class _ReadarrCommandBody(BaseModel):
    """Command body attributes."""

    sendUpdatesToClient: bool | None = None
    updateScheduledTask: bool | None = None
    completionMessage: str | None = None
    requiresDiskAccess: bool | None = None
    isExclusive: bool | None = None
    isTypeExclusive: bool | None = None
    name: str | None = None
    lastExecutionTime: str | None = None
    lastStartTime: str | None = None
    trigger: str | None = None
    suppressMessages: bool | None = None
    clientUserAgent: str | None = None
