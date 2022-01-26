"""Lidarr Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from ..const import ARTIST_ID, DATE, PATH, TITLE
from .base import BaseModel
from .lidarr_common import (
    _LidarrAddOptions,
    _LidarrAlbumCommon,
    _LidarrArtist,
    _LidarrArtistTitleInfo,
    _LidarrAudioTags,
    _LidarrCommon,
    _LidarrCommon3,
    _LidarrCommon5,
    _LidarrFields,
    _LidarrImportListPreset,
    _LidarrMediaInfo_Quality,
)
from .request_common import (
    _Common3,
    _Common4,
    _Common7,
    _Common8,
    _Editor,
    _HistoryData,
    _IsLoaded,
    _ManualImport,
    _Monitor,
    _MonitorOption,
    _Quality,
    _Ratings,
    _RecordCommon,
    _ReleaseCommon,
    _Rename,
    _RetagChange,
    _StatusMessage,
    _TagDetails,
)


class LidarrCommands(str, Enum):
    """Lidarr commands."""

    ALBUM_SEARCH = "AlbumSearch"
    APP_UPDATE_CHECK = "ApplicationUpdateCheck"
    ARTIST_SEARCH = "ArtistSearch"
    DOWNLOADED_ALBUMS_SCAN = "DownloadedAlbumsScan"
    MISSING_ALBUM_SEARCH = "MissingAlbumSearch"
    REFRESH_ALBUM = "RefreshAlbum"
    REFRESH_ARTIST = "RefreshArtist"


class LidarrEventType(Enum):
    """Lidarr event types."""

    DELETED = 5
    DOWNLOAD_FAILED = 4
    DOWNLOAD_IMPORTED = 8
    GRABBED = 1
    IGNORED = 7
    IMPORT_FAILED = 7
    RENAMED = 6
    RETAGGED = 9
    TRACK_IMPORTED = 3


class LidarrImportListActionType(str, Enum):
    """Lidarr import list action types."""

    GET_PLAYLISTS = "getPlaylists"
    GET_PROFILES = "getProfiles"
    GET_TAGS = "getTags"


class LidarrImportListType(str, Enum):
    """Lidarr import list type."""

    LAST_FM = "lastFm"
    OTHER = "other"
    PROGRAM = "program"
    SPOTIFY = "spotify"


class LidarrImportListMonitorType(str, Enum):
    """Lidarr import list monitor type."""

    ENTIRE_ARTIST = "entireArtist"
    NONE = "none"
    SPECIFIC_ALBUM = "specificAlbum"


class LidarrSortKeys(str, Enum):
    """Lidarr sort keys."""

    ALBUM_TITLE = "albums.title"
    ARTIST_ID = ARTIST_ID
    DATE = DATE
    DOWNLOAD_CLIENT = "downloadClient"
    ID = "id"
    INDEXER = "indexer"
    MESSAGE = "message"
    PATH = PATH
    PROGRESS = "progress"
    PROTOCOL = "protocol"
    QUALITY = "quality"
    RATINGS = "ratings"
    RELEASE_DATE = "albums.releaseDate"
    SOURCE_TITLE = "sourcetitle"
    STATUS = "status"
    TIMELEFT = "timeleft"
    TITLE = TITLE


@dataclass(init=False)
class LidarrAlbum(_LidarrCommon3, _LidarrAlbumCommon):
    """Lidarr album attributes."""

    added: datetime | None = None
    addOptions: _LidarrAddOptions | None = None
    albumReleases: _IsLoaded | None = None
    artistMetadata: _IsLoaded | None = None
    artistMetadataId: int | None = None
    cleanTitle: str | None = None
    lastInfoSync: datetime | None = None
    oldForeignAlbumIds: list[str] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _LidarrAddOptions(self.addOptions) or {}
        self.artistMetadata = _IsLoaded(self.artistMetadata) or {}
        self.albumReleases = _IsLoaded(self.albumReleases) or {}


@dataclass(init=False)
class LidarrArtist(_LidarrArtist):
    """Lidarr artist attributes."""

    lastAlbum: LidarrAlbum | None = None
    nextAlbum: LidarrAlbum | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.lastAlbum = LidarrAlbum(self.lastAlbum) or {}
        self.nextAlbum = LidarrAlbum(self.nextAlbum) or {}


@dataclass(init=False)
class LidarrAlbumEditor(BaseModel):
    """Lidarr album editor attributes."""

    albumids: list[int] | None = None
    monitored: bool | None = None


@dataclass(init=False)
class LidarrAlbumLookup(_LidarrAlbumCommon):
    """Lidarr album lookup attributes."""

    remoteCover: str | None = None


@dataclass(init=False)
class LidarrBlocklistItem(_Common7, _LidarrCommon5):
    """Lidarr blocklist item attributes."""

    albumIds: list[int] | None = None
    message: str | None = None


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
class LidarrImportList(_Common3, _LidarrImportListPreset):
    """Lidarr import list attributes."""

    fields: list[_LidarrFields] | None = None
    implementationName: str | None = None
    monitorNewItems: str | None = None
    presets: list[_LidarrImportListPreset] | None = None
    rootFolderPath: str | None = None
    shouldMonitorExisting: bool | None = None
    shouldSearch: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]
        self.presets = [_LidarrImportListPreset(x) for x in self.presets or []]


@dataclass(init=False)
class LidarrAlbumHistory(_LidarrCommon, _LidarrCommon5):
    """Lidarr album history attributes."""

    album: LidarrAlbum | None = None
    data: _HistoryData | None = None
    downloadId: str | None = None
    eventType: str | None = None
    trackId: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = LidarrAlbum(self.album) or {}
        self.data = _HistoryData(self.data) or {}


@dataclass(init=False)
class LidarrHistory(_RecordCommon):
    """Lidarr history attributes."""

    records: list[LidarrAlbumHistory] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrAlbumHistory(field) for field in self.records or []]


@dataclass(init=False)
class _LidarrAlbumType(BaseModel):
    """Lidarr album type attributes."""

    albumType: _Common3 | None = None
    allowed: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.albumType = _Common3(self.albumType) or {}


@dataclass(init=False)
class _LidarrReleaseStatus(BaseModel):
    """Lidarr release status attributes."""

    allowed: bool | None = None
    releaseStatus: _Common3 | None = None

    def __post_init__(self):
        """Post init."""
        self.releaseStatus = _Common3(self.releaseStatus) or {}


@dataclass(init=False)
class LidarrMetadataProfile(_Common3):
    """Lidarr metadata profile attributes."""

    primaryAlbumTypes: list[_LidarrAlbumType] | None = None
    releaseStatuses: list[_LidarrReleaseStatus] | None = None
    secondaryAlbumTypes: list[_LidarrAlbumType] | None = None

    def __post_init__(self):
        """Post init."""
        self.primaryAlbumTypes = [
            _LidarrAlbumType(x) for x in self.primaryAlbumTypes or []
        ]
        self.releaseStatuses = [
            _LidarrReleaseStatus(x) for x in self.releaseStatuses or []
        ]
        self.secondaryAlbumTypes = [
            _LidarrAlbumType(x) for x in self.secondaryAlbumTypes or []
        ]


@dataclass(init=False)
class LidarrQueueItem(_Common4, _Common7, _Common8):
    """Lidarr queue item attributes."""

    album: _LidarrQueueItemAlbum | None = None
    albumId: int | None = None
    artist: _LidarrArtist | None = None
    artistId: int | None = None
    downloadForced: bool | None = None

    def __post_init__(self):
        """Post init."""
        self.album = _LidarrQueueItemAlbum(self.album) or {}
        self.artist = _LidarrArtist(self.artist) or {}
        self.quality = _Quality(self.quality) or {}
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class LidarrQueue(_RecordCommon):
    """Lidarr queue attributes."""

    records: list[LidarrQueueItem] | None = None

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrQueueItem(record) for record in self.records or []]


@dataclass(init=False)
class _LidarrQueueItemAlbum(_LidarrAlbumCommon):
    """Lidarr queue detail album attributes."""

    id: int | None = None


@dataclass(init=False)
class LidarrRelease(_ReleaseCommon):
    """Lidarr release attributes."""

    albumTitle: str | None = None
    artistName: str | None = None
    discography: bool | None = None
    preferredWordScore: int | None = None
    quality: _Quality | None = None
    releaseHash: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class LidarrRename(_Rename):
    """Lidarr rename attributes."""

    albumId: int | None = None
    artistId: int | None = None
    trackFileId: int | None = None
    trackNumbers: list[int] | None = None


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

    artist: LidarrArtist | None = None
    foreignId: str | None = None
    id: int | None = None

    def __post_init__(self):
        """Post init."""
        self.artist = LidarrArtist(self.artist) or {}


@dataclass(init=False)
class LidarrTagDetails(_TagDetails):
    """Lidarr tag details attributes."""

    artistIds: list[int] | None = None


@dataclass(init=False)
class LidarrTrack(LidarrRename):
    """Lidarr track attributes."""

    absoluteTrackNumber: int | None = None
    artist: LidarrArtist | None = None
    duration: int | None = None
    explicit: bool | None = None
    hasFile: bool | None = None
    id: int | None = None
    mediumNumber: int | None = None
    ratings: _Ratings | None = None
    title: str | None = None
    trackNumber: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = LidarrArtist(self.artist) or {}
        self.ratings = _Ratings(self.ratings) or {}


@dataclass(init=False)
class LidarrTrackFile(_LidarrMediaInfo_Quality, _LidarrCommon):
    """Lidarr track file attributes."""

    artistId: int | None = None
    audioTags: _LidarrAudioTags | None = None
    dateAdded: datetime | None = None
    path: str | None = None
    qualityWeight: int | None = None
    size: int | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _LidarrAudioTags(self.audioTags) or {}


@dataclass(init=False)
class LidarrTrackFileEditor(BaseModel):
    """Lidarr track file attributes."""

    quality: _Quality | None = None
    trackFileIds: list[int] | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class _LidarrParsedAlbumInfo(BaseModel):
    """Lidarr parsed album info attributes."""

    albumTitle: str | None = None
    artistName: str | None = None
    artistTitleInfo: _LidarrArtistTitleInfo | None = None
    quality: _Quality | None = None
    releaseDate: int | datetime | None = None
    discography: bool | None = None
    discographyStart: int | None = None
    discographyEnd: int | None = None
    releaseGroup: str | None = None
    releaseHash: str | None = None
    releaseVersion: str | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo) or {}
        self.quality = _Quality(self.quality) or {}


@dataclass(init=False)
class LidarrParse(BaseModel):
    """Lidarr parse attributes."""

    albums: list[LidarrAlbum] | None = None
    artist: LidarrArtist | None = None
    parsedAlbumInfo: _LidarrParsedAlbumInfo | None = None
    title: str | None = None

    def __post_init__(self):
        """Post init."""
        self.albums = [LidarrAlbum(album) for album in self.albums or []]
        self.artist = LidarrArtist(self.artist) or {}
        self.parsedAlbumInfo = _LidarrParsedAlbumInfo(self.parsedAlbumInfo) or {}


@dataclass(init=False)
class LidarrArtistEditor(_Editor):
    """Lidarr artist editor attributes."""

    artistIds: list[int] | None = None


@dataclass(init=False)
class LidarrManualImport(_ManualImport):
    """Lidarr manual import attributes."""

    additionalFile: bool | None = None
    album: LidarrAlbum | None = None
    albumReleaseId: int | None = None
    artist: _LidarrArtist | None = None
    audioTags: _LidarrAudioTags | None = None
    disableReleaseSwitching: bool | None = None
    replaceExistingFiles: bool | None = None
    tracks: list[LidarrTrack] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = LidarrAlbum(self.album) or {}
        self.artist = LidarrArtist(self.artist) or {}
        self.audioTags = _LidarrAudioTags(self.audioTags) or {}
        self.tracks = [LidarrTrack(track) for track in self.tracks or []]


@dataclass(init=False)
class LidarrMetadataProvider(BaseModel):
    """Lidarr metadata provider attributes."""

    metadataSource: str | None = None
    writeAudioTags: str | None = None
    scrubAudioTags: bool | None = None
    id: int | None = None


@dataclass(init=False)
class LidarrAlbumStudio(BaseModel):
    """Lidarr album studio attributes."""

    artist: list[_Monitor] | None = None
    monitoringOptions: _MonitorOption | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = [_Monitor(x) for x in self.artist or []]
        self.monitoringOptions = _MonitorOption(self.monitoringOptions) or {}
