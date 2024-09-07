"""Request Models."""

# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

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
    _RootFolder,
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

    freeSpace: int
    label: str
    path: str
    totalSpace: int


@dataclass(init=False)
class Logs(_RecordCommon):
    """Log attributes."""

    records: list[_LogRecord] = field(default_factory=list[_LogRecord])

    def __post_init__(self):
        """Post init."""
        self.records = [_LogRecord(record) for record in self.records]


@dataclass(init=False)
class LogFile(BaseModel):
    """Log file attributes."""

    contentsUrl: str
    downloadUrl: str
    filename: str
    id: int
    lastWriteTime: datetime


@dataclass(init=False)
class Tag(_Tag):
    """Tag attributes."""


@dataclass(init=False)
class SystemBackup(_Common3):
    """System backup attributes."""

    path: str
    time: datetime
    type: str


@dataclass(init=False)
class CustomFilter(BaseModel):
    """Custom filter attributes."""

    id: int
    filters: list[_CustomFilterAttr] | None = None
    label: str
    type: str

    def __post_init__(self):
        """Post init."""
        self.filters = [_CustomFilterAttr(filter) for filter in self.filters or []]


@dataclass(init=False)
class RootFolder(_RootFolder):
    """Root folder attributes."""


@dataclass(init=False)
class HostConfig(BaseModel):
    """Host config attributes."""

    analyticsEnabled: bool
    apiKey: str
    authenticationMethod: str
    backupFolder: str
    backupInterval: int
    backupRetention: int
    bindAddress: str
    branch: str
    certificateValidation: str
    consoleLogLevel: str
    enableSsl: bool
    id: int
    launchBrowser: bool
    logLevel: str
    password: str
    port: int
    proxyBypassFilter: str
    proxyBypassLocalAddresses: bool
    proxyEnabled: bool
    proxyHostname: str
    proxyPassword: str
    proxyPort: int
    proxyType: str
    proxyUsername: str
    sslCertHash: str
    sslCertPassword: str
    sslCertPath: str
    sslPort: int
    updateAutomatically: bool
    updateMechanism: str
    updateScriptPath: str
    urlBase: str
    username: str


@dataclass(init=False)
class UIConfig(BaseModel):
    """UI config attributes."""

    calendarWeekColumnHeader: str
    enableColorImpairedMode: bool
    firstDayOfWeek: int
    id: int
    longDateFormat: str
    movieInfoLanguage: int
    movieRuntimeFormat: str
    shortDateFormat: str
    showRelativeDates: bool
    timeFormat: str
    uiLanguage: int


@dataclass(init=False)
class SystemStatus(BaseModel):
    """System status attributes."""

    appData: str
    appName: str
    authentication: str
    branch: str
    buildTime: datetime
    instanceName: str
    isAdmin: bool
    isDebug: bool
    isDocker: bool
    isLinux: bool
    isMono: bool
    isMonoRuntime: bool
    isNetCore: bool
    isOsx: bool
    isProduction: bool
    isUserInteractive: bool
    isWindows: bool
    migrationVersion: int
    mode: str
    osName: str
    osVersion: str
    packageUpdateMechanism: str
    runtimeName: str
    runtimeVersion: str
    sqliteVersion: str
    startTime: datetime
    startupPath: str
    urlBase: str
    version: str


@dataclass(init=False)
class Command(_Common3):
    """Command attributes."""

    body: type[_CommandBody] = field(default=_CommandBody)
    commandName: str
    duration: str
    ended: datetime
    lastExecutionTime: datetime
    message: str
    priority: str
    queued: datetime
    sendUpdatesToClient: bool
    started: datetime
    stateChangeTime: datetime
    status: str
    trigger: str
    updateScheduledTask: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.body = _CommandBody(self.body)


@dataclass(init=False)
class DownloadClient(_Common):
    """Download client attributes."""

    configContract: str
    enable: bool
    id: int
    priority: int
    protocol: ProtocolType
    tags: list[int]


@dataclass(init=False)
class DownloadClientConfig(BaseModel):
    """Download client configuration attributes."""

    autoRedownloadFailed: bool
    checkForFinishedDownloadInterval: int
    downloadClientWorkingFolders: str
    enableCompletedDownloadHandling: bool
    id: int
    removeCompletedDownloads: bool
    removeFailedDownloads: bool


@dataclass(init=False)
class Filesystem(BaseModel):
    """Filesystem attributes."""

    directories: list[_FilesystemDirectory] | None = None
    files: list
    parent: str

    def __post_init__(self):
        """Post init."""
        self.directories = [_FilesystemDirectory(x) for x in self.directories or []]


@dataclass(init=False)
class Health(BaseModel):
    """Health attributes."""

    message: str
    source: str
    type: str
    wikiUrl: str


@dataclass(init=False)
class ImportListExclusion(BaseModel):
    """Import list exclusion attributes."""

    artistName: str
    authorName: str
    foreignId: str
    id: int | None = None
    movieTitle: str
    movieYear: int
    title: str
    tmdbId: int
    tvdbId: int


@dataclass(init=False)
class Indexer(_Common3):
    """Indexer attributes."""

    configContract: str
    enableAutomaticSearch: bool
    enableInteractiveSearch: bool
    enableRss: bool
    fields: list[_Fields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    priority: int
    protocol: ProtocolType
    supportsRss: bool
    supportsSearch: bool
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class IndexerConfig(BaseModel):
    """Indexer configuration attributes."""

    allowHardcodedSubs: bool
    availabilityDelay: int
    id: int
    maximumSize: int
    minimumAge: int
    preferIndexerFlags: bool
    retention: int
    rssSyncInterval: int
    whitelistedHardcodedSubs: str


@dataclass(init=False)
class Language(_Common3):
    """Language attributes."""

    nameLower: str


@dataclass(init=False)
class Localization(BaseModel):
    """Localization attributes."""

    Strings: type[_LocalizationStrings] = field(default=_LocalizationStrings)

    def __post_init__(self):
        """Post init."""
        self.Strings = _LocalizationStrings(self.Strings)


@dataclass(init=False)
class MediaManagementConfig(BaseModel):
    """Media management config attributes."""

    allowFingerprinting: str
    autoRenameFolders: bool
    autoUnmonitorPreviouslyDownloadedBooks: bool
    autoUnmonitorPreviouslyDownloadedEpisodes: bool
    autoUnmonitorPreviouslyDownloadedMovies: bool
    autoUnmonitorPreviouslyDownloadedTracks: bool
    chmodFolder: str
    chownGroup: str
    copyUsingHardlinks: bool
    createEmptyAuthorFolders: bool
    createEmptyMovieFolders: bool
    createEmptySeriesFolders: bool
    deleteEmptyFolders: bool
    downloadPropersAndRepacks: str
    enableMediaInfo: bool
    episodeTitleRequired: str
    extraFileExtensions: str
    fileDate: str
    id: int
    importExtraFiles: bool
    minimumFreeSpaceWhenImporting: int
    pathsDefaultStatic: bool
    recycleBin: str
    recycleBinCleanupDays: int
    rescanAfterRefresh: str
    setPermissionsLinux: bool
    skipFreeSpaceCheckWhenImporting: bool
    watchLibraryForChanges: bool


@dataclass(init=False)
class MetadataConfig(_Common3):
    """Metadata config attributes."""

    configContract: str
    enable: bool
    fields: list[_MetadataFields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.fields = [_MetadataFields(field) for field in self.fields or []]


@dataclass(init=False)
class QualityDefinition(BaseModel):
    """Quality definition attributes."""

    id: int
    maxSize: float
    minSize: float
    preferredSize: int
    quality: type[_QualityInfo] = field(default=_QualityInfo)
    title: str
    weight: int

    def __post_init__(self):
        """Post init."""
        self.quality = _QualityInfo(self.quality)


@dataclass(init=False)
class QualityProfile(_Common3):
    """Quality profile attributes."""

    cutoff: int
    cutoffFormatScore: int
    formatItems: list
    items: list[_QualityProfileItems] | None = None
    language: type[_Common3] = field(default=_Common3)
    minFormatScore: int
    upgradeAllowed: bool

    def __post_init__(self):
        """Post init."""
        self.items = [_QualityProfileItems(item) for item in self.items or []]
        self.language = _Common3(self.language)


@dataclass(init=False)
class QueueStatus(BaseModel):
    """Queue status attributes."""

    count: int
    errors: bool
    totalCount: int
    unknownCount: int
    unknownErrors: bool
    unknownWarnings: bool
    warnings: bool


@dataclass(init=False)
class ReleaseProfile(BaseModel):
    """Release profile attributes."""

    enabled: bool
    id: int
    ignored: str
    includePreferredWhenRenaming: bool
    indexerId: int
    preferred: list[_ReleaseProfilePreferred] | None = None
    required: str
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.preferred = [_ReleaseProfilePreferred(x) for x in self.preferred or []]


@dataclass(init=False)
class RemotePathMapping(BaseModel):
    """Remote path mapping attributes."""

    host: str
    id: int
    localPath: str
    remotePath: str


@dataclass(init=False)
class SystemTask(_Common3):
    """System task attributes."""

    interval: int
    lastDuration: str
    lastExecution: datetime
    lastStartTime: datetime
    nextExecution: datetime
    taskName: str


@dataclass(init=False)
class Update(BaseModel):
    """Update attributes."""

    branch: str
    changes: type[_UpdateChanges] = field(default=_UpdateChanges)
    fileName: str
    hash: str
    installable: bool
    installed: bool
    installedOn: datetime
    latest: bool
    releaseDate: datetime
    url: str
    version: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.changes = _UpdateChanges(self.changes)


@dataclass(init=False)
class DelayProfile(BaseModel):
    """Delay profile attributes."""

    bypassIfHighestQuality: bool
    enableTorrent: bool
    enableUsenet: bool
    id: int
    order: int
    preferredProtocol: ProtocolType
    tags: list[int]
    torrentDelay: int
    usenetDelay: int


@dataclass(init=False)
class FilesystemFolder(_FilesystemFolder):
    """Filesystem folder attributes."""
