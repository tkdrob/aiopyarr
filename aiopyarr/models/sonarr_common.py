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

    seasonNumber: int
    title: str


@dataclass(init=False)
class _SonarrCommon2(_SonarrSeriesAlternateTitle, _Common6):
    """Sonarr common attributes."""

    airDate: datetime
    airDateUtc: datetime
    episodeFileId: int
    episodeNumber: int
    hasFile: bool
    id: int
    seriesId: int


@dataclass(init=False)
class _SonarrQualityProfileValueAttr(_Common3):
    """Sonarr quality profile value attributes."""

    weight: int


@dataclass(init=False)
class _SonarrImages(_Common5):
    """Sonarr images attributes."""

    remoteUrl: str


@dataclass(init=False)
class _SonarrSeries2(_Common6, _Common9):
    """Sonarr parse attributes."""

    added: datetime
    airTime: str
    cleanTitle: str
    ended: bool
    firstAired: datetime
    folder: str
    id: int
    images: list[_SonarrImages] | None = None
    languageProfileId: int
    lastInfoSync: datetime
    network: str
    path: str
    qualityProfileId: int
    ratings: _Ratings | None = None
    seasonFolder: bool
    seasons: list[_SonarrSeriesSeason] | None = None
    seriesType: str
    sortTitle: str
    status: str
    tags: list[int]
    titleSlug: int
    tvdbId: int
    tvMazeId: int
    tvRageId: int
    useSceneNumbering: bool

    def __post_init__(self):
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.ratings = _Ratings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]


@dataclass(init=False)
class _SonarrEpisodeFile(_QualityCommon):
    """Sonarr episode file attributes."""

    dateAdded: datetime
    id: int
    language: _SonarrQualityProfileValueAttr | None = None
    languageCutoffNotMet: bool
    mediaInfo: _CommonAttrs | None = None
    path: str
    relativePath: str
    releaseGroup: str
    seasonNumber: int
    seriesId: int
    size: int

    def __post_init__(self):
        super().__post_init__()
        self.language = _SonarrQualityProfileValueAttr(self.language) or {}
        self.mediaInfo = _CommonAttrs(self.mediaInfo) or {}


@dataclass(init=False)
class _SonarrEpisodeMonitor(_SonarrCommon2):
    """Sonarr common attributes."""

    absoluteEpisodeNumber: int
    unverifiedSceneNumbering: bool


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

    approved: bool
    downloadAllowed: bool
    downloadClientName: str
    droppedPath: str
    fileId: int
    guid: str
    importedPath: str
    indexerId: int
    preferredWordScore: int
    qualityWeight: int
    rejections: list[str]
    sceneSource: bool
    seasonNumber: int
    title: str
    tvdbId: str
    tvRageId: int


@dataclass(init=False)
class _SonarrSeasonStatistics(BaseModel):
    """Sonarr season statistics attributes."""

    episodeCount: int
    episodeFileCount: int
    percentOfEpisodes: float
    previousAiring: str | None = None
    seasonCount: int
    sizeOnDisk: int
    totalEpisodeCount: int

    def __post_init__(self):
        self.previousAiring = get_datetime(self.previousAiring)


@dataclass(init=False)
class _SonarrSeriesSeason(BaseModel):
    """Sonarr wanted missing series season attributes."""

    monitored: bool
    seasonNumber: int
    statistics: _SonarrSeasonStatistics | None = None

    def __post_init__(self):
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrSeriesCommon(_SonarrSeries2):
    """Sonarr series common attributes."""

    images: list[_SonarrImages] | None = None
    remotePoster: str
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

    downloading: bool
    sceneEpisodeNumber: int
    sceneSeasonNumber: int
    series: _SonarrSeries2 | None = None
    tvDbEpisodeId: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.series = _SonarrSeries2(self.series) or {}


@dataclass(init=False)
class _SonarrParseEpisodeInfo(BaseModel):
    """Sonarr parse episode info attributes."""

    absoluteEpisodeNumbers: list[int]
    episodeNumbers: list[int]
    fullSeason: bool
    isAbsoluteNumbering: bool
    isDaily: bool
    isMultiSeason: bool
    isPartialSeason: bool
    isPossibleSceneSeasonSpecial: bool
    isPossibleSpecialEpisode: bool
    isSeasonExtra: bool
    language: _Common3 | None = None
    quality: _Quality | None = None
    releaseGroup: str
    releaseHash: str
    releaseTitle: str
    releaseTokens: str
    seasonNumber: int
    seasonPart: int
    seriesTitle: str
    seriesTitleInfo: _TitleInfo
    special: bool
    specialAbsoluteEpisodeNumbers: list[int]

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
    allowed: bool

    def __post_init__(self):
        self.language = _Common3(self.language) or {}
