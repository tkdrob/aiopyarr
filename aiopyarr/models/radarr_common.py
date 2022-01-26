"""Radarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import BaseModel
from .request_common import (
    _Common3,
    _Common5,
    _Common9,
    _CommonAttrs,
    _MetadataFields,
    _Quality,
    _Ratings,
    _SelectOption,
)


@dataclass(init=False)
class _RadarrMovieFileMediaInfo(_CommonAttrs):
    """Radarr movie file media attributes."""

    audioAdditionalFeatures: str | None = None


@dataclass(init=False)
class _RadarrMovieImages(_Common5):
    """Radarr movie images attributes."""

    remoteUrl: str | None = None


@dataclass(init=False)
class _RadarrDatabaseRating(_Ratings):
    """Radarr databade rating attributes."""

    type: str | None = None


@dataclass(init=False)
class _RadarrMovieRatings(BaseModel):
    """Radarr movie ratings attributes."""

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
    """Radarr movie collection attributes."""

    images: list[_RadarrMovieImages] | None = None
    name: str | None = None
    tmdbId: int | None = None

    def __post_init__(self):
        self.images = [_RadarrMovieImages(image) for image in self.images or []]


@dataclass(init=False)
class _RadarrMovieFields(_MetadataFields, _SelectOption):
    """Radarr movie fields attributes."""


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
    """Radarr movie specifications attributes."""

    negate: bool | None = None
    required: bool | None = None


@dataclass(init=False)
class _RadarrMovieCustomFormats(_Common3):
    """Radarr movie custom formats attributes."""

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
class _RadarrCommon3(_Common9):
    """Radarr common attributes."""

    collection: _RadarrMovieCollection | None = None
    digitalRelease: datetime | None = None
    images: list[_RadarrMovieImages] | None = None
    inCinemas: datetime | None = None
    physicalRelease: datetime | None = None
    ratings: _RadarrMovieRatings | None = None
    sortTitle: str | None = None
    status: str | None = None
    studio: str | None = None
    tmdbId: int | None = None
    website: str | None = None
    youTubeTrailerId: str | None = None

    def __post_init__(self):
        """Post init."""
        self.collection = _RadarrMovieCollection(self.collection) or {}
        self.images = [_RadarrMovieImages(image) for image in self.images or []]
        self.ratings = _RadarrMovieRatings(self.ratings) or {}


@dataclass(init=False)
class _RadarrMovieCommon(BaseModel):
    """Radarr movie common attributes."""

    edition: str | None = None
    id: int | None = None
    languages: list[_Common3] | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        self.languages = [_Common3(language) for language in self.languages or []]
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _RadarrMovieHistoryBlocklistBase(_RadarrMovieCommon):
    """Radarr movie history/blocklist attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    date: datetime | None = None
    movieId: int | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        super().__post_init__()
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]


@dataclass(init=False)
class _RadarrNotificationMessage(BaseModel):
    """Radarr notification message attributes."""

    message: str | None = None
    type: str | None = None


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Radarr movie history data attributes."""

    downloadClient: str | None = None
    downloadClientName: str | None = None
    droppedPath: str | None = None
    fileId: int | None = None
    importedPath: str | None = None
    reason: str | None = None


@dataclass(init=False)
class _RadarrMovieAlternateTitle(BaseModel):
    """Radarr movie history alternate title attributes."""

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
