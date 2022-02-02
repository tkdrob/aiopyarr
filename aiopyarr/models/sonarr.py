"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from ..const import DATE, EPISODE_ID, PATH, SERIES_ID
from .base import BaseModel
from .request_common import (
    _Common2,
    _Common3,
    _Common4,
    _Common7,
    _Common8,
    _Fields,
    _ImportListCommon,
    _ManualImport,
    _Monitor,
    _MonitorOption,
    _Notification,
    _Quality,
    _QualityCommon,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _StatusMessage,
    _TagDetails,
)
from .sonarr_common import (
    _SonarrAddOptions,
    _SonarrCommon,
    _SonarrCommon2,
    _SonarrEpisodeFile,
    _SonarrEpisodeHistoryData,
    _SonarrEpisodeMonitor,
    _SonarrLanguageItem,
    _SonarrParseEpisodeInfo,
    _SonarrSeries2,
    _SonarrSeriesAlternateTitle,
    _SonarrSeriesCommon,
    _SonarrWantedMissingRecord,
)


class SonarrCommands(str, Enum):
    """Sonarr commands."""

    DOWNLOADED_EPISODES_SCAN = "DownloadedEpisodesScan"
    EPISODE_SEARCH = "EpisodeSearch"
    REFRESH_SERIES = "RefreshSeries"
    RENAME_SERIES = "RenameSeries"
    RESCAN_SERIES = "RescanSeries"
    SEASON_SEARCH = "SeasonSearch"
    SERIES_SEARCH = "SeriesSearch"


class SonarrEventType(Enum):
    """Sonarr event types."""

    DELETED = 5
    FAILED = 4
    GRABBED = 1
    IGNORED = 7
    IMPORTED = 3
    RENAMED = 6


class SonarrSortKeys(str, Enum):
    """Sonarr sort keys."""

    AIR_DATE_UTC = "episode.airDateUtc"
    DATE = DATE
    DOWNLOAD_CLIENT = "downloadClient"
    EPISODE = "episode"
    EPISODE_ID = EPISODE_ID
    EPISODE_TITLE = "episode.title"
    ID = "id"
    INDEXER = "indexer"
    LANGUAGE = "language"
    MESSAGE = "message"
    PATH = PATH
    PROGRESS = "progress"
    PROTOCOL = "protocol"
    QUALITY = "quality"
    RATINGS = "ratings"
    SERIES_ID = SERIES_ID
    SERIES_TITLE = "series.sortTitle"
    SIZE = "size"
    SOURCE_TITLE = "sourcetitle"
    STATUS = "status"
    TIMELEFT = "timeleft"


@dataclass(init=False)
class SonarrCalendar(_SonarrWantedMissingRecord, _SonarrCommon2):
    """Sonarr calendar attributes."""

    series: _SonarrSeries2 | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class SonarrEpisode(_SonarrCommon):
    """Sonarr episode attributes."""

    series: _SonarrSeriesCommon | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeriesCommon(self.series) or {}


@dataclass(init=False)
class SonarrEpisodeFile(_SonarrEpisodeFile):
    """Sonarr episode file attributes."""


@dataclass(init=False)
class SonarrEpisodeHistory(_Common2, _QualityCommon):
    """Sonarr history record attributes."""

    data: _SonarrEpisodeHistoryData | None = None
    date: datetime | None = None
    episodeId: int | None = None
    id: int | None = None
    language: _Common3 | None = None
    languageCutoffNotMet: bool | None = None
    seriesId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _SonarrEpisodeHistoryData(self.data) or {}
        self.language = _Common3(self.language) or {}


@dataclass(init=False)
class SonarrHistory(_RecordCommon):
    """Sonarr history attributes."""

    records: list[SonarrEpisodeHistory] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrEpisodeHistory(record) for record in self.records or []]


@dataclass(init=False)
class SonarrWantedMissing(_RecordCommon):
    """Sonarr wanted missing attributes."""

    records: list[_SonarrWantedMissingRecord] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [
            _SonarrWantedMissingRecord(record) for record in self.records or []
        ]


@dataclass(init=False)
class SonarrQueue(_RecordCommon):
    """Sonarr queue attributes."""

    records: list[SonarrQueueDetail] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [SonarrQueueDetail(record) for record in self.records or []]


@dataclass(init=False)
class SonarrParse(BaseModel):
    """Sonarr parse attributes."""

    episodes: list[SonarrEpisode] | None = None
    parsedEpisodeInfo: _SonarrParseEpisodeInfo | None = None
    series: _SonarrSeries2 | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.episodes = [SonarrEpisode(episode) for episode in self.episodes or []]
        self.parsedEpisodeInfo = _SonarrParseEpisodeInfo(self.parsedEpisodeInfo) or {}
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class _SonarrSceneMapping(BaseModel):
    """Sonarr scene mapping attributes."""

    title: str | None = None
    seasonNumber: int | None = None


@dataclass(init=False)
class SonarrRelease(_ReleaseCommon):
    """Sonarr release attributes."""

    absoluteEpisodeNumbers: list[int] | None = None
    episodeNumbers: list[int] | None = None
    episodeRequested: bool | None = None
    fullSeason: bool | None = None
    isAbsoluteNumbering: bool | None = None
    isDaily: bool | None = None
    isPossibleSpecialEpisode: bool | None = None
    language: _Common3 | None = None
    languageWeight: int | None = None
    mappedAbsoluteEpisodeNumbers: list[int] | None = None
    mappedEpisodeNumbers: list[int] | None = None
    mappedSeasonNumber: int | None = None
    preferredWordScore: int | None = None
    quality: _Quality | None = None
    rejected: bool | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    releaseWeight: int | None = None
    sceneMapping: _SonarrSceneMapping | None = None
    seasonNumber: int | None = None
    seriesTitle: str | None = None
    special: bool | None = None
    tvdbId: int | None = None
    tvRageId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}
        self.sceneMapping = _SonarrSceneMapping(self.sceneMapping) or {}


@dataclass(init=False)
class SonarrSeries(_SonarrSeriesCommon):
    """Sonarr series attributes."""

    alternateTitles: list[_SonarrSeriesAlternateTitle] | None = None
    rootFolderPath: str | None = None
    previousAiring: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _SonarrSeriesAlternateTitle(altTit) for altTit in self.alternateTitles or []
        ]


@dataclass(init=False)
class SonarrSeriesAdd(SonarrSeries):
    """Sonarr series add attributes."""

    addOptions: _SonarrAddOptions | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _SonarrAddOptions(self.addOptions) or {}


@dataclass(init=False)
class SonarrSeriesLookup(_SonarrSeriesCommon):
    """Sonarr series lookup attributes."""


@dataclass(init=False)
class SonarrBlocklistSeries(_Common7):
    """Sonarr blocklist series attributes."""

    date: datetime | None = None
    episodeIds: list[int] | None = None
    language: _Common3 | None = None
    message: str | None = None
    quality: _Quality | None = None
    seriesId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class SonarrBlocklist(_RecordCommon):
    """Sonarr blocklist attributes."""

    records: list[SonarrBlocklistSeries] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrBlocklistSeries(record) for record in self.records or []]


@dataclass(init=False)
class SonarrNamingConfig(BaseModel):
    """Sonarr naming config attributes."""

    animeEpisodeFormat: str | None = None
    dailyEpisodeFormat: str | None = None
    id: int | None = None
    includeEpisodeTitle: bool | None = None
    includeQuality: bool | None = None
    includeSeriesTitle: bool | None = None
    multiEpisodeStyle: int | None = None
    numberStyle: str | None = None
    renameEpisodes: bool | None = None
    replaceIllegalCharacters: bool | None = None
    replaceSpaces: bool | None = None
    seasonFolderFormat: str | None = None
    separator: str | None = None
    seriesFolderFormat: str | None = None
    specialsFolderFormat: str | None = None
    standardEpisodeFormat: str | None = None


@dataclass(init=False)
class SonarrNotification(_Common3, _Notification):
    """Sonarr notification attributes."""

    fields: list[_Fields] | None = None
    onEpisodeFileDelete: bool | None = None
    onEpisodeFileDeleteForUpgrade: bool | None = None
    onSeriesDelete: bool | None = None
    supportsOnEpisodeFileDelete: bool | None = None
    supportsOnEpisodeFileDeleteForUpgrade: bool | None = None
    supportsOnSeriesDelete: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrQueueDetail(_Common4, _Common8):
    """Sonarr queue detail attributes."""

    episode: _SonarrCommon | None = None
    episodeId: int | None = None
    language: _Common3 | None = None
    series: _SonarrSeries2 | None = None
    seriesId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}
        self.episode = _SonarrCommon(self.episode) or {}
        self.language = _Common3(self.language) or {}
        self.series = _SonarrSeries2(self.series) or {}
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class SonarrRename(_Rename):
    """Sonarr rename attributes."""

    episodeFileId: int | None = None
    episodeNumbers: list[int] | None = None
    seasonNumber: int | None = None
    seriesId: int | None = None


@dataclass(init=False)
class SonarrTagDetails(_TagDetails):
    """Sonarr tag details attributes."""

    indexerIds: list[int] | None = None
    seriesIds: list[int] | None = None


@dataclass(init=False)
class SonarrImportList(_ImportListCommon, _Common3):
    """Sonarr importlist attributes."""

    enableAutomaticAdd: bool | None = None
    fields: list[_Fields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    languageProfileId: int | None = None
    listType: str | None = None
    qualityProfileId: int | None = None
    seasonFolder: bool | None = None
    seriesType: str | None = None
    shouldMonitor: str | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrManualImport(_ManualImport):
    """Sonarr manual import attributes."""

    episodes: list[SonarrEpisodeMonitor] | None = None
    folderName: str | None = None
    language: _Common3 | None = None
    relativePath: str | None = None
    seasonNumber: int | None = None
    series: _SonarrSeries2 | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.episodes = [
            SonarrEpisodeMonitor(episode) for episode in self.episodes or []
        ]
        self.language = _Common3(self.language) or {}
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class SonarrSeasonPass(BaseModel):
    """Sonarr season pass attributes."""

    monitoringOptions: _MonitorOption | None = None
    series: list[_Monitor] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.monitoringOptions = _MonitorOption(self.monitoringOptions) or {}
        self.series = [_Monitor(x) for x in self.series or []]


@dataclass(init=False)
class SonarrLanguage(BaseModel):
    """Sonarr launguage attributes."""

    cutoff: _Common3 | None = None
    id: int | None = None
    languages: list[_SonarrLanguageItem] | None = None
    name: str | None = None
    upgradeAllowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.cutoff = _Common3(self.cutoff) or {}
        self.languages = [_SonarrLanguageItem(x) for x in self.languages or []]


@dataclass(init=False)
class SonarrEpisodeMonitor(_SonarrEpisodeMonitor):
    """Sonarr episode monitor attributes."""
