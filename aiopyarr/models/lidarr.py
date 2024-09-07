"""Lidarr Models."""

# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass, field
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
    _RootFolderExended,
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

    added: datetime
    addOptions: type[_LidarrAddOptions] = field(default=_LidarrAddOptions)
    albumReleases: type[_IsLoaded] = field(default=_IsLoaded)
    artistMetadata: type[_IsLoaded] = field(default=_IsLoaded)
    artistMetadataId: int
    cleanTitle: str
    lastInfoSync: datetime
    oldForeignAlbumIds: list[str]

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.addOptions = _LidarrAddOptions(self.addOptions)
        self.artistMetadata = _IsLoaded(self.artistMetadata)
        self.albumReleases = _IsLoaded(self.albumReleases)


@dataclass(init=False)
class LidarrArtist(_LidarrArtist):
    """Lidarr artist attributes."""

    lastAlbum: type[LidarrAlbum] = field(default=LidarrAlbum)
    nextAlbum: type[LidarrAlbum] = field(default=LidarrAlbum)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.lastAlbum = LidarrAlbum(self.lastAlbum)
        self.nextAlbum = LidarrAlbum(self.nextAlbum)


@dataclass(init=False)
class LidarrAlbumEditor(BaseModel):
    """Lidarr album editor attributes."""

    albumids: list[int]
    monitored: bool


@dataclass(init=False)
class LidarrAlbumLookup(_LidarrAlbumCommon):
    """Lidarr album lookup attributes."""

    remoteCover: str


@dataclass(init=False)
class LidarrBlocklistItem(_Common7, _LidarrCommon5):
    """Lidarr blocklist item attributes."""

    albumIds: list[int]
    message: str


@dataclass(init=False)
class LidarrBlocklist(_RecordCommon):
    """Lidarr blocklist attributes."""

    records: list[LidarrBlocklistItem] = field(
        default_factory=list[LidarrBlocklistItem]
    )

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrBlocklistItem(record) for record in self.records]


@dataclass(init=False)
class LidarrCalendar(LidarrAlbum):
    """Lidarr calendar attributes."""


@dataclass(init=False)
class LidarrWantedCutoff(_RecordCommon):
    """Lidarr wanted cutoff attributes."""

    records: list[LidarrAlbum] = field(default_factory=list[LidarrAlbum])

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrAlbum(record) for record in self.records]


@dataclass(init=False)
class LidarrImportList(_Common3, _LidarrImportListPreset):
    """Lidarr import list attributes."""

    fields: list[_LidarrFields] | None = None
    implementationName: str
    monitorNewItems: str
    presets: list[_LidarrImportListPreset] | None = None
    rootFolderPath: str
    shouldMonitorExisting: bool
    shouldSearch: bool

    def __post_init__(self):
        """Post init."""
        self.fields = [_LidarrFields(field) for field in self.fields or []]
        self.presets = [_LidarrImportListPreset(x) for x in self.presets or []]


@dataclass(init=False)
class LidarrAlbumHistory(_LidarrCommon, _LidarrCommon5):
    """Lidarr album history attributes."""

    album: type[LidarrAlbum] = field(default=LidarrAlbum)
    data: type[_HistoryData] = field(default=_HistoryData)
    downloadId: str
    eventType: str
    trackId: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = LidarrAlbum(self.album)
        self.data = _HistoryData(self.data)


@dataclass(init=False)
class LidarrHistory(_RecordCommon):
    """Lidarr history attributes."""

    records: list[LidarrAlbumHistory] = field(default_factory=list[LidarrAlbumHistory])

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrAlbumHistory(field) for field in self.records]


@dataclass(init=False)
class _LidarrAlbumType(BaseModel):
    """Lidarr album type attributes."""

    albumType: type[_Common3] = field(default=_Common3)
    allowed: bool

    def __post_init__(self):
        """Post init."""
        self.albumType = _Common3(self.albumType)


@dataclass(init=False)
class _LidarrReleaseStatus(BaseModel):
    """Lidarr release status attributes."""

    allowed: bool
    releaseStatus: type[_Common3] = field(default=_Common3)

    def __post_init__(self):
        """Post init."""
        self.releaseStatus = _Common3(self.releaseStatus)


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
class _LidarrQueueItemAlbum(_LidarrAlbumCommon):
    """Lidarr queue detail album attributes."""

    id: int


@dataclass(init=False)
class LidarrQueueItem(_Common4, _Common7, _Common8):
    """Lidarr queue item attributes."""

    album: type[_LidarrQueueItemAlbum] = field(default=_LidarrQueueItemAlbum)
    albumId: int
    artist: type[_LidarrArtist] = field(default=_LidarrArtist)
    artistId: int
    downloadForced: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = _LidarrQueueItemAlbum(self.album)
        self.artist = _LidarrArtist(self.artist)
        self.quality = _Quality(self.quality)
        self.statusMessages = [_StatusMessage(x) for x in self.statusMessages or []]


@dataclass(init=False)
class LidarrQueue(_RecordCommon):
    """Lidarr queue attributes."""

    records: list[LidarrQueueItem] = field(default_factory=list[LidarrQueueItem])

    def __post_init__(self):
        """Post init."""
        self.records = [LidarrQueueItem(record) for record in self.records]


@dataclass(init=False)
class LidarrRelease(_ReleaseCommon):
    """Lidarr release attributes."""

    albumTitle: str
    artistName: str
    discography: bool
    preferredWordScore: int
    quality: type[_Quality] = field(default=_Quality)
    releaseHash: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class LidarrRename(_Rename):
    """Lidarr rename attributes."""

    albumId: int
    artistId: int
    trackFileId: int
    trackNumbers: list[int]


@dataclass(init=False)
class LidarrRetag(LidarrRename):
    """Lidarr retag attributes."""

    changes: list[_RetagChange] | None = None
    path: str

    def __post_init__(self):
        """Post init."""
        self.changes = [_RetagChange(change) for change in self.changes or []]


@dataclass(init=False)
class LidarrSearch(BaseModel):
    """Lidarr search attributes."""

    artist: type[LidarrArtist] = field(default=LidarrArtist)
    foreignId: str
    id: int

    def __post_init__(self):
        """Post init."""
        self.artist = LidarrArtist(self.artist)


@dataclass(init=False)
class LidarrTagDetails(_TagDetails):
    """Lidarr tag details attributes."""

    artistIds: list[int]


@dataclass(init=False)
class LidarrTrack(LidarrRename):
    """Lidarr track attributes."""

    absoluteTrackNumber: int
    artist: type[LidarrArtist] = field(default=LidarrArtist)
    duration: int
    explicit: bool
    hasFile: bool
    id: int
    mediumNumber: int
    ratings: type[_Ratings] = field(default=_Ratings)
    title: str
    trackNumber: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = LidarrArtist(self.artist)
        self.ratings = _Ratings(self.ratings)


@dataclass(init=False)
class LidarrTrackFile(_LidarrMediaInfo_Quality, _LidarrCommon):
    """Lidarr track file attributes."""

    artistId: int
    audioTags: type[_LidarrAudioTags] = field(default=_LidarrAudioTags)
    dateAdded: datetime
    path: str
    qualityWeight: int
    size: int

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.audioTags = _LidarrAudioTags(self.audioTags)


@dataclass(init=False)
class LidarrTrackFileEditor(BaseModel):
    """Lidarr track file attributes."""

    quality: type[_Quality] = field(default=_Quality)
    trackFileIds: list[int]

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _LidarrParsedAlbumInfo(BaseModel):
    """Lidarr parsed album info attributes."""

    albumTitle: str
    artistName: str
    artistTitleInfo: type[_LidarrArtistTitleInfo] = field(
        default=_LidarrArtistTitleInfo
    )
    quality: type[_Quality] = field(default=_Quality)
    releaseDate: int | datetime
    discography: bool
    discographyStart: int
    discographyEnd: int
    releaseGroup: str
    releaseHash: str
    releaseVersion: str

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artistTitleInfo = _LidarrArtistTitleInfo(self.artistTitleInfo)
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class LidarrParse(BaseModel):
    """Lidarr parse attributes."""

    albums: list[LidarrAlbum] | None = None
    artist: type[LidarrArtist] = field(default=LidarrArtist)
    parsedAlbumInfo: type[_LidarrParsedAlbumInfo] = field(
        default=_LidarrParsedAlbumInfo
    )
    title: str

    def __post_init__(self):
        """Post init."""
        self.albums = [LidarrAlbum(album) for album in self.albums or []]
        self.artist = LidarrArtist(self.artist)
        self.parsedAlbumInfo = _LidarrParsedAlbumInfo(self.parsedAlbumInfo)


@dataclass(init=False)
class LidarrArtistEditor(_Editor):
    """Lidarr artist editor attributes."""

    artistIds: list[int]


@dataclass(init=False)
class LidarrManualImport(_ManualImport):
    """Lidarr manual import attributes."""

    additionalFile: bool
    album: type[LidarrAlbum] = field(default=LidarrAlbum)
    albumReleaseId: int
    artist: type[_LidarrArtist] = field(default=LidarrArtist)
    audioTags: type[_LidarrAudioTags] = field(default=_LidarrAudioTags)
    disableReleaseSwitching: bool
    replaceExistingFiles: bool
    tracks: list[LidarrTrack] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.album = LidarrAlbum(self.album)
        self.artist = LidarrArtist(self.artist)
        self.audioTags = _LidarrAudioTags(self.audioTags)
        self.tracks = [LidarrTrack(track) for track in self.tracks or []]


@dataclass(init=False)
class LidarrMetadataProvider(BaseModel):
    """Lidarr metadata provider attributes."""

    metadataSource: str
    writeAudioTags: str
    scrubAudioTags: bool
    id: int


@dataclass(init=False)
class LidarrAlbumStudio(BaseModel):
    """Lidarr album studio attributes."""

    artist: list[_Monitor] | None = None
    monitoringOptions: type[_MonitorOption] = field(default=_MonitorOption)

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.artist = [_Monitor(x) for x in self.artist or []]
        self.monitoringOptions = _MonitorOption(self.monitoringOptions)


@dataclass(init=False)
class LidarrRootFolder(_RootFolderExended):
    """Lidarr root folder attributes."""
