"""Sonarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import BaseModel, get_time_from_string
from .common import _RecordCommon

from .sonarr_common import (  # isort:skip
    _FileEpisodeQuality,
    _SonarrBlocklistSeriesLanguage,
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

    downloading: bool | None = None
    series: SonarrSeries | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    tvDbEpisodeId: int | None = None
    unverifiedSceneNumbering: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = SonarrSeries(self.series) or {}


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
class SonarrQueue(_SonarrCommon6):
    """Sonarr queue attributes."""

    downloadId: str | None = None
    episode: _SonarrHistoryRecordEpisode | None = None
    estimatedCompletionTime: datetime | None = None
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
        self.episode = _SonarrHistoryRecordEpisode(self.episode) or {}
        self.estimatedCompletionTime = get_time_from_string(
            self.estimatedCompletionTime
        )
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
        self.parsedEpisodeInfo = _SonarrParseEpisodeInfo(self.parsedEpisodeInfo) or {}


@dataclass(init=False)
class SonarrQualityProfile(_SonarrCommon4):
    """Sonarr quality profile attributes."""

    cutoff: _SonarrCutoff | None = None
    items: list[_SonarrQualityProfileValueItems] | None = None


@dataclass(init=False)
class SonarrRelease(_SonarrCommon3, _SonarrCommon7):
    """Sonarr release attributes."""

    publishDate: datetime | None = None

    def __post_init__(self):
        super().__post_init__()
        self.publishDate = get_time_from_string(self.publishDate)


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

    remotePoster: str | None = None


@dataclass(init=False)
class SonarrSeriesUpdateParams(_SonarrSeriesCommon3):
    """Sonarr series update parameters."""

    profileId: int | None = None
    seasons: list[_SonarrWantedMissingSeriesSeason] | None = None


@dataclass(init=False)
class SonarrBlocklistSeries(BaseModel):
    """Blocklist series attributes."""

    date: datetime | None = None
    episodeIds: list[int] | None = None
    id: int | None = None
    indexer: str | None = None
    language: _SonarrBlocklistSeriesLanguage | None = None
    message: str | None = None
    protocol: str | None = None
    quality: _SonarrQualitySub | None = None
    seriesId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        self.date = get_time_from_string(self.date)
        self.language = _SonarrBlocklistSeriesLanguage(self.language) or {}
        self.quality = _SonarrQualitySub(self.quality) or {}


@dataclass(init=False)
class SonarrBlocklist(_RecordCommon):
    """Blocklist attributes."""

    records: list[SonarrBlocklistSeries] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [SonarrBlocklistSeries(record) for record in self.records or []]
