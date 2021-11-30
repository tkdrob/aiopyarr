"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import APIResponseType, BaseModel

from .sonarr_common import (  # isort:skip
    _FileEpisodeQuality,
    _SonarrCommon,
    _SonarrCommon3,
    _SonarrCommon4,
    _SonarrCommon5,
    _SonarrCommon6,
    _SonarrCommon7,
    _SonarrCutoff,
    _SonarrEpisodeFile,
    _SonarrHistoryRecord,
    _SonarrHistoryRecordEpisode,
    _SonarrHistoryRecordSeries,
    _SonarrLogRecord,
    _SonarrParseEpisodeInfo,
    _SonarrQualityProfileValueItems,
    _SonarrQualitySub,
    _SonarrSeasonStatistics,
    _SonarrSeries2,
    _SonarrSeriesAlternateTitle,
    _SonarrSeriesCommon,
    _SonarrSeriesCommon3,
    _SonarrWantedMissingRecord,
    _SonarrWantedMissingSeriesSeason,
)


@dataclass(init=False)
class SonarrCalendar(_SonarrCommon5):
    """Sonarr calendar attributes."""

    _responsetype = APIResponseType.LIST

    downloading: bool | None = None
    series: SonarrSeries | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    tvDbEpisodeId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = SonarrSeries(self.series) or {}


@dataclass(init=False)
class SonarrCommand(_SonarrCommon4):
    """Sonarr command attributes."""

    sendUpdatesToClient: bool | None = None
    startedOn: str | None = None
    state: str | None = None
    stateChangeTime: str | None = None


@dataclass(init=False)
class SonarrEpisode(_SonarrCommon5):
    """Sonarr episode attributes."""

    absoluteEpisodeNumber: int | None = None
    episodeFile: _SonarrEpisodeFile | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    series: _SonarrHistoryRecordSeries | None = None
    tvDbEpisodeId: int | None = None
    unverifiedSceneNumbering: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.episodeFile = _SonarrEpisodeFile(self.episodeFile) or {}
        self.series = _SonarrHistoryRecordSeries(self.series) or {}


@dataclass(init=False)
class SonarrEpisodeFile(_SonarrEpisodeFile):
    """Sonarr episode file attributes."""


@dataclass(init=False)
class SonarrEpisodeFileQuailty(_SonarrCommon6):
    """Required input for updating episode file quality."""

    quality: _FileEpisodeQuality | None = None


@dataclass(init=False)
class SonarrHistory(_SonarrCommon):
    """Sonarr history attributes."""

    records: list[_SonarrHistoryRecord] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [_SonarrHistoryRecord(record) for record in self.records or []]


@dataclass(init=False)
class SonarrWantedMissing(_SonarrCommon):
    """Sonarr wanted missing attributes."""

    records: list[_SonarrWantedMissingRecord] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [
            _SonarrWantedMissingRecord(record) for record in self.records or []
        ]


@dataclass(init=False)
class SonarrQueueNew(_SonarrCommon6):
    """Sonarr queue attributes."""

    _responsetype = APIResponseType.LIST

    downloadId: str | None = None
    episode: _SonarrHistoryRecordEpisode | None = None
    estimatedCompletionTime: str | None = None
    protocol: str | None = None
    quality: _SonarrQualitySub | None = None
    series: _SonarrHistoryRecordSeries | None = None
    size: int | None = None
    sizeleft: int | None = None
    status: str | None = None
    statusMessages: list[str] | None = None
    timeleft: str | None = None
    title: str | None = None
    trackedDownloadStatus: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.episode = _SonarrHistoryRecordEpisode(self.episode) or {}
        self.quality = _SonarrQualitySub(self.quality) or {}
        if isinstance(self.series, dict):
            self.series = _SonarrHistoryRecordSeries(self.series) or {}


@dataclass(init=False)
class SonarrParse(BaseModel):
    """Sonarr parse attributes."""

    episodes: list[SonarrEpisode] | None = None
    parsedEpisodeInfo: _SonarrParseEpisodeInfo | None = None
    series: _SonarrSeries2 | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.parsedEpisodeInfo = _SonarrParseEpisodeInfo(self.parsedEpisodeInfo) or {}


@dataclass(init=False)
class SonarrQualityProfile(_SonarrCommon4):
    """Sonarr quality profile attributes."""

    _responsetype = APIResponseType.LIST

    cutoff: _SonarrCutoff | None = None
    items: list[_SonarrQualityProfileValueItems] | None = None


@dataclass(init=False)
class SonarrRelease(_SonarrCommon3, _SonarrCommon7):
    """Sonarr release attributes."""

    publishDate: str | None = None


@dataclass(init=False)
class SonarrRootFolder(_SonarrCommon6):
    """Sonarr root folder attributes."""

    _responsetype = APIResponseType.LIST

    freeSpace: int | None = None
    path: str | None = None
    unmappedFolders: list[str] | None = None


@dataclass(init=False)
class SonarrSeries(_SonarrSeasonStatistics, _SonarrHistoryRecordSeries):
    """Sonarr series attributes."""

    alternateTitles: list[_SonarrSeriesAlternateTitle] | None = None
    languageProfileId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _SonarrSeriesAlternateTitle(altTit) for altTit in self.alternateTitles or []
        ]


@dataclass(init=False)
class SonarrSeriesLookup(_SonarrSeriesCommon):
    """Sonarr series lookup attributes."""

    _responsetype = APIResponseType.LIST

    remotePoster: str | None = None


@dataclass(init=False)
class SonarrSystemStatus(BaseModel):
    """Sonarr system status attributes."""

    appData: str | None = None
    authentication: bool | None = None
    branch: str | None = None
    buildTime: str | None = None
    isAdmin: bool | None = None
    isDebug: bool | None = None
    isLinux: bool | None = None
    isMono: bool | None = None
    isProduction: bool | None = None
    isUserInteractive: bool | None = None
    isWindows: bool | None = None
    osVersion: str | None = None
    startOfWeek: int | None = None
    startupPath: str | None = None
    urlBase: str | None = None
    version: str | None = None


@dataclass(init=False)
class SonarrSystemBackup(_SonarrCommon4):
    """Sonarr system backup attributes."""

    _responsetype = APIResponseType.LIST

    path: str | None = None
    time: str | None = None
    type: str | None = None


@dataclass(init=False)
class SonarrTag(_SonarrCommon6):
    """Sonarr tag attributes."""

    label: str | None = None


@dataclass(init=False)
class SonarrSeriesUpdateParams(_SonarrSeriesCommon3):
    """Sonarr series update parameters."""

    profileId: int | None = None
    seasons: list[_SonarrWantedMissingSeriesSeason] | None = None


@dataclass(init=False)
class Logs(_SonarrCommon):
    """Log attributes."""

    records: list[_SonarrLogRecord] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [_SonarrLogRecord(record) for record in self.records or []]
