"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

import attr

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

    dateAdded: datetime = attr.ib(type=datetime)
    edition: str = attr.ib(type=str)
    indexerFlags: int = attr.ib(type=int)
    mediaInfo: _RadarrMovieFileMediaInfo = attr.ib(type=_RadarrMovieFileMediaInfo)
    movieId: int = attr.ib(type=int)
    originalFilePath: str = attr.ib(type=str)
    path: str = attr.ib(type=str)
    qualityCutoffNotMet: bool = attr.ib(type=bool)
    relativePath: str = attr.ib(type=str)
    sceneName: str = attr.ib(type=str)
    size: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _RadarrMovieFileMediaInfo(self.mediaInfo) or {}


@dataclass(init=False)
class RadarrMovieHistory(_RadarrMovieHistoryBlocklistBase, _Common2):
    """Radarr movie history attributes."""

    data: _RadarrMovieHistoryData = attr.ib(type=_RadarrMovieHistoryData)
    qualityCutoffNotMet: bool = attr.ib(type=bool)

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
    errorMessage: str = attr.ib(type=str)
    languages: list[_Common3] | None = None
    movieId: int = attr.ib(type=int)

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

    enableAuto: bool = attr.ib(type=bool)
    enabled: bool = attr.ib(type=bool)
    listType: str = attr.ib(type=str)
    searchOnAdd: bool = attr.ib(type=bool)
    shouldMonitor: bool = attr.ib(type=bool)
    tags: list[int] = attr.ib(type="list[int]")


@dataclass(init=False)
class RadarrNotification(_Common3, _Notification):
    """Radarr notification attributes."""

    fields: list[_MetadataFields] | None = None
    message: _RadarrNotificationMessage = attr.ib(type=_RadarrNotificationMessage)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.fields = [_MetadataFields(field) for field in self.fields or []]
        self.message = _RadarrNotificationMessage(self.message) or {}


@dataclass(init=False)
class RadarrTagDetails(_TagDetails):
    """Radarr tag details attributes."""

    indexerIds: list[int] = attr.ib(type="list[int]")
    movieIds: list[int] = attr.ib(type="list[int]")


@dataclass(init=False)
class RadarrNamingConfig(BaseModel):
    """Radarr host naming config attributes."""

    colonReplacementFormat: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    includeQuality: bool = attr.ib(type=bool)
    movieFolderFormat: str = attr.ib(type=str)
    renameMovies: bool = attr.ib(type=bool)
    replaceIllegalCharacters: bool = attr.ib(type=bool)
    replaceSpaces: bool = attr.ib(type=bool)
    standardMovieFormat: str = attr.ib(type=str)


@dataclass(init=False)
class RadarrMovie(_RadarrCommon2, _RadarrCommon3, _Common6):
    """Radarr movie attributes."""

    added: datetime = attr.ib(type=datetime)
    alternateTitles: list[_RadarrMovieAlternateTitle] | None = None
    cleanTitle: str = attr.ib(type=str)
    folderName: str = attr.ib(type=str)
    hasFile: bool = attr.ib(type=bool)
    isAvailable: bool = attr.ib(type=bool)
    movieFile: RadarrMovieFile = attr.ib(type=RadarrMovieFile)
    originalTitle: str = attr.ib(type=str)
    path: str = attr.ib(type=str)
    rootFolderPath: str = attr.ib(type=str)
    secondaryYearSourceId: int = attr.ib(type=int)
    sizeOnDisk: int = attr.ib(type=int)
    tags: list[int] = attr.ib(type="list[int]")
    titleSlug: int = attr.ib(type=int)

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

    folder: str = attr.ib(type=str)
    isExcluded: bool = attr.ib(type=bool)
    isExisting: bool = attr.ib(type=bool)
    isRecommendation: bool = attr.ib(type=bool)
    lists: list[int] = attr.ib(type="list[int]")
    overview: str = attr.ib(type=str)
    remotePoster: str = attr.ib(type=str)


@dataclass(init=False)
class RadarrCalendar(RadarrMovie, _RadarrCommon2):
    """Radarr calendar attributes."""

    digitalRelease: datetime = attr.ib(type=datetime)
    minimumAvailability: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    secondaryYearSourceId: int = attr.ib(type=int)


@dataclass(init=False)
class RadarrMovieEditor(_Editor):
    """Radarr root folder attributes."""

    movieIds: list[int] = attr.ib(type="list[int]")


@dataclass(init=False)
class RadarrParse(BaseModel):
    """Radarr parse attributes."""

    movie: RadarrMovie = attr.ib(type=RadarrMovie)
    parsedMovieInfo: _RadarrParsedMovieInfo = attr.ib(type=_RadarrParsedMovieInfo)
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.movie = RadarrMovie(self.movie) or {}
        self.parsedMovieInfo = _RadarrParsedMovieInfo(self.parsedMovieInfo) or {}


@dataclass(init=False)
class RadarrRelease(_ReleaseCommon):
    """Radarr release attributes."""

    customFormats: list[_RadarrCustomFormats] | None = None
    customFormatScore: int = attr.ib(type=int)
    edition: str = attr.ib(type=str)
    imdbId: int = attr.ib(type=int)
    indexerFlags: list[str] = attr.ib(type="list[str]")
    languages: list[_Common3] | None = None
    movieTitles: list[str] = attr.ib(type="list[str]")
    quality: _Quality = attr.ib(type=_Quality)
    releaseGroup: str = attr.ib(type=str)
    releaseHash: str = attr.ib(type=str)
    tmdbId: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.customFormats = [_RadarrCustomFormats(x) for x in self.customFormats or []]
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class RadarrRename(_Rename):
    """Radarr rename attributes."""

    movieFileId: int = attr.ib(type=int)
    movieId: int = attr.ib(type=int)


@dataclass(init=False)
class RadarrManualImport(_ManualImport):
    """Radarr manual import attributes."""

    folderName: str = attr.ib(type=str)
    languages: list[_Common3] | None = None
    movie: RadarrMovie = attr.ib(type=RadarrMovie)
    relativePath: str = attr.ib(type=str)
    releaseGroup: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.languages = [_Common3(x) for x in self.languages or []]
        self.movie = RadarrMovie(self.movie) or {}


@dataclass(init=False)
class RadarrExtraFile(BaseModel):
    """Radarr extra file attributes."""

    extension: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    movieFileId: int = attr.ib(type=int)
    movieId: int = attr.ib(type=int)
    relativePath: str = attr.ib(type=str)
    type: str = attr.ib(type=str)


@dataclass(init=False)
class RadarrIndexerFlag(Language):
    """Radarr indexer flag attributes."""


@dataclass(init=False)
class RadarrRestriction(BaseModel):
    """Radarr restriction attributes."""

    id: int = attr.ib(type=int)
    ignored: str = attr.ib(type=str)
    required: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type="list[int]")


@dataclass(init=False)
class RadarrCredit(BaseModel):
    """Radarr credit attributes."""

    personName: str = attr.ib(type=str)
    creditTmdbId: str = attr.ib(type=str)
    personTmdbId: int = attr.ib(type=int)
    movieId: int = attr.ib(type=int)
    images: list[_Common5] | None = None
    character: str = attr.ib(type=str)
    order: int = attr.ib(type=int)
    type: str = attr.ib(type=str)
    id: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_Common5(image) for image in self.images or []]


@dataclass(init=False)
class RadarrAltTitle(BaseModel):
    """Radarr alternate title attributes."""

    sourceType: str = attr.ib(type=str)
    movieId: int = attr.ib(type=int)
    title: str = attr.ib(type=str)
    sourceId: int = attr.ib(type=int)
    votes: int = attr.ib(type=int)
    voteCount: int = attr.ib(type=int)
    language: _Common3 = attr.ib(type=_Common3)
    id: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language) or {}
