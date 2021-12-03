"""Radarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel

from .radarr_common import (  # isort:skip
    _RadarrCalendarMovieFile,
    _RadarrCommandBody,
    _RadarrCommon,
    _RadarrCommon2,
    _RadarrCommon4,
    _RadarrCustomFilterAttr,
    _RadarrMovieCustomFormats,
    _RadarrMovie,
    _RadarrMovieFileCommon,
    _RadarrMovieHistoryBlocklistBase,
    _RadarrMovieHistoryData,
    _RadarrMovieQuality,
    _RadarrNotificationMessage,
    _RadarrQualityProfileItems,
    _RadarrQueueStatusMessages,
    _RadarrUnmappedRootFolder,
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
class RadarrBlocklist(BaseModel):
    """Blocklist attributes."""

    page: int | None = None
    pageSize: int | None = None
    records: list[RadarrBlocklistMovie] | None = None
    sortDirection: str | None = None
    sortKey: str | None = None
    totalRecords: int | None = None

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
class RadarrQueue(BaseModel):
    """Radarr queue attributes."""

    page: int | None = None
    pageSize: int | None = None
    sortKey: str | None = None
    sortDirection: str | None = None
    totalRecords: int | None = None
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
class RadarrTag(BaseModel):
    """Radarr tag attributes."""

    id: int | None = None
    label: str | None = None


@dataclass(init=False)
class RadarrTagDetails(RadarrTag):
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
class RadarrUIConfig(BaseModel):
    """Radarr UI config attributes."""

    calendarWeekColumnHeader: str | None = None
    enableColorImpairedMode: bool | None = None
    firstDayOfWeek: int | None = None
    id: int | None = None
    longDateFormat: str | None = None
    movieInfoLanguage: int | None = None
    movieRuntimeFormat: str | None = None
    shortDateFormat: str | None = None
    showRelativeDates: bool | None = None
    timeFormat: str | None = None


@dataclass(init=False)
class RadarrHostConfig(BaseModel):
    """Radarr host config attributes."""

    analyticsEnabled: bool | None = None
    apiKey: str | None = None
    authenticationMethod: str | None = None
    backupFolder: str | None = None
    backupInterval: int | None = None
    backupRetention: int | None = None
    bindAddress: str | None = None
    branch: str | None = None
    certificateValidation: str | None = None
    consoleLogLevel: str | None = None
    enableSsl: bool | None = None
    id: int | None = None
    launchBrowser: bool | None = None
    logLevel: str | None = None
    password: str | None = None
    port: int | None = None
    proxyBypassFilter: str | None = None
    proxyBypassLocalAddresses: bool | None = None
    proxyEnabled: bool | None = None
    proxyHostname: str | None = None
    proxyPassword: str | None = None
    proxyPort: int | None = None
    proxyType: str | None = None
    proxyUsername: str | None = None
    sslCertPassword: str | None = None
    sslCertPath: str | None = None
    sslPort: int | None = None
    urlBase: str | None = None
    updateAutomatically: bool | None = None
    updateMechanism: str | None = None
    updateScriptPath: str | None = None
    username: str | None = None


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
class RadarrSystemStatus(BaseModel):
    """Radarr system status attributes."""

    appData: str | None = None
    authentication: str | None = None
    branch: str | None = None
    buildTime: str | None = None
    isAdmin: bool | None = None
    isDebug: bool | None = None
    isDocker: bool | None = None
    isLinux: bool | None = None
    isMono: bool | None = None
    isNetCore: bool | None = None
    isOsx: bool | None = None
    isProduction: bool | None = None
    isUserInteractive: bool | None = None
    isWindows: bool | None = None
    migrationVersion: int | None = None
    mode: str | None = None
    osName: str | None = None
    osVersion: str | None = None
    packageUpdateMechanism: str | None = None
    runtimeVersion: str | None = None
    runtimeName: str | None = None
    sqliteVersion: str | None = None
    startTime: str | None = None
    startupPath: str | None = None
    urlBase: str | None = None
    version: str | None = None


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
class RadarrCustomFilter(BaseModel):
    """Radarr custom filter attributes."""

    id: int | None = None
    filters: list[_RadarrCustomFilterAttr] | None = None
    label: str | None = None
    type: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.filters = [
            _RadarrCustomFilterAttr(filter) for filter in self.filters or []
        ]


@dataclass(init=False)
class RadarrRemotePathMapping(BaseModel):
    """Radarr remote path mapping attributes."""

    id: int | None = None
    host: str | None = None
    localPath: str | None = None
    remotePath: str | None = None


@dataclass(init=False)
class RadarrRootFolder(BaseModel):
    """Radarr root folder attributes."""

    id: int | None = None
    freeSpace: int | None = None
    path: str | None = None
    unmappedFolders: list[_RadarrUnmappedRootFolder] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.unmappedFolders = [
            _RadarrUnmappedRootFolder(unmap) for unmap in self.unmappedFolders or []
        ]


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
class RadarrCommand(_RadarrCommon4):
    """Radarr command attributes."""

    body: _RadarrCommandBody | None = None
    commandName: str | None = None
    duration: str | None = None
    ended: str | None = None
    lastExecutionTime: str | None = None
    message: str | None = None
    priority: str | None = None
    queued: str | None = None
    sendUpdatesToClient: bool | None = None
    started: str | None = None
    stateChangeTime: str | None = None
    status: str | None = None
    trigger: str | None = None
    updateScheduledTask: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.body = _RadarrCommandBody(self.body) or {}


@dataclass(init=False)
class RadarrMovie(_RadarrMovie):
    """Movie attributes."""

    movieFile: RadarrMovieFile | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.movieFile = RadarrMovieFile(self.movieFile) or {}
