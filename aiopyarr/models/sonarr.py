"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

import attr

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


@dataclass(init=False)
class SonarrEpisode(_SonarrCommon):
    """Sonarr episode attributes."""

    series: _SonarrSeriesCommon = attr.ib(type=_SonarrSeriesCommon)

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

    data: _SonarrEpisodeHistoryData = attr.ib(type=_SonarrEpisodeHistoryData)
    date: datetime = attr.ib(type=datetime)
    episodeId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    language: _Common3 = attr.ib(type=_Common3)
    languageCutoffNotMet: bool = attr.ib(type=bool)
    seriesId: int = attr.ib(type=int)
    sourceTitle: str = attr.ib(type=str)

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

    records: list[_SonarrWantedMissingRecord] = field(
        default_factory=list[_SonarrWantedMissingRecord]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [
            _SonarrWantedMissingRecord(record) for record in self.records or []
        ]


@dataclass(init=False)
class SonarrQueueDetail(_Common4, _Common8):
    """Sonarr queue detail attributes."""

    episode: _SonarrCommon = attr.ib(type=_SonarrCommon)
    episodeId: int = attr.ib(type=int)
    language: _Common3 = attr.ib(type=_Common3)
    series: _SonarrSeries2 = attr.ib(type=_SonarrSeries2)
    seriesId: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}
        self.episode = _SonarrCommon(self.episode) or {}
        self.language = _Common3(self.language) or {}
        self.series = _SonarrSeries2(self.series) or {}
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class SonarrQueue(_RecordCommon):
    """Sonarr queue attributes."""

    records: list[SonarrQueueDetail] = field(default_factory=list[SonarrQueueDetail])

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [SonarrQueueDetail(record) for record in self.records or []]


@dataclass(init=False)
class SonarrParse(BaseModel):
    """Sonarr parse attributes."""

    episodes: list[SonarrEpisode] = field(default_factory=list[SonarrEpisode])
    parsedEpisodeInfo: _SonarrParseEpisodeInfo = attr.ib(type=_SonarrParseEpisodeInfo)
    series: _SonarrSeries2 = attr.ib(type=_SonarrSeries2)
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.episodes = [SonarrEpisode(episode) for episode in self.episodes or []]
        self.parsedEpisodeInfo = _SonarrParseEpisodeInfo(self.parsedEpisodeInfo) or {}
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class _SonarrSceneMapping(BaseModel):
    """Sonarr scene mapping attributes."""

    title: str = attr.ib(type=str)
    seasonNumber: int = attr.ib(type=int)


@dataclass(init=False)
class SonarrRelease(_ReleaseCommon):
    """Sonarr release attributes."""

    absoluteEpisodeNumbers: list[int] = attr.ib(type=list[int])
    episodeNumbers: list[int] = attr.ib(type=list[int])
    episodeRequested: bool = attr.ib(type=bool)
    fullSeason: bool = attr.ib(type=bool)
    isAbsoluteNumbering: bool = attr.ib(type=bool)
    isDaily: bool = attr.ib(type=bool)
    isPossibleSpecialEpisode: bool = attr.ib(type=bool)
    language: _Common3 = attr.ib(type=_Common3)
    languageWeight: int = attr.ib(type=int)
    mappedAbsoluteEpisodeNumbers: list[int] = attr.ib(type=list[int])
    mappedEpisodeNumbers: list[int] = attr.ib(type=list[int])
    mappedSeasonNumber: int = attr.ib(type=int)
    preferredWordScore: int = attr.ib(type=int)
    quality: _Quality = attr.ib(type=_Quality)
    rejected: bool = attr.ib(type=bool)
    releaseGroup: str = attr.ib(type=str)
    releaseHash: str = attr.ib(type=str)
    releaseWeight: int = attr.ib(type=int)
    sceneMapping: _SonarrSceneMapping = attr.ib(type=_SonarrSceneMapping)
    seasonNumber: int = attr.ib(type=int)
    seriesTitle: str = attr.ib(type=str)
    special: bool = attr.ib(type=bool)
    tvdbId: int = attr.ib(type=int)
    tvRageId: int = attr.ib(type=int)

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
    rootFolderPath: str = attr.ib(type=str)
    previousAiring: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _SonarrSeriesAlternateTitle(altTit) for altTit in self.alternateTitles or []
        ]


@dataclass(init=False)
class SonarrSeriesAdd(SonarrSeries):
    """Sonarr series add attributes."""

    addOptions: _SonarrAddOptions = attr.ib(type=_SonarrAddOptions)

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

    date: datetime = attr.ib(type=datetime)
    episodeIds: list[int] = attr.ib(type=list[int])
    language: _Common3 = attr.ib(type=_Common3)
    message: str = attr.ib(type=str)
    quality: _Quality = attr.ib(type=_Quality)
    seriesId: int = attr.ib(type=int)
    sourceTitle: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class SonarrBlocklist(_RecordCommon):
    """Sonarr blocklist attributes."""

    records: list[SonarrBlocklistSeries] = field(
        default_factory=list[SonarrBlocklistSeries]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrBlocklistSeries(record) for record in self.records or []]


@dataclass(init=False)
class SonarrNamingConfig(BaseModel):
    """Sonarr naming config attributes."""

    animeEpisodeFormat: str = attr.ib(type=str)
    dailyEpisodeFormat: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    includeEpisodeTitle: bool = attr.ib(type=bool)
    includeQuality: bool = attr.ib(type=bool)
    includeSeriesTitle: bool = attr.ib(type=bool)
    multiEpisodeStyle: int = attr.ib(type=int)
    numberStyle: str = attr.ib(type=str)
    renameEpisodes: bool = attr.ib(type=bool)
    replaceIllegalCharacters: bool = attr.ib(type=bool)
    replaceSpaces: bool = attr.ib(type=bool)
    seasonFolderFormat: str = attr.ib(type=str)
    separator: str = attr.ib(type=str)
    seriesFolderFormat: str = attr.ib(type=str)
    specialsFolderFormat: str = attr.ib(type=str)
    standardEpisodeFormat: str = attr.ib(type=str)


@dataclass(init=False)
class SonarrNotification(_Common3, _Notification):
    """Sonarr notification attributes."""

    fields: list[_Fields] | None = None
    onEpisodeFileDelete: bool = attr.ib(type=bool)
    onEpisodeFileDeleteForUpgrade: bool = attr.ib(type=bool)
    onSeriesDelete: bool = attr.ib(type=bool)
    supportsOnEpisodeFileDelete: bool = attr.ib(type=bool)
    supportsOnEpisodeFileDeleteForUpgrade: bool = attr.ib(type=bool)
    supportsOnSeriesDelete: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrRename(_Rename):
    """Sonarr rename attributes."""

    episodeFileId: int = attr.ib(type=int)
    episodeNumbers: list[int] = attr.ib(type=list[int])
    seasonNumber: int = attr.ib(type=int)
    seriesId: int = attr.ib(type=int)


@dataclass(init=False)
class SonarrTagDetails(_TagDetails):
    """Sonarr tag details attributes."""

    indexerIds: list[int] = attr.ib(type=list[int])
    seriesIds: list[int] = attr.ib(type=list[int])


@dataclass(init=False)
class SonarrImportList(_ImportListCommon, _Common3):
    """Sonarr importlist attributes."""

    enableAutomaticAdd: bool = attr.ib(type=bool)
    fields: list[_Fields] | None = None
    implementation: str = attr.ib(type=str)
    implementationName: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    languageProfileId: int = attr.ib(type=int)
    listType: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    seasonFolder: bool = attr.ib(type=bool)
    seriesType: str = attr.ib(type=str)
    shouldMonitor: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type=list[int])

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrManualImport(_ManualImport):
    """Sonarr manual import attributes."""

    episodes: list[SonarrEpisodeMonitor] | None = None
    folderName: str = attr.ib(type=str)
    language: _Common3 = attr.ib(type=_Common3)
    relativePath: str = attr.ib(type=str)
    seasonNumber: int = attr.ib(type=int)
    series: _SonarrSeries2 = attr.ib(type=_SonarrSeries2)

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

    monitoringOptions: _MonitorOption = attr.ib(type=_MonitorOption)
    series: list[_Monitor] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.monitoringOptions = _MonitorOption(self.monitoringOptions) or {}
        self.series = [_Monitor(x) for x in self.series or []]


@dataclass(init=False)
class SonarrLanguage(BaseModel):
    """Sonarr launguage attributes."""

    cutoff: _Common3 = attr.ib(type=_Common3)
    id: int = attr.ib(type=int)
    languages: list[_SonarrLanguageItem] | None = None
    name: str = attr.ib(type=str)
    upgradeAllowed: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.cutoff = _Common3(self.cutoff) or {}
        self.languages = [_SonarrLanguageItem(x) for x in self.languages or []]


@dataclass(init=False)
class SonarrEpisodeMonitor(_SonarrEpisodeMonitor):
    """Sonarr episode monitor attributes."""
