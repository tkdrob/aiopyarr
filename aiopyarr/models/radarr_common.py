"""Radarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import attr

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

    audioAdditionalFeatures: str = attr.ib(type=str)


@dataclass(init=False)
class _RadarrMovieImages(_Common5):
    """Radarr movie images attributes."""

    remoteUrl: str = attr.ib(type=str)


@dataclass(init=False)
class _RadarrDatabaseRating(_Ratings):
    """Radarr databade rating attributes."""

    type: str = attr.ib(type=str)


@dataclass(init=False)
class _RadarrMovieRatings(BaseModel):
    """Radarr movie ratings attributes."""

    imdb: _RadarrDatabaseRating = attr.ib(type=_RadarrDatabaseRating)
    metacritic: _RadarrDatabaseRating = attr.ib(type=_RadarrDatabaseRating)
    rottenTomatoes: _RadarrDatabaseRating = attr.ib(type=_RadarrDatabaseRating)
    tmdb: _RadarrDatabaseRating = attr.ib(type=_RadarrDatabaseRating)

    def __post_init__(self):
        self.imdb = _RadarrDatabaseRating(self.imdb) or {}
        self.metacritic = _RadarrDatabaseRating(self.metacritic) or {}
        self.rottenTomatoes = _RadarrDatabaseRating(self.rottenTomatoes) or {}
        self.tmdb = _RadarrDatabaseRating(self.tmdb) or {}


@dataclass(init=False)
class _RadarrMovieCollection(BaseModel):
    """Radarr movie collection attributes."""

    images: list[_RadarrMovieImages] | None = None
    name: str = attr.ib(type=str)
    tmdbId: int = attr.ib(type=int)

    def __post_init__(self):
        self.images = [_RadarrMovieImages(image) for image in self.images or []]


@dataclass(init=False)
class _RadarrMovieFields(_MetadataFields, _SelectOption):
    """Radarr movie fields attributes."""


@dataclass(init=False)
class _RadarrCommon(BaseModel):
    """Radarr indexers attributes."""

    fields: list[_RadarrMovieFields] | None = None
    implementation: str = attr.ib(type=str)
    implementationName: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    name: str = attr.ib(type=str)

    def __post_init__(self):
        self.fields = [_RadarrMovieFields(field) for field in self.fields or []]


@dataclass(init=False)
class _RadarrMovieSpecifications(_RadarrCommon):
    """Radarr movie specifications attributes."""

    negate: bool = attr.ib(type=bool)
    required: bool = attr.ib(type=bool)


@dataclass(init=False)
class _RadarrMovieCustomFormats(_Common3):
    """Radarr movie custom formats attributes."""

    includeCustomFormatWhenRenaming: bool = attr.ib(type=bool)
    specifications: list[_RadarrMovieSpecifications] | None = None

    def __post_init__(self):
        self.specifications = [
            _RadarrMovieSpecifications(spec) for spec in self.specifications or []
        ]


@dataclass(init=False)
class _RadarrCommon2(BaseModel):
    """Radarr common attributes."""

    id: int = attr.ib(type=int)
    minimumAvailability: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)


@dataclass(init=False)
class _RadarrCommon3(_Common9):
    """Radarr common attributes."""

    collection: _RadarrMovieCollection = attr.ib(type=_RadarrMovieCollection)
    digitalRelease: datetime = attr.ib(type=datetime)
    images: list[_RadarrMovieImages] | None = None
    inCinemas: datetime = attr.ib(type=datetime)
    physicalRelease: datetime = attr.ib(type=datetime)
    ratings: _RadarrMovieRatings = attr.ib(type=_RadarrMovieRatings)
    sortTitle: str = attr.ib(type=str)
    status: str = attr.ib(type=str)
    studio: str = attr.ib(type=str)
    tmdbId: int = attr.ib(type=int)
    website: str = attr.ib(type=str)
    youTubeTrailerId: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        self.collection = _RadarrMovieCollection(self.collection) or {}
        self.images = [_RadarrMovieImages(image) for image in self.images or []]
        self.ratings = _RadarrMovieRatings(self.ratings) or {}


@dataclass(init=False)
class _RadarrMovieCommon(BaseModel):
    """Radarr movie common attributes."""

    edition: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    languages: list[_Common3] | None = None
    quality: _Quality = attr.ib(type=_Quality)

    def __post_init__(self):
        self.languages = [_Common3(language) for language in self.languages or []]
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _RadarrMovieHistoryBlocklistBase(_RadarrMovieCommon):
    """Radarr movie history/blocklist attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    date: datetime = attr.ib(type=datetime)
    movieId: int = attr.ib(type=int)
    sourceTitle: str = attr.ib(type=str)

    def __post_init__(self):
        super().__post_init__()
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]


@dataclass(init=False)
class _RadarrNotificationMessage(BaseModel):
    """Radarr notification message attributes."""

    message: str = attr.ib(type=str)
    type: str = attr.ib(type=str)


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Radarr movie history data attributes."""

    downloadClient: str = attr.ib(type=str)
    downloadClientName: str = attr.ib(type=str)
    droppedPath: str = attr.ib(type=str)
    fileId: int = attr.ib(type=int)
    importedPath: str = attr.ib(type=str)
    reason: str = attr.ib(type=str)


@dataclass(init=False)
class _RadarrMovieAlternateTitle(BaseModel):
    """Radarr movie history alternate title attributes."""

    id: int = attr.ib(type=int)
    language: _Common3 = attr.ib(type=_Common3)
    movieId: int = attr.ib(type=int)
    sourceId: int = attr.ib(type=int)
    sourceType: str = attr.ib(type=str)
    title: str = attr.ib(type=str)
    voteCount: int = attr.ib(type=int)
    votes: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.language = _Common3(self.language) or {}


@dataclass(init=False)
class _RadarrParsedMovieInfo(BaseModel):
    """Radarr parsed movie info attributes."""

    edition: str = attr.ib(type=str)
    extraInfo: dict = attr.ib(dict)
    imdbId: str = attr.ib(type=str)
    languages: list[_Common3] | None = None
    movieTitle: str = attr.ib(type=str)
    movieTitles: list[str] = attr.ib(type=list[str])
    originalTitle: str = attr.ib(type=str)
    primaryMovieTitle: str = attr.ib(type=str)
    quality: _Quality = attr.ib(type=_Quality)
    releaseHash: str = attr.ib(type=str)
    releaseTitle: str = attr.ib(type=str)
    simpleReleaseTitle: str = attr.ib(type=str)
    tmdbId: int = attr.ib(type=int)
    year: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _RadarrCustomFormatsSpecsFields(BaseModel):
    """Radarr custom formats specifications fields attributes."""

    value: int = attr.ib(type=int)


@dataclass(init=False)
class _RadarrCustomFormatsSpecs(BaseModel):
    """Radarr custom formats specifications attributes."""

    fields: _RadarrCustomFormatsSpecsFields = attr.ib(
        type=_RadarrCustomFormatsSpecsFields
    )
    implementation: str = attr.ib(type=str)
    negate: bool = attr.ib(type=bool)
    required: bool = attr.ib(type=bool)

    def __post_init__(self):
        """Post init."""
        self.fields = _RadarrCustomFormatsSpecsFields(self.fields) or {}


@dataclass(init=False)
class _RadarrCustomFormats(BaseModel):
    """Radarr custom formats attributes."""

    includeCustomFormatWhenRenaming: bool = attr.ib(type=bool)
    name: str = attr.ib(type=str)
    specifications: list[_RadarrCustomFormatsSpecs] | None = None

    def __post_init__(self):
        """Post init."""
        self.specifications = [
            _RadarrCustomFormatsSpecs(x) for x in self.specifications or []
        ]
