"""Lidarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .base import BaseModel, get_datetime
from .request_common import _Fields, _Revision

from .request_common import (  # isort:skip
    _Common3,
    _Common4,
    _Notification,
    _Quality,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _RetagChange,
    _TagDetails,
)

# TODO try consolidate with readarr


class LidarrEventType(str, Enum):
    """Lidarr event types."""

    ALBUM_IMPORT_INCOMPLETE = "albumImportIncomplete"
    ARTIST_FOLDER_IMPORTED = "artistFolderImported"
    DOWNLOAD_FAILED = "downloadFailed"
    DOWNLOAD_IGNORED = "downloadIgnored"
    DOWNLOAD_IMPORTED = "downloadImported"
    GRABBED = "grabbed"
    TRACK_DELETED = "trackFileDeleted"
    TRACK_IMPORTED = "trackFileImported"
    TRACK_RENAMED = "trackFileRenamed"
    TRACK_RETAGGED = "trackFileRetagged"
    UNKNOWN = "unknown"



class LidarrCommands(str, Enum):
    """Lidarr commands."""

    ALBUM_SEARCH = "AlbumSearch"
    APP_UPDATE_CHECK = "ApplicationUpdateCheck"
    ARTIST_SEARCH = "ArtistSearch"
    DOWNLOADED_ALBUMS_SCAN = "DownloadedAlbumsScan"
    MISSING_ALBUM_SEARCH = "MissingAlbumSearch"
    REFRESH_ALBUM = "RefreshAlbum"
    REFRESH_ARTIST = "RefreshArtist"


@dataclass(init=False)
class _Rating(BaseModel):
    """Rating attributes."""

    value: float | None = None
    votes: int | None = None


@dataclass(init=False)
class _LidarrMedia(BaseModel):
    """Lidarr release mediaattributes."""

    mediumNumber: int | None = None
    mediumName: str | None = None
    mediumFormat: str | None = None


@dataclass(init=False)
class _LidarrRelease(BaseModel):
    """Lidarr release attributes."""

    id: int | None = None
    albumId: int | None = None
    foreignReleaseId: str | None = None
    title: str | None = None
    status: str | None = None
    duration: int | None = None
    trackCount: int | None = None
    media: list[_LidarrMedia] | None = None
    mediumCount: int | None = None
    disambiguation: str | None = None
    country: list[str] | None = None
    label: str | None = None
    format: str | None = None
    monitored: bool | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__() #TODO
        self.media = [_LidarrMedia(x) for x in self.media or []]


@dataclass(init=False)
class _LidarrLink(BaseModel):
    """Lidarr links attributes."""

    url: str | None = None
    name: str | None = None


@dataclass(init=False)
class _LidarrImage(BaseModel):
    """Lidarr image attributes."""

    url: str | None = None
    coverType: str | None = None
    extension: str | None = None


@dataclass(init=False)
class _LidarrStatistics(BaseModel):
    """Lidarr statistics attributes."""

    albumCount: int | None = None  # TODO seperate from below 5
    trackFileCount: int | None = None
    trackCount: int | None = None
    totalTrackCount: int | None = None
    sizeOnDisk: int | None = None
    percentOfTracks: float | None = None


@dataclass(init=False)
class LidarrArtist(BaseModel):
    """Lidarr artist attributes."""

    status: str | None = None
    ended: bool | None = None
    artistName: str | None = None
    foreignArtistId: str | None = None
    tadbId: int | None = None
    discogsId: int | None = None
    overview: str | None = None
    artistType: str | None = None
    disambiguation: str | None = None
    links: list[_LidarrLink] | None = None
    images: list[_LidarrImage] | None = None
    path: str | None = None
    qualityProfileId: int | None = None
    metadataProfileId: int | None = None
    monitored: bool | None = None
    genres: list[str] | None = None
    cleanName: str | None = None
    sortName: str | None = None
    tags: list[int] | None = None
    added: str | None = None
    ratings: _Rating | None = None
    statistics: _LidarrStatistics | None = None
    id: int | None = None
    foreignAlbumId: str | None = None
    mbId: str | None = None
    allMusicId: str | None = None
    artistMetadataId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_LidarrLink(link) for link in self.links or []]
        self.ratings = _Rating(self.ratings) or {}
        self.statistics = _LidarrStatistics(self.statistics) or {}


@dataclass(init=False)
class LidarrAlbum(BaseModel):
    """Lidarr album attributes."""

    title: str | None = None
    disambiguation: str | None = None
    overview: str | None = None
    artistId: int | None = None
    foreignAlbumId: str | None = None
    monitored: bool | None = None
    anyReleaseOk: bool | None = None
    profileId: int | None = None
    duration: int | None = None
    albumType: str | None = None
    secondaryTypes: list[str] | None = None #TODO
    mediumCount: int | None = None
    ratings: _Rating | None = None
    releaseDate: str | None = None
    releases: list[_LidarrRelease] | None = None
    genres: list[str] | None = None
    media: list[_LidarrMedia] | None = None
    artist: LidarrArtist | None = None
    images: list[_LidarrImage] | None = None
    links: list[_LidarrLink] | None = None
    statistics: _LidarrStatistics | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        #self.releaseDate = get_datetime(self.releaseDate)
        self.artist = LidarrArtist(self.artist) or {}
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_LidarrLink(link) for link in self.links or []]
        self.media = [_LidarrMedia(x) for x in self.media or []]
        self.ratings = _Rating(self.ratings) or {}
        self.releases = [_LidarrRelease(release) for release in self.releases or []]
        self.statistics = _LidarrStatistics(self.statistics) or {}


@dataclass(init=False)
class _LidarrAlbumStudioArtist(LidarrArtist):
    """Lidarr album studio artist attributes."""

    nextAlbum: LidarrArtist | None = None
    lastAlbum: LidarrArtist | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.lastAlbum = LidarrArtist(self.lastAlbum) or {}
        self.nextAlbum = LidarrArtist(self.nextAlbum) or {}


@dataclass(init=False)
class LidarrAlbumEditor(BaseModel):
    """Lidarr album editor attributes."""

    albumids: list[int] | None = None
    monitored: bool | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()  # TODO try to run super without having to specify it everywhere


@dataclass(init=False)
class LidarrAlbumLookup(BaseModel):
    """Lidarr album lookup attributes."""

    title: str | None = None
    disambiguation: str | None = None
    overview: str | None = None
    artistId: int | None = None
    foreignAlbumId: str | None = None
    monitored: bool | None = None
    anyReleaseOk: bool | None = None
    profileId: int | None = None
    duration: int | None = None
    albumType: str | None = None
    secondaryTypes: list[str] | None = None #TODO
    mediumCount: int | None = None
    ratings: _Rating | None = None
    releaseDate: str | None = None
    releases: list[_LidarrRelease] | None = None
    genres: list[str] | None = None
    media: list[_LidarrMedia] | None = None
    artist: LidarrArtist | None = None
    images: list[_LidarrImage] | None = None
    links: list[_LidarrLink] | None = None
    remoteCover: str | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.releaseDate = get_datetime(self.releaseDate)
        self.artist = LidarrArtist(self.artist) or {}
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_LidarrLink(link) for link in self.links or []]
        self.media = [_LidarrMedia(x) for x in self.media or []]
        self.ratings = _Rating(self.ratings) or {}
        self.releases = [_LidarrRelease(release) for release in self.releases or []]


@dataclass(init=False)
class _LidarrMonitoringOptions(BaseModel):
    """Lidarr monitoring options attributes."""

    monitor: str | None = None
    albumsToMonitor: list[str] | None = None
    monitored: bool | None = None


@dataclass(init=False)
class _LidarrAlbumStudioAlbum(LidarrAlbum):
    """Lidarr album studio album attributes."""


@dataclass(init=False)
class _LidarrAlbumStudioArtistExtra(LidarrAlbum):
    """Lidarr album studio album attributes."""


@dataclass(init=False)
class _LidarrAlbumStudioArtist(LidarrAlbum):
    """Lidarr album studio artist attributes."""

    id: int | None = None
    monitored: bool | None = None
    albums: list[_LidarrAlbumStudioArtistExtra] | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.albums = [_LidarrAlbumStudioArtistExtra(x) for x in self.albums or []]


@dataclass(init=False)
class LidarrAlbumStudio(BaseModel):
    """Lidarr album studio attributes."""

    artist: list[_LidarrAlbumStudioArtist] | None = None
    monitoringOptions: _LidarrMonitoringOptions | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.artist = [_LidarrAlbumStudioArtist(x) for x in self.artist or []]
        self.monitoringOptions = _LidarrMonitoringOptions(self.monitoringOptions) or {}


@dataclass(init=False)
class _LidarrQuality(BaseModel):
    """Lidarr quality item attributes."""

    quality: _Common3 | None = None
    revision: _Revision | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Common3(self.quality) or {}
        self.revision = _Revision(self.revision) or {}


@dataclass(init=False)
class LidarrBlocklistItem(BaseModel):
    """Lidarr blocklist item attributes."""

    artistId: int | None = None
    albumIds: list[int] | None = None
    sourceTitle: str | None = None
    quality: _LidarrQuality | None = None
    date: str | None = None
    protocol: str | None = None
    indexer: str | None = None
    message: str | None = None
    id: int | None = None
    artist: LidarrArtist | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = LidarrArtist(self.artist) or {}
        self.quality = _LidarrQuality(self.quality) or {}


@dataclass(init=False)
class LidarrBlocklist(_RecordCommon):
    """Lidarr blocklist attributes."""

    records: list[LidarrBlocklistItem] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrBlocklistItem(record) for record in self.records or []]


@dataclass(init=False)
class LidarrCalendar(LidarrAlbum):
    """Lidarr calendar attributes."""


@dataclass(init=False)
class LidarrWantedCutoff(_RecordCommon):
    """Lidarr wanted cutoff attributes."""

    records: list[LidarrAlbum] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrAlbum(record) for record in self.records or []]


@dataclass(init=False)
class _LidarrFields(_Fields):
    """Lidarr fields attributes."""

    selectOptionsProviderAction: str | None = None


@dataclass(init=False)
class _LidarrImportListPreset(BaseModel):
    """Lidarr import list preset attributes."""

    enableAutomaticAdd: bool | None = None
    shouldMonitor: str | None = None
    qualityProfileId: int | None = None
    metadataProfileId: int | None = None
    listType: str | None = None
    listOrder: int | None = None
    name: str | None = None
    fields: list[_Fields] | None = None
    implementation: str | None = None
    configContract: str | None = None
    infoLink: str | None = None
    tags: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class LidarrImportList(_Common3):
    """Lidarr import list attributes."""

    configContract: str | None = None
    enableAutomaticAdd: bool | None = None
    fields: list[_LidarrFields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    listOrder: int | None = None
    listType: str | None = None
    metadataProfileId: int | None = None
    monitorNewItems: str | None = None
    qualityProfileId: int | None = None
    rootFolderPath: str | None = None
    shouldMonitor: str | None = None
    shouldMonitorExisting: bool | None = None
    shouldSearch: bool | None = None
    tags: list[int | None] | None = None
    presets: list[_LidarrImportListPreset] | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]
        self.presets = [_LidarrImportListPreset(x) for x in self.presets or []]


@dataclass(init=False)
class _LidarrAlbumHistoryData(BaseModel):
    """Lidarr album history data attributes."""

    indexer: str | None = None
    nzbInfoUrl: str | None = None
    releaseGroup: str | None = None
    age: str | None = None
    ageHours: str | None = None
    ageMinutes: str | None = None
    publishedDate: str | None = None,
    downloadClient: str | None = None
    size: str | None = None
    downloadUrl: str | None = None
    guid: str | None = None
    protocol: str | None = None
    downloadForced: str | None = None
    torrentInfoHash: str | None = None


@dataclass(init=False)
class LidarrAlbumHistory(BaseModel):
    """Lidarr album history attributes."""

    albumId: int | None = None
    artistId: int | None = None
    trackId: int | None = None
    sourceTitle: str | None = None
    quality: _Quality | None = None
    qualityCutoffNotMet: bool | None = None
    date: str | None = None
    downloadId: str | None = None
    eventType: str | None = None
    data: _LidarrAlbumHistoryData | None = None
    album: LidarrAlbum | None = None
    artist: LidarrArtist | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = LidarrAlbum(self.album) or {}
        self.artist = LidarrArtist(self.artist) or {}
        self.data = _LidarrAlbumHistoryData(self.data) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class LidarrHistory(_RecordCommon):
    """Lidarr history attributes."""

    records: list[LidarrAlbumHistory] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [LidarrAlbumHistory(field) for field in self.records or []]


@dataclass(init=False)
class _LidarrAlbumType(BaseModel):
    """Lidarr album type attributes."""

    albumType: _Common3 | None = None
    allowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.albumType = _Common3(self.albumType) or  {}


@dataclass(init=False)
class _LidarrReleaseStatus(BaseModel):
    """Lidarr release status attributes."""

    releaseStatus: _Common3 | None = None
    allowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.releaseStatus = _Common3(self.releaseStatus) or  {}


@dataclass(init=False)
class LidarrMetadataProfile(BaseModel):
    """Lidarr metadata profile attributes."""

    name: str | None = None
    primaryAlbumTypes: list[_LidarrAlbumType] | None = None
    secondaryAlbumTypes: list[_LidarrAlbumType] | None = None
    releaseStatuses: list[_LidarrReleaseStatus] | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.primaryAlbumTypes = [_LidarrAlbumType(x) for x in self.primaryAlbumTypes or []]
        self.releaseStatuses = [_LidarrReleaseStatus(x) for x in self.releaseStatuses or []]
        self.secondaryAlbumTypes = [_LidarrAlbumType(x) for x in self.secondaryAlbumTypes or []]


@dataclass(init=False)
class _LidarrStatusMessage(BaseModel):
    """Lidarr status message attributes."""

    title: str | None = None
    messages: list[str] | None = None


@dataclass(init=False)
class LidarrQueueRecord(BaseModel):
    """Lidarr queue record attributes."""


    artistId: int | None = None
    albumId: int | None = None
    quality: _Quality | None = None
    size: float | None = None
    title: str | None = None
    sizeleft: float | None = None
    timeleft: str | None = None
    estimatedCompletionTime: str | None = None
    status: str | None = None
    trackedDownloadStatus: str | None = None
    trackedDownloadState: str | None = None
    statusMessages: list[_LidarrStatusMessage] | None = None
    downloadId: str | None = None
    protocol: str | None = None
    downloadClient: str | None = None
    indexer: str | None = None
    outputPath: str | None = None
    downloadForced: bool | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.estimatedCompletionTime = get_datetime(self.estimatedCompletionTime)
        self.quality = _Quality(self.quality) or {}
        self.statusMessages = [_LidarrStatusMessage(x) for x in self.statusMessages or []]



@dataclass(init=False)
class LidarrQueue(_RecordCommon):
    """Lidarr queue attributes."""

    records: list[LidarrQueueRecord] | None = None

    def __post_init__(self):
        """Post init."""
        #super().__post_init__()
        self.records = [LidarrQueueRecord(record) for record in self.records or []]


@dataclass(init=False)
class _LidarrQueueDetailAlbum(BaseModel):
    """Lidarr queue detail album attributes."""

    title: str | None = None
    disambiguation: str | None = None
    overview: str | None = None
    artistId: int | None = None
    foreignAlbumId: str | None = None
    monitored: bool | None = None
    anyReleaseOk: bool | None = None
    profileId: int | None = None
    duration: int | None = None
    albumType: str | None = None
    secondaryTypes: list[int] | None = None
    mediumCount: int | None = None
    ratings: _Rating | None = None
    releaseDate: str | None = None
    releases: list[_LidarrRelease] | None = None
    genres: list[str] | None = None
    media: list[_LidarrMedia] | None = None
    artist: LidarrArtist | None = None
    images: list[_LidarrImage] | None = None
    links: list[_LidarrLink] | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = LidarrArtist(self.artist) or {}
        self.images = [_LidarrImage(image) for image in self.images or []]
        self.links = [_LidarrLink(link) for link in self.links or []]
        self.media = [_LidarrMedia(x) for x in self.media or []]
        self.releases = [_LidarrRelease(release) for release in self.releases or []]


@dataclass(init=False)
class LidarrQueueDetail(BaseModel):
    """Lidarr queue detail attributes."""

    artistId: int | None = None
    artist: LidarrArtist | None = None
    albumId: int | None = None
    album: _LidarrQueueDetailAlbum | None = None
    quality: _Quality | None = None
    size: float | None = None
    title: str | None = None
    sizeleft: float | None = None
    timeleft: str | None = None
    estimatedCompletionTime: str | None = None
    status: str | None = None
    trackedDownloadStatus: str | None = None
    trackedDownloadState: str | None = None
    statusMessages: list[_LidarrStatusMessage] | None = None
    downloadId: str | None = None
    protocol: str | None = None
    downloadClient: str | None = None
    indexer: str | None = None
    outputPath: str | None = None
    downloadForced: bool | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = _LidarrQueueDetailAlbum(self.album) or {}
        self.artist = LidarrArtist(self.artist) or {}
        self.quality = _Quality(self.quality) or {}
        self.statusMessages = [_LidarrStatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class LidarrRelease(BaseModel):
    """Lidarr release attributes."""

    guid: str | None = None
    quality: _Quality | None = None
    qualityWeight: int | None = None
    age: int | None = None
    ageHours: float | None = None
    ageMinutes: float | None = None
    size: int | None = None
    indexerId: int | None = None
    indexer: str | None = None
    releaseHash: str | None = None
    title: str | None = None
    discography: bool | None = None
    sceneSource: bool | None = None
    artistName: str | None = None
    albumTitle: str | None = None
    approved: bool | None = None
    temporarilyRejected: bool | None = None
    rejected: bool | None = None
    rejections: list[str] | None = None
    publishDate: str | None = None
    commentUrl: str | None = None
    downloadUrl: str | None = None
    infoUrl: str | None = None
    downloadAllowed: bool | None = None
    releaseWeight: int | None = None
    preferredWordScore: int | None = None
    magnetUrl: str | None = None
    infoHash: str | None = None
    seeders: int | None = None
    leechers: int | None = None
    protocol: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class LidarrRename(_Rename):
    """Lidarr rename attributes."""

    artistId: int | None = None
    albumId: int | None = None
    trackNumbers: list[int] | None = None
    trackFileId: int | None = None


@dataclass(init=False)
class LidarrRetag(LidarrRename):
    """Lidarr retag attributes."""

    changes: list[_RetagChange] | None = None
    path: str | None = None

    def __post_init__(self):
        """Post init."""
        self.changes = [_RetagChange(change) for change in self.changes or []]


@dataclass(init=False)
class LidarrSearch(BaseModel):
    """Lidarr search attributes."""

    foreignId: str | None = None
    artist: LidarrArtist | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        self.artist = LidarrArtist(self.artist) or {}


@dataclass(init=False)
class LidarrTagDetails(_TagDetails):
    """Lidarr tag details attributes."""

    artistIds: list[int] | None = None


@dataclass(init=False)
class LidarrTrack(BaseModel):
    """Lidarr track attributes."""

    artistId: int | None = None
    trackFileId: int | None = None
    albumId: int | None = None
    explicit: bool | None = None
    absoluteTrackNumber: int | None = None
    trackNumber: int | None = None
    title: str | None = None
    duration: int | None = None
    mediumNumber: int | None = None
    hasFile: bool | None = None
    ratings: _Rating | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.ratings = _Rating(self.ratings) or {}


@dataclass(init=False)
class LidarrTrackDetails(BaseModel):
    """Lidarr track details attributes."""

    artistId: int | None = None
    trackFileId: int | None = None
    albumId: int | None = None
    explicit: bool | None = None
    absoluteTrackNumber: int | None = None
    trackNumber: str | None = None
    title: str | None = None
    duration: int | None = None
    mediumNumber: int | None = None
    hasFile: bool | None = None
    artist: LidarrArtist | None = None
    ratings: _Rating | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = LidarrArtist(self.artist) or {}
        self.ratings = _Rating(self.ratings) or {}


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


@dataclass(init=False)
class LidarrTrackFile(BaseModel):
    """Lidarr track file attributes."""

    artistId: int | None = None
    albumId: int | None = None
    path: str | None = None
    size: int | None = None
    dateAdded: str | None = None
    quality: _Quality | None = None
    qualityWeight: int | None = None
    mediaInfo: _LidarrMediaInfo | None = None
    qualityCutoffNotMet: bool | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrArtistTitleInfo(BaseModel):
    """Lidarr artist title info attributes."""

    title: str | None = None
    year: int | None = None


@dataclass(init=False)
class _LidarrAudioTags(BaseModel):
    """Lidarr audio tags attributes."""

    title: str | None = None
    cleanTitle: str | None = None
    artistTitle: str | None = None
    albumTitle: str | None = None
    artistTitleInfo: _LidarrArtistTitleInfo | None = None
    discNumber: int | None = None
    discCount: int | None = None
    year: int | None = None
    duration: str | None = None
    quality: _Quality | None = None
    mediaInfo: _LidarrMediaInfo | None = None
    trackNumbers: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo) or {}
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class LidarrTrackFileDetails(BaseModel):
    """Lidarr track file details attributes."""

    artistId: int | None = None
    albumId: int | None = None
    path: str | None = None
    size: int | None = None
    dateAdded: str | None = None
    quality: _Quality | None = None
    qualityWeight: int | None = None
    mediaInfo: _LidarrMediaInfo | None = None
    qualityCutoffNotMet: bool | None = None
    audioTags: _LidarrAudioTags | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _LidarrAudioTags(self.audioTags) or {}
        self.mediaInfo = _LidarrMediaInfo(self.mediaInfo) or {}
        self.quality = _Quality(self.quality) or {}
