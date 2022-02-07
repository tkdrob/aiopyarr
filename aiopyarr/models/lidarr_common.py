"""Lidarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import attr

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

    mediumFormat: str = attr.ib(type=str)
    mediumName: str = attr.ib(type=str)
    mediumNumber: int = attr.ib(type=int)


@dataclass(init=False)
class _LidarrCommon(BaseModel):
    """Lidarr common attributes."""

    albumId: int = attr.ib(type=int)
    id: int = attr.ib(type=int)
    qualityCutoffNotMet: bool = attr.ib(type=bool)


@dataclass(init=False)
class _LidarrCommon2(BaseModel):
    """Lidarr album common mediaattributes."""

    images: list[_LidarrImage] | None = None
    links: list[_Link] | None = None
    ratings: _Ratings = attr.ib(type=_Ratings)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _Ratings(self.ratings) or {}


@dataclass(init=False)
class _LidarrStatistics(BaseModel):
    """Lidarr statistics attributes."""

    albumCount: int = attr.ib(type=int)
    percentOfTracks: float = attr.ib(type=float)
    sizeOnDisk: int = attr.ib(type=int)
    totalTrackCount: int = attr.ib(type=int)
    trackCount: int = attr.ib(type=int)
    trackFileCount: int = attr.ib(type=int)


@dataclass(init=False)
class _LidarrCommon3(BaseModel):
    """Lidarr common attributes."""

    id: int = attr.ib(type=int)
    statistics: _LidarrStatistics = attr.ib(type=_LidarrStatistics)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.statistics = _LidarrStatistics(self.statistics) or {}


@dataclass(init=False)
class _LidarrCommon4(BaseModel):
    """Lidarr common attributes."""

    disambiguation: str = attr.ib(type=str)
    foreignAlbumId: str = attr.ib(type=str)
    genres: list[str] = attr.ib(type='list[str]')


@dataclass(init=False)
class _LidarrArtist(_LidarrCommon2, _LidarrCommon3, _LidarrCommon4, _Common6):
    """Lidarr artist attributes."""

    added: datetime = attr.ib(type=datetime)
    allMusicId: str = attr.ib(type=str)
    artistMetadataId: int = attr.ib(type=int)
    artistName: str = attr.ib(type=str)
    artistType: str = attr.ib(type=str)
    cleanName: str = attr.ib(type=str)
    discogsId: int = attr.ib(type=int)
    ended: bool = attr.ib(type=bool)
    foreignArtistId: str = attr.ib(type=str)
    mbId: str = attr.ib(type=str)
    metadataProfileId: int = attr.ib(type=int)
    path: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    remotePoster: str = attr.ib(type=str)
    sortName: str = attr.ib(type=str)
    rootFolderPath: str = attr.ib(type=str)
    status: StatusType = attr.ib(type=StatusType)
    tadbId: int = attr.ib(type=int)
    tags: list[int] = attr.ib(type='list[int]')


@dataclass(init=False)
class _LidarrCommon5(BaseModel):
    """Lidarr common attributes."""

    artist: _LidarrArtist = attr.ib(type=_LidarrArtist)
    artistId: int = attr.ib(type=int)
    date: datetime = attr.ib(type=datetime)
    quality: _Quality = attr.ib(type=_Quality)
    sourceTitle: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = _LidarrArtist(self.artist) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrAlbumCommon(_LidarrCommon2, _LidarrCommon4, _Common6):
    """Lidarr album common media attributes."""

    albumType: str = attr.ib(type=str)
    anyReleaseOk: bool = attr.ib(type=bool)
    artist: _LidarrArtist = attr.ib(type=_LidarrArtist)
    artistId: int = attr.ib(type=int)
    duration: int = attr.ib(type=int)
    media: list[_LidarrMedia] | None = None
    mediumCount: int = attr.ib(type=int)
    profileId: int = attr.ib(type=int)
    releaseDate: datetime = attr.ib(type=datetime)
    releases: list[_LidarrRelease] | None = None
    secondaryTypes: list[_Common3] | None = None
    title: str = attr.ib(type=str)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = _LidarrArtist(self.artist) or {}
        self.media = [_LidarrMedia(x) for x in self.media or []]
        self.releases = [_LidarrRelease(release) for release in self.releases or []]
        self.secondaryTypes = [_Common3(x) for x in self.secondaryTypes or []]


@dataclass(init=False)
class _LidarrRelease(BaseModel):
    """Lidarr release attributes."""

    albumId: int = attr.ib(type=int)
    country: list[str] = attr.ib(type='list[str]')
    disambiguation: str = attr.ib(type=str)
    duration: int = attr.ib(type=int)
    foreignReleaseId: str = attr.ib(type=str)
    format: str = attr.ib(type=str)
    id: int = attr.ib(type=int)
    label: str = attr.ib(type=str)
    media: list[_LidarrMedia] | None = None
    mediumCount: int = attr.ib(type=int)
    monitored: bool = attr.ib(type=bool)
    status: str = attr.ib(type=str)
    title: str = attr.ib(type=str)
    trackCount: int = attr.ib(type=int)

    def __post_init__(self):
        """Post init."""
        self.media = [_LidarrMedia(x) for x in self.media or []]


@dataclass(init=False)
class _LidarrImage(BaseModel):
    """Lidarr image attributes."""

    coverType: str = attr.ib(type=str)
    extension: str = attr.ib(type=str)
    url: str = attr.ib(type=str)


@dataclass(init=False)
class _LidarrFields(_Fields):
    """Lidarr fields attributes."""

    selectOptionsProviderAction: str = attr.ib(type=str)


@dataclass(init=False)
class _LidarrImportListPreset(_ImportListCommon):
    """Lidarr import list preset attributes."""

    enableAutomaticAdd: bool = attr.ib(type=bool)
    fields: list[_LidarrFields] | None = None
    implementation: str = attr.ib(type=str)
    infoLink: str = attr.ib(type=str)
    listType: str = attr.ib(type=str)
    metadataProfileId: int = attr.ib(type=int)
    name: str = attr.ib(type=str)
    qualityProfileId: int = attr.ib(type=int)
    shouldMonitor: str = attr.ib(type=str)
    tags: list[int] = attr.ib(type='list[int]')

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]


@dataclass(init=False)
class _LidarrArtistTitleInfo(BaseModel):
    """Lidarr artist title info attributes."""

    title: str = attr.ib(type=str)
    year: int = attr.ib(type=int)


@dataclass(init=False)
class _LidarrMediaInfo(BaseModel):
    """Lidarr media info attributes."""

    audioBitrate: str = attr.ib(type=str)
    audioBitRate: str = attr.ib(type=str)
    audioBits: str = attr.ib(type=str)
    audioChannels: int | float = attr.ib(type=float)
    audioCodec: str = attr.ib(type=str)
    audioFormat: str = attr.ib(type=str)
    audioSampleRate: str = attr.ib(type=str)


@dataclass(init=False)
class _LidarrMediaInfo_Quality(BaseModel):
    """Lidarr media info/quality attributes."""

    mediaInfo: _LidarrMediaInfo = attr.ib(type=_LidarrMediaInfo)
    quality: _Quality = attr.ib(type=_Quality)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrAudioTags(_LidarrMediaInfo_Quality, _LidarrArtistTitleInfo):
    """Lidarr audio tags attributes."""

    albumTitle: str = attr.ib(type=str)
    artistTitle: str = attr.ib(type=str)
    artistTitleInfo: _LidarrArtistTitleInfo = attr.ib(type=_LidarrArtistTitleInfo)
    cleanTitle: str = attr.ib(type=str)
    discCount: int = attr.ib(type=int)
    discNumber: int = attr.ib(type=int)
    duration: str = attr.ib(type=str)
    trackNumbers: list[int] = attr.ib(type='list[int]')

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo) or {}


@dataclass(init=False)
class _LidarrAddOptions(BaseModel):
    """Lidarr add options attributes."""

    addType: str = attr.ib(type=str)
    searchForNewAlbum: bool = attr.ib(type=bool)
