"""Radarr Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel
from .common import _CommonAttrs


@dataclass(init=False)
class _RadarrMovieQualityRevision(BaseModel):
    """Movie file revision attributes."""

    isRepack: bool | None = None
    real: int | None = None
    version: int | None = None


@dataclass(init=False)
class _RadarrCommon4(BaseModel):
    """Movie file language attributes."""

    id: int | None = None
    name: str | None = None


@dataclass(init=False)
class _RadarrMovieQualityInfo(_RadarrCommon4):
    """Movie file quality attributes."""

    modifier: str | None = None
    resolution: int | None = None
    source: str | None = None


@dataclass(init=False)
class _RadarrMovieQuality(BaseModel):
    """Movie file quality attributes."""

    quality: _RadarrMovieQualityInfo | None = None
    revision: _RadarrMovieQualityRevision | None = None

    def __post_init__(self):
        super().__post_init__()
        self.quality = _RadarrMovieQualityInfo(self.quality) or {}
        self.revision = _RadarrMovieQualityRevision(self.revision) or {}


@dataclass(init=False)
class _RadarrMovieFileMediaInfo(_CommonAttrs):
    """Movie file media attributes."""

    audioAdditionalFeatures: str | None = None


@dataclass(init=False)
class _RadarrMovieImages(BaseModel):
    """Movie images attributes."""

    coverType: str | None = None
    remoteUrl: str | None = None
    url: str | None = None


@dataclass(init=False)
class _RadarrMovieRatings(BaseModel):
    """Movie ratings attributes."""

    value: float | None = None
    votes: int | None = None


@dataclass(init=False)
class _RadarrMovieCollection(BaseModel):
    """Movie collection attributes."""

    images: list[_RadarrMovieImages] | None = None
    name: str | None = None
    tmdbId: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.images = [_RadarrMovieImages(image) for image in self.images or []]


@dataclass(init=False)
class _RadarrMovieFields(BaseModel):
    """Movie fields attributes."""

    advanced: bool | None = None
    helpText: str | None = None
    label: str | None = None
    name: str | None = None
    order: int | None = None
    type: str | None = None
    value: str | None = None


@dataclass(init=False)
class _RadarrCommon(BaseModel):
    """Radarr indexers attributes."""

    fields: list[_RadarrMovieFields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    name: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.fields = [_RadarrMovieFields(field) for field in self.fields or []]


@dataclass(init=False)
class _RadarrMovieSpecifications(_RadarrCommon):
    """Movie specifications attributes."""

    negate: bool | None = None
    required: bool | None = None


@dataclass(init=False)
class _RadarrMovieCustomFormats(_RadarrCommon4):
    """Movie custom formats attributes."""

    includeCustomFormatWhenRenaming: bool | None = None
    specifications: list[_RadarrMovieSpecifications] | None = None

    def __post_init__(self):
        super().__post_init__()
        self.specifications = [
            _RadarrMovieSpecifications(spec) for spec in self.specifications or []
        ]


@dataclass(init=False)
class _RadarrCommon2(BaseModel):
    """Radarr common attributes."""

    id: int | None = None
    minimumAvailability: str | None = None
    qualityProfileId: int | None = None


@dataclass(init=False)
class _RadarrMovieCommon(BaseModel):
    """Movie common attributes."""

    edition: str | None = None
    id: int | None = None
    languages: list[_RadarrCommon4] | None = None
    quality: _RadarrMovieQuality | None = None

    def __post_init__(self):
        super().__post_init__()
        self.languages = [_RadarrCommon4(language) for language in self.languages or []]
        self.quality = _RadarrMovieQuality(self.quality) or {}


@dataclass(init=False)
class _RadarrMovieHistoryBlocklistBase(_RadarrMovieCommon):
    """Movie history/blocklist attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    date: str | None = None
    movieId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]


@dataclass(init=False)
class _RadarrQueueStatusMessages(BaseModel):
    """Radarr queue status messages."""

    title: str | None = None
    messages: list[dict] | None = None


@dataclass(init=False)
class _RadarrNotificationMessage(BaseModel):
    """Radarr notification message attributes."""

    message: str | None = None
    type: str | None = None


@dataclass(init=False)
class _RadarrUpdateChanges(BaseModel):
    """Radarr recent updates changes attributes."""

    fixed: list[str] | None = None
    new: list[str] | None = None


@dataclass(init=False)
class _RadarrQualityProfileItems(_RadarrCommon4):
    """Radarr quality profile items attributes."""

    allowed: bool | None = None
    items: list[_RadarrQualityProfileItems] | None = None
    quality: _RadarrMovieQualityInfo | None = None

    def __post_init__(self):
        super().__post_init__()
        self.items = [_RadarrQualityProfileItems(item) for item in self.items or []]
        if isinstance(self.quality, dict):
            self.quality = _RadarrMovieQualityInfo(self.quality) or {}


@dataclass(init=False)
class _RadarrMovieFileCommon(_RadarrMovieCommon):
    """Movie file attributes."""

    dateAdded: str | None = None
    indexerFlags: int | None = None
    mediaInfo: _RadarrMovieFileMediaInfo | None = None
    movieId: int | None = None
    originalFilePath: str | None = None
    path: str | None = None
    qualityCutoffNotMet: bool | None = None
    relativePath: str | None = None
    releaseGroup: str | None = None
    size: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.mediaInfo = _RadarrMovieFileMediaInfo(self.mediaInfo) or {}


@dataclass(init=False)
class _RadarrCalendarMovieFile(_RadarrMovieFileCommon):
    """Calendar movie file attributes."""

    edition: str | None = None
    originalFilePath: str | None = None
    sceneName: str | None = None


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Movie history data attributes."""

    reason: str | None = None


@dataclass(init=False)
class _RadarrMovieAlternateTitle(BaseModel):
    """Movie history alternate title attributes."""

    id: int | None = None
    language: _RadarrCommon4 | None = None
    movieId: int | None = None
    sourceId: int | None = None
    sourceType: str | None = None
    title: str | None = None
    voteCount: int | None = None
    votes: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.language = _RadarrCommon4(self.language) or {}


@dataclass(init=False)
class _RadarrMovie(_RadarrCommon2):
    """Movie attributes."""

    added: str | None = None
    alternateTitles: list[_RadarrMovieAlternateTitle] | None = None
    certification: str | None = None
    cleanTitle: str | None = None
    collection: _RadarrMovieCollection | None = None
    folderName: str | None = None
    genres: list[str] | None = None
    hasFile: bool | None = None
    imdbId: str | None = None
    images: list[_RadarrMovieImages] | None = None
    inCinemas: str | None = None
    isAvailable: bool | None = None
    monitored: bool | None = None
    originalTitle: str | None = None
    overview: str | None = None
    path: str | None = None
    physicalRelease: str | None = None
    ratings: _RadarrMovieRatings | None = None
    rootFolderPath: str | None = None
    runtime: int | None = None
    sizeOnDisk: int | None = None
    sortTitle: str | None = None
    status: str | None = None
    studio: str | None = None
    tags: list[int] | None = None
    title: str | None = None
    titleSlug: str | None = None
    tmdbId: int | None = None
    website: str | None = None
    year: int | None = None
    youTubeTrailerId: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.alternateTitles = [
            _RadarrMovieAlternateTitle(alternateTitle)
            for alternateTitle in self.alternateTitles or []
        ]
        self.images = [_RadarrMovieImages(image) for image in self.images or []]
        self.ratings = _RadarrMovieRatings(self.ratings) or {}
        if isinstance(self.collection, dict):
            self.collection = _RadarrMovieCollection(self.collection) or {}
