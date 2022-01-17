"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .base import BaseModel

from .request_common import (  # isort:skip
    _Common3,
    _Common4,
    _Fields,
    _Notification,
    _Quality,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _TagDetails,
)

from .sonarr_common import (  # isort:skip
    _SonarrCommon,
    _SonarrCommon2,
    _SonarrEpisodeFile,
    _SonarrHistoryRecord,
    _SonarrParseEpisodeInfo,
    _SonarrSeriesAlternateTitle,
    _SonarrSeriesCommon,
    _SonarrSeries2,
    _SonarrStatusMesssage,
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


class SonarrEventType(str, Enum):
    """Sonarr event types."""

    DOWNLOAD_FAILED = "downloadFailed" #assumed
    EPISODE_DELETED = "episodeFileDeleted"
    GRABBED = "grabbed"
    IMPORTED = "downloadFolderImported"


@dataclass(init=False)
class SonarrCalendar(_SonarrWantedMissingRecord, _SonarrCommon2):
    """Sonarr calendar attributes."""

    unverifiedSceneNumbering: bool | None = None


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
class SonarrHistory(_RecordCommon):
    """Sonarr history attributes."""

    records: list[_SonarrHistoryRecord] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [_SonarrHistoryRecord(record) for record in self.records or []]


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
class SonarrSeriesLookup(_SonarrSeriesCommon):
    """Sonarr series lookup attributes."""


@dataclass(init=False)
class SonarrSeriesUpdateParams(BaseModel):
    """Sonarr series update parameters."""

    profileId: int | None = None
    title: str | None = None
    titleSlug: str | None = None
    tvdbId: int | None = None


@dataclass(init=False)
class SonarrBlocklistSeries(BaseModel):
    """Sonarr blocklist series attributes."""

    date: str | None = None
    episodeIds: list[int] | None = None
    id: int | None = None
    indexer: str | None = None
    language: _Common3 | None = None
    message: str | None = None
    protocol: str | None = None
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
class SonarrQueueDetail(_Common4):
    """Sonarr queue detail attributes."""

    episode: _SonarrCommon | None = None
    episodeId: int | None = None
    id: int | None = None
    language: _Common3 | None = None
    protocol: str | None = None
    quality: _Quality | None = None
    series: _SonarrSeries2 | None = None
    seriesId: int | None = None
    size: float | None = None
    sizeleft: float | None = None
    status: str | None = None
    statusMessages: list[_SonarrStatusMesssage] | None = None
    timeleft: str | None = None
    title: str | None = None
    trackedDownloadState: str | None = None
    trackedDownloadStatus: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.episode = _SonarrCommon(self.episode) or {}
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}
        self.series = _SonarrSeries2(self.series) or {}
        self.statusMessages = [
            _SonarrStatusMesssage(x) for x in self.statusMessages or []
        ]


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
class SonarrImportList(_Common3):
    """Sonarr importlist attributes."""

    configContract: str | None = None
    enableAutomaticAdd: bool | None = None
    fields: list[_Fields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    languageProfileId: int | None = None
    listOrder: int | None = None
    listType: str | None = None
    qualityProfileId: int | None = None
    rootFolderPath: str | None = None
    seasonFolder: bool | None = None
    seriesType: str | None = None
    shouldMonitor: str | None = None
    tags: list[int | None] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]
