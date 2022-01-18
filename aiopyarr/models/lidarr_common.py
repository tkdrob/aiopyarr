"""Lidarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel
from .request_common import _Common3, _Common6, _Fields, _Link, _Quality, _Ratings


@dataclass(init=False)
class _LidarrMedia(BaseModel):
    """Lidarr release mediaattributes."""

    mediumFormat: str | None = None
    mediumName: str | None = None
    mediumNumber: int | None = None


@dataclass(init=False)
class _LidarrCommon(BaseModel):
    """Lidarr common attributes."""

    albumId: int | None = None
    id: int | None = None
    qualityCutoffNotMet: bool | None = None


@dataclass(init=False)
class _LidarrCommon2(BaseModel):
    """Lidarr album common mediaattributes."""

    images: list[_LidarrImage] | None = None
    links: list[_Link] | None = None
    ratings: _Ratings | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_Link(link) for link in self.links or []]
        self.ratings = _Ratings(self.ratings) or {}


@dataclass(init=False)
class _LidarrCommon3(BaseModel):
    """Lidarr common attributes."""

    id: int | None = None
    statistics: _LidarrStatistics | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.statistics = _LidarrStatistics(self.statistics) or {}


@dataclass(init=False)
class _LidarrCommon4(BaseModel):
    """Lidarr common attributes."""

    disambiguation: str | None = None
    foreignAlbumId: str | None = None
    genres: list[str] | None = None


@dataclass(init=False)
class _LidarrCommon5(BaseModel):
    """Lidarr common attributes."""

    artist: _LidarrArtist | None = None
    artistId: int | None = None
    date: str | None = None
    quality: _Quality | None = None
    sourceTitle: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = _LidarrArtist(self.artist) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrArtist(_LidarrCommon2, _LidarrCommon3, _LidarrCommon4, _Common6):
    """Lidarr artist attributes."""

    added: str | None = None
    allMusicId: str | None = None
    artistMetadataId: int | None = None
    artistName: str | None = None
    artistType: str | None = None
    cleanName: str | None = None
    discogsId: int | None = None
    ended: bool | None = None
    foreignArtistId: str | None = None
    mbId: str | None = None
    metadataProfileId: int | None = None
    path: str | None = None
    qualityProfileId: int | None = None
    remotePoster: str | None = None
    sortName: str | None = None
    rootFolderPath: str | None = None
    status: str | None = None
    tadbId: int | None = None
    tags: list[int] | None = None


@dataclass(init=False)
class _LidarrAlbumCommon(_LidarrCommon2, _LidarrCommon4, _Common6):
    """Lidarr album common media attributes."""

    albumType: str | None = None
    anyReleaseOk: bool | None = None
    artist: _LidarrArtist | None = None
    artistId: int | None = None
    duration: int | None = None
    media: list[_LidarrMedia] | None = None
    mediumCount: int | None = None
    profileId: int | None = None
    releaseDate: str | None = None
    releases: list[_LidarrRelease] | None = None
    secondaryTypes: list[_Common3] | None = None
    title: str | None = None

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

    albumId: int | None = None
    country: list[str] | None = None
    disambiguation: str | None = None
    duration: int | None = None
    foreignReleaseId: str | None = None
    format: str | None = None
    id: int | None = None
    label: str | None = None
    media: list[_LidarrMedia] | None = None
    mediumCount: int | None = None
    monitored: bool | None = None
    status: str | None = None
    title: str | None = None
    trackCount: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.media = [_LidarrMedia(x) for x in self.media or []]


@dataclass(init=False)
class _LidarrImage(BaseModel):
    """Lidarr image attributes."""

    coverType: str | None = None
    extension: str | None = None
    url: str | None = None


@dataclass(init=False)
class _LidarrStatistics(BaseModel):
    """Lidarr statistics attributes."""

    albumCount: int | None = None
    percentOfTracks: float | None = None
    sizeOnDisk: int | None = None
    totalTrackCount: int | None = None
    trackCount: int | None = None
    trackFileCount: int | None = None


@dataclass(init=False)
class LidarrAlbum(_LidarrAlbumCommon, _LidarrCommon3):
    """Lidarr album attributes."""


@dataclass(init=False)
class _LidarrFields(_Fields):
    """Lidarr fields attributes."""

    selectOptionsProviderAction: str | None = None


@dataclass(init=False)
class _LidarrImportListPreset(BaseModel):
    """Lidarr import list preset attributes."""

    configContract: str | None = None
    enableAutomaticAdd: bool | None = None
    fields: list[_LidarrFields] | None = None
    implementation: str | None = None
    infoLink: str | None = None
    listOrder: int | None = None
    listType: str | None = None
    metadataProfileId: int | None = None
    name: str | None = None
    qualityProfileId: int | None = None
    shouldMonitor: str | None = None
    tags: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]


@dataclass(init=False)
class _LidarrArtistTitleInfo(BaseModel):
    """Lidarr artist title info attributes."""

    title: str | None = None
    year: int | None = None


@dataclass(init=False)
class _LidarrMediaInfo_Quality(BaseModel):
    """Lidarr media info/quality attributes."""

    mediaInfo: _LidarrMediaInfo | None = None
    quality: _Quality | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrAudioTags(_LidarrMediaInfo_Quality, _LidarrArtistTitleInfo):
    """Lidarr audio tags attributes."""

    albumTitle: str | None = None
    artistTitle: str | None = None
    artistTitleInfo: _LidarrArtistTitleInfo | None = None
    cleanTitle: str | None = None
    discCount: int | None = None
    discNumber: int | None = None
    duration: str | None = None
    trackNumbers: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo) or {}


@dataclass(init=False)
class _LidarrMediaInfo(BaseModel):
    """Lidarr media info attributes."""

    audioBitrate: str | None = None
    audioBitRate: str | None = None
    audioBits: str | None = None
    audioChannels: float | None = None
    audioCodec: str | None = None
    audioFormat: str | None = None
    audioSampleRate: str | None = None
