"""Request Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

import attr

from ..const import ALL
from .base import BaseModel
from .const import ProtocolType
from .request_common import (
    _CommandBody,
    _Common,
    _Common3,
    _CustomFilterAttr,
    _Fields,
    _FilesystemDirectory,
    _FilesystemFolder,
    _LocalizationStrings,
    _LogRecord,
    _MetadataFields,
    _QualityInfo,
    _QualityProfileItems,
    _RecordCommon,
    _ReleaseProfilePreferred,
    _Tag,
    _UpdateChanges,
)


class AddTypes(str, Enum):
    """Add types."""

    AUTOMATIC = "automatic"
    MANUAL = "manual"


class AllowFingerprintingType(str, Enum):
    """Allow fingerprinting type."""

    ALL_FILES = "allFiles"
    NEVER = "never"
    NEW_FILES = "newFiles"


class AuthenticationType(str, Enum):
    """Authentication type."""

    BASIC = "basic"
    FORMS = "forms"
    NONE = "none"


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
    MANUAL_IMPORT = "ManualImport"
    MESSAGING_CLEANUP = "MessagingCleanup"
    REFRESH_MONITORED_DOWNLOADS = "RefreshMonitoredDownloads"
    RENAME_FILES = "RenameFiles"
    RSS_SYNC = "RssSync"


class CertificateValidationType(str, Enum):
    """Certificate validation type."""

    DISABLED = "disabled"
    DISABLED_LOCAL = "disabledForLocalAddresses"
    ENABLED = "enabled"


class CommandPriorityType(str, Enum):
    """Command priority type."""

    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"


class CommandStatusType(str, Enum):
    """Command status type."""

    QUEUED = "queued"
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"
    ABORTED = "aborted"
    CANCELLED = "cancelled"
    ORPHANED = "orphaned"


class CommandTriggerType(str, Enum):
    """Command trigger type."""

    MANUAL = "manual"
    SCHEDULED = "scheduled"
    UNSPECIFIED = "unspecified"


class HealthType(str, Enum):
    """Health type."""

    ERROR = "error"
    NOTICE = "notice"
    OK = "ok"
    WARNING = "warning"


class HostUpdateType(str, Enum):
    """Host update type."""

    APT = "apt"
    BUILT_IN = "builtIn"
    DOCKER = "docker"
    EXTERNAL = "external"
    SCRIPT = "script"


class ImageSize(str, Enum):
    """Image size."""

    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


class ImageType(str, Enum):
    """Image type."""

    BANNER = "banner"
    COVER = "cover"
    DISC = "disc"
    FANART = "fanart"
    HEADSHOT = "headshot"
    LOGO = "logo"
    POSTER = "poster"
    SCREENSHOT = "screenshot"
    UNKNOWN = "unknown"


class LogSortKeys(str, Enum):
    """Log sort keys."""

    ID = "id"
    LEVEL = "level"
    LOGGER = "logger"
    MESSAGE = "message"
    TIME = "time"


class MonitoringOptionsType(str, Enum):
    """Monitoring options type."""

    ALL = ALL
    EXISTING = "existing"
    FIRST = "first"
    FUTURE = "future"
    LATEST = "latest"
    MISSING = "missing"
    NONE = "none"
    UNKNOWN = "unknown"


class ProxyType(str, Enum):
    """Proxy type."""

    HTTP = "http"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


class RescanAfterRefreshType(str, Enum):
    """Rescan after refresh type."""

    AFTER_MANUAL = "afterManual"
    ALWAYS = "always"
    NEVER = "never"


class SortDirection(str, Enum):
    """Sort direction type."""

    ASCENDING = "ascending"
    DEFAULT = "default"
    DESCENDING = "descending"


class StatusType(str, Enum):
    """Status type."""

    CONTINUING = "continuing"
    ENDED = "ended"


@dataclass(init=False)
class Diskspace(BaseModel):
    """Diskspace attributes."""

    freeSpace: int = attr.ib(type=int)
    label: str = attr.ib(type=str)
    path: str = attr.ib(type=str)
    totalSpace: int = attr.ib(type=int)


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

    contentsUrl: str = attr.ib(type=str)
    downloadUrl: str = attr.ib(type=str)
    filename: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    lastWriteTime: datetime = attr.ib(type=datetime)


@dataclass(init=False)
class Tag(_Tag):
    """Tag attributes."""


@dataclass(init=False)
class SystemBackup(_Common3):
    """System backup attributes."""

    path: str = attr.ib(type=str)
    time: datetime = attr.ib(type=datetime)
    type: str = attr.ib(type=str)


@dataclass(init=False)
class CustomFilter(BaseModel):
    """Custom filter attributes."""

    id: int = attr.ib(type=int)
    filters: list[_CustomFilterAttr] | None = None
    label: str = attr.ib(type=str)
    type: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.filters = [_CustomFilterAttr(filter) for filter in self.filters or []]


@dataclass(init=False)
class RootFolder(BaseModel):
    """Root folder attributes."""

    freeSpace: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    path: str = attr.ib(type=str)
    unmappedFolders: list[FilesystemFolder] | None = None

    def __post_init__(self):
        """Post init."""
        self.unmappedFolders = [
            FilesystemFolder(unmap) for unmap in self.unmappedFolders or []
        ]


@dataclass(init=False)
class HostConfig(BaseModel):
    """Host config attributes."""

    analyticsEnabled: bool = attr.ib(type=bool)
    apiKey: str = attr.ib(type=str)
    authenticationMethod: str = attr.ib(type=str)
    backupFolder: str = attr.ib(type=str)
    backupInterval: int = attr.ib(type=int)
    backupRetention: int = attr.ib(type=int)
    bindAddress: str = attr.ib(type=str)
    branch: str = attr.ib(type=str)
    certificateValidation: str = attr.ib(type=str)
    consoleLogLevel: str = attr.ib(type=str)
    enableSsl: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    launchBrowser: bool = attr.ib(type=bool)
    logLevel: str = attr.ib(type=str)
    password: str = attr.ib(type=str)
    port: int = attr.ib(type=int)
    proxyBypassFilter: str = attr.ib(type=str)
    proxyBypassLocalAddresses: bool = attr.ib(type=bool)
    proxyEnabled: bool = attr.ib(type=bool)
    proxyHostname: str = attr.ib(type=str)
    proxyPassword: str = attr.ib(type=str)
    proxyPort: int = attr.ib(type=int)
    proxyType: str = attr.ib(type=str)
    proxyUsername: str = attr.ib(type=str)
    sslCertHash: str = attr.ib(type=str)
    sslCertPassword: str = attr.ib(type=str)
    sslCertPath: str = attr.ib(type=str)
    sslPort: int = attr.ib(type=int)
    updateAutomatically: bool = attr.ib(type=bool)
    updateMechanism: str = attr.ib(type=str)
    updateScriptPath: str = attr.ib(type=str)
    urlBase: str = attr.ib(type=str)
    username: str = attr.ib(type=str)


@dataclass(init=False)
class UIConfig(BaseModel):
    """UI config attributes."""

    calendarWeekColumnHeader: str = attr.ib(type=str)
    enableColorImpairedMode: bool = attr.ib(type=bool)
    firstDayOfWeek: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    longDateFormat: str = attr.ib(type=str)
    movieInfoLanguage: int = attr.ib(type=int)
    movieRuntimeFormat: str = attr.ib(type=str)
    shortDateFormat: str = attr.ib(type=str)
    showRelativeDates: bool = attr.ib(type=bool)
    timeFormat: str = attr.ib(type=str)
    uiLanguage: int = attr.ib(type=int)


@dataclass(init=False)
class SystemStatus(BaseModel):
    """System status attributes."""

    appData: str = attr.ib(type=str)
    authentication: str = attr.ib(type=str)
    branch: str = attr.ib(type=str)
    buildTime: datetime = attr.ib(type=datetime)
    isAdmin: bool = attr.ib(type=bool)
    isDebug: bool = attr.ib(type=bool)
    isDocker: bool = attr.ib(type=bool)
    isLinux: bool = attr.ib(type=bool)
    isMono: bool = attr.ib(type=bool)
    isMonoRuntime: bool = attr.ib(type=bool)
    isNetCore: bool = attr.ib(type=bool)
    isOsx: bool = attr.ib(type=bool)
    isProduction: bool = attr.ib(type=bool)
    isUserInteractive: bool = attr.ib(type=bool)
    isWindows: bool = attr.ib(type=bool)
    migrationVersion: int = attr.ib(type=int)
    mode: str = attr.ib(type=str)
    osName: str = attr.ib(type=str)
    osVersion: str = attr.ib(type=str)
    packageUpdateMechanism: str = attr.ib(type=str)
    runtimeName: str = attr.ib(type=str)
    runtimeVersion: str = attr.ib(type=str)
    sqliteVersion: str = attr.ib(type=str)
    startTime: datetime = attr.ib(type=datetime)
    startupPath: str = attr.ib(type=str)
    urlBase: str = attr.ib(type=str)
    version: str = attr.ib(type=str)


@dataclass(init=False)
class Command(_Common3):
    """Command attributes."""

    body: _CommandBody = attr.ib(type=_CommandBody)
    commandName: str = attr.ib(type=str)
    duration: str = attr.ib(type=str)
    ended: datetime = attr.ib(type=datetime)
    lastExecutionTime: datetime = attr.ib(type=datetime)
    message: str = attr.ib(type=str)
    priority: str = attr.ib(type=str)
    queued: datetime = attr.ib(type=datetime)
    sendUpdatesToClient: bool = attr.ib(type=bool)
    started: datetime = attr.ib(type=datetime)
    stateChangeTime: datetime = attr.ib(type=datetime)
    status: str = attr.ib(type=str)
    trigger: str = attr.ib(type=str)
    updateScheduledTask: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.body = _CommandBody(self.body) or {}


@dataclass(init=False)
class DownloadClient(_Common):
    """Download client attributes."""

    configContract: str = attr.ib(type=str)
    enable: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    priority: int = attr.ib(type=int)
    protocol: ProtocolType = attr.ib(type=ProtocolType)
    tags: list[int] = attr.ib(type=list[int])


@dataclass(init=False)
class DownloadClientConfig(BaseModel):
    """Download client configuration attributes."""

    autoRedownloadFailed: bool = attr.ib(type=bool)
    checkForFinishedDownloadInterval: int = attr.ib(type=int)
    downloadClientWorkingFolders: str = attr.ib(type=str)
    enableCompletedDownloadHandling: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    removeCompletedDownloads: bool = attr.ib(type=bool)
    removeFailedDownloads: bool = attr.ib(type=bool)


@dataclass(init=False)
class Filesystem(BaseModel):
    """Filesystem attributes."""

    directories: list[_FilesystemDirectory] | None = None
    files: list = attr.ib(type=list)
    parent: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.directories = [_FilesystemDirectory(x) for x in self.directories or []]


@dataclass(init=False)
class Health(BaseModel):
    """Health attributes."""

    message: str = attr.ib(type=str)
    source: str = attr.ib(type=str)
    type: str = attr.ib(type=str)
    wikiUrl: str = attr.ib(type=str)


@dataclass(init=False)
class ImportListExclusion(BaseModel):
    """Import list exclusion attributes."""

    artistName: str = attr.ib(type=str)
    authorName: str = attr.ib(type=str)
    foreignId: str = attr.ib(type=str)
    id: int | None = None
    movieTitle: str = attr.ib(type=str)
    movieYear: int = attr.ib(type=int)
    title: str = attr.ib(type=str)
    tmdbId: int = attr.ib(type=int)
    tvdbId: int = attr.ib(type=int)


@dataclass(init=False)
class Indexer(_Common3):
    """Indexer attributes."""

    configContract: str = attr.ib(type=str)
    enableAutomaticSearch: bool = attr.ib(type=bool)
    enableInteractiveSearch: bool = attr.ib(type=bool)
    enableRss: bool = attr.ib(type=bool)
    fields: list[_Fields] | None = None
    implementation: str = attr.ib(type=str)
    implementationName: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    priority: int = attr.ib(type=int)
    protocol: ProtocolType = attr.ib(type=ProtocolType)
    supportsRss: bool = attr.ib(type=bool)
    supportsSearch: bool = attr.ib(type=bool)
    tags: list[int] = attr.ib(type=list[int])

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class IndexerConfig(BaseModel):
    """Indexer configuration attributes."""

    allowHardcodedSubs: bool = attr.ib(type=bool)
    availabilityDelay: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    maximumSize: int = attr.ib(type=int)
    minimumAge: int = attr.ib(type=int)
    preferIndexerFlags: bool = attr.ib(type=bool)
    retention: int = attr.ib(type=int)
    rssSyncInterval: int = attr.ib(type=int)
    whitelistedHardcodedSubs: str = attr.ib(type=str)


@dataclass(init=False)
class Language(_Common3):
    """Language attributes."""

    nameLower: str = attr.ib(type=str)


@dataclass(init=False)
class Localization(BaseModel):
    """Localization attributes."""

    Strings: _LocalizationStrings = attr.ib(type=_LocalizationStrings)

    def __post_init__(self):
        """Post init."""
        self.Strings = _LocalizationStrings(self.Strings) or {}


@dataclass(init=False)
class MediaManagementConfig(BaseModel):
    """Media management config attributes."""

    allowFingerprinting: str = attr.ib(type=str)
    autoRenameFolders: bool = attr.ib(type=bool)
    autoUnmonitorPreviouslyDownloadedBooks: bool = attr.ib(type=bool)
    autoUnmonitorPreviouslyDownloadedEpisodes: bool = attr.ib(type=bool)
    autoUnmonitorPreviouslyDownloadedMovies: bool = attr.ib(type=bool)
    chmodFolder: str = attr.ib(type=str)
    chownGroup: str = attr.ib(type=str)
    copyUsingHardlinks: bool = attr.ib(type=bool)
    createEmptyAuthorFolders: bool = attr.ib(type=bool)
    createEmptyMovieFolders: bool = attr.ib(type=bool)
    createEmptySeriesFolders: bool = attr.ib(type=bool)
    deleteEmptyFolders: bool = attr.ib(type=bool)
    downloadPropersAndRepacks: str = attr.ib(type=str)
    enableMediaInfo: bool = attr.ib(type=bool)
    episodeTitleRequired: str = attr.ib(type=str)
    extraFileExtensions: str = attr.ib(type=str)
    fileDate: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    importExtraFiles: bool = attr.ib(type=bool)
    minimumFreeSpaceWhenImporting: int = attr.ib(type=int)
    pathsDefaultStatic: bool = attr.ib(type=bool)
    recycleBin: str = attr.ib(type=str)
    recycleBinCleanupDays: int = attr.ib(type=int)
    rescanAfterRefresh: str = attr.ib(type=str)
    setPermissionsLinux: bool = attr.ib(type=bool)
    skipFreeSpaceCheckWhenImporting: bool = attr.ib(type=bool)
    watchLibraryForChanges: bool = attr.ib(type=bool)


@dataclass(init=False)
class MetadataConfig(_Common3):
    """Metadata config attributes."""

    configContract: str = attr.ib(type=str)
    enable: bool = attr.ib(type=bool)
    fields: list[_MetadataFields] | None = None
    implementation: str = attr.ib(type=str)
    implementationName: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type=list[int])

    def __post_init__(self):
        """Post init."""
        self.fields = [_MetadataFields(field) for field in self.fields or []]


@dataclass(init=False)
class QualityDefinition(BaseModel):
    """Quality definition attributes."""

    id: int = attr.ib(type=int)
    maxSize: float = attr.ib(type=float)
    minSize: float = attr.ib(type=float)
    preferredSize: int = attr.ib(type=int)
    quality: _QualityInfo = attr.ib(type=_QualityInfo)
    title: str = attr.ib(type=str)
    weight: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.quality = _QualityInfo(self.quality) or {}


@dataclass(init=False)
class QualityProfile(_Common3):
    """Quality profile attributes."""

    cutoff: int = attr.ib(type=int)
    cutoffFormatScore: int = attr.ib(type=int)
    formatItems: list = attr.ib(type=list)
    items: list[_QualityProfileItems] | None = None
    language: _Common3 = attr.ib(type=_Common3)
    minFormatScore: int = attr.ib(type=int)
    upgradeAllowed: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.items = [_QualityProfileItems(item) for item in self.items or []]
        self.language = _Common3(self.language) or {}


@dataclass(init=False)
class QueueStatus(BaseModel):
    """Queue status attributes."""

    count: int = attr.ib(type=int)
    errors: bool = attr.ib(type=bool)
    totalCount: int = attr.ib(type=int)
    unknownCount: int = attr.ib(type=int)
    unknownErrors: bool = attr.ib(type=bool)
    unknownWarnings: bool = attr.ib(type=bool)
    warnings: bool = attr.ib(type=bool)


@dataclass(init=False)
class ReleaseProfile(BaseModel):
    """Release profile attributes."""

    enabled: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    ignored: str = attr.ib(type=str)
    includePreferredWhenRenaming: bool = attr.ib(type=bool)
    indexerId: int = attr.ib(type=int)
    preferred: list[_ReleaseProfilePreferred] | None = None
    required: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type=list[int])

    def __post_init__(self):
        """Post init."""
        self.preferred = [_ReleaseProfilePreferred(x) for x in self.preferred or []]


@dataclass(init=False)
class RemotePathMapping(BaseModel):
    """Remote path mapping attributes."""

    host: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    localPath: str = attr.ib(type=str)
    remotePath: str = attr.ib(type=str)


@dataclass(init=False)
class SystemTask(_Common3):
    """System task attributes."""

    interval: int = attr.ib(type=int)
    lastDuration: str = attr.ib(type=str)
    lastExecution: datetime = attr.ib(type=datetime)
    lastStartTime: datetime = attr.ib(type=datetime)
    nextExecution: datetime = attr.ib(type=datetime)
    taskName: str = attr.ib(type=str)


@dataclass(init=False)
class Update(BaseModel):
    """Update attributes."""

    branch: str = attr.ib(type=str)
    changes: _UpdateChanges = attr.ib(type=_UpdateChanges)
    fileName: str = attr.ib(type=str)
    hash: str = attr.ib(type=str)
    installable: bool = attr.ib(type=bool)
    installed: bool = attr.ib(type=bool)
    installedOn: datetime = attr.ib(type=datetime)
    latest: bool = attr.ib(type=bool)
    releaseDate: datetime = attr.ib(type=datetime)
    url: str = attr.ib(type=str)
    version: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.changes = _UpdateChanges(self.changes) or {}


@dataclass(init=False)
class DelayProfile(BaseModel):
    """Delay profile attributes."""

    bypassIfHighestQuality: bool = attr.ib(type=bool)
    enableTorrent: bool = attr.ib(type=bool)
    enableUsenet: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    order: int = attr.ib(type=int)
    preferredProtocol: ProtocolType = attr.ib(type=ProtocolType)
    tags: list[int] = attr.ib(type=list[int])
    torrentDelay: int = attr.ib(type=int)
    usenetDelay: int = attr.ib(type=int)


@dataclass(init=False)
class FilesystemFolder(_FilesystemFolder):
    """Filesystem folder attributes."""

    relativePath: str = attr.ib(type=str)
