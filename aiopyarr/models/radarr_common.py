"""Radarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
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

    audioAdditionalFeatures: str


@dataclass(init=False)
class _RadarrMovieImages(_Common5):
    """Radarr movie images attributes."""

    remoteUrl: str


@dataclass(init=False)
class _RadarrDatabaseRating(_Ratings):
    """Radarr databade rating attributes."""

    type: str


@dataclass(init=False)
class _RadarrMovieRatings(BaseModel):
    """Radarr movie ratings attributes."""

    imdb: type[_RadarrDatabaseRating] = field(default=_RadarrDatabaseRating)
    metacritic: type[_RadarrDatabaseRating] = field(default=_RadarrDatabaseRating)
    rottenTomatoes: type[_RadarrDatabaseRating] = field(default=_RadarrDatabaseRating)
    tmdb: type[_RadarrDatabaseRating] = field(default=_RadarrDatabaseRating)

    def __post_init__(self):
        self.imdb = _RadarrDatabaseRating(self.imdb)
        self.metacritic = _RadarrDatabaseRating(self.metacritic)
        self.rottenTomatoes = _RadarrDatabaseRating(self.rottenTomatoes)
        self.tmdb = _RadarrDatabaseRating(self.tmdb)


@dataclass(init=False)
class _RadarrMovieCollection(BaseModel):
    """Radarr movie collection attributes."""

    images: list[_RadarrMovieImages] | None = None
    name: str
    tmdbId: int

    def __post_init__(self):
        self.images = [_RadarrMovieImages(image) for image in self.images or []]


@dataclass(init=False)
class _RadarrMovieFields(_MetadataFields, _SelectOption):
    """Radarr movie fields attributes."""


@dataclass(init=False)
class _RadarrCommon(BaseModel):
    """Radarr indexers attributes."""

    fields: list[_RadarrMovieFields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    name: str

    def __post_init__(self):
        self.fields = [_RadarrMovieFields(field) for field in self.fields or []]


@dataclass(init=False)
class _RadarrMovieSpecifications(_RadarrCommon):
    """Radarr movie specifications attributes."""

    negate: bool
    required: bool


@dataclass(init=False)
class _RadarrMovieCustomFormats(_Common3):
    """Radarr movie custom formats attributes."""

    includeCustomFormatWhenRenaming: bool
    specifications: list[_RadarrMovieSpecifications] | None = None

    def __post_init__(self):
        self.specifications = [
            _RadarrMovieSpecifications(spec) for spec in self.specifications or []
        ]


@dataclass(init=False)
class _RadarrCommon2(BaseModel):
    """Radarr common attributes."""

    id: int
    minimumAvailability: str
    qualityProfileId: int


@dataclass(init=False)
class _RadarrCommon3(_Common9):
    """Radarr common attributes."""

    collection: type[_RadarrMovieCollection] = field(default=_RadarrMovieCollection)
    digitalRelease: datetime
    images: list[_RadarrMovieImages] | None = None
    inCinemas: datetime
    physicalRelease: datetime
    ratings: type[_RadarrMovieRatings] = field(default=_RadarrMovieRatings)
    sortTitle: str
    status: str
    studio: str
    tmdbId: int
    website: str
    youTubeTrailerId: str

    def __post_init__(self):
        """Post init."""
        self.collection = _RadarrMovieCollection(self.collection)
        self.images = [_RadarrMovieImages(image) for image in self.images or []]
        self.ratings = _RadarrMovieRatings(self.ratings)

    @property
    def releaseDate(self) -> datetime:
        """Return latest known release date for all formats."""
        result = datetime(1, 1, 1)
        for date in ("digitalRelease", "physicalRelease", "inCinemas"):
            try:
                if result < getattr(self, date):
                    result = getattr(self, date)
            except AttributeError:
                continue
        return result


@dataclass(init=False)
class _RadarrMovieCommon(BaseModel):
    """Radarr movie common attributes."""

    edition: str
    id: int
    languages: list[_Common3] | None = None
    quality: type[_Quality] = field(default=_Quality)

    def __post_init__(self):
        self.languages = [_Common3(language) for language in self.languages or []]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _RadarrMovieHistoryBlocklistBase(_RadarrMovieCommon):
    """Radarr movie history/blocklist attributes."""

    customFormats: list[_RadarrMovieCustomFormats] | None = None
    date: datetime
    movieId: int
    sourceTitle: str

    def __post_init__(self):
        super().__post_init__()
        self.customFormats = [
            _RadarrMovieCustomFormats(custForm) for custForm in self.customFormats or []
        ]


@dataclass(init=False)
class _RadarrNotificationMessage(BaseModel):
    """Radarr notification message attributes."""

    message: str
    type: str


@dataclass(init=False)
class _RadarrMovieHistoryData(BaseModel):
    """Radarr movie history data attributes."""

    downloadClient: str
    downloadClientName: str
    droppedPath: str
    fileId: int
    importedPath: str
    reason: str


@dataclass(init=False)
class _RadarrMovieAlternateTitle(BaseModel):
    """Radarr movie history alternate title attributes."""

    id: int
    language: type[_Common3] = field(default=_Common3)
    movieId: int
    sourceId: int
    sourceType: str
    title: str
    voteCount: int
    votes: int

    def __post_init__(self):
        """Post init."""
        self.language = _Common3(self.language)


@dataclass(init=False)
class _RadarrParsedMovieInfo(BaseModel):
    """Radarr parsed movie info attributes."""

    edition: str
    extraInfo: dict
    imdbId: str
    languages: list[_Common3] | None = None
    movieTitle: str
    movieTitles: list[str]
    originalTitle: str
    primaryMovieTitle: str
    quality: type[_Quality] = field(default=_Quality)
    releaseHash: str
    releaseTitle: str
    simpleReleaseTitle: str
    tmdbId: int
    year: int

    def __post_init__(self):
        """Post init."""
        self.languages = [_Common3(x) for x in self.languages or []]
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _RadarrCustomFormatsSpecsFields(BaseModel):
    """Radarr custom formats specifications fields attributes."""

    value: int


@dataclass(init=False)
class _RadarrCustomFormatsSpecs(BaseModel):
    """Radarr custom formats specifications attributes."""

    fields: type[_RadarrCustomFormatsSpecsFields] = field(
        default=_RadarrCustomFormatsSpecsFields
    )
    implementation: str
    negate: bool
    required: bool

    def __post_init__(self):
        """Post init."""
        self.fields = _RadarrCustomFormatsSpecsFields(self.fields)


@dataclass(init=False)
class _RadarrCustomFormats(BaseModel):
    """Radarr custom formats attributes."""

    includeCustomFormatWhenRenaming: bool
    name: str
    specifications: list[_RadarrCustomFormatsSpecs] | None = None

    def __post_init__(self):
        """Post init."""
        self.specifications = [
            _RadarrCustomFormatsSpecs(x) for x in self.specifications or []
        ]
