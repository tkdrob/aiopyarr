"""Sonarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-few-public-methods
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel, get_datetime_from_string

from .request_common import (  # isort:skip
    _Common2,
    _Common3,
    _Common4,
    _Common5,
    _CommonAttrs,
    _Fields,
    _Quality,
    _SelectOption,
    _TitleInfo,
)


@dataclass(init=False)
class _SonarrSeriesAlternateTitle(BaseModel):
    """Sonarr series alternate titles attributes."""

    seasonNumber: int | None = None
    title: str | None = None


@dataclass(init=False)
class _SonarrCommon2(_SonarrSeriesAlternateTitle):
    """Sonarr common attributes."""

    airDate: str | None = None
    airDateUtc: str | None = None
    episodeFileId: int | None = None
    episodeNumber: int | None = None
    hasFile: bool | None = None
    id: int | None = None
    monitored: bool | None = None
    overview: str | None = None
    seriesId: int | None = None


@dataclass(init=False)
class _SonarrQualityProfileValueAttr(_Common3):
    """Sonarr quality profile value attributes."""

    weight: int | None = None


@dataclass(init=False)
class _SonarrQualityProfileValueItems(BaseModel):
    """Sonarr quality profile value items attributes."""

    allowed: bool | None = None
    quality: _SonarrQualityProfileValueAttr | None = None

    def __post_init__(self):
        self.quality = _SonarrQualityProfileValueAttr(self.quality) or {}


@dataclass(init=False)
class _SonarrQualityProfile(BaseModel):
    """Sonarr quality profile attributes."""

    isLoaded: bool | None = None
    value: _SonarrQualityProfileValueAttr | None = None

    def __post_init__(self):
        self.value = _SonarrQualityProfileValueAttr(self.value) or {}


@dataclass(init=False)
class _SonarrImages(_Common5):
    """Sonarr images attributes."""

    remoteUrl: str | None = None


@dataclass(init=False)
class _SonarrSeries2(BaseModel):
    """Sonarr parse attributes."""

    added: str | None = None
    airTime: str | None = None
    certification: str | None = None
    cleanTitle: str | None = None
    ended: bool | None = None
    firstAired: str | None = None
    folder: str | None = None
    genres: list[str] | None = None
    id: int | None = None
    images: list[_SonarrImages] | None = None
    imdbId: str | None = None
    languageProfileId: int | None = None
    lastInfoSync: str | None = None
    monitored: bool | None = None
    network: str | None = None
    overview: str | None = None
    path: str | None = None
    qualityProfile: _SonarrQualityProfile | None = None
    qualityProfileId: int | None = None
    ratings: _SonarrRatings | None = None
    runtime: int | None = None
    seasonFolder: bool | None = None
    seasons: list[_SonarrSeriesSeason] | None = None
    seriesType: str | None = None
    sortTitle: str | None = None
    status: str | None = None
    tags: list[int | None] | None = None
    title: str | None = None
    titleSlug: str | None = None
    tvdbId: int | None = None
    tvMazeId: int | None = None
    tvRageId: int | None = None
    useSceneNumbering: bool | None = None
    year: int | None = None

    def __post_init__(self):
        self.added = get_datetime_from_string(self.added)
        self.firstAired = get_datetime_from_string(self.firstAired)
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.lastInfoSync = get_datetime_from_string(self.lastInfoSync)
        self.qualityProfile = _SonarrQualityProfile(self.qualityProfile) or {}
        self.ratings = _SonarrRatings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]


@dataclass(init=False)
class _SonarrEpisodeFile(BaseModel):
    """Sonarr episode file attributes."""

    dateAdded: str | None = None
    id: int | None = None
    language: _SonarrQualityProfileValueAttr | None = None
    languageCutoffNotMet: bool | None = None
    mediaInfo: _CommonAttrs | None = None
    path: str | None = None
    quality: _Quality | None = None
    qualityCutoffNotMet: bool | None = None
    relativePath: str | None = None
    releaseGroup: str | None = None
    seasonNumber: int | None = None
    seriesId: int | None = None
    size: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.language = _SonarrQualityProfileValueAttr(self.language) or {}
        self.mediaInfo = _CommonAttrs(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _SonarrCommon(_SonarrCommon2):
    """Sonarr common attributes."""

    absoluteEpisodeNumber: int | None = None
    episodeFile: _SonarrEpisodeFile | None = None
    unverifiedSceneNumbering: bool | None = None

    def __post_init__(self):
        super().__post_init__()
        self.episodeFile = _SonarrEpisodeFile(self.episodeFile) or {}


@dataclass(init=False)
class _SonarrHistoryRecordData(_Common4):
    """Sonarr history record data attributes."""

    age: int | None = None
    ageHours: float | None = None
    ageMinutes: float | None = None
    approved: bool | None = None
    downloadAllowed: bool | None = None
    downloadClientName: str | None = None
    downloadUrl: str | None = None
    droppedPath: str | None = None
    fileId: int | None = None
    guid: str | None = None
    importedPath: str | None = None
    indexer: str | None = None
    indexerId: int | None = None
    nzbInfoUrl: str | None = None
    preferredWordScore: int | None = None
    protocol: int | None = None
    publishedDate: str | None = None
    qualityWeight: int | None = None
    rejections: list[str] | None = None
    releaseGroup: str | None = None
    sceneSource: bool | None = None
    seasonNumber: int | None = None
    size: int | None = None
    title: str | None = None
    torrentInfoHash: str | None = None
    tvdbId: str | None = None
    tvRageId: int | None = None


@dataclass(init=False)
class _SonarrRatings(BaseModel):
    """Sonarr ratings attributes."""

    value: float | None = None
    votes: int | None = None


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
        self.previousAiring = get_datetime_from_string(self.previousAiring)


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
    qualityProfile: _SonarrQualityProfile | None = None
    remotePoster: str | None = None
    seasons: list[_SonarrSeriesSeason] | None = None
    statistics: _SonarrSeasonStatistics | None = None

    def __post_init__(self):
        self.added = get_datetime_from_string(self.added)
        self.firstAired = get_datetime_from_string(self.firstAired)
        self.images = [_SonarrImages(image) for image in self.images or []]
        self.qualityProfile = _SonarrQualityProfile(self.qualityProfile) or {}
        self.ratings = _SonarrRatings(self.ratings) or {}
        self.seasons = [_SonarrSeriesSeason(season) for season in self.seasons or []]
        self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrHistoryRecord(_Common2):
    """Sonarr history record attributes."""

    data: _SonarrHistoryRecordData | None = None
    date: str | None = None
    episodeId: int | None = None
    id: int | None = None
    language: _Common3 | None = None
    languageCutoffNotMet: bool | None = None
    quality: _Quality | None = None
    qualityCutoffNotMet: bool | None = None
    seriesId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.data = _SonarrHistoryRecordData(self.data) or {}
        self.language = _Common3(self.language) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _SonarrWantedMissingRecord(_SonarrCommon):
    """Sonarr wanted missing record attributes."""

    downloading: bool | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    tvDbEpisodeId: int | None = None


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
class _SonarrFields(_Fields, _SelectOption):
    """Sonarr fields attributes."""

    hidden: str | None = None
    selectOptions: list[_SelectOption] | None = None

    def __post_init__(self):
        """Post init."""
        self.selectOptions = [_SelectOption(x) for x in self.selectOptions or []]


@dataclass(init=False)
class _SonarrStatusMesssage(BaseModel):
    """Sonarr status meessage attributes."""

    messages: list[str] | None = None
    title: str | None = None
