"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
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

    dateAdded: datetime | None = None
    edition: str | None = None
    indexerFlags: int | None = None
    mediaInfo: _RadarrMovieFileMediaInfo | None = None
    movieId: int | None = None
    originalFilePath: str | None = None
    path: str | None = None
    qualityCutoffNotMet: bool | None = None
    relativePath: str | None = None
    sceneName: str | None = None
    size: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _RadarrMovieFileMediaInfo(self.mediaInfo) or {}


@dataclass(init=False)
class RadarrMovieHistory(_RadarrMovieHistoryBlocklistBase, _Common2):
    """Radarr movie history attributes."""

    data: _RadarrMovieHistoryData | None = None
    qualityCutoffNotMet: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _RadarrMovieHistoryData(self.data) or {}


@dataclass(init=False)
class RadarrHistory(_RecordCommon):
    """Radarr history attributes."""

    records: list[RadarrMovieHistory] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [RadarrMovieHistory(record) for record in self.records or []]


@dataclass(init=False)
class RadarrBlocklistMovie(_Common7, _RadarrMovieHistoryBlocklistBase):
    """Radarr blocklist movie attributes."""


@dataclass(init=False)
class RadarrBlocklist(_RecordCommon):
    """Radarr blocklist attributes."""

    records: list[RadarrBlocklistMovie] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [RadarrBlocklistMovie(record) for record in self.records or []]


@dataclass(init=False)
class RadarrQueueDetail(_Common4, _Common8):
    """Radarr queue details attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    errorMessage: str | None = None
    languages: list[_Common3] | None = None
    movieId: int | None = None

    def __post_init__(self):
        """Post init."""
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]
        self.languages = [_Common3(language) for language in self.languages or []]
        self.statusMessages = [
            _StatusMessage(statMsg) for statMsg in self.statusMessages or []
        ]
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class RadarrQueue(_RecordCommon):
    """Radarr queue attributes."""

    records: list[RadarrQueueDetail] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [RadarrQueueDetail(record) for record in self.records or []]


@dataclass(init=False)
class RadarrImportList(_ImportListCommon, _RadarrCommon, _RadarrCommon2):
    """Radarr import attributes."""

    enableAuto: bool | None = None
    enabled: bool | None = None
    listType: str | None = None
    searchOnAdd: bool | None = None
    shouldMonitor: bool | None = None
    tags: list[int | None] | None = None


@dataclass(init=False)
class RadarrNotification(_Common3, _Notification):
    """Radarr notification attributes."""

    fields: list[_MetadataFields] | None = None
    message: _RadarrNotificationMessage | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.fields = [_MetadataFields(field) for field in self.fields or []]
        self.message = _RadarrNotificationMessage(self.message) or {}


@dataclass(init=False)
class RadarrTagDetails(_TagDetails):
    """Radarr tag details attributes."""

    indexerIds: list[int] | None = None
    movieIds: list[int] | None = None


@dataclass(init=False)
class RadarrNamingConfig(BaseModel):
    """Radarr host naming config attributes."""

    colonReplacementFormat: str | None = None
    id: int | None = None
    includeQuality: bool | None = None
    movieFolderFormat: str | None = None
    renameMovies: bool | None = None
    replaceIllegalCharacters: bool | None = None
    replaceSpaces: bool | None = None
    standardMovieFormat: str | None = None


@dataclass(init=False)
class RadarrMovie(_RadarrCommon2, _RadarrCommon3, _Common6):
    """Radarr movie attributes."""

    added: datetime | None = None
    alternateTitles: list[_RadarrMovieAlternateTitle] | None = None
    cleanTitle: str | None = None
    folderName: str | None = None
    hasFile: bool | None = None
    isAvailable: bool | None = None
    movieFile: RadarrMovieFile | None = None
    originalTitle: str | None = None
    path: str | None = None
    rootFolderPath: str | None = None
    secondaryYearSourceId: int | None = None
    sizeOnDisk: int | None = None
    tags: list[int | None] | None = None
    titleSlug: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _RadarrMovieAlternateTitle(alternateTitle)
            for alternateTitle in self.alternateTitles or []
        ]
        self.movieFile = RadarrMovieFile(self.movieFile) or {}


@dataclass(init=False)
class RadarrImportListMovie(_RadarrCommon3):
    """Radarr import list movie attributes."""

    folder: str | None = None
    isExcluded: bool | None = None
    isExisting: bool | None = None
    isRecommendation: bool | None = None
    lists: list[int] | None = None
    overview: str | None = None
    remotePoster: str | None = None


@dataclass(init=False)
class RadarrCalendar(RadarrMovie, _RadarrCommon2):
    """Radarr calendar attributes."""

    digitalRelease: datetime | None = None
    minimumAvailability: str | None = None
    qualityProfileId: int | None = None
    secondaryYearSourceId: int | None = None


@dataclass(init=False)
class RadarrMovieEditor(_Editor):
    """Radarr root folder attributes."""

    movieIds: list[int] | None = None


@dataclass(init=False)
class RadarrParse(BaseModel):
    """Radarr parse attributes."""

    movie: RadarrMovie | None = None
    parsedMovieInfo: _RadarrParsedMovieInfo | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.movie = RadarrMovie(self.movie) or {}
        self.parsedMovieInfo = _RadarrParsedMovieInfo(self.parsedMovieInfo) or {}


@dataclass(init=False)
class RadarrRelease(_ReleaseCommon):
    """Radarr release attributes."""

    customFormats: list[_RadarrCustomFormats] | None = None
    customFormatScore: int | None = None
    edition: str | None = None
    imdbId: int | None = None
    indexerFlags: list[str] | None = None
    languages: list[_Common3] | None = None
    movieTitles: list[str] | None = None
    quality: _Quality | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    tmdbId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.customFormats = [_RadarrCustomFormats(x) for x in self.customFormats or []]
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class RadarrRename(_Rename):
    """Radarr rename attributes."""

    movieFileId: int | None = None
    movieId: int | None = None


@dataclass(init=False)
class RadarrManualImport(_ManualImport):
    """Radarr manual import attributes."""

    folderName: str | None = None
    languages: list[_Common3] | None = None
    movie: RadarrMovie | None = None
    relativePath: str | None = None
    releaseGroup: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.languages = [_Common3(x) for x in self.languages or []]
        self.movie = RadarrMovie(self.movie) or {}


@dataclass(init=False)
class RadarrExtraFile(BaseModel):
    """Radarr extra file attributes."""

    extension: str | None = None
    id: int | None = None
    movieFileId: int | None = None
    movieId: int | None = None
    relativePath: str | None = None
    type: str | None = None


@dataclass(init=False)
class RadarrIndexerFlag(Language):
    """Radarr indexer flag attributes."""


@dataclass(init=False)
class RadarrRestriction(BaseModel):
    """Radarr restriction attributes."""

    id: int | None = None
    ignored: str | None = None
    required: str | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrCredit(BaseModel):
    """Radarr credit attributes."""

    personName: str | None = None
    creditTmdbId: str | None = None
    personTmdbId: int | None = None
    movieId: int | None = None
    images: list[_Common5] | None = None
    character: str | None = None
    order: int | None = None
    type: str | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_Common5(image) for image in self.images or []]


@dataclass(init=False)
class RadarrAltTitle(BaseModel):
    """Radarr alternate title attributes."""

    sourceType: str | None = None
    movieId: int | None = None
    title: str | None = None
    sourceId: int | None = None
    votes: int | None = None
    voteCount: int | None = None
    language: _Common3 | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language) or {}
