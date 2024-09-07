"""Lidarr Common Models. These are only for internal module use."""

# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .base import BaseModel
from .request import StatusType
from .request_common import (
    _Common3,
    _Common6,
    _Fields,
    _ImportListCommon,
    _Link,
    _Quality,
    _Ratings,
)


@dataclass(init=False)
class _LidarrMedia(BaseModel):
    """Lidarr release mediaattributes."""

    mediumFormat: str
    mediumName: str
    mediumNumber: int


@dataclass(init=False)
class _LidarrCommon(BaseModel):
    """Lidarr common attributes."""

    albumId: int
    id: int
    qualityCutoffNotMet: bool


@dataclass(init=False)
class _LidarrCommon2(BaseModel):
    """Lidarr album common mediaattributes."""

    images: list[_LidarrImage] | None = None
    links: list[_Link] | None = None
    ratings: type[_Ratings] = field(default=_Ratings)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _Ratings(self.ratings)


@dataclass(init=False)
class _LidarrStatistics(BaseModel):
    """Lidarr statistics attributes."""

    albumCount: int
    percentOfTracks: float
    sizeOnDisk: int
    totalTrackCount: int
    trackCount: int
    trackFileCount: int


@dataclass(init=False)
class _LidarrCommon3(BaseModel):
    """Lidarr common attributes."""

    id: int
    statistics: type[_LidarrStatistics] = field(default=_LidarrStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.statistics = _LidarrStatistics(self.statistics)


@dataclass(init=False)
class _LidarrCommon4(BaseModel):
    """Lidarr common attributes."""

    disambiguation: str
    foreignAlbumId: str
    genres: list[str]


@dataclass(init=False)
class _LidarrArtist(_LidarrCommon2, _LidarrCommon3, _LidarrCommon4, _Common6):
    """Lidarr artist attributes."""

    added: datetime
    allMusicId: str
    artistMetadataId: int
    artistName: str
    artistType: str
    cleanName: str
    discogsId: int
    ended: bool
    foreignArtistId: str
    mbId: str
    metadataProfileId: int
    path: str
    qualityProfileId: int
    remotePoster: str
    sortName: str
    rootFolderPath: str
    status: StatusType
    tadbId: int
    tags: list[int]


@dataclass(init=False)
class _LidarrCommon5(BaseModel):
    """Lidarr common attributes."""

    artist: type[_LidarrArtist] = field(default=_LidarrArtist)
    artistId: int
    date: datetime
    quality: type[_Quality] = field(default=_Quality)
    sourceTitle: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = _LidarrArtist(self.artist)
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _LidarrAlbumCommon(_LidarrCommon2, _LidarrCommon4, _Common6):
    """Lidarr album common media attributes."""

    albumType: str
    anyReleaseOk: bool
    artist: type[_LidarrArtist] = field(default=_LidarrArtist)
    artistId: int
    duration: int
    media: list[_LidarrMedia] | None = None
    mediumCount: int
    profileId: int
    releaseDate: datetime
    releases: list[_LidarrRelease] | None = None
    secondaryTypes: list[_Common3] | None = None
    title: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = _LidarrArtist(self.artist)
        self.media = [_LidarrMedia(x) for x in self.media or []]
        self.releases = [_LidarrRelease(release) for release in self.releases or []]
        self.secondaryTypes = [_Common3(x) for x in self.secondaryTypes or []]


@dataclass(init=False)
class _LidarrRelease(BaseModel):
    """Lidarr release attributes."""

    albumId: int
    country: list[str]
    disambiguation: str
    duration: int
    foreignReleaseId: str
    format: str
    id: int
    label: str
    media: list[_LidarrMedia] | None = None
    mediumCount: int
    monitored: bool
    status: str
    title: str
    trackCount: int

    def __post_init__(self):
        """Post init."""
        self.media = [_LidarrMedia(x) for x in self.media or []]


@dataclass(init=False)
class _LidarrImage(BaseModel):
    """Lidarr image attributes."""

    coverType: str
    extension: str
    url: str


@dataclass(init=False)
class _LidarrFields(_Fields):
    """Lidarr fields attributes."""

    selectOptionsProviderAction: str


@dataclass(init=False)
class _LidarrImportListPreset(_ImportListCommon):
    """Lidarr import list preset attributes."""

    enableAutomaticAdd: bool
    fields: list[_LidarrFields] | None = None
    implementation: str
    infoLink: str
    listType: str
    metadataProfileId: int
    name: str
    qualityProfileId: int
    shouldMonitor: str
    tags: list[int]

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]


@dataclass(init=False)
class _LidarrArtistTitleInfo(BaseModel):
    """Lidarr artist title info attributes."""

    title: str
    year: int


@dataclass(init=False)
class _LidarrMediaInfo(BaseModel):
    """Lidarr media info attributes."""

    audioBitrate: str
    audioBitRate: str
    audioBits: str
    audioChannels: int | float
    audioCodec: str
    audioFormat: str
    audioSampleRate: str


@dataclass(init=False)
class _LidarrMediaInfo_Quality(BaseModel):
    """Lidarr media info/quality attributes."""

    mediaInfo: type[_LidarrMediaInfo] = field(default=_LidarrMediaInfo)
    quality: type[_Quality] = field(default=_Quality)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo)
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _LidarrAudioTags(_LidarrMediaInfo_Quality, _LidarrArtistTitleInfo):
    """Lidarr audio tags attributes."""

    albumTitle: str
    artistTitle: str
    artistTitleInfo: type[_LidarrArtistTitleInfo] = field(
        default=_LidarrArtistTitleInfo
    )
    cleanTitle: str
    discCount: int
    discNumber: int
    duration: str
    trackNumbers: list[int]

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo)


@dataclass(init=False)
class _LidarrAddOptions(BaseModel):
    """Lidarr add options attributes."""

    addType: str
    searchForNewAlbum: bool
