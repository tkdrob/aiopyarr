"""Sonarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-few-public-methods
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import BaseModel, get_datetime
from .request_common import (
    _Common3,
    _Common4,
    _Common5,
    _Common6,
    _Common9,
    _CommonAttrs,
    _HistoryCommon,
    _Quality,
    _QualityCommon,
    _Ratings,
    _TitleInfo,
)


@dataclass(init=False)
class _SonarrSeriesAlternateTitle(BaseModel):
    """Sonarr series alternate titles attributes."""

    seasonNumber: int | None = None
    title: str | None = None


@dataclass(init=False)
class _SonarrCommon2(_SonarrSeriesAlternateTitle, _Common6):
    """Sonarr common attributes."""

    airDate: datetime | None = None
    airDateUtc: datetime | None = None
    episodeFileId: int | None = None
    episodeNumber: int | None = None
    hasFile: bool | None = None
    id: int | None = None
    seriesId: int | None = None


@dataclass(init=False)
class _SonarrQualityProfileValueAttr(_Common3):
    """Sonarr quality profile value attributes."""

    weight: int | None = None


@dataclass(init=False)
class _SonarrImages(_Common5):
    """Sonarr images attributes."""

    remoteUrl: str | None = None


@dataclass(init=False)
class _SonarrSeries2(_Common6, _Common9):
    """Sonarr parse attributes."""

    added: datetime | None = None
    airTime: str | None = None
    cleanTitle: str | None = None
    ended: bool | None = None
    firstAired: datetime | None = None
    folder: str | None = None
    id: int | None = None
    images: list[_SonarrImages] | None = None
    languageProfileId: int | None = None
    lastInfoSync: datetime | None = None
    network: str | None = None
    path: str | None = None
    qualityProfileId: int | None = None
    ratings: _Ratings | None = None
    seasonFolder: bool | None = None
    seasons: list[_SonarrSeriesSeason] | None = None
    seriesType: str | None = None
    sortTitle: str | None = None
    status: str | None = None
    tags: list[int | None] | None = None
    titleSlug: int | None = None
    tvdbId: int | None = None
    tvMazeId: int | None = None
    tvRageId: int | None = None
    useSceneNumbering: bool | None = None

    def __post_init__(self):
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.ratings = _Ratings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]


@dataclass(init=False)
class _SonarrEpisodeFile(_QualityCommon):
    """Sonarr episode file attributes."""

    dateAdded: datetime | None = None
    id: int | None = None
    language: _SonarrQualityProfileValueAttr | None = None
    languageCutoffNotMet: bool | None = None
    mediaInfo: _CommonAttrs | None = None
    path: str | None = None
    relativePath: str | None = None
    releaseGroup: str | None = None
    seasonNumber: int | None = None
    seriesId: int | None = None
    size: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.language = _SonarrQualityProfileValueAttr(self.language) or {}
        self.mediaInfo = _CommonAttrs(self.mediaInfo) or {}


@dataclass(init=False)
class _SonarrEpisodeMonitor(_SonarrCommon2):
    """Sonarr common attributes."""

    absoluteEpisodeNumber: int | None = None
    unverifiedSceneNumbering: bool | None = None


@dataclass(init=False)
class _SonarrCommon(_SonarrEpisodeMonitor):
    """Sonarr common attributes."""

    episodeFile: _SonarrEpisodeFile | None = None

    def __post_init__(self):
        super().__post_init__()
        self.episodeFile = _SonarrEpisodeFile(self.episodeFile) or {}


@dataclass(init=False)
class _SonarrEpisodeHistoryData(_Common4, _HistoryCommon):
    """Sonarr history record data attributes."""

    approved: bool | None = None
    downloadAllowed: bool | None = None
    downloadClientName: str | None = None
    droppedPath: str | None = None
    fileId: int | None = None
    guid: str | None = None
    importedPath: str | None = None
    indexerId: int | None = None
    preferredWordScore: int | None = None
    qualityWeight: int | None = None
    rejections: list[str] | None = None
    sceneSource: bool | None = None
    seasonNumber: int | None = None
    title: str | None = None
    tvdbId: str | None = None
    tvRageId: int | None = None


@dataclass(init=False)
class _SonarrSeasonStatistics(BaseModel):
    """Sonarr season statistics attributes."""

    episodeCount: int | None = None
    episodeFileCount: int | None = None
    percentOfEpisodes: float | None = None
    previousAiring: str | None = None
    seasonCount: int | None = None
    sizeOnDisk: int | None = None
    totalEpisodeCount: int | None = None

    def __post_init__(self):
        self.previousAiring = get_datetime(self.previousAiring)


@dataclass(init=False)
class _SonarrSeriesSeason(BaseModel):
    """Sonarr wanted missing series season attributes."""

    monitored: bool | None = None
    seasonNumber: int | None = None
    statistics: _SonarrSeasonStatistics | None = None

    def __post_init__(self):
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrSeriesCommon(_SonarrSeries2):
    """Sonarr series common attributes."""

    images: list[_SonarrImages] | None = None
    remotePoster: str | None = None
    seasons: list[_SonarrSeriesSeason] | None = None
    statistics: _SonarrSeasonStatistics | None = None

    def __post_init__(self):
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.ratings = _Ratings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrWantedMissingRecord(_SonarrCommon):
    """Sonarr wanted missing record attributes."""

    downloading: bool | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    series: _SonarrSeries2 | None = None
    tvDbEpisodeId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class _SonarrParseEpisodeInfo(BaseModel):
    """Sonarr parse episode info attributes."""

    absoluteEpisodeNumbers: list[int] | None = None
    episodeNumbers: list[int] | None = None
    fullSeason: bool | None = None
    isAbsoluteNumbering: bool | None = None
    isDaily: bool | None = None
    isMultiSeason: bool | None = None
    isPartialSeason: bool | None = None
    isPossibleSceneSeasonSpecial: bool | None = None
    isPossibleSpecialEpisode: bool | None = None
    isSeasonExtra: bool | None = None
    language: _Common3 | None = None
    quality: _Quality | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    releaseTitle: str | None = None
    releaseTokens: str | None = None
    seasonNumber: int | None = None
    seasonPart: int | None = None
    seriesTitle: str | None = None
    seriesTitleInfo: _TitleInfo | None = None
    special: bool | None = None
    specialAbsoluteEpisodeNumbers: list[int] | None = None

    def __post_init__(self):
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}
        self.seriesTitleInfo = _TitleInfo(self.seriesTitleInfo) or {}


@dataclass(init=False)
class _SonarrAddOptions(BaseModel):
    """Sonarr add options attributes."""

    ignoreEpisodesWithFiles: bool | None = None
    ignoreEpisodesWithoutFiles: bool | None = None
    searchForMissingEpisodes: bool | None = None


@dataclass(init=False)
class _SonarrLanguageItem(BaseModel):
    """Sonarr language item attributes."""

    language: _Common3 | None = None
    allowed: bool | None = None

    def __post_init__(self):
        self.language = _Common3(self.language) or {}
