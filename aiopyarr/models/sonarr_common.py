"""Sonarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-few-public-methods
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import BaseModel, get_time_from_string
from .common import _CommonAttrs


@dataclass(init=False)
class _SonarrCommon6(BaseModel):
    """Sonarr common attributes."""

    id: int | None = None


@dataclass(init=False)
class _SonarrSeriesAlternateTitle(BaseModel):
    """Sonarr series alternate titles attributes."""

    seasonNumber: int | None = None
    title: str | None = None


@dataclass(init=False)
class _SonarrCommon5(_SonarrSeriesAlternateTitle, _SonarrCommon6):
    """Sonarr common attributes."""

    airDate: datetime | None = None
    airDateUtc: datetime | None = None
    episodeFileId: int | None = None
    episodeNumber: int | None = None
    hasFile: bool | None = None
    monitored: bool | None = None
    overview: str | None = None
    seriesId: int | None = None

    def __post_init__(self):
        self.airDate = get_time_from_string(self.airDate)
        self.airDateUtc = get_time_from_string(self.airDateUtc)


@dataclass(init=False)
class _SonarrCommon4(_SonarrCommon6):  # TODO remove
    """Sonarr common attributes."""

    allowed: list[_SonarrQualityProfileValueAttr] | None = None
    cutoff: _SonarrCutoff | None = None
    items: list[_SonarrQualityProfileValueItems] | None = None
    name: str | None = None

    def __post_init__(self):
        self.allowed = [
            _SonarrQualityProfileValueAttr(allowed) for allowed in self.allowed or []
        ]
        if isinstance(self.cutoff, dict):
            self.cutoff = _SonarrCutoff(self.cutoff) or {}
        if isinstance(self.items, list):
            self.items = [
                _SonarrQualityProfileValueItems(item) for item in self.items or []
            ]


@dataclass(init=False)
class _SonarrQualityProfileValueAttr(_SonarrCommon4):
    """Sonarr quality profile value attributes."""

    weight: int | None = None


@dataclass(init=False)
class _SonarrCutoff(_SonarrCommon6):
    """Sonarr cutoff attributes."""

    name: str | None = None
    weight: int | None = None


@dataclass(init=False)
class _SonarrQualityProfileValueItems(BaseModel):
    """Sonarr quality profile value items attributes."""

    allowed: bool | None = None
    quality: _SonarrCutoff | None = None

    def __post_init__(self):
        self.quality = _SonarrCutoff(self.quality) or {}


@dataclass(init=False)
class _SonarrQualityProfile(BaseModel):
    """Sonarr quality profile attributes."""

    isLoaded: bool | None = None
    value: _SonarrQualityProfileValueAttr | None = None

    def __post_init__(self):
        self.value = _SonarrQualityProfileValueAttr(self.value) or {}


@dataclass(init=False)
class _SonarrImages(BaseModel):
    """Sonarr images attributes."""

    coverType: str | None = None
    remoteUrl: str | None = None
    url: str | None = None


@dataclass(init=False)
class _SonarrSeriesCommon3:
    """Sonarr series common attributes."""

    images: list[_SonarrImages] | None = None
    title: str | None = None
    titleSlug: str | None = None
    tvdbId: int | None = None


@dataclass(init=False)
class _SonarrSeriesCommon2(_SonarrSeriesCommon3):
    """Sonarr series common attributes."""

    airTime: str | None = None
    cleanTitle: str | None = None
    ended: bool | None = None
    firstAired: datetime | None = None
    imdbId: str | None = None
    languageProfileId: int | None = None
    monitored: bool | None = None
    network: str | None = None
    qualityProfile: _SonarrQualityProfile | None = None
    qualityProfileId: int | None = None
    runtime: int | None = None
    seasonFolder: bool | None = None
    seriesType: str | None = None
    status: str | None = None
    tvRageId: int | None = None
    useSceneNumbering: bool | None = None
    year: int | None = None

    def __post_init__(self):
        self.firstAired = get_time_from_string(self.firstAired)
        self.images = [_SonarrImages(image) for image in self.images or []]
        if isinstance(self.qualityProfile, dict):
            self.qualityProfile = _SonarrQualityProfile(self.qualityProfile) or {}


@dataclass(init=False)
class _SonarrSeries2(_SonarrSeriesCommon2):
    """Sonarr series attributes."""

    lastInfoSync: datetime | None = None
    overview: str | None = None
    path: str | None = None
    qualityProfile: _SonarrQualityProfile | None = None

    def __post_init__(self):
        super().__post_init__()
        self.lastInfoSync = get_time_from_string(self.lastInfoSync)


@dataclass(init=False)
class _SonarrEpisodeFileCommon:
    """Sonarr episode file common attributes."""

    languageCutoffNotMet: bool | None = None
    quality: _SonarrQualitySub | None = None
    qualityCutoffNotMet: bool | None = None
    seriesId: int | None = None

    def __post_init__(self):
        self.quality = _SonarrQualitySub(self.quality) or {}


@dataclass(init=False)
class _SonarrCommon8(BaseModel):
    """Sonarr episode file common attributes."""

    dateAdded: datetime | None = None
    path: str | None = None
    sceneName: str | None = None
    seasonNumber: int | None = None
    size: int | None = None


@dataclass(init=False)
class _SonarrEpisodeFile(_SonarrEpisodeFileCommon, _SonarrCommon6, _SonarrCommon8):
    """Sonarr episode file attributes."""

    language: _SonarrCutoff | None = None
    mediaInfo: _CommonAttrs | None = None
    relativePath: str | None = None
    releaseGroup: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.dateAdded = get_time_from_string(self.dateAdded)
        if isinstance(self.language, dict):
            self.language = _SonarrCutoff(self.language) or {}
        if isinstance(self.mediaInfo, dict):
            self.mediaInfo = _CommonAttrs(self.mediaInfo) or {}


@dataclass(init=False)
class _SonarrCommon2(_SonarrCommon5):
    """Sonarr common attributes."""

    absoluteEpisodeNumber: int | None = None
    episodeFile: _SonarrEpisodeFile | None = None

    def __post_init__(self):
        super().__post_init__()
        if isinstance(self.episodeFile, dict):
            self.episodeFile = _SonarrEpisodeFile(self.episodeFile) or {}


@dataclass(init=False)
class _SonarrEpisodeQuality:
    """Sonarr episode quality attributes."""

    proper: bool | None = None
    quality: _SonarrQualitySubSub | None = None

    def __post_init__(self):
        self.quality = _SonarrQualitySubSub(self.quality) or {}


@dataclass(init=False)
class _SonarrRevisionAttr(BaseModel):
    """Sonarr revision attributes."""

    real: int | None = None
    version: int | None = None
    isRepack: bool | None = None


class _SonarrQualitySubSub(_SonarrCommon6):
    """Sonarr quality attributes."""

    allowed: list | None = []  # contents not known
    name: str | None = None
    source: str | None = None
    resolution: int | None = None


@dataclass(init=False)
class _SonarrQualitySub(BaseModel):
    """Sonarr quality attributes."""

    quality: _SonarrQualitySubSub | None = None
    proper: bool | None = None
    revision: _SonarrRevisionAttr | None = None

    def __post_init__(self):
        self.quality = _SonarrQualitySubSub(self.quality) or {}
        if isinstance(self.revision, dict):
            self.revision = _SonarrRevisionAttr(self.revision) or {}


@dataclass(init=False)
class _SonarrCommon7(BaseModel):
    """Sonarr common attributes."""

    age: int | None = None
    approved: bool | None = None
    downloadAllowed: bool | None = None
    downloadUrl: str | None = None
    guid: str | None = None
    indexer: str | None = None
    indexerId: int | None = None
    rejections: list[str] | None = None
    sceneSource: bool | None = None
    seasonNumber: int | None = None
    size: int | None = None
    title: str | None = None
    tvRageId: int | None = None


@dataclass(init=False)
class _SonarrHistoryRecordData(_SonarrCommon7):
    """Sonarr history record data attributes."""

    downloadClient: str | None = None
    droppedPath: str | None = None
    importedPath: str | None = None
    nzbInfoUrl: str | None = None
    releaseGroup: str | None = None
    ageHours: float | None = None
    ageMinutes: float | None = None
    fileId: int | None = None
    downloadClientName: str | None = None
    preferredWordScore: int | None = None
    publishedDate: str | None = None
    tvdbId: str | None = None
    protocol: int | None = None
    torrentInfoHash: str | None = None


@dataclass(init=False)
class _SonarrEpisodeFile2(_SonarrCommon6, _SonarrCommon8):
    """Sonarr episode file attributes."""

    quality: _SonarrEpisodeQuality | None = None
    seriesId: int | None = None


@dataclass(init=False)
class _SonarrHistoryRecordEpisode(_SonarrCommon2):
    """Sonarr history record episode attributes."""

    unverifiedSceneNumbering: bool | None = None


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
    previousAiring: datetime | None = None
    sizeOnDisk: int | None = None
    totalEpisodeCount: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.previousAiring = get_time_from_string(self.previousAiring)


@dataclass(init=False)
class _SonarrWantedMissingSeriesSeason(BaseModel):
    """Sonarr wanted missing series season attributes."""

    monitored: bool | None = None
    seasonNumber: int | None = None
    statistics: _SonarrSeasonStatistics | None = None

    def __post_init__(self):
        if isinstance(self.statistics, dict):
            self.statistics = _SonarrSeasonStatistics(self.statistics) or {}


@dataclass(init=False)
class _SonarrSeriesCommon(_SonarrSeriesCommon2, BaseModel):
    """Sonarr series common attributes."""

    added: datetime | None = None
    certification: str | None = None
    genres: list[str] | None = None
    overview: str | None = None
    profileId: int | None = None
    ratings: _SonarrRatings | None = None
    seasonCount: int | None = None
    seasons: list[_SonarrWantedMissingSeriesSeason] | None = None
    sortTitle: str | None = None
    tags: list[int] | None = None
    tvMazeId: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.added = get_time_from_string(self.added)
        if isinstance(self.ratings, dict):
            self.ratings = _SonarrRatings(self.ratings) or {}
        if isinstance(self.seasons, list):
            self.seasons = [
                _SonarrWantedMissingSeriesSeason(season)
                for season in self.seasons or []
            ]


@dataclass(init=False)
class _SonarrHistoryRecordSeries(_SonarrSeriesCommon, _SonarrCommon6):
    """Sonarr history record series attributes."""

    lastInfoSync: datetime | None = None
    path: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.lastInfoSync = get_time_from_string(self.lastInfoSync)


@dataclass(init=False)
class _SonarrHistoryRecord(_SonarrEpisodeFileCommon, _SonarrCommon6):
    """Sonarr history record attributes."""

    data: _SonarrHistoryRecordData | None = None
    date: datetime | None = None
    downloadId: str | None = None
    episodeId: int | None = None
    eventType: str | None = None
    language: _SonarrCommon4 | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.date = get_time_from_string(self.date)
        self.data = _SonarrHistoryRecordData(self.data) or {}
        self.language = _SonarrCommon4(self.language) or {}


@dataclass(init=False)
class _SonarrWantedMissingSeries(_SonarrSeries2, _SonarrCommon6):
    """Sonarr wanted missing series attributes."""

    seasons: list[_SonarrWantedMissingSeriesSeason] | None = None

    def __post_init__(self):
        super().__post_init__()
        self.seasons = [
            _SonarrWantedMissingSeriesSeason(season) for season in self.seasons or []
        ]


@dataclass(init=False)
class _SonarrWantedMissingRecord(_SonarrCommon2):
    """Sonarr wanted missing record attributes."""

    downloading: bool | None = None
    sceneEpisodeNumber: int | None = None
    sceneSeasonNumber: int | None = None
    series: _SonarrWantedMissingSeries | None = None
    tvDbEpisodeId: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.series = _SonarrWantedMissingSeries(self.series) or {}


@dataclass(init=False)
class _SonarrSeriesTitleInfo(BaseModel):
    """Sonarr series title info attributes."""

    title: str | None = None
    titleWithoutYear: str | None = None
    year: int | None = None


@dataclass(init=False)
class _SonarrCommon3(BaseModel):
    """Sonarr common attributes."""

    episodeNumbers: list[int] | None = None
    fullSeason: bool | None = None
    language: str | None = None
    quality: _SonarrQualitySub | None = None
    releaseGroup: str | None = None
    seriesTitle: str | None = None

    def __post_init__(self):
        self.quality = _SonarrQualitySub(self.quality) or {}


@dataclass(init=False)
class _SonarrParseEpisodeInfo(_SonarrCommon3):
    """Sonarr parse episode info attributes."""

    absoluteEpisodeNumbers: list[int] | None = None
    isAbsoluteNumbering: bool | None = None
    isDaily: bool | None = None
    isPossibleSpecialEpisode: bool | None = None
    releaseHash: str | None = None
    releaseTitle: str | None = None
    seasonNumber: int | None = None
    seriesTitleInfo: _SonarrSeriesTitleInfo | None = None
    special: bool | None = None

    def __post_init__(self):
        super().__post_init__()
        self.seriesTitleInfo = _SonarrSeriesTitleInfo(self.seriesTitleInfo) or {}


@dataclass(init=False)
class _FileRevision:
    """File revision for updating episode file."""

    version: int | None = None
    real: int | None = None


@dataclass(init=False)
class _FileEpisodeQuality:
    """File quality for updating episode file."""

    quality: _SonarrCommon6 | None = None
    revision: _FileRevision | None = None


@dataclass(init=False)
class _SonarrBlocklistSeriesLanguage(BaseModel):
    """Blocklist series language attributes."""

    id: int | None = None
    name: str | None = None
