"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
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

    AIR_DATE_UTC = "airDateUtc"
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

    series: type[_SonarrSeriesCommon] = field(default=_SonarrSeriesCommon)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeriesCommon(self.series)


@dataclass(init=False)
class SonarrEpisodeFile(_SonarrEpisodeFile):
    """Sonarr episode file attributes."""


@dataclass(init=False)
class SonarrEpisodeHistory(_Common2, _QualityCommon):
    """Sonarr history record attributes."""

    data: type[_SonarrEpisodeHistoryData] = field(default=_SonarrEpisodeHistoryData)
    date: datetime
    episodeId: int
    id: int
    language: type[_Common3] = field(default=_Common3)
    languageCutoffNotMet: bool
    seriesId: int
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.data = _SonarrEpisodeHistoryData(self.data)
        self.language = _Common3(self.language)


@dataclass(init=False)
class SonarrHistory(_RecordCommon):
    """Sonarr history attributes."""

    records: list[SonarrEpisodeHistory] = field(
        default_factory=list[SonarrEpisodeHistory]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrEpisodeHistory(record) for record in self.records]


@dataclass(init=False)
class SonarrWantedMissing(_RecordCommon):
    """Sonarr wanted missing attributes."""

    records: list[_SonarrWantedMissingRecord] = field(
        default_factory=list[_SonarrWantedMissingRecord]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [_SonarrWantedMissingRecord(record) for record in self.records]


@dataclass(init=False)
class SonarrQueueDetail(_Common4, _Common8):
    """Sonarr queue detail attributes."""

    episode: type[_SonarrCommon] = field(default=_SonarrCommon)
    episodeId: int
    language: type[_Common3] = field(default=_Common3)
    series: type[_SonarrSeries2] = field(default=_SonarrSeries2)
    seriesId: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality)
        self.episode = _SonarrCommon(self.episode)
        self.language = _Common3(self.language)
        self.series = _SonarrSeries2(self.series)
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class SonarrQueue(_RecordCommon):
    """Sonarr queue attributes."""

    records: list[SonarrQueueDetail] = field(default_factory=list[SonarrQueueDetail])

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [SonarrQueueDetail(record) for record in self.records]


@dataclass(init=False)
class SonarrParse(BaseModel):
    """Sonarr parse attributes."""

    episodes: list[SonarrEpisode] | None = None
    parsedEpisodeInfo: type[_SonarrParseEpisodeInfo] = field(
        default=_SonarrParseEpisodeInfo
    )
    series: type[_SonarrSeries2] = field(default=_SonarrSeries2)
    title: str

    def __post_init__(self):
        """Post init."""
        self.episodes = [SonarrEpisode(episode) for episode in self.episodes or []]
        self.parsedEpisodeInfo = _SonarrParseEpisodeInfo(self.parsedEpisodeInfo)
        self.series = _SonarrSeries2(self.series)


@dataclass(init=False)
class _SonarrSceneMapping(BaseModel):
    """Sonarr scene mapping attributes."""

    title: str
    seasonNumber: int


@dataclass(init=False)
class SonarrRelease(_ReleaseCommon):
    """Sonarr release attributes."""

    absoluteEpisodeNumbers: list[int]
    episodeNumbers: list[int]
    episodeRequested: bool
    fullSeason: bool
    isAbsoluteNumbering: bool
    isDaily: bool
    isPossibleSpecialEpisode: bool
    language: type[_Common3] = field(default=_Common3)
    languageWeight: int
    mappedAbsoluteEpisodeNumbers: list[int]
    mappedEpisodeNumbers: list[int]
    mappedSeasonNumber: int
    preferredWordScore: int
    quality: type[_Quality] = field(default=_Quality)
    rejected: bool
    releaseGroup: str
    releaseHash: str
    releaseWeight: int
    sceneMapping: type[_SonarrSceneMapping] = field(default=_SonarrSceneMapping)
    seasonNumber: int
    seriesTitle: str
    special: bool
    tvdbId: int
    tvRageId: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language)
        self.quality = _Quality(self.quality)
        self.sceneMapping = _SonarrSceneMapping(self.sceneMapping)


@dataclass(init=False)
class SonarrSeries(_SonarrSeriesCommon):
    """Sonarr series attributes."""

    alternateTitles: list[_SonarrSeriesAlternateTitle] | None = None
    rootFolderPath: str
    previousAiring: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _SonarrSeriesAlternateTitle(altTit) for altTit in self.alternateTitles or []
        ]


@dataclass(init=False)
class SonarrSeriesAdd(SonarrSeries):
    """Sonarr series add attributes."""

    addOptions: type[_SonarrAddOptions] = field(default=_SonarrAddOptions)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _SonarrAddOptions(self.addOptions)


@dataclass(init=False)
class SonarrSeriesLookup(_SonarrSeriesCommon):
    """Sonarr series lookup attributes."""


@dataclass(init=False)
class SonarrBlocklistSeries(_Common7):
    """Sonarr blocklist series attributes."""

    date: datetime
    episodeIds: list[int]
    language: type[_Common3] = field(default=_Common3)
    message: str
    quality: type[_Quality] = field(default=_Quality)
    seriesId: int
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _Common3(self.language)
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class SonarrBlocklist(_RecordCommon):
    """Sonarr blocklist attributes."""

    records: list[SonarrBlocklistSeries] = field(
        default_factory=list[SonarrBlocklistSeries]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrBlocklistSeries(record) for record in self.records]


@dataclass(init=False)
class SonarrNamingConfig(BaseModel):
    """Sonarr naming config attributes."""

    animeEpisodeFormat: str
    dailyEpisodeFormat: str
    id: int
    includeEpisodeTitle: bool
    includeQuality: bool
    includeSeriesTitle: bool
    multiEpisodeStyle: int
    numberStyle: str
    renameEpisodes: bool
    replaceIllegalCharacters: bool
    replaceSpaces: bool
    seasonFolderFormat: str
    separator: str
    seriesFolderFormat: str
    specialsFolderFormat: str
    standardEpisodeFormat: str


@dataclass(init=False)
class SonarrNotification(_Common3, _Notification):
    """Sonarr notification attributes."""

    fields: list[_Fields] | None = None
    onEpisodeFileDelete: bool
    onEpisodeFileDeleteForUpgrade: bool
    onSeriesDelete: bool
    supportsOnEpisodeFileDelete: bool
    supportsOnEpisodeFileDeleteForUpgrade: bool
    supportsOnSeriesDelete: bool

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrRename(_Rename):
    """Sonarr rename attributes."""

    episodeFileId: int
    episodeNumbers: list[int]
    seasonNumber: int
    seriesId: int


@dataclass(init=False)
class SonarrTagDetails(_TagDetails):
    """Sonarr tag details attributes."""

    indexerIds: list[int]
    seriesIds: list[int]


@dataclass(init=False)
class SonarrImportList(_ImportListCommon, _Common3):
    """Sonarr importlist attributes."""

    enableAutomaticAdd: bool
    fields: list[_Fields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    languageProfileId: int
    listType: str
    qualityProfileId: int
    seasonFolder: bool
    seriesType: str
    shouldMonitor: str
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class SonarrManualImport(_ManualImport):
    """Sonarr manual import attributes."""

    episodes: list[SonarrEpisodeMonitor] | None = None
    folderName: str
    language: type[_Common3] = field(default=_Common3)
    relativePath: str
    seasonNumber: int
    series: type[_SonarrSeries2] = field(default=_SonarrSeries2)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.episodes = [
            SonarrEpisodeMonitor(episode) for episode in self.episodes or []
        ]
        self.language = _Common3(self.language)
        self.series = _SonarrSeries2(self.series)


@dataclass(init=False)
class SonarrSeasonPass(BaseModel):
    """Sonarr season pass attributes."""

    monitoringOptions: type[_MonitorOption] = field(default=_MonitorOption)
    series: list[_Monitor] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.monitoringOptions = _MonitorOption(self.monitoringOptions)
        self.series = [_Monitor(x) for x in self.series or []]


@dataclass(init=False)
class SonarrLanguage(BaseModel):
    """Sonarr launguage attributes."""

    cutoff: type[_Common3] = field(default=_Common3)
    id: int
    languages: list[_SonarrLanguageItem] | None = None
    name: str
    upgradeAllowed: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.cutoff = _Common3(self.cutoff)
        self.languages = [_SonarrLanguageItem(x) for x in self.languages or []]


@dataclass(init=False)
class SonarrEpisodeMonitor(_SonarrEpisodeMonitor):
    """Sonarr episode monitor attributes."""
