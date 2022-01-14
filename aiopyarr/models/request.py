"""Request Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .base import BaseModel

from .request_common import (  # isort:skip
    _Common,
    _Common3,
    _CommandBody,
    _CustomFilterAttr,
    _Fields,
    _FilesystemDirectory,
    _LocalizationStrings,
    _LogRecord,
    _MetadataFields,
    _QualityInfo,
    _QualityProfileItems,
    _RecordCommon,
    _ReleaseProfilePreferred,
    _Tag,
    _UnmappedRootFolder,
    _UpdateChanges,
)


class Commands(str, Enum):
    """Commands."""

    APPLICATION_UPDATE = "ApplicationUpdate"
    BACKUP = "Backup"
    CHECK_HEALTH = "CheckHealth"
    CLEAN_RECYCLE_BIN = "CleanUpRecycleBin"
    CLEAR_BLOCKLIST = "ClearBlocklist"
    DELETE_LOGS = "DeleteLogFiles"
    DELETE_UPDATE_LOGS = "DeleteUpdateLogFiles"
    HOUSEKEEPING = "Housekeeping"
    IMPORT_LIST_SYNC = "ImportListSync"
    MESSAGING_CLEANUP = "MessagingCleanup"
    REFRESH_MONITORED_DOWNLOADS = "RefreshMonitoredDownloads"
    RENAME_FILES = "RenameFiles"
    RSS_SYNC = "RssSync"


@dataclass(init=False)
class Diskspace(BaseModel):
    """Radarr diskspace attributes."""

    freeSpace: int | None = None
    label: str | None = None
    path: str | None = None
    totalSpace: int | None = None


@dataclass(init=False)
class Logs(_RecordCommon):
    """Log attributes."""

    records: list[_LogRecord] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [_LogRecord(record) for record in self.records or []]


@dataclass(init=False)
class LogFile(BaseModel):
    """Log file attributes."""

    contentsUrl: str | None = None
    downloadUrl: str | None = None
    filename: str | None = None
    id: int | None = None
    lastWriteTime: str | None = None


@dataclass(init=False)
class Tag(_Tag):
    """Tag attributes."""


@dataclass(init=False)
class SystemBackup(_Common3):
    """System backup attributes."""

    path: str | None = None
    time: str | None = None
    type: str | None = None


@dataclass(init=False)
class CustomFilter(BaseModel):
    """Custom filter attributes."""

    id: int | None = None
    filters: list[_CustomFilterAttr] | None = None
    label: str | None = None
    type: str | None = None

    def __post_init__(self):
        """Post init."""
        self.filters = [_CustomFilterAttr(filter) for filter in self.filters or []]


@dataclass(init=False)
class RootFolder(BaseModel):
    """Root folder attributes."""

    freeSpace: int | None = None
    id: int | None = None
    path: str | None = None
    unmappedFolders: list[_UnmappedRootFolder] | None = None

    def __post_init__(self):
        """Post init."""
        self.unmappedFolders = [
            _UnmappedRootFolder(unmap) for unmap in self.unmappedFolders or []
        ]


@dataclass(init=False)
class HostConfig(BaseModel):
    """Host config attributes."""

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
    sslCertHash: str | None = None
    sslCertPassword: str | None = None
    sslCertPath: str | None = None
    sslPort: int | None = None
    updateAutomatically: bool | None = None
    updateMechanism: str | None = None
    updateScriptPath: str | None = None
    urlBase: str | None = None
    username: str | None = None


@dataclass(init=False)
class UIConfig(BaseModel):
    """UI config attributes."""

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
    uiLanguage: int | None = None


@dataclass(init=False)
class SystemStatus(BaseModel):
    """system status attributes."""

    appData: str | None = None
    authentication: str | None = None
    branch: str | None = None
    buildTime: str | None = None
    isAdmin: bool | None = None
    isDebug: bool | None = None
    isDocker: bool | None = None
    isLinux: bool | None = None
    isMono: bool | None = None
    isMonoRuntime: bool | None = None
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
    runtimeName: str | None = None
    runtimeVersion: str | None = None
    sqliteVersion: str | None = None
    startTime: str | None = None
    startupPath: str | None = None
    urlBase: str | None = None
    version: str | None = None


@dataclass(init=False)
class Command(_Common3):
    """Command attributes."""

    body: _CommandBody | None = None
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
        self.body = _CommandBody(self.body) or {}


@dataclass(init=False)
class DownloadClient(_Common):
    """Download client attributes."""

    configContract: str | None = None
    enable: bool | None = None
    id: int | None = None
    priority: int | None = None
    protocol: str | None = None
    tags: list[int | None] | None = None


@dataclass(init=False)
class DownloadClientConfig(BaseModel):
    """Download client configuration attributes."""

    autoRedownloadFailed: bool | None = None
    checkForFinishedDownloadInterval: int | None = None
    downloadClientWorkingFolders: str | None = None
    enableCompletedDownloadHandling: bool | None = None
    id: int | None = None
    removeCompletedDownloads: bool | None = None
    removeFailedDownloads: bool | None = None


@dataclass(init=False)
class Filesystem(BaseModel):
    """Filesystem attributes."""

    directories: list[_FilesystemDirectory] | None = None
    files: list | None = None

    def __post_init__(self):
        """Post init."""
        self.directories = [_FilesystemDirectory(x) for x in self.directories or []]


@dataclass(init=False)
class Health(BaseModel):
    """Failed health check attributes."""

    message: str | None = None
    source: str | None = None
    type: str | None = None
    wikiUrl: str | None = None


@dataclass(init=False)
class ImportListExclusion(BaseModel):
    """import list exclusion attributes."""

    authorName: str | None = None
    foreignId: str | None = None
    id: int | None = None
    title: str | None = None
    tvdbId: int | None = None


@dataclass(init=False)
class Indexer(_Common3):
    """Indexer attributes."""

    configContract: str | None = None
    enableAutomaticSearch: bool | None = None
    enableInteractiveSearch: bool | None = None
    enableRss: bool | None = None
    fields: list[_Fields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    priority: int | None = None
    protocol: str | None = None
    supportsRss: bool | None = None
    supportsSearch: bool | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class IndexerConfig(BaseModel):
    """Indexer configuration attributes."""

    allowHardcodedSubs: bool | None = None
    availabilityDelay: int | None = None
    id: int | None = None
    maximumSize: int | None = None
    minimumAge: int | None = None
    preferIndexerFlags: bool | None = None
    retention: int | None = None
    rssSyncInterval: int | None = None
    whitelistedHardcodedSubs: str | None = None


@dataclass(init=False)
class Language(_Common3):
    """Language attributes."""

    nameLower: str | None = None


@dataclass(init=False)
class Localization(BaseModel):
    """Localization attributes."""

    Strings: _LocalizationStrings | None = None

    def __post_init__(self):
        """Post init."""
        self.Strings = _LocalizationStrings(self.Strings) or {}


@dataclass(init=False)
class MediaManagementConfig(BaseModel):
    """Media management config attributes."""

    allowFingerprinting: str | None = None
    autoRenameFolders: bool | None = None
    autoUnmonitorPreviouslyDownloadedBooks: bool | None = None
    autoUnmonitorPreviouslyDownloadedEpisodes: bool | None = None
    autoUnmonitorPreviouslyDownloadedMovies: bool | None = None
    chmodFolder: str | None = None
    chownGroup: str | None = None
    copyUsingHardlinks: bool | None = None
    createEmptyAuthorFolders: bool | None = None
    createEmptyMovieFolders: bool | None = None
    createEmptySeriesFolders: bool | None = None
    deleteEmptyFolders: bool | None = None
    downloadPropersAndRepacks: str | None = None
    enableMediaInfo: bool | None = None
    episodeTitleRequired: str | None = None
    extraFileExtensions: str | None = None
    fileDate: str | None = None
    id: int | None = None
    importExtraFiles: bool | None = None
    minimumFreeSpaceWhenImporting: int | None = None
    pathsDefaultStatic: bool | None = None
    recycleBin: str | None = None
    recycleBinCleanupDays: int | None = None
    rescanAfterRefresh: str | None = None
    setPermissionsLinux: bool | None = None
    skipFreeSpaceCheckWhenImporting: bool | None = None
    watchLibraryForChanges: bool | None = None


@dataclass(init=False)
class MetadataConfig(_Common3):
    """Metadata config attributes."""

    configContract: str | None = None
    enable: bool | None = None
    fields: list[_MetadataFields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_MetadataFields(field) for field in self.fields or []]


@dataclass(init=False)
class QualityDefinition(BaseModel):
    """Quality definition attributes."""

    id: int | None = None
    maxSize: float | None = None
    minSize: float | None = None
    preferredSize: int | None = None
    quality: _QualityInfo | None = None
    title: str | None = None
    weight: int | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _QualityInfo(self.quality) or {}


@dataclass(init=False)
class QualityProfile(_Common3):
    """Quality profile attributes."""

    cutoff: int | None = None
    cutoffFormatScore: int | None = None
    formatItems: list | None = None
    items: list[_QualityProfileItems] | None = None
    language: _Common3 | None = None
    minFormatScore: int | None = None
    upgradeAllowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.items = [_QualityProfileItems(item) for item in self.items or []]
        self.language = _Common3(self.language) or {}


@dataclass(init=False)
class QueueStatus(BaseModel):
    """Queue status attributes."""

    count: int | None = None
    errors: bool | None = None
    totalCount: int | None = None
    unknownCount: int | None = None
    unknownErrors: bool | None = None
    unknownWarnings: bool | None = None
    warnings: bool | None = None


@dataclass(init=False)
class ReleaseProfile(BaseModel):
    """Release profile attributes."""

    enabled: bool | None = None
    id: int | None = None
    ignored: str | None = None
    includePreferredWhenRenaming: bool | None = None
    indexerId: int | None = None
    preferred: list[_ReleaseProfilePreferred] | None = None
    required: str | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.preferred = [_ReleaseProfilePreferred(x) for x in self.preferred or []]


@dataclass(init=False)
class RemotePathMapping(BaseModel):
    """Remote path mapping attributes."""

    host: str | None = None
    id: int | None = None
    localPath: str | None = None
    remotePath: str | None = None


@dataclass(init=False)
class SystemTask(_Common3):
    """System task attributes."""

    interval: int | None = None
    lastDuration: str | None = None
    lastExecution: str | None = None
    lastStartTime: str | None = None
    nextExecution: str | None = None
    taskName: str | None = None


@dataclass(init=False)
class Update(BaseModel):
    """Update attributes."""

    branch: str | None = None
    changes: _UpdateChanges | None = None
    fileName: str | None = None
    hash: str | None = None
    installable: bool | None = None
    installed: bool | None = None
    installedOn: str | None = None
    latest: bool | None = None
    releaseDate: str | None = None
    url: str | None = None
    version: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.changes = _UpdateChanges(self.changes) or {}
