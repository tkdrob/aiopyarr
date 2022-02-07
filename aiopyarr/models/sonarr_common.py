"""Sonarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-few-public-methods
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import attr

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

    seasonNumber: int = attr.ib(type=int)
    title: str = attr.ib(type=str)


@dataclass(init=False)
class _SonarrCommon2(_SonarrSeriesAlternateTitle, _Common6):
    """Sonarr common attributes."""

    airDate: datetime = attr.ib(type=datetime)
    airDateUtc: datetime = attr.ib(type=datetime)
    episodeFileId: int = attr.ib(type=int)
    episodeNumber: int = attr.ib(type=int)
    hasFile: bool = attr.ib(type=bool)
    id: int = attr.ib(type=int)
    seriesId: int = attr.ib(type=int)


@dataclass(init=False)
class _SonarrQualityProfileValueAttr(_Common3):
    """Sonarr quality profile value attributes."""

    weight: int = attr.ib(type=int)


@dataclass(init=False)
class _SonarrImages(_Common5):
    """Sonarr images attributes."""

    remoteUrl: str = attr.ib(type=str)


@dataclass(init=False)
class _SonarrSeries2(_Common6, _Common9):
    """Sonarr parse attributes."""

    added: datetime = attr.ib(type=datetime)
    airTime: str = attr.ib(type=str)
    cleanTitle: str = attr.ib(type=str)
    ended: bool = attr.ib(type=bool)
    firstAired: datetime = attr.ib(type=datetime)
    folder: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    images: list[_SonarrImages] | None = None
    languageProfileId: int = attr.ib(type=int)
    lastInfoSync: datetime = attr.ib(type=datetime)
    network: str = attr.ib(type=str)
    path: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    ratings: _Ratings = attr.ib(type=_Ratings)
    seasonFolder: bool = attr.ib(type=bool)
    seasons: list[_SonarrSeriesSeason] | None = None
    seriesType: str = attr.ib(type=str)
    sortTitle: str = attr.ib(type=str)
    status: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type="list[int]")
    titleSlug: int = attr.ib(type=int)
    tvdbId: int = attr.ib(type=int)
    tvMazeId: int = attr.ib(type=int)
    tvRageId: int = attr.ib(type=int)
    useSceneNumbering: bool = attr.ib(type=bool)

    def __post_init__(self):
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.ratings = _Ratings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]


@dataclass(init=False)
class _SonarrEpisodeFile(_QualityCommon):
    """Sonarr episode file attributes."""

    dateAdded: datetime = attr.ib(type=datetime)
    id: int = attr.ib(type=int)
    language: _SonarrQualityProfileValueAttr = attr.ib(
        type=_SonarrQualityProfileValueAttr
    )
    languageCutoffNotMet: bool = attr.ib(type=bool)
    mediaInfo: _CommonAttrs = attr.ib(type=_CommonAttrs)
    path: str = attr.ib(type=str)
    relativePath: str = attr.ib(type=str)
    releaseGroup: str = attr.ib(type=str)
    seasonNumber: int = attr.ib(type=int)
    seriesId: int = attr.ib(type=int)
    size: int = attr.ib(type=int)

    def __post_init__(self):
        super().__post_init__()
        self.language = _SonarrQualityProfileValueAttr(self.language) or {}
        self.mediaInfo = _CommonAttrs(self.mediaInfo) or {}


@dataclass(init=False)
class _SonarrEpisodeMonitor(_SonarrCommon2):
    """Sonarr common attributes."""

    absoluteEpisodeNumber: int = attr.ib(type=int)
    unverifiedSceneNumbering: bool = attr.ib(type=bool)


@dataclass(init=False)
class _SonarrCommon(_SonarrEpisodeMonitor):
    """Sonarr common attributes."""

    episodeFile: _SonarrEpisodeFile = attr.ib(type=_SonarrEpisodeFile)

    def __post_init__(self):
        super().__post_init__()
        self.episodeFile = _SonarrEpisodeFile(self.episodeFile) or {}


@dataclass(init=False)
class _SonarrEpisodeHistoryData(_Common4, _HistoryCommon):
    """Sonarr history record data attributes."""

    approved: bool = attr.ib(type=bool)
    downloadAllowed: bool = attr.ib(type=bool)
    downloadClientName: str = attr.ib(type=str)
    droppedPath: str = attr.ib(type=str)
    fileId: int = attr.ib(type=int)
    guid: str = attr.ib(type=str)
    importedPath: str = attr.ib(type=str)
    indexerId: int = attr.ib(type=int)
    preferredWordScore: int = attr.ib(type=int)
    qualityWeight: int = attr.ib(type=int)
    rejections: list[str] = attr.ib(type="list[str]")
    sceneSource: bool = attr.ib(type=bool)
    seasonNumber: int = attr.ib(type=int)
    title: str = attr.ib(type=str)
    tvdbId: str = attr.ib(type=str)
    tvRageId: int = attr.ib(type=int)


@dataclass(init=False)
class _SonarrSeasonStatistics(BaseModel):
    """Sonarr season statistics attributes."""

    episodeCount: int = attr.ib(type=int)
    episodeFileCount: int = attr.ib(type=int)
    percentOfEpisodes: float = attr.ib(type=float)
    previousAiring: str | None = None
    seasonCount: int = attr.ib(type=int)
    sizeOnDisk: int = attr.ib(type=int)
    totalEpisodeCount: int = attr.ib(type=int)

    def __post_init__(self):
        self.previousAiring = get_datetime(self.previousAiring)


@dataclass(init=False)
class _SonarrSeriesSeason(BaseModel):
    """Sonarr wanted missing series season attributes."""

    monitored: bool = attr.ib(type=bool)
    seasonNumber: int = attr.ib(type=int)
    statistics: _SonarrSeasonStatistics = attr.ib(type=_SonarrSeasonStatistics)

    def __post_init__(self):
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrSeriesCommon(_SonarrSeries2):
    """Sonarr series common attributes."""

    images: list[_SonarrImages] | None = None
    remotePoster: str = attr.ib(type=str)
    seasons: list[_SonarrSeriesSeason] | None = None
    statistics: _SonarrSeasonStatistics = attr.ib(type=_SonarrSeasonStatistics)

    def __post_init__(self):
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.ratings = _Ratings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrWantedMissingRecord(_SonarrCommon):
    """Sonarr wanted missing record attributes."""

    downloading: bool = attr.ib(type=bool)
    sceneEpisodeNumber: int = attr.ib(type=int)
    sceneSeasonNumber: int = attr.ib(type=int)
    series: _SonarrSeries2 = attr.ib(type=_SonarrSeries2)
    tvDbEpisodeId: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class _SonarrParseEpisodeInfo(BaseModel):
    """Sonarr parse episode info attributes."""

    absoluteEpisodeNumbers: list[int] = attr.ib(type="list[int]")
    episodeNumbers: list[int] = attr.ib(type="list[int]")
    fullSeason: bool = attr.ib(type=bool)
    isAbsoluteNumbering: bool = attr.ib(type=bool)
    isDaily: bool = attr.ib(type=bool)
    isMultiSeason: bool = attr.ib(type=bool)
    isPartialSeason: bool = attr.ib(type=bool)
    isPossibleSceneSeasonSpecial: bool = attr.ib(type=bool)
    isPossibleSpecialEpisode: bool = attr.ib(type=bool)
    isSeasonExtra: bool = attr.ib(type=bool)
    language: _Common3 = attr.ib(type=_Common3)
    quality: _Quality = attr.ib(type=_Quality)
    releaseGroup: str = attr.ib(type=str)
    releaseHash: str = attr.ib(type=str)
    releaseTitle: str = attr.ib(type=str)
    releaseTokens: str = attr.ib(type=str)
    seasonNumber: int = attr.ib(type=int)
    seasonPart: int = attr.ib(type=int)
    seriesTitle: str = attr.ib(type=str)
    seriesTitleInfo: _TitleInfo = attr.ib(type=_TitleInfo)
    special: bool = attr.ib(type=bool)
    specialAbsoluteEpisodeNumbers: list[int] = attr.ib(type="list[int]")

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

    language: _Common3 = attr.ib(type=_Common3)
    allowed: bool = attr.ib(type=bool)

    def __post_init__(self):
        self.language = _Common3(self.language) or {}
