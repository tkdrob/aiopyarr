"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from .base import BaseModel
from .radarr_common import (
    _RadarrCommon,
    _RadarrCommon2,
    _RadarrCustomFormats,
    _RadarrMovie,
    _RadarrMovieCustomFormats,
    _RadarrMovieFile,
    _RadarrMovieHistoryBlocklistBase,
    _RadarrMovieHistoryData,
    _RadarrNotificationMessage,
    _RadarrParsedMovieInfo,
)
from .request_common import (
    _Common2,
    _Common3,
    _Common4,
    _Common7,
    _Common8,
    _Editor,
    _ImportListCommon,
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


class RadarrEventType(str, Enum):
    """Radarr event types."""

    DELETED = "movieFileDeleted"
    DOWNLOAD_FAILED = "downloadFailed"
    GRABBED = "grabbed"
    IMPORTED = "downloadFolderImported"
    UNKNOWN = "unknown"


class RadarrSortKeys(str, Enum):
    """Radarr sort keys."""

    DATE = "date"
    ID = "id"
    INDEXER = "indexer"
    MESSAGE = "message"
    MOVIE_ID = "movieid"
    PATH = "path"
    QUALITY = "quality"
    RATINGS = "ratings"
    SOURCE_TITLE = "sourcetitle"
    TIMELEFT = "timeleft"
    TITLE = "title"


@dataclass(init=False)
class RadarrMovieFile(_RadarrMovieFile):
    """Radarr movie file attributes."""


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
class Diskspace(BaseModel):
    """Radarr diskspace attributes."""

    freeSpace: int | None = None
    label: str | None = None
    path: str | None = None
    totalSpace: int | None = None


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
class RadarrCalendar(_RadarrMovie, _RadarrCommon2):
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
class RadarrMovie(_RadarrMovie):
    """Movie attributes."""


@dataclass(init=False)
class RadarrParse(BaseModel):
    """Radarr parse attributes."""

    movie: _RadarrMovie | None = None
    parsedMovieInfo: _RadarrParsedMovieInfo | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.movie = _RadarrMovie(self.movie) or {}
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
