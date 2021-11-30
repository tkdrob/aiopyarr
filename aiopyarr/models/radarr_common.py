"""Radarr Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import APIResponseType, BaseModel
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
class _RadarrMovieFileMediaInfo(_CommonAttrs, BaseModel):
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

    _responsetype = APIResponseType.LIST

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
class _RadarrCustomFilterAttr(BaseModel):
    """Radarr custom filter attributes."""

    key: str | None = None
    type: str | None = None
    value: list[str] | None = None


@dataclass(init=False)
class _RadarrCommandBody(BaseModel):
    """Radarr command body attributes."""

    completionMessage: str | None = None
    isExclusive: bool | None = None
    isNewMovie: bool | None = None
    isTypeExclusive: bool | None = None
    lastExecutionTime: str | None = None
    lastStartTime: str | None = None
    name: str | None = None
    requiresDiskAccess: bool | None = None
    sendUpdatesToClient: bool | None = None
    suppressMessages: bool | None = None
    trigger: str | None = None
    updateScheduledTask: bool | None = None


@dataclass(init=False)
class _RadarrUnmappedRootFolder(BaseModel):
    """Radarr root unmapped folder attributes."""

    name: str | None = None
    path: str | None = None


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Movie history data attributes."""

    reason: str | None = None
