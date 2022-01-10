"""Radarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel, get_datetime_from_string

from .request_common import (  # isort:skip
    _Common3,
    _Common5,
    _CommonAttrs,
    _MetadataFields,
    _Quality,
    _SelectOption,
)


@dataclass(init=False)
class _RadarrMovieFileMediaInfo(_CommonAttrs):
    """Movie file media attributes."""

    audioAdditionalFeatures: str | None = None


@dataclass(init=False)
class _RadarrMovieImages(_Common5):
    """Movie images attributes."""

    remoteUrl: str | None = None


@dataclass(init=False)
class _RadarrDatabaseRating(BaseModel):
    """Radarr databade rating attributes."""

    type: str | None = None
    value: int | float | None = None
    votes: int | None = None


@dataclass(init=False)
class _RadarrMovieRatings(BaseModel):
    """Movie ratings attributes."""

    imdb: _RadarrDatabaseRating | None = None
    metacritic: _RadarrDatabaseRating | None = None
    rottenTomatoes: _RadarrDatabaseRating | None = None
    tmdb: _RadarrDatabaseRating | None = None

    def __post_init__(self):
        self.imdb = _RadarrDatabaseRating(self.imdb) or {}
        self.metacritic = _RadarrDatabaseRating(self.metacritic) or {}
        self.rottenTomatoes = _RadarrDatabaseRating(self.rottenTomatoes) or {}
        self.tmdb = _RadarrDatabaseRating(self.tmdb) or {}


@dataclass(init=False)
class _RadarrMovieCollection(BaseModel):
    """Movie collection attributes."""

    images: list[_RadarrMovieImages] | None = None
    name: str | None = None
    tmdbId: int | None = None

    def __post_init__(self):
        self.images = [_RadarrMovieImages(image) for image in self.images or []]


@dataclass(init=False)
class _RadarrMovieFields(_MetadataFields, _SelectOption):
    """Movie fields attributes."""


@dataclass(init=False)
class _RadarrNotificationFields(_MetadataFields, _SelectOption):
    """Radarr notification fields attributes."""

    selectOptions: list[_SelectOption] | None = None

    def __post_init__(self):
        self.selectOptions = [_SelectOption(x) for x in self.selectOptions or []]


@dataclass(init=False)
class _RadarrCommon(BaseModel):
    """Radarr indexers attributes."""

    fields: list[_RadarrMovieFields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    name: str | None = None

    def __post_init__(self):
        self.fields = [_RadarrMovieFields(field) for field in self.fields or []]


@dataclass(init=False)
class _RadarrMovieSpecifications(_RadarrCommon):
    """Movie specifications attributes."""

    negate: bool | None = None
    required: bool | None = None


@dataclass(init=False)
class _RadarrMovieCustomFormats(_Common3):
    """Movie custom formats attributes."""

    includeCustomFormatWhenRenaming: bool | None = None
    specifications: list[_RadarrMovieSpecifications] | None = None

    def __post_init__(self):
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
    languages: list[_Common3] | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        self.languages = [_Common3(language) for language in self.languages or []]
        self.quality = _Quality(self.quality) or {}


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

    messages: list[str] | None = None
    title: str | None = None


@dataclass(init=False)
class _RadarrNotificationMessage(BaseModel):
    """Radarr notification message attributes."""

    message: str | None = None
    type: str | None = None


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Movie history data attributes."""

    reason: str | None = None


@dataclass(init=False)
class _RadarrMovieAlternateTitle(BaseModel):
    """Movie history alternate title attributes."""

    id: int | None = None
    language: _Common3 | None = None
    movieId: int | None = None
    sourceId: int | None = None
    sourceType: str | None = None
    title: str | None = None
    voteCount: int | None = None
    votes: int | None = None

    def __post_init__(self):
        """Post init."""
        self.language = _Common3(self.language) or {}


@dataclass(init=False)
class _RadarrMovie(_RadarrCommon2):
    """Movie attributes."""

    added: str | None = None
    alternateTitles: list[_RadarrMovieAlternateTitle] | None = None
    certification: str | None = None
    cleanTitle: str | None = None
    collection: _RadarrMovieCollection | None = None
    digitalRelease: str | None = None
    folderName: str | None = None
    genres: list[str] | None = None
    hasFile: bool | None = None
    images: list[_RadarrMovieImages] | None = None
    imdbId: str | None = None
    inCinemas: str | None = None
    isAvailable: bool | None = None
    monitored: bool | None = None
    movieFile: _RadarrMovieFile | None = None
    originalTitle: str | None = None
    overview: str | None = None
    path: str | None = None
    physicalRelease: str | None = None
    ratings: _RadarrMovieRatings | None = None
    rootFolderPath: str | None = None
    runtime: int | None = None
    secondaryYearSourceId: int | None = None
    sizeOnDisk: int | None = None
    sortTitle: str | None = None
    status: str | None = None
    studio: str | None = None
    tags: list[int | None] | None = None
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
        self.movieFile = _RadarrMovieFile(self.movieFile) or {}
        self.ratings = _RadarrMovieRatings(self.ratings) or {}
        self.collection = _RadarrMovieCollection(self.collection) or {}


@dataclass(init=False)
class _RadarrParsedMovieInfo(BaseModel):
    """Radarr parsed movie info attributes."""

    edition: str | None = None
    extraInfo: dict | None = None
    imdbId: str | None = None
    languages: list[_Common3] | None = None
    movieTitle: str | None = None
    movieTitles: list[str] | None = None
    originalTitle: str | None = None
    primaryMovieTitle: str | None = None
    quality: _Quality | None = None
    releaseHash: str | None = None
    releaseTitle: str | None = None
    simpleReleaseTitle: str | None = None
    tmdbId: int | None = None
    year: int | None = None

    def __post_init__(self):
        """Post init."""
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _RadarrCustomFormatsSpecsFields(BaseModel):
    """Radarr custom formats specifications fields attributes."""

    value: int | None = None


@dataclass(init=False)
class _RadarrCustomFormatsSpecs(BaseModel):
    """Radarr custom formats specifications attributes."""

    fields: _RadarrCustomFormatsSpecsFields | None = None
    implementation: str | None = None
    negate: bool | None = None
    required: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = _RadarrCustomFormatsSpecsFields(self.fields) or {}


@dataclass(init=False)
class _RadarrCustomFormats(BaseModel):
    """Radarr custom formats attributes."""

    includeCustomFormatWhenRenaming: bool | None = None
    name: str | None = None
    specifications: list[_RadarrCustomFormatsSpecs] | None = None

    def __post_init__(self):
        """Post init."""
        self.specifications = [
            _RadarrCustomFormatsSpecs(x) for x in self.specifications or []
        ]


@dataclass(init=False)
class _RadarrMovieFile(_RadarrMovieCommon):
    """Movie file attributes."""

    dateAdded: str | None = None
    edition: str | None = None
    indexerFlags: int | None = None
    mediaInfo: _RadarrMovieFileMediaInfo | None = None
    movieId: int | None = None
    originalFilePath: str | None = None
    path: str | None = None
    qualityCutoffNotMet: bool | None = None
    relativePath: str | None = None
    sceneName: str | None = None
    size: int | None = None

    def __post_init__(self):
        super().__post_init__()
        self.dateAdded = get_datetime_from_string(self.dateAdded)
        self.mediaInfo = _RadarrMovieFileMediaInfo(self.mediaInfo) or {}
