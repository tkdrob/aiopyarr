"""Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel


@dataclass(init=False)
class Diskspace(BaseModel):
    """Radarr diskspace attributes."""

    freeSpace: int | None = None
    label: str | None = None
    path: str | None = None
    totalSpace: int | None = None


@dataclass(init=False)
class _CommonAttrs(BaseModel):
    """Common attributes."""

    audioBitrate: str | None = None
    audioChannels: float | None = None
    audioCodec: str | None = None
    audioLanguages: str | None = None
    audioStreamCount: int | None = None
    resolution: str | None = None
    runTime: str | None = None
    scanType: str | None = None
    subtitles: str | None = None
    videoBitDepth: int | None = None
    videoBitrate: int | None = None
    videoCodec: str | None = None
    videoFps: float | None = None


@dataclass(init=False)
class _LogRecord(BaseModel):
    """Sonarr log record attributes."""

    exception: str | None = None
    exceptionType: str | None = None
    id: int | None = None
    level: str | None = None
    logger: str | None = None
    message: str | None = None
    time: str | None = None


@dataclass(init=False)
class _RecordCommon(BaseModel):
    """Sonarr common attributes."""

    page: int | None = None
    pageSize: int | None = None
    sortDirection: str | None = None
    sortKey: str | None = None
    totalRecords: int | None = None


@dataclass(init=False)
class Logs(_RecordCommon):
    """Log attributes."""

    records: list[_LogRecord] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [_LogRecord(record) for record in self.records or []]


@dataclass(init=False)
class LogFiles(BaseModel):
    """Log file attributes."""

    filename: str | None = None
    lastWriteTime: str | None = None
    contentsUrl: str | None = None
    downloadUrl: str | None = None
    id: int | None = None


@dataclass(init=False)
class Tag(BaseModel):
    """Radarr tag attributes."""

    id: int | None = None
    label: str | None = None


@dataclass(init=False)
class SystemBackup(BaseModel):
    """System backup attributes."""

    id: int | None = None
    name: str | None = None
    path: str | None = None
    time: str | None = None
    type: str | None = None


@dataclass(init=False)
class _CustomFilterAttr(BaseModel):
    """Custom filter attributes."""

    key: str | None = None
    type: str | None = None
    value: list[str] | None = None


@dataclass(init=False)
class CustomFilter(BaseModel):
    """Custom filter attributes."""

    id: int | None = None
    filters: list[_CustomFilterAttr] | None = None
    label: str | None = None
    type: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.filters = [_CustomFilterAttr(filter) for filter in self.filters or []]


@dataclass(init=False)
class _UnmappedRootFolder(BaseModel):
    """Unmapped folder attributes."""

    name: str | None = None
    path: str | None = None


@dataclass(init=False)
class RootFolder(BaseModel):
    """Root folder attributes."""

    id: int | None = None
    freeSpace: int | None = None
    path: str | None = None
    unmappedFolders: list[_UnmappedRootFolder] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
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
    urlBase: str | None = None
    updateAutomatically: bool | None = None
    updateMechanism: str | None = None
    updateScriptPath: str | None = None
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
    runtimeVersion: str | None = None
    runtimeName: str | None = None
    sqliteVersion: str | None = None
    startTime: str | None = None
    startupPath: str | None = None
    urlBase: str | None = None
    version: str | None = None


@dataclass(init=False)
class Command(BaseModel):
    """Command attributes."""

    name: str | None = None
    commandName: str | None = None
    message: str | None = None
    body: dict
    priority: str | None = None
    status: str | None = None
    queued: str | None = None
    started: str | None = None
    ended: str | None = None
    duration: str | None = None
    trigger: str | None = None
    stateChangeTime: str | None = None
    sendUpdatesToClient: bool | None = None
    updateScheduledTask: bool | None = None
    lastExecutionTime: str | None = None
    id: int | None = None
