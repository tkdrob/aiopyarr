"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel
from .common import Tag, _RecordCommon

from .radarr_common import (  # isort:skip
    _RadarrCalendarMovieFile,
    _RadarrCommon,
    _RadarrCommon2,
    _RadarrCommon4,
    _RadarrMovieCustomFormats,
    _RadarrMovie,
    _RadarrMovieFileCommon,
    _RadarrMovieHistoryBlocklistBase,
    _RadarrMovieHistoryData,
    _RadarrMovieQuality,
    _RadarrNotificationMessage,
    _RadarrQualityProfileItems,
    _RadarrQueueStatusMessages,
    _RadarrUpdateChanges,
)


@dataclass(init=False)
class RadarrMovieFile(_RadarrMovieFileCommon):
    """Movie file attributes."""


@dataclass(init=False)
class RadarrMovieHistory(_RadarrMovieHistoryBlocklistBase):
    """Movie file quality attributes."""

    data: _RadarrMovieHistoryData | None = None
    downloadId: str | None = None
    eventType: str | None = None
    qualityCutoffNotMet: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _RadarrMovieHistoryData(self.data) or {}


@dataclass(init=False)
class RadarrBlocklistMovie(_RadarrMovieHistoryBlocklistBase):
    """Blocklist movie attributes."""

    indexer: str | None = None
    protocol: str | None = None


@dataclass(init=False)
class RadarrBlocklist(_RecordCommon):
    """Blocklist attributes."""

    records: list[RadarrBlocklistMovie] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [RadarrBlocklistMovie(record) for record in self.records or []]


@dataclass(init=False)
class RadarrQueueDetail(BaseModel):
    """Radarr queue details attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    downloadClient: str | None = None
    downloadId: str | None = None
    errorMessage: str | None = None
    estimatedCompletionTime: str | None = None
    id: int | None = None
    indexer: str | None = None
    languages: list[_RadarrCommon4] | None = None
    movieId: int | None = None
    outputPath: str | None = None
    protocol: str | None = None
    quality: _RadarrMovieQuality | None = None
    size: int | None = None
    sizeleft: int | None = None
    status: str | None = None
    statusMessages: list[_RadarrQueueStatusMessages] | None = None
    timeleft: str | None = None
    title: str | None = None
    trackedDownloadStatus: str | None = None
    trackedDownloadState: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]
        self.languages = [_RadarrCommon4(language) for language in self.languages or []]
        self.statusMessages = [
            _RadarrQueueStatusMessages(statMsg) for statMsg in self.statusMessages or []
        ]
        self.quality = _RadarrMovieQuality(self.quality) or {}


@dataclass(init=False)
class RadarrQueue(_RecordCommon):
    """Radarr queue attributes."""

    records: list[RadarrQueueDetail] | None = None


@dataclass(init=False)
class RadarrQueueStatus(BaseModel):
    """Radarr queue status attributes."""

    totalCount: int | None = None
    count: int | None = None
    unknownCount: int | None = None
    errors: bool | None = None
    warnings: bool | None = None
    unknownErrors: bool | None = None
    unknownWarnings: bool | None = None


@dataclass(init=False)
class RadarrIndexer(_RadarrCommon):
    """Radarr indexers attributes."""

    configContract: str | None = None
    enableAutomaticSearch: bool | None = None
    enableInteractiveSearch: bool | None = None
    enableRss: bool | None = None
    id: int | None = None
    protocol: str | None = None
    priority: int | None = None
    supportsRss: bool | None = None
    supportsSearch: bool | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrDownloadClient(_RadarrCommon):
    """Radarr indexers attributes."""

    configContract: str | None = None
    enable: bool | None = None
    id: int | None = None
    priority: int | None = None
    protocol: str | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrImportList(_RadarrCommon, _RadarrCommon2):
    """Radarr import attributes."""

    configContract: str | None = None
    enableAuto: bool | None = None
    enabled: bool | None = None
    listOrder: int | None = None
    listType: str | None = None
    rootFolderPath: str | None = None
    searchOnAdd: bool | None = None
    shouldMonitor: bool | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrNotification(_RadarrCommon):
    """Radarr notification attributes."""

    configContract: str | None = None
    id: int | None = None
    includeHealthWarnings: bool | None = None
    message: _RadarrNotificationMessage | None = None
    onDelete: bool | None = None
    onDownload: bool | None = None
    onGrab: bool | None = None
    onHealthIssue: bool | None = None
    onRename: bool | None = None
    onUpgrade: bool | None = None
    supportsOnDelete: bool | None = None
    supportsOnDownload: bool | None = None
    supportsOnGrab: bool | None = None
    supportsOnHealthIssue: bool | None = None
    supportsOnRename: bool | None = None
    supportsOnUpgrade: bool | None = None
    tags: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.message = _RadarrNotificationMessage(self.message) or {}


@dataclass(init=False)
class RadarrTagDetails(Tag):
    """Radarr tag details attributes."""

    delayProfileIds: list[int] | None = None
    notificationIds: list[int] | None = None
    restrictionIds: list[int] | None = None
    netImportIds: list[int] | None = None
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
class RadarrMetadataConfig(_RadarrCommon, BaseModel):
    """Radarr metadata consumer config attributes."""

    configContract: str | None = None
    enable: bool | None = None
    id: int | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrHealth(BaseModel):
    """Radarr failed health check attributes."""

    message: str | None = None
    source: str | None = None
    type: str | None = None
    wikiUrl: str | None = None


@dataclass(init=False)
class RadarrUpdate(BaseModel):
    """Radarr recent updates attributes."""

    branch: str | None = None
    changes: _RadarrUpdateChanges | None = None
    fileName: str | None = None
    hash: str | None = None
    installable: bool | None = None
    installed: bool | None = None
    latest: bool | None = None
    releaseDate: str | None = None
    url: str | None = None
    version: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.changes = _RadarrUpdateChanges(self.changes) or {}


@dataclass(init=False)
class RadarrQualityProfile(_RadarrCommon4):
    """Radarr quality profile attributes."""

    cutoff: int | None = None
    cutoffFormatScore: int | None = None
    formatItems: list | None = None
    items: list[_RadarrQualityProfileItems] | None = None
    language: _RadarrCommon4 | None = None
    minFormatScore: int | None = None
    upgradeAllowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.items = [_RadarrQualityProfileItems(item) for item in self.items or []]
        self.language = _RadarrCommon4(self.language) or {}


@dataclass(init=False)
class RadarrCalendar(_RadarrMovie, _RadarrCommon2):
    """Radarr calendar attributes."""

    digitalRelease: str | None = None
    minimumAvailability: str | None = None
    movieFile: _RadarrCalendarMovieFile | None = None
    qualityProfileId: int | None = None
    secondaryYearSourceId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        if isinstance(self.images, list):
            self.movieFile = _RadarrCalendarMovieFile(self.movieFile) or {}


@dataclass(init=False)
class RadarrRemotePathMapping(BaseModel):
    """Radarr remote path mapping attributes."""

    id: int | None = None
    host: str | None = None
    localPath: str | None = None
    remotePath: str | None = None


@dataclass(init=False)
class RadarrMovieEditor(BaseModel):
    """Radarr root folder attributes."""

    applyTags: str | None = None
    minimumAvailability: str | None = None
    monitored: bool | None = None
    moveFiles: bool | None = None
    movieIds: list[int] | None = None
    qualityProfileId: int | None = None
    rootFolderPath: str | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class RadarrMovie(_RadarrMovie):
    """Movie attributes."""

    movieFile: RadarrMovieFile | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.movieFile = RadarrMovieFile(self.movieFile) or {}
