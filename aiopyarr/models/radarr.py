"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from ..const import DATE, MOVIE_ID, PATH, TITLE
from .base import BaseModel
from .radarr_common import (
    _RadarrCommon,
    _RadarrCommon2,
    _RadarrCommon3,
    _RadarrCustomFormats,
    _RadarrMovieAlternateTitle,
    _RadarrMovieCommon,
    _RadarrMovieCustomFormats,
    _RadarrMovieFileMediaInfo,
    _RadarrMovieHistoryBlocklistBase,
    _RadarrMovieHistoryData,
    _RadarrNotificationMessage,
    _RadarrParsedMovieInfo,
)
from .request import Language
from .request_common import (
    _Common2,
    _Common3,
    _Common4,
    _Common5,
    _Common6,
    _Common7,
    _Common8,
    _Editor,
    _ImportListCommon,
    _ManualImport,
    _MetadataFields,
    _Notification,
    _Quality,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _StatusMessage,
    _TagDetails,
)


class RadarrCommands(str, Enum):
    """Radarr commands."""

    DOWNLOADED_MOVIES_SCAN = "DownloadedMoviesScan"
    MISSING_MOVIES_SEARCH = "MissingMoviesSearch"
    REFRESH_MOVIE = "RefreshMovie"
    RENAME_MOVIE = "RenameMovie"
    RESCAN_MOVIE = "RescanMovie"


class RadarrEventType(Enum):
    """Radarr event types."""

    DELETED = 6
    FAILED = 4
    GRABBED = 1
    IGNORED = 9
    IMPORTED = 3
    RENAMED = 8


class RadarrImportListActionType(str, Enum):
    """Radarr import list action types."""

    GET_PROFILES = "getProfiles"
    GET_TAGS = "getTags"


class RadarrSortKeys(str, Enum):
    """Radarr sort keys."""

    DATE = DATE
    DOWNLOAD_CLIENT = "downloadClient"
    ID = "id"
    INDEXER = "indexer"
    LANGUAGES = "languages"
    MESSAGE = "message"
    MOVIE_ID = MOVIE_ID
    MOVIE_TITLE = "movies.sortTitle"
    PATH = PATH
    PROGRESS = "progress"
    PROTOCOL = "protocol"
    QUALITY = "quality"
    RATINGS = "ratings"
    RELEASE_TITLE = TITLE
    SIZE = "size"
    SOURCE_TITLE = "sourcetitle"
    STATUS = "status"
    TIMELEFT = "timeleft"


@dataclass(init=False)
class RadarrMovieFile(_RadarrMovieCommon):
    """Radarr movie file attributes."""

    dateAdded: datetime
    edition: str
    indexerFlags: int
    mediaInfo: type[_RadarrMovieFileMediaInfo] = field(
        default=_RadarrMovieFileMediaInfo
    )
    movieId: int
    originalFilePath: str
    path: str
    qualityCutoffNotMet: bool
    relativePath: str
    sceneName: str
    size: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _RadarrMovieFileMediaInfo(self.mediaInfo)


@dataclass(init=False)
class RadarrMovieHistory(_RadarrMovieHistoryBlocklistBase, _Common2):
    """Radarr movie history attributes."""

    data: type[_RadarrMovieHistoryData] = field(default=_RadarrMovieHistoryData)
    qualityCutoffNotMet: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _RadarrMovieHistoryData(self.data)


@dataclass(init=False)
class RadarrHistory(_RecordCommon):
    """Radarr history attributes."""

    records: list[RadarrMovieHistory] = field(default_factory=list[RadarrMovieHistory])

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [RadarrMovieHistory(record) for record in self.records]


@dataclass(init=False)
class RadarrBlocklistMovie(_Common7, _RadarrMovieHistoryBlocklistBase):
    """Radarr blocklist movie attributes."""


@dataclass(init=False)
class RadarrBlocklist(_RecordCommon):
    """Radarr blocklist attributes."""

    records: list[RadarrBlocklistMovie] = field(
        default_factory=list[RadarrBlocklistMovie]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [RadarrBlocklistMovie(record) for record in self.records]


@dataclass(init=False)
class RadarrQueueDetail(_Common4, _Common8):
    """Radarr queue details attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    errorMessage: str
    languages: list[_Common3] | None = None
    movieId: int

    def __post_init__(self):
        """Post init."""
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]
        self.languages = [_Common3(language) for language in self.languages or []]
        self.statusMessages = [
            _StatusMessage(statMsg) for statMsg in self.statusMessages or []
        ]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class RadarrQueue(_RecordCommon):
    """Radarr queue attributes."""

    records: list[RadarrQueueDetail] = field(default_factory=list[RadarrQueueDetail])

    def __post_init__(self):
        """Post init."""
        self.records = [RadarrQueueDetail(record) for record in self.records]


@dataclass(init=False)
class RadarrImportList(_ImportListCommon, _RadarrCommon, _RadarrCommon2):
    """Radarr import attributes."""

    enableAuto: bool
    enabled: bool
    listType: str
    searchOnAdd: bool
    shouldMonitor: bool
    tags: list[int]


@dataclass(init=False)
class RadarrNotification(_Common3, _Notification):
    """Radarr notification attributes."""

    fields: list[_MetadataFields] | None = None
    message: type[_RadarrNotificationMessage] = field(
        default=_RadarrNotificationMessage
    )

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.fields = [_MetadataFields(field) for field in self.fields or []]
        self.message = _RadarrNotificationMessage(self.message)


@dataclass(init=False)
class RadarrTagDetails(_TagDetails):
    """Radarr tag details attributes."""

    indexerIds: list[int]
    movieIds: list[int]


@dataclass(init=False)
class RadarrNamingConfig(BaseModel):
    """Radarr host naming config attributes."""

    colonReplacementFormat: str
    id: int
    includeQuality: bool
    movieFolderFormat: str
    renameMovies: bool
    replaceIllegalCharacters: bool
    replaceSpaces: bool
    standardMovieFormat: str


@dataclass(init=False)
class RadarrMovie(_RadarrCommon2, _RadarrCommon3, _Common6):
    """Radarr movie attributes."""

    added: datetime
    alternateTitles: list[_RadarrMovieAlternateTitle] | None = None
    cleanTitle: str
    folderName: str
    hasFile: bool
    isAvailable: bool
    movieFile: type[RadarrMovieFile] = field(default=RadarrMovieFile)
    originalTitle: str
    path: str
    rootFolderPath: str
    secondaryYearSourceId: int
    sizeOnDisk: int
    tags: list[int]
    titleSlug: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _RadarrMovieAlternateTitle(alternateTitle)
            for alternateTitle in self.alternateTitles or []
        ]
        self.movieFile = RadarrMovieFile(self.movieFile)


@dataclass(init=False)
class RadarrImportListMovie(_RadarrCommon3):
    """Radarr import list movie attributes."""

    folder: str
    isExcluded: bool
    isExisting: bool
    isRecommendation: bool
    lists: list[int]
    overview: str
    remotePoster: str


@dataclass(init=False)
class RadarrCalendar(RadarrMovie, _RadarrCommon2):
    """Radarr calendar attributes."""

    digitalRelease: datetime
    minimumAvailability: str
    qualityProfileId: int
    secondaryYearSourceId: int


@dataclass(init=False)
class RadarrMovieEditor(_Editor):
    """Radarr root folder attributes."""

    movieIds: list[int]


@dataclass(init=False)
class RadarrParse(BaseModel):
    """Radarr parse attributes."""

    movie: type[RadarrMovie] = field(default=RadarrMovie)
    parsedMovieInfo: type[_RadarrParsedMovieInfo] = field(
        default=_RadarrParsedMovieInfo
    )
    title: str

    def __post_init__(self):
        """Post init."""
        self.movie = RadarrMovie(self.movie)
        self.parsedMovieInfo = _RadarrParsedMovieInfo(self.parsedMovieInfo)


@dataclass(init=False)
class RadarrRelease(_ReleaseCommon):
    """Radarr release attributes."""

    customFormats: list[_RadarrCustomFormats] | None = None
    customFormatScore: int
    edition: str
    imdbId: int
    indexerFlags: list[str]
    languages: list[_Common3] | None = None
    movieTitles: list[str]
    quality: type[_Quality] = field(default=_Quality)
    releaseGroup: str
    releaseHash: str
    tmdbId: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.customFormats = [_RadarrCustomFormats(x) for x in self.customFormats or []]
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class RadarrRename(_Rename):
    """Radarr rename attributes."""

    movieFileId: int
    movieId: int


@dataclass(init=False)
class RadarrManualImport(_ManualImport):
    """Radarr manual import attributes."""

    folderName: str
    languages: list[_Common3] | None = None
    movie: type[RadarrMovie] = field(default=RadarrMovie)
    relativePath: str
    releaseGroup: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.languages = [_Common3(x) for x in self.languages or []]
        self.movie = RadarrMovie(self.movie)


@dataclass(init=False)
class RadarrExtraFile(BaseModel):
    """Radarr extra file attributes."""

    extension: str
    id: int
    movieFileId: int
    movieId: int
    relativePath: str
    type: str


@dataclass(init=False)
class RadarrIndexerFlag(Language):
    """Radarr indexer flag attributes."""


@dataclass(init=False)
class RadarrRestriction(BaseModel):
    """Radarr restriction attributes."""

    id: int
    ignored: str
    required: str
    tags: list[int]


@dataclass(init=False)
class RadarrCredit(BaseModel):
    """Radarr credit attributes."""

    personName: str
    creditTmdbId: str
    personTmdbId: int
    movieId: int
    images: list[_Common5] | None = None
    character: str
    order: int
    type: str
    id: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_Common5(image) for image in self.images or []]


@dataclass(init=False)
class RadarrAltTitle(BaseModel):
    """Radarr alternate title attributes."""

    sourceType: str
    movieId: int
    title: str
    sourceId: int
    votes: int
    voteCount: int
    language: type[_Common3] = field(default=_Common3)
    id: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language)
