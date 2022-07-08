"""Tests for Lidarr object models."""
# pylint:disable=line-too-long, too-many-lines, too-many-statements
from datetime import datetime
import json

import pytest

from aiopyarr.exceptions import ArrException
from aiopyarr.lidarr_client import LidarrClient
from aiopyarr.models.const import ProtocolType
from aiopyarr.models.lidarr import (
    LidarrAlbum,
    LidarrAlbumEditor,
    LidarrAlbumHistory,
    LidarrAlbumStudio,
    LidarrArtist,
    LidarrCommands,
    LidarrEventType,
    LidarrImportList,
    LidarrImportListActionType,
    LidarrImportListMonitorType,
    LidarrImportListType,
    LidarrManualImport,
    LidarrMetadataProfile,
    LidarrMetadataProvider,
    LidarrRelease,
    LidarrSortKeys,
    LidarrTrackFile,
    LidarrTrackFileEditor,
    LidarrWantedCutoff,
)
from aiopyarr.models.request import (
    AddTypes,
    Command,
    ImageType,
    SortDirection,
    StatusType,
)

from tests import LIDARR_API, load_fixture


@pytest.mark.asyncio
async def test_async_get_albums(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album/0?includeAllArtistAlbums=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/album.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_albums(albumids=0)
    assert data.title == "string"
    assert data.disambiguation == "string"
    assert data.overview == "string"
    assert isinstance(data.artistId, int)
    assert data.foreignAlbumId == "string"
    assert data.monitored is True
    assert data.anyReleaseOk is True
    assert isinstance(data.profileId, int)
    assert isinstance(data.duration, int)
    assert data.albumType == "string"
    assert isinstance(data.secondaryTypes[0].id, int)
    assert data.secondaryTypes[0].name == "string"
    assert isinstance(data.mediumCount, int)
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert data.releaseDate == datetime(2010, 8, 23, 0, 0)
    assert isinstance(data.releases[0].id, int)
    assert isinstance(data.releases[0].albumId, int)
    assert data.releases[0].foreignReleaseId == "string"
    assert data.releases[0].title == "string"
    assert data.releases[0].status == "string"
    assert isinstance(data.releases[0].duration, int)
    assert isinstance(data.releases[0].trackCount, int)
    assert isinstance(data.releases[0].media[0].mediumNumber, int)
    assert data.releases[0].media[0].mediumName == "string"
    assert data.releases[0].media[0].mediumFormat == "string"
    assert isinstance(data.releases[0].mediumCount, int)
    assert data.releases[0].disambiguation == "string"
    assert data.releases[0].country == ["string"]
    assert data.releases[0].label == ["string"]
    assert data.releases[0].format == "string"
    assert data.releases[0].monitored is True
    assert data.genres == ["string"]
    assert isinstance(data.media[0].mediumNumber, int)
    assert data.media[0].mediumName == "string"
    assert data.media[0].mediumFormat == "string"
    assert data.artist.status == StatusType.ENDED.value
    assert data.artist.ended is True
    assert data.artist.artistName == "string"
    assert data.artist.foreignArtistId == "string"
    assert isinstance(data.artist.tadbId, int)
    assert isinstance(data.artist.discogsId, int)
    assert data.artist.overview == "string"
    assert data.artist.artistType == "string"
    assert data.artist.disambiguation == "string"
    assert data.artist.links[0].url == "string"
    assert data.artist.links[0].name == "string"
    assert data.artist.images[0].url == "string"
    assert data.artist.images[0].coverType == ImageType.POSTER.value
    assert data.artist.images[0].extension == "string"
    assert data.artist.path == "string"
    assert isinstance(data.artist.qualityProfileId, int)
    assert isinstance(data.artist.metadataProfileId, int)
    assert data.artist.monitored is True
    assert data.artist.genres == ["string"]
    assert data.artist.cleanName == "string"
    assert data.artist.sortName == "string"
    assert isinstance(data.artist.tags[0], int)
    assert data.artist.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data.artist.ratings.votes, int)
    assert isinstance(data.artist.ratings.value, float)
    assert isinstance(data.artist.statistics.albumCount, int)
    assert isinstance(data.artist.statistics.trackFileCount, int)
    assert isinstance(data.artist.statistics.trackCount, int)
    assert isinstance(data.artist.statistics.totalTrackCount, int)
    assert isinstance(data.artist.statistics.sizeOnDisk, int)
    assert isinstance(data.artist.statistics.percentOfTracks, float)
    assert isinstance(data.artist.id, int)
    assert data.images[0].url == "string"
    assert data.images[0].coverType == ImageType.POSTER.value
    assert data.images[0].extension == "string"
    assert data.links[0].url == "string"
    assert data.links[0].name == "string"
    assert isinstance(data.statistics.trackFileCount, int)
    assert isinstance(data.statistics.trackCount, int)
    assert isinstance(data.statistics.totalTrackCount, int)
    assert isinstance(data.statistics.sizeOnDisk, int)
    assert isinstance(data.statistics.percentOfTracks, float)
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album?includeAllArtistAlbums=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_albums()

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album?includeAllArtistAlbums=False&albumids=0&albumids=1&artistId=0&foreignAlbumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_albums(albumids=[0, 1], artistid=0, foreignalbumid=0)


@pytest.mark.asyncio
async def test_async_add_album(aresponses, lidarr_client: LidarrClient) -> None:
    """Test adding album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_add_album(LidarrAlbum("test"))
    assert isinstance(data, LidarrAlbum)


@pytest.mark.asyncio
async def test_async_edit_albums(aresponses, lidarr_client: LidarrClient) -> None:
    """Test editing album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_edit_albums(LidarrAlbum("test"))
    assert isinstance(data, LidarrAlbum)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album/monitor",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    editor = LidarrAlbumEditor({"albumids": [0], "monitored": True})
    assert isinstance(editor.albumids[0], int)
    assert editor.monitored is True
    await lidarr_client.async_edit_albums(editor)


@pytest.mark.asyncio
async def test_async_delete_album(aresponses, lidarr_client: LidarrClient) -> None:
    """Test deleting album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_delete_album(0)


@pytest.mark.asyncio
async def test_async_album_studio(aresponses, lidarr_client: LidarrClient) -> None:
    """Test setting monitor options in albumstudio."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/albumstudio",
        "POST",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = LidarrAlbumStudio({"artist": [{"id": 0, "monitored": True}]})
    await lidarr_client.async_album_studio(data)
    assert isinstance(data.artist[0].id, int)
    assert data.artist[0].monitored
    assert data.monitoringOptions.monitor is None


@pytest.mark.asyncio
async def test_async_get_artists(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting artists."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/artist.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_artists(0)
    assert data.status == "string"
    assert data.ended is True
    assert data.artistName == "string"
    assert data.foreignArtistId == "string"
    assert isinstance(data.tadbId, int)
    assert isinstance(data.discogsId, int)
    assert data.overview == "string"
    assert data.artistType == "string"
    assert data.disambiguation == "string"
    assert data.links[0].url == "string"
    assert data.links[0].name == "string"
    assert isinstance(data.nextAlbum.artistMetadataId, int)
    assert data.nextAlbum.foreignAlbumId == "string"
    assert data.nextAlbum.oldForeignAlbumIds == ["string"]
    assert data.nextAlbum.title == "string"
    assert data.nextAlbum.overview == "string"
    assert data.nextAlbum.disambiguation == "string"
    assert data.nextAlbum.releaseDate == datetime(2011, 8, 23, 0, 0)
    assert data.nextAlbum.images[0].url == "string"
    assert data.nextAlbum.images[0].coverType == ImageType.POSTER.value
    assert data.nextAlbum.images[0].extension == "string"
    assert data.nextAlbum.links[0].url == "string"
    assert data.nextAlbum.links[0].name == "string"
    assert data.nextAlbum.genres == ["string"]
    assert data.nextAlbum.albumType == "string"
    assert isinstance(data.nextAlbum.secondaryTypes[0].id, int)
    assert data.nextAlbum.secondaryTypes[0].name == "string"
    assert isinstance(data.nextAlbum.ratings.votes, int)
    assert isinstance(data.nextAlbum.ratings.value, float)
    assert data.nextAlbum.cleanTitle == "string"
    assert isinstance(data.nextAlbum.profileId, int)
    assert data.nextAlbum.monitored is True
    assert data.nextAlbum.anyReleaseOk is True
    assert data.nextAlbum.lastInfoSync == datetime(2020, 12, 27, 10, 52, 27, 220039)
    assert data.nextAlbum.added == datetime(1, 1, 1, 0, 0)
    assert data.nextAlbum.addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.nextAlbum.artistMetadata.isLoaded is False
    assert data.nextAlbum.albumReleases.isLoaded is False
    # data.nextAlbum.artist not included, duplicate name so causes issues
    assert isinstance(data.nextAlbum.id, int)
    assert isinstance(data.lastAlbum.artistMetadataId, int)
    assert data.lastAlbum.foreignAlbumId == "string"
    assert data.lastAlbum.oldForeignAlbumIds == ["string"]
    assert data.lastAlbum.title == "string"
    assert data.lastAlbum.overview == "string"
    assert data.lastAlbum.disambiguation == "string"
    assert data.lastAlbum.releaseDate == datetime(2010, 8, 23, 0, 0)
    assert data.lastAlbum.images[0].url == "string"
    assert data.lastAlbum.images[0].coverType == ImageType.POSTER.value
    assert data.lastAlbum.images[0].extension == "string"
    assert data.lastAlbum.links[0].url == "string"
    assert data.lastAlbum.links[0].name == "string"
    assert data.lastAlbum.genres == ["string"]
    assert data.lastAlbum.albumType == "string"
    assert isinstance(data.lastAlbum.secondaryTypes[0].id, int)
    assert data.lastAlbum.secondaryTypes[0].name == "string"
    assert isinstance(data.lastAlbum.ratings.votes, int)
    assert isinstance(data.lastAlbum.ratings.value, float)
    assert data.lastAlbum.cleanTitle == "string"
    assert isinstance(data.lastAlbum.profileId, int)
    assert data.lastAlbum.monitored is True
    assert data.lastAlbum.anyReleaseOk is True
    assert data.lastAlbum.lastInfoSync == datetime(2021, 12, 27, 10, 52, 27, 220039)
    assert data.lastAlbum.added == datetime(1, 1, 1, 0, 0)
    assert data.lastAlbum.addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.lastAlbum.artistMetadata.isLoaded is False
    assert data.lastAlbum.albumReleases.isLoaded is False
    # data.lastAlbum.artist not included, duplicate name so causes issues
    assert isinstance(data.lastAlbum.id, int)
    assert data.images[0].url == "string"
    assert data.images[0].coverType == ImageType.POSTER.value
    assert data.images[0].extension == "string"
    assert data.path == "string"
    assert isinstance(data.qualityProfileId, int)
    assert isinstance(data.metadataProfileId, int)
    assert data.monitored is True
    assert data.rootFolderPath == "string"
    assert data.genres == ["string"]
    assert data.cleanName == "string"
    assert data.sortName == "string"
    assert isinstance(data.tags[0], int)
    assert data.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert isinstance(data.statistics.albumCount, int)
    assert isinstance(data.statistics.trackFileCount, int)
    assert isinstance(data.statistics.trackCount, int)
    assert isinstance(data.statistics.totalTrackCount, int)
    assert isinstance(data.statistics.sizeOnDisk, int)
    assert isinstance(data.statistics.percentOfTracks, float)
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_artists()

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist?mbId=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_artists("test")


@pytest.mark.asyncio
async def test_async_add_artist(aresponses, lidarr_client: LidarrClient) -> None:
    """Test adding artist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_add_artist(LidarrArtist("test"))
    assert isinstance(data, LidarrArtist)


@pytest.mark.asyncio
async def test_async_edit_artists(aresponses, lidarr_client: LidarrClient) -> None:
    """Test editing artist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_edit_artists(LidarrArtist("test"))
    assert isinstance(data, LidarrArtist)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist/editor",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_edit_artists("test")


@pytest.mark.asyncio
async def test_async_delete_artists(aresponses, lidarr_client: LidarrClient) -> None:
    """Test deleting artists."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_delete_artists(0)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist/editor",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_delete_artists([0])


@pytest.mark.asyncio
async def test_async_album_lookup(aresponses, lidarr_client: LidarrClient) -> None:
    """Test album lookup."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album/lookup?term=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/album-lookup.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_album_lookup("test")
    assert data[0].title == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert isinstance(data[0].artistId, int)
    assert data[0].foreignAlbumId == "string"
    assert data[0].monitored is False
    assert data[0].anyReleaseOk is True
    assert isinstance(data[0].profileId, int)
    assert isinstance(data[0].duration, int)
    assert data[0].albumType == "string"
    assert isinstance(data[0].secondaryTypes[0].id, int)
    assert data[0].secondaryTypes[0].name == "string"
    assert isinstance(data[0].mediumCount, int)
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert data[0].releaseDate == datetime(2018, 3, 9, 0, 0)
    assert isinstance(data[0].releases[0].id, int)
    assert isinstance(data[0].releases[0].albumId, int)
    assert data[0].releases[0].foreignReleaseId == "string"
    assert data[0].releases[0].title == "string"
    assert data[0].releases[0].status == "string"
    assert isinstance(data[0].releases[0].duration, int)
    assert isinstance(data[0].releases[0].trackCount, int)
    assert isinstance(data[0].releases[0].media[0].mediumNumber, int)
    assert data[0].releases[0].media[0].mediumName == "string"
    assert data[0].releases[0].media[0].mediumFormat == "string"
    assert isinstance(data[0].releases[0].mediumCount, int)
    assert data[0].releases[0].disambiguation == "string"
    assert data[0].releases[0].country == ["string"]
    assert data[0].releases[0].label == ["string"]
    assert data[0].releases[0].format == "string"
    assert data[0].releases[0].monitored is True
    assert data[0].genres == ["string"]
    assert isinstance(data[0].media[0].mediumNumber, int)
    assert data[0].media[0].mediumName == "string"
    assert data[0].media[0].mediumFormat == "string"
    assert data[0].artist.status == "string"
    assert data[0].artist.ended is False
    assert data[0].artist.artistName == "string"
    assert data[0].artist.foreignArtistId == "string"
    assert isinstance(data[0].artist.tadbId, int)
    assert isinstance(data[0].artist.discogsId, int)
    assert data[0].artist.overview == "string"
    assert data[0].artist.artistType == "string"
    assert data[0].artist.disambiguation == "string"
    assert data[0].artist.links[0].url == "string"
    assert data[0].artist.links[0].name == "string"
    assert data[0].artist.images[0].url == "string"
    assert data[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres == ["string"]
    assert data[0].artist.cleanName == "string"
    assert data[0].artist.sortName == "string"
    assert isinstance(data[0].artist.tags[0], int)
    assert data[0].artist.added == datetime(2021, 8, 21, 15, 36, 8, 777408)
    assert isinstance(data[0].artist.ratings.votes, int)
    assert isinstance(data[0].artist.ratings.value, float)
    assert isinstance(data[0].artist.statistics.albumCount, int)
    assert isinstance(data[0].artist.statistics.trackFileCount, int)
    assert isinstance(data[0].artist.statistics.trackCount, int)
    assert isinstance(data[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].artist.id, int)
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].remoteCover == "string"


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting blocklist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/blacklist?page=1&pageSize=10&sortDirection=default&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_blocklist()
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == LidarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DESCENDING.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].artistId, int)
    assert isinstance(data.records[0].albumIds[0], int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].date == datetime(2020, 2, 15, 19, 24, 28, 476060)
    assert data.records[0].protocol is ProtocolType.UNKNOWN
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert data.records[0].artist.status == StatusType.ENDED.value
    assert data.records[0].artist.ended is True
    assert data.records[0].artist.artistName == "string"
    assert data.records[0].artist.foreignArtistId == "string"
    assert isinstance(data.records[0].artist.tadbId, int)
    assert isinstance(data.records[0].artist.discogsId, int)
    assert data.records[0].artist.overview == "string"
    assert data.records[0].artist.artistType == "string"
    assert data.records[0].artist.disambiguation == "string"
    assert data.records[0].artist.links[0].url == "string"
    assert data.records[0].artist.links[0].name == "string"
    assert data.records[0].artist.images[0].url == "string"
    assert data.records[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data.records[0].artist.images[0].extension == "string"
    assert data.records[0].artist.path == "string"
    assert isinstance(data.records[0].artist.qualityProfileId, int)
    assert isinstance(data.records[0].artist.metadataProfileId, int)
    assert data.records[0].artist.monitored is True
    assert data.records[0].artist.genres == ["string"]
    assert data.records[0].artist.cleanName == "string"
    assert data.records[0].artist.sortName == "string"
    assert isinstance(data.records[0].artist.tags[0], int)
    assert data.records[0].artist.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data.records[0].artist.ratings.votes, int)
    assert isinstance(data.records[0].artist.ratings.value, float)
    assert isinstance(data.records[0].artist.statistics.albumCount, int)
    assert isinstance(data.records[0].artist.statistics.trackFileCount, int)
    assert isinstance(data.records[0].artist.statistics.trackCount, int)
    assert isinstance(data.records[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data.records[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data.records[0].artist.id, int)
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/calendar?unmonitored=False&start=2020-11-30&end=2020-12-01",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/calendar.json"),
        ),
        match_querystring=True,
    )
    start = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    end = datetime.strptime("Dec 1 2020  1:33PM", "%b %d %Y %I:%M%p")
    data = await lidarr_client.async_get_calendar(start, end)
    assert data[0].title == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert isinstance(data[0].artistId, int)
    assert data[0].foreignAlbumId == "string"
    assert data[0].monitored is True
    assert data[0].anyReleaseOk is True
    assert isinstance(data[0].profileId, int)
    assert isinstance(data[0].duration, int)
    assert data[0].albumType == "string"
    assert isinstance(data[0].secondaryTypes[0].id, int)
    assert data[0].secondaryTypes[0].name == "string"
    assert isinstance(data[0].mediumCount, int)
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert data[0].releaseDate == datetime(2020, 2, 14, 0, 0)
    assert isinstance(data[0].releases[0].id, int)
    assert isinstance(data[0].releases[0].albumId, int)
    assert data[0].releases[0].foreignReleaseId == "string"
    assert data[0].releases[0].title == "string"
    assert data[0].releases[0].status == "string"
    assert isinstance(data[0].releases[0].duration, int)
    assert isinstance(data[0].releases[0].trackCount, int)
    assert isinstance(data[0].releases[0].media[0].mediumNumber, int)
    assert data[0].releases[0].media[0].mediumName == "string"
    assert data[0].releases[0].media[0].mediumFormat == "string"
    assert isinstance(data[0].releases[0].mediumCount, int)
    assert data[0].releases[0].disambiguation == "string"
    assert data[0].releases[0].country == ["string"]
    assert data[0].releases[0].label == ["string"]
    assert data[0].releases[0].format == "string"
    assert data[0].releases[0].monitored is True
    assert data[0].genres == ["string"]
    assert isinstance(data[0].media[0].mediumNumber, int)
    assert data[0].media[0].mediumName == "string"
    assert data[0].media[0].mediumFormat == "string"
    assert data[0].artist.status == StatusType.ENDED.value
    assert data[0].artist.ended is True
    assert data[0].artist.artistName == "string"
    assert data[0].artist.foreignArtistId == "string"
    assert isinstance(data[0].artist.tadbId, int)
    assert isinstance(data[0].artist.discogsId, int)
    assert data[0].artist.overview == "string"
    assert data[0].artist.artistType == "string"
    assert data[0].artist.disambiguation == "string"
    assert data[0].artist.links[0].url == "string"
    assert data[0].artist.links[0].name == "string"
    assert data[0].artist.images[0].url == "string"
    assert data[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres == ["string"]
    assert data[0].artist.cleanName == "string"
    assert data[0].artist.sortName == "string"
    assert isinstance(data[0].artist.tags[0], int)
    assert data[0].artist.added == datetime(2021, 8, 21, 15, 37, 39, 225947)
    assert isinstance(data[0].artist.ratings.votes, int)
    assert isinstance(data[0].artist.ratings.value, float)
    assert isinstance(data[0].artist.statistics.albumCount, int)
    assert isinstance(data[0].artist.statistics.trackFileCount, int)
    assert isinstance(data[0].artist.statistics.trackCount, int)
    assert isinstance(data[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].artist.id, int)
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert isinstance(data[0].statistics.trackFileCount, int)
    assert isinstance(data[0].statistics.trackCount, int)
    assert isinstance(data[0].statistics.totalTrackCount, int)
    assert isinstance(data[0].statistics.sizeOnDisk, int)
    assert isinstance(data[0].statistics.percentOfTracks, float)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_lidarr_commands(aresponses, lidarr_client: LidarrClient) -> None:
    """Test sending lidarr commands."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_lidarr_command(LidarrCommands.ALBUM_SEARCH)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.APP_UPDATE_CHECK)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.ARTIST_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.ALBUM_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.MISSING_ALBUM_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.REFRESH_ALBUM)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_lidarr_command(LidarrCommands.REFRESH_ARTIST)


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting wanted."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/wanted/cutoff/0?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/album.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_wanted(recordid=0, missing=False)
    assert data.title == "string"
    assert data.disambiguation == "string"
    assert data.overview == "string"
    assert isinstance(data.artistId, int)
    assert data.foreignAlbumId == "string"
    assert data.monitored is True
    assert data.anyReleaseOk is True
    assert isinstance(data.profileId, int)
    assert isinstance(data.duration, int)
    assert data.albumType == "string"
    assert isinstance(data.secondaryTypes[0].id, int)
    assert data.secondaryTypes[0].name == "string"
    assert isinstance(data.mediumCount, int)
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert data.releaseDate == datetime(2010, 8, 23, 0, 0)
    assert isinstance(data.releases[0].id, int)
    assert isinstance(data.releases[0].albumId, int)
    assert data.releases[0].foreignReleaseId == "string"
    assert data.releases[0].title == "string"
    assert data.releases[0].status == "string"
    assert isinstance(data.releases[0].duration, int)
    assert isinstance(data.releases[0].trackCount, int)
    assert isinstance(data.releases[0].media[0].mediumNumber, int)
    assert data.releases[0].media[0].mediumName == "string"
    assert data.releases[0].media[0].mediumFormat == "string"
    assert isinstance(data.releases[0].mediumCount, int)
    assert data.releases[0].disambiguation == "string"
    assert data.releases[0].country == ["string"]
    assert data.releases[0].label == ["string"]
    assert data.releases[0].format == "string"
    assert data.releases[0].monitored is True
    assert data.genres == ["string"]
    assert isinstance(data.media[0].mediumNumber, int)
    assert data.media[0].mediumName == "string"
    assert data.media[0].mediumFormat == "string"
    assert data.artist.status == StatusType.ENDED.value
    assert data.artist.ended is True
    assert data.artist.artistName == "string"
    assert data.artist.foreignArtistId == "string"
    assert isinstance(data.artist.tadbId, int)
    assert isinstance(data.artist.discogsId, int)
    assert data.artist.overview == "string"
    assert data.artist.artistType == "string"
    assert data.artist.disambiguation == "string"
    assert data.artist.links[0].url == "string"
    assert data.artist.links[0].name == "string"
    assert data.artist.images[0].url == "string"
    assert data.artist.images[0].coverType == ImageType.POSTER.value
    assert data.artist.images[0].extension == "string"
    assert data.artist.path == "string"
    assert isinstance(data.artist.qualityProfileId, int)
    assert isinstance(data.artist.metadataProfileId, int)
    assert data.artist.monitored is True
    assert data.artist.genres == ["string"]
    assert data.artist.cleanName == "string"
    assert data.artist.sortName == "string"
    assert isinstance(data.artist.tags[0], int)
    assert data.artist.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data.artist.ratings.votes, int)
    assert isinstance(data.artist.ratings.value, float)
    assert isinstance(data.artist.statistics.albumCount, int)
    assert isinstance(data.artist.statistics.trackFileCount, int)
    assert isinstance(data.artist.statistics.trackCount, int)
    assert isinstance(data.artist.statistics.totalTrackCount, int)
    assert isinstance(data.artist.statistics.sizeOnDisk, int)
    assert isinstance(data.artist.statistics.percentOfTracks, float)
    assert isinstance(data.artist.id, int)
    assert data.images[0].url == "string"
    assert data.images[0].coverType == ImageType.POSTER.value
    assert data.images[0].extension == "string"
    assert data.links[0].url == "string"
    assert data.links[0].name == "string"
    assert isinstance(data.statistics.trackFileCount, int)
    assert isinstance(data.statistics.trackCount, int)
    assert isinstance(data.statistics.totalTrackCount, int)
    assert isinstance(data.statistics.sizeOnDisk, int)
    assert isinstance(data.statistics.percentOfTracks, float)
    assert isinstance(data.id, int)

    data = {"records": ["test"]}
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/wanted/missing?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=json.dumps(data),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_wanted()
    assert isinstance(data, LidarrWantedCutoff)
    assert isinstance(data.records[0], LidarrAlbum)


@pytest.mark.asyncio
async def test_async_parse(aresponses, lidarr_client: LidarrClient) -> None:
    """Test parsing track file name."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/parse?title=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/parse.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_parse("test")
    assert data.title == "string"
    assert data.parsedAlbumInfo.albumTitle == "string"
    assert data.parsedAlbumInfo.artistName == "string"
    assert data.parsedAlbumInfo.artistTitleInfo.title == "string"
    assert isinstance(data.parsedAlbumInfo.artistTitleInfo.year, int)
    assert isinstance(data.parsedAlbumInfo.quality.quality.id, int)
    assert data.parsedAlbumInfo.quality.quality.name == "string"
    assert isinstance(data.parsedAlbumInfo.quality.revision.version, int)
    assert isinstance(data.parsedAlbumInfo.quality.revision.real, int)
    assert data.parsedAlbumInfo.quality.revision.isRepack is False
    assert isinstance(data.parsedAlbumInfo.releaseDate, int)
    assert data.parsedAlbumInfo.discography is False
    assert isinstance(data.parsedAlbumInfo.discographyStart, int)
    assert isinstance(data.parsedAlbumInfo.discographyEnd, int)
    assert data.parsedAlbumInfo.releaseGroup == "string"
    assert data.parsedAlbumInfo.releaseHash == "string"
    assert data.parsedAlbumInfo.releaseVersion == "string"
    assert isinstance(data.artist, LidarrArtist)
    assert isinstance(data.albums[0], LidarrAlbum)


@pytest.mark.asyncio
async def test_async_get_importlist(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting import list."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/importlist.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_import_lists()
    assert data[0].enableAutomaticAdd is False
    assert data[0].shouldMonitor == LidarrImportListMonitorType.ENTIRE_ARTIST.value
    assert data[0].rootFolderPath == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert isinstance(data[0].metadataProfileId, int)
    assert data[0].listType == LidarrImportListType.OTHER.value
    assert isinstance(data[0].listOrder, int)
    assert data[0].name == "string"
    assert isinstance(data[0].fields[0].order, int)
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == []
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].selectOptionsProviderAction == "string"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert isinstance(data[0].tags[0], int)
    _value = data[0].presets[0]
    assert _value.enableAutomaticAdd is False
    assert _value.shouldMonitor == LidarrImportListMonitorType.ENTIRE_ARTIST.value
    assert _value.rootFolderPath == "string"
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert _value.listType == LidarrImportListType.OTHER.value
    assert isinstance(_value.listOrder, int)
    assert _value.name == "string"
    assert isinstance(_value.fields[0].order, int)
    assert _value.fields[0].name == "string"
    assert _value.fields[0].label == "string"
    assert _value.fields[0].value == "string"
    assert _value.fields[0].type == "string"
    assert _value.fields[0].advanced is True
    assert _value.implementation == "string"
    assert _value.configContract == "string"
    assert _value.infoLink == "string"
    assert isinstance(_value.tags[0], int)
    assert isinstance(data[0].id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_import_lists(0)


@pytest.mark.asyncio
async def test_async_edit_importlist(aresponses, lidarr_client: LidarrClient) -> None:
    """Test editing import list."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_edit_import_list(LidarrImportList("test"))
    assert isinstance(data, LidarrImportList)


@pytest.mark.asyncio
async def test_async_add_importlist(aresponses, lidarr_client: LidarrClient) -> None:
    """Test adding import list."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_add_import_list(LidarrImportList("test"))
    assert isinstance(data, LidarrImportList)


@pytest.mark.asyncio
async def test_async_test_import_lists(aresponses, lidarr_client: LidarrClient) -> None:
    """Test import list testing."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/test",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    data = LidarrImportList("test")
    assert await lidarr_client.async_test_import_lists(data) is True

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    assert await lidarr_client.async_test_import_lists() is True

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    assert await lidarr_client.async_test_import_lists() is False


@pytest.mark.asyncio
async def test_async_importlist_action(aresponses, lidarr_client: LidarrClient) -> None:
    """Test performing import list action."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/action/getProfiles",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_importlist_action(LidarrImportListActionType.GET_PROFILES)

    with pytest.raises(ArrException):
        await lidarr_client.async_importlist_action(
            LidarrImportListActionType.GET_PLAYLISTS
        )


@pytest.mark.asyncio
async def test_async_get_history(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting_history."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history?page=1&pageSize=10&sortKey=date&sortDirection=default&eventType=1&includeArtist=True&includeAlbum=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/history.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_history(
        event_type=LidarrEventType.GRABBED, artist=True, album=True
    )
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == LidarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DESCENDING.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].albumId, int)
    assert isinstance(data.records[0].artistId, int)
    assert isinstance(data.records[0].trackId, int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].qualityCutoffNotMet is False
    assert data.records[0].date == datetime(2020, 2, 16, 14, 3, 43, 622491)
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == LidarrEventType.GRABBED.name.lower()
    assert data.records[0].data.indexer == "string"
    assert data.records[0].data.nzbInfoUrl == "string"
    assert data.records[0].data.releaseGroup == "string"
    assert isinstance(data.records[0].data.age, int)
    assert isinstance(data.records[0].data.ageHours, float)
    assert isinstance(data.records[0].data.ageMinutes, float)
    assert data.records[0].data.publishedDate == datetime(2020, 2, 16, 6, 11)
    assert data.records[0].data.downloadClient == "string"
    assert isinstance(data.records[0].data.size, int)
    assert data.records[0].data.downloadUrl == "string"
    assert data.records[0].data.guid == "string"
    assert data.records[0].data.protocol is ProtocolType.UNKNOWN
    assert data.records[0].data.downloadForced is False
    assert data.records[0].data.torrentInfoHash == "string"
    _value = data.records[0].album
    assert _value.title == "string"
    assert _value.disambiguation == "string"
    assert _value.overview == "string"
    assert isinstance(_value.artistId, int)
    assert _value.foreignAlbumId == "string"
    assert _value.monitored is True
    assert _value.anyReleaseOk is True
    assert isinstance(_value.profileId, int)
    assert isinstance(_value.duration, int)
    assert _value.albumType == "string"
    assert isinstance(_value.secondaryTypes[0].id, int)
    assert _value.secondaryTypes[0].name == "string"
    assert isinstance(_value.mediumCount, int)
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert _value.releaseDate == datetime(2015, 11, 13, 0, 0)
    assert isinstance(_value.releases[0].id, int)
    assert isinstance(_value.releases[0].albumId, int)
    assert _value.releases[0].foreignReleaseId == "string"
    assert _value.releases[0].title == "string"
    assert _value.releases[0].status == "string"
    assert isinstance(_value.releases[0].duration, int)
    assert isinstance(_value.releases[0].trackCount, int)
    assert isinstance(_value.releases[0].media[0].mediumNumber, int)
    assert _value.releases[0].media[0].mediumName == "string"
    assert _value.releases[0].media[0].mediumFormat == "string"
    assert isinstance(_value.releases[0].mediumCount, int)
    assert _value.releases[0].disambiguation == "string"
    assert _value.releases[0].country == ["string"]
    assert _value.releases[0].label == ["string"]
    assert _value.releases[0].format == "string"
    assert _value.releases[0].monitored is False
    assert _value.genres == ["string"]
    assert isinstance(_value.media[0].mediumNumber, int)
    assert _value.media[0].mediumName == "string"
    assert _value.media[0].mediumFormat == "string"
    _valu = _value.artist
    assert _valu.status == StatusType.ENDED.value
    assert _valu.ended is False
    assert _valu.artistName == "string"
    assert _valu.foreignArtistId == "string"
    assert isinstance(_valu.tadbId, int)
    assert isinstance(_valu.discogsId, int)
    assert _valu.overview == "string"
    assert _valu.artistType == "string"
    assert _valu.disambiguation == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.path == "string"
    assert isinstance(_valu.qualityProfileId, int)
    assert isinstance(_valu.metadataProfileId, int)
    assert _valu.monitored is True
    assert _valu.genres == ["string"]
    assert _valu.cleanName == "string"
    assert _valu.sortName == "string"
    assert isinstance(_valu.tags[0], int)
    assert _valu.added == datetime(2021, 8, 21, 15, 56, 31, 922597)
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.statistics.albumCount, int)
    assert isinstance(_valu.statistics.trackFileCount, int)
    assert isinstance(_valu.statistics.trackCount, int)
    assert isinstance(_valu.statistics.sizeOnDisk, int)
    assert isinstance(_valu.statistics.percentOfTracks, float)
    assert isinstance(_valu.id, int)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.id, int)
    assert data.records[0].artist.status == StatusType.ENDED.value
    assert data.records[0].artist.ended is False
    assert data.records[0].artist.artistName == "string"
    assert data.records[0].artist.foreignArtistId == "string"
    assert isinstance(data.records[0].artist.tadbId, int)
    assert isinstance(data.records[0].artist.discogsId, int)
    assert data.records[0].artist.overview == "string"
    assert data.records[0].artist.artistType == "string"
    assert data.records[0].artist.disambiguation == "string"
    assert data.records[0].artist.links[0].url == "string"
    assert data.records[0].artist.links[0].name == "string"
    assert data.records[0].artist.images[0].url == "string"
    assert data.records[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data.records[0].artist.images[0].extension == "string"
    assert data.records[0].artist.path == "string"
    assert isinstance(data.records[0].artist.qualityProfileId, int)
    assert isinstance(data.records[0].artist.metadataProfileId, int)
    assert data.records[0].artist.monitored is True
    assert data.records[0].artist.genres == ["string"]
    assert data.records[0].artist.cleanName == "string"
    assert data.records[0].artist.sortName == "string"
    assert isinstance(data.records[0].artist.tags[0], int)
    assert data.records[0].artist.added == datetime(2021, 8, 21, 15, 56, 31, 922597)
    assert isinstance(data.records[0].artist.ratings.votes, int)
    assert isinstance(data.records[0].artist.ratings.value, float)
    assert isinstance(data.records[0].artist.statistics.albumCount, int)
    assert isinstance(data.records[0].artist.statistics.trackFileCount, int)
    assert isinstance(data.records[0].artist.statistics.trackCount, int)
    assert isinstance(data.records[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data.records[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data.records[0].artist.id, int)
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_history_since(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting history since specified date."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/since?eventType=1&date=2020-11-30",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    date = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    data = await lidarr_client.async_get_history_since(
        date=date, event_type=LidarrEventType.GRABBED
    )
    assert isinstance(data, LidarrAlbumHistory)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/artist?artistId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_history_since(artistid=0)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/artist?artistId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )

    with pytest.raises(ArrException):
        await lidarr_client.async_get_history_since()


@pytest.mark.asyncio
async def test_async_get_metadata_profiles(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/metadataprofile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/metadata-profile.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_metadata_profiles()
    assert data[0].name == "string"
    assert isinstance(data[0].primaryAlbumTypes[0].albumType.id, int)
    assert data[0].primaryAlbumTypes[0].albumType.name == "string"
    assert data[0].primaryAlbumTypes[0].allowed is False
    assert isinstance(data[0].secondaryAlbumTypes[0].albumType.id, int)
    assert data[0].secondaryAlbumTypes[0].albumType.name == "string"
    assert data[0].secondaryAlbumTypes[0].allowed is True
    assert isinstance(data[0].releaseStatuses[0].releaseStatus.id, int)
    assert data[0].releaseStatuses[0].releaseStatus.name == "string"
    assert data[0].releaseStatuses[0].allowed is False
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_edit_metadata_profile(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test editing metadata profile."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/metadataprofile",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = LidarrMetadataProfile("test")
    data = await lidarr_client.async_edit_metadata_profile(data)
    assert isinstance(data, LidarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_add_metadata_profile(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test adding metadata profile."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/metadataprofile",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = LidarrMetadataProfile("test")
    data = await lidarr_client.async_add_metadata_profile(data)
    assert isinstance(data, LidarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_get_queue(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/queue?page=1&pageSize=10&sortKey=timeleft&includeUnknownArtistItems=False&includeArtist=False&includeAlbum=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/queue.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_queue()
    assert isinstance(data.page, int)
    assert isinstance(data.page, int)
    assert data.sortKey == LidarrSortKeys.TIMELEFT.value
    assert data.sortDirection == SortDirection.ASCENDING.value
    assert isinstance(data.totalRecords, int)
    _value = data.records[0]
    assert isinstance(_value.artistId, int)
    assert isinstance(_value.albumId, int)
    assert _value.artist.status == "string"
    assert _value.artist.ended is False
    assert _value.artist.artistName == "string"
    assert _value.artist.foreignArtistId == "string"
    assert isinstance(_value.artist.tadbId, int)
    assert isinstance(_value.artist.discogsId, int)
    assert _value.artist.overview == "string"
    assert _value.artist.artistType == "string"
    assert _value.artist.disambiguation == "string"
    assert _value.artist.links[0].url == "string"
    assert _value.artist.links[0].name == "string"
    assert _value.artist.images[0].url == "string"
    assert _value.artist.images[0].coverType == ImageType.POSTER.value
    assert _value.artist.images[0].extension == "string"
    assert _value.artist.path == "string"
    assert isinstance(_value.artist.qualityProfileId, int)
    assert isinstance(_value.artist.metadataProfileId, int)
    assert _value.artist.monitored is True
    assert _value.artist.genres == ["string"]
    assert _value.artist.cleanName == "string"
    assert _value.artist.sortName == "string"
    assert isinstance(_value.artist.tags[0], int)
    assert _value.artist.added == datetime(2021, 8, 21, 15, 38, 22, 723851)
    assert isinstance(_value.artist.ratings.votes, int)
    assert isinstance(_value.artist.ratings.value, float)
    assert isinstance(_value.artist.statistics.albumCount, int)
    assert isinstance(_value.artist.statistics.trackFileCount, int)
    assert isinstance(_value.artist.statistics.trackCount, int)
    assert isinstance(_value.artist.statistics.sizeOnDisk, int)
    assert isinstance(_value.artist.statistics.percentOfTracks, float)
    assert isinstance(_value.artist.id, int)
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is False
    assert isinstance(_value.size, int)
    assert _value.title == "string"
    assert isinstance(_value.sizeleft, int)
    assert _value.timeleft == "00:00:00"
    assert _value.estimatedCompletionTime == datetime(2020, 2, 16, 23, 34, 44, 885649)
    assert _value.status == "string"
    assert _value.trackedDownloadStatus == "string"
    assert _value.trackedDownloadState == "string"
    assert _value.statusMessages[0].title == "string"
    assert _value.statusMessages[0].messages == ["string"]
    assert _value.downloadId == "string"
    assert _value.protocol is ProtocolType.UNKNOWN
    assert _value.downloadClient == "string"
    assert _value.indexer == "string"
    assert _value.outputPath == "string"
    assert _value.downloadForced is False
    assert isinstance(_value.id, int)


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/queue/details?includeArtist=False&includeAlbum=True&artistId=0&albumIds=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_queue_details(artistid=0, albumids=[0])
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert data[0].artist.status == "string"
    assert data[0].artist.ended is False
    assert data[0].artist.artistName == "string"
    assert data[0].artist.foreignArtistId == "string"
    assert isinstance(data[0].artist.tadbId, int)
    assert isinstance(data[0].artist.discogsId, int)
    assert data[0].artist.overview == "string"
    assert data[0].artist.artistType == "string"
    assert data[0].artist.disambiguation == "string"
    assert data[0].artist.links[0].url == "string"
    assert data[0].artist.links[0].name == "string"
    assert data[0].artist.images[0].url == "string"
    assert data[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres == ["string"]
    assert data[0].artist.cleanName == "string"
    assert data[0].artist.sortName == "string"
    assert isinstance(data[0].artist.tags[0], int)
    assert data[0].artist.added == datetime(2021, 8, 21, 15, 56, 31, 922597)
    assert isinstance(data[0].artist.ratings.votes, int)
    assert isinstance(data[0].artist.ratings.value, float)
    assert isinstance(data[0].artist.statistics.albumCount, int)
    assert isinstance(data[0].artist.statistics.trackFileCount, int)
    assert isinstance(data[0].artist.statistics.trackCount, int)
    assert isinstance(data[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].artist.id, int)
    assert data[0].album.title == "string"
    assert data[0].album.disambiguation == "string"
    assert data[0].album.overview == "string"
    assert isinstance(data[0].album.artistId, int)
    assert data[0].album.foreignAlbumId == "string"
    assert data[0].album.monitored is True
    assert data[0].album.anyReleaseOk is True
    assert isinstance(data[0].album.profileId, int)
    assert isinstance(data[0].album.duration, int)
    assert data[0].album.albumType == "string"
    assert isinstance(data[0].album.secondaryTypes[0].id, int)
    assert data[0].album.secondaryTypes[0].name == "string"
    assert isinstance(data[0].album.mediumCount, int)
    assert isinstance(data[0].album.ratings.votes, int)
    assert isinstance(data[0].album.ratings.value, float)
    assert data[0].album.releaseDate == datetime(2010, 11, 12, 0, 0)
    assert isinstance(data[0].album.releases[0].id, int)
    assert isinstance(data[0].album.releases[0].albumId, int)
    assert data[0].album.releases[0].foreignReleaseId == "string"
    assert data[0].album.releases[0].title == "string"
    assert data[0].album.releases[0].status == "string"
    assert isinstance(data[0].album.releases[0].duration, int)
    assert isinstance(data[0].album.releases[0].trackCount, int)
    assert isinstance(data[0].album.releases[0].media[0].mediumNumber, int)
    assert data[0].album.releases[0].media[0].mediumName == "string"
    assert data[0].album.releases[0].media[0].mediumFormat == "string"
    assert isinstance(data[0].album.releases[0].mediumCount, int)
    assert data[0].album.releases[0].disambiguation == "string"
    assert data[0].album.releases[0].country == ["string"]
    assert data[0].album.releases[0].label == ["string"]
    assert data[0].album.releases[0].format == "string"
    assert data[0].album.releases[0].monitored is False
    assert data[0].album.genres == ["string"]
    assert isinstance(data[0].album.media[0].mediumNumber, int)
    assert data[0].album.media[0].mediumName == "string"
    assert data[0].album.media[0].mediumFormat == "string"
    assert data[0].album.artist.status == "string"
    assert data[0].album.artist.ended is False
    assert data[0].album.artist.artistName == "string"
    assert data[0].album.artist.foreignArtistId == "string"
    assert isinstance(data[0].album.artist.tadbId, int)
    assert isinstance(data[0].album.artist.discogsId, int)
    assert data[0].album.artist.overview == "string"
    assert data[0].album.artist.artistType == "string"
    assert data[0].album.artist.disambiguation == "string"
    assert data[0].album.artist.links[0].url == "string"
    assert data[0].album.artist.links[0].name == "string"
    assert data[0].album.artist.images[0].url == "string"
    assert data[0].album.artist.images[0].coverType == ImageType.POSTER.value
    assert data[0].album.artist.images[0].extension == "string"
    assert data[0].album.artist.path == "string"
    assert isinstance(data[0].album.artist.qualityProfileId, int)
    assert isinstance(data[0].album.artist.metadataProfileId, int)
    assert data[0].album.artist.monitored is True
    assert data[0].album.artist.genres == ["string"]
    assert data[0].album.artist.cleanName == "string"
    assert data[0].album.artist.sortName == "string"
    assert isinstance(data[0].album.artist.tags[0], int)
    assert data[0].album.artist.added == datetime(2021, 8, 21, 15, 56, 31, 922597)
    assert isinstance(data[0].album.artist.ratings.votes, int)
    assert isinstance(data[0].album.artist.ratings.value, float)
    assert isinstance(data[0].album.artist.statistics.albumCount, int)
    assert isinstance(data[0].album.artist.statistics.trackFileCount, int)
    assert isinstance(data[0].album.artist.statistics.trackCount, int)
    assert isinstance(data[0].album.artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].album.artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].album.artist.id, int)
    assert data[0].album.images[0].url == "string"
    assert data[0].album.images[0].coverType == ImageType.POSTER.value
    assert data[0].album.images[0].extension == "string"
    assert data[0].album.links[0].url == "string"
    assert data[0].album.links[0].name == "string"
    assert isinstance(data[0].album.id, int)
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].size, int)
    assert data[0].title == "string"
    assert isinstance(data[0].sizeleft, int)
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2020, 2, 16, 23, 49, 45, 143727)
    assert data[0].status == "string"
    assert data[0].trackedDownloadStatus == "string"
    assert data[0].trackedDownloadState == "string"
    assert data[0].statusMessages[0].title == "string"
    assert data[0].statusMessages[0].messages == ["string"]
    assert data[0].downloadId == "string"
    assert data[0].protocol is ProtocolType.UNKNOWN
    assert data[0].downloadClient == "string"
    assert data[0].indexer == "string"
    assert data[0].outputPath == "string"
    assert data[0].downloadForced is False
    assert isinstance(data[0].id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/queue/details?includeArtist=False&includeAlbum=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_get_queue_details()


@pytest.mark.asyncio
async def test_async_get_release(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting release."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/release?artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/release.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_release(artistid=0, albumid=0)
    assert data[0].guid == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].qualityWeight, int)
    assert isinstance(data[0].age, int)
    assert isinstance(data[0].ageHours, float)
    assert isinstance(data[0].ageMinutes, float)
    assert isinstance(data[0].size, int)
    assert isinstance(data[0].indexerId, int)
    assert data[0].indexer == "string"
    assert data[0].releaseHash == "string"
    assert data[0].title == "string"
    assert data[0].discography is False
    assert data[0].sceneSource is False
    assert data[0].artistName == "string"
    assert data[0].albumTitle == "string"
    assert data[0].approved is False
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is True
    assert data[0].rejections[0].reason == "string"
    assert data[0].rejections[0].type == "permanent"
    assert data[0].publishDate == datetime(2020, 2, 16, 20, 8, 16)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoHash == "string"
    assert data[0].downloadAllowed is True
    assert isinstance(data[0].releaseWeight, int)
    assert isinstance(data[0].preferredWordScore, int)
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert isinstance(data[0].seeders, int)
    assert isinstance(data[0].leechers, int)
    assert data[0].protocol is ProtocolType.UNKNOWN


@pytest.mark.asyncio
async def test_async_download_release(aresponses, lidarr_client: LidarrClient) -> None:
    """Test downloading release."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/release",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_download_release("test", 0)
    assert isinstance(data, LidarrRelease)


@pytest.mark.asyncio
async def test_async_get_root_folders(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting root folders."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/rootfolder",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/rootfolder.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_root_folders()

    assert data[0].name == "music"
    assert data[0].path == "/music/"
    assert isinstance(data[0].defaultMetadataProfileId, int)
    assert isinstance(data[0].defaultQualityProfileId, int)
    assert data[0].defaultMonitorOption == "all"
    assert data[0].defaultNewItemMonitorOption == "all"
    assert data[0].defaultTags == []
    assert data[0].accessible is True
    assert isinstance(data[0].freeSpace, int)
    assert isinstance(data[0].totalSpace, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_push_release(aresponses, lidarr_client: LidarrClient) -> None:
    """Test pushing release."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/release/push",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_push_release("test")
    assert isinstance(data, LidarrRelease)


@pytest.mark.asyncio
async def test_async_get_rename(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/rename?artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/rename.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_rename(0, albumid=0)
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert isinstance(data[0].trackNumbers[0], int)
    assert isinstance(data[0].trackFileId, int)
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_manual_import(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting manual import."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/manualimport?artistId=0&downloadId=abc123&filterExistingFiles=True&folder=&replaceExistingFiles=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/manualimport.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_manual_import("abc123")
    assert data[0].path == "string"
    assert data[0].name == "string"
    assert isinstance(data[0].size, int)
    assert data[0].artist.status == StatusType.CONTINUING.value
    assert data[0].artist.ended is False
    assert data[0].artist.artistName == "string"
    assert isinstance(data[0].artist.foreignArtistId, str)
    assert isinstance(data[0].artist.tadbId, int)
    assert isinstance(data[0].artist.discogsId, int)
    assert data[0].artist.overview == "string"
    assert data[0].artist.artistType == "Person"
    assert data[0].artist.disambiguation == "string"
    assert data[0].artist.links[0].url == "string"
    assert data[0].artist.links[0].name == "discogs"
    assert data[0].artist.images[0].url == "string"
    assert data[0].artist.images[0].coverType == ImageType.BANNER.value
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres == ["string"]
    assert data[0].artist.cleanName == "string"
    assert data[0].artist.sortName == "string"
    assert isinstance(data[0].artist.tags[0], int)
    assert data[0].artist.added == datetime(2020, 2, 20, 14, 6, 21, 541356)
    assert isinstance(data[0].artist.ratings.votes, int)
    assert isinstance(data[0].artist.ratings.value, float)
    assert isinstance(data[0].artist.statistics.albumCount, int)
    assert isinstance(data[0].artist.statistics.trackFileCount, int)
    assert isinstance(data[0].artist.statistics.trackCount, int)
    assert isinstance(data[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].artist.id, int)
    assert data[0].album.title == "string"
    assert data[0].album.disambiguation == "string"
    assert data[0].album.overview == "string"
    assert isinstance(data[0].album.artistId, int)
    assert isinstance(data[0].album.foreignAlbumId, str)
    assert data[0].album.monitored is True
    assert data[0].album.anyReleaseOk is True
    assert isinstance(data[0].album.profileId, int)
    assert isinstance(data[0].album.duration, int)
    assert data[0].album.albumType == "string"
    assert isinstance(data[0].album.secondaryTypes[0].id, int)
    assert data[0].album.secondaryTypes[0].name == "string"
    assert isinstance(data[0].album.mediumCount, int)
    assert isinstance(data[0].album.ratings.votes, int)
    assert isinstance(data[0].album.ratings.value, float)
    assert data[0].album.releaseDate == datetime(2019, 7, 25, 0, 0)
    assert isinstance(data[0].album.releases[0].id, int)
    assert isinstance(data[0].album.releases[0].albumId, int)
    assert data[0].album.releases[0].foreignReleaseId == "string"
    assert data[0].album.releases[0].title == "string"
    assert data[0].album.releases[0].status == "Official"
    assert isinstance(data[0].album.releases[0].duration, int)
    assert isinstance(data[0].album.releases[0].trackCount, int)
    assert isinstance(data[0].album.releases[0].media[0].mediumNumber, int)
    assert data[0].album.releases[0].media[0].mediumName == "string"
    assert data[0].album.releases[0].media[0].mediumFormat == "string"
    assert isinstance(data[0].album.releases[0].mediumCount, int)
    assert data[0].album.releases[0].disambiguation == "string"
    assert data[0].album.releases[0].country == ["string"]
    assert data[0].album.releases[0].label == ["string"]
    assert data[0].album.releases[0].format == "string"
    assert data[0].album.releases[0].monitored is False
    assert data[0].album.genres == ["string"]
    assert isinstance(data[0].album.media[0].mediumNumber, int)
    assert data[0].album.media[0].mediumName == "string"
    assert data[0].album.media[0].mediumFormat == "string"
    assert data[0].album.artist.status == StatusType.CONTINUING.value
    assert data[0].album.artist.ended is False
    assert data[0].album.artist.artistName == "string"
    assert isinstance(data[0].album.artist.foreignArtistId, str)
    assert isinstance(data[0].album.artist.tadbId, int)
    assert isinstance(data[0].album.artist.discogsId, int)
    assert data[0].album.artist.overview == "string"
    assert data[0].album.artist.artistType == "Person"
    assert data[0].album.artist.disambiguation == "string"
    assert data[0].album.artist.links[0].url == "string"
    assert data[0].album.artist.links[0].name == "discogs"
    assert data[0].album.artist.images[0].url == "string"
    assert data[0].album.artist.images[0].coverType == ImageType.BANNER.value
    assert data[0].album.artist.images[0].extension == "string"
    assert data[0].album.artist.path == "string"
    assert isinstance(data[0].album.artist.qualityProfileId, int)
    assert isinstance(data[0].album.artist.metadataProfileId, int)
    assert data[0].album.artist.monitored is True
    assert data[0].album.artist.genres == ["string"]
    assert data[0].album.artist.cleanName == "string"
    assert data[0].album.artist.sortName == "string"
    assert isinstance(data[0].album.artist.tags[0], int)
    assert data[0].album.artist.added == datetime(2020, 2, 20, 14, 6, 21, 541356)
    assert isinstance(data[0].album.artist.ratings.votes, int)
    assert isinstance(data[0].album.artist.ratings.value, float)
    assert isinstance(data[0].album.artist.statistics.albumCount, int)
    assert isinstance(data[0].album.artist.statistics.trackFileCount, int)
    assert isinstance(data[0].album.artist.statistics.trackCount, int)
    assert isinstance(data[0].album.artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].album.artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].album.artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].album.artist.id, int)
    assert data[0].album.images[0].url == "string"
    assert data[0].album.images[0].coverType == ImageType.COVER.value
    assert data[0].album.images[0].extension == "string"
    assert data[0].album.links[0].url == "string"
    assert data[0].album.links[0].name == "string"
    assert isinstance(data[0].album.id, int)
    assert isinstance(data[0].albumReleaseId, int)
    assert isinstance(data[0].tracks[0].artistId, int)
    assert isinstance(data[0].tracks[0].trackFileId, int)
    assert isinstance(data[0].tracks[0].albumId, int)
    assert data[0].tracks[0].explicit is False
    assert isinstance(data[0].tracks[0].absoluteTrackNumber, int)
    assert isinstance(data[0].tracks[0].trackNumber, int)
    assert data[0].tracks[0].title == "string"
    assert isinstance(data[0].tracks[0].duration, int)
    assert isinstance(data[0].tracks[0].mediumNumber, int)
    assert data[0].tracks[0].hasFile is False
    assert isinstance(data[0].tracks[0].ratings.votes, int)
    assert isinstance(data[0].tracks[0].ratings.value, float)
    assert isinstance(data[0].tracks[0].id, int)
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].qualityWeight, int)
    assert data[0].downloadId == "string"
    assert data[0].rejections[0].reason == "string"
    assert data[0].rejections[0].type == "permanent"
    assert data[0].audioTags.title == "string"
    assert data[0].audioTags.cleanTitle == "string"
    assert data[0].audioTags.artistTitle == "string"
    assert data[0].audioTags.artistTitleInfo.title == "string"
    assert isinstance(data[0].audioTags.artistTitleInfo.year, int)
    assert isinstance(data[0].audioTags.discNumber, int)
    assert isinstance(data[0].audioTags.discCount, int)
    assert isinstance(data[0].audioTags.year, int)
    assert data[0].audioTags.duration == "00:00:00.4800000"
    assert isinstance(data[0].audioTags.quality.quality.id, int)
    assert data[0].audioTags.quality.quality.name == "FLAC"
    assert isinstance(data[0].audioTags.quality.revision.version, int)
    assert isinstance(data[0].audioTags.quality.revision.real, int)
    assert data[0].audioTags.quality.revision.isRepack is False
    assert data[0].audioTags.mediaInfo.audioFormat == "string"
    assert isinstance(data[0].audioTags.mediaInfo.audioBitrate, int)
    assert isinstance(data[0].audioTags.mediaInfo.audioChannels, int)
    assert isinstance(data[0].audioTags.mediaInfo.audioBits, int)
    assert isinstance(data[0].audioTags.mediaInfo.audioSampleRate, int)
    assert isinstance(data[0].audioTags.trackNumbers[0], int)
    assert data[0].additionalFile is False
    assert data[0].replaceExistingFiles is True
    assert data[0].disableReleaseSwitching is False
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_edit_manual_import(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test editing manual import."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/manualimport",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_edit_manual_import(LidarrManualImport("test"))
    assert isinstance(data, LidarrManualImport)


@pytest.mark.asyncio
async def test_async_get_retag(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/retag?artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/retag.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_retag(0, albumid=0)
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert isinstance(data[0].trackNumbers[0], int)
    assert isinstance(data[0].trackFileId, int)
    assert data[0].path == "string"
    assert data[0].changes[0].field == "string"
    assert data[0].changes[0].oldValue == "string"
    assert data[0].changes[0].newValue == "string"


@pytest.mark.asyncio
async def test_async_search(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/search?term=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/search.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_search("test")
    assert data[0].foreignId == "string"
    assert data[0].artist.status == "string"
    assert data[0].artist.ended is True
    assert data[0].artist.artistName == "string"
    assert data[0].artist.foreignArtistId == "string"
    assert isinstance(data[0].artist.tadbId, int)
    assert isinstance(data[0].artist.discogsId, int)
    assert data[0].artist.overview == "string"
    assert data[0].artist.artistType == "string"
    assert data[0].artist.disambiguation == "string"
    assert data[0].artist.links[0].url == "string"
    assert data[0].artist.links[0].name == "string"
    assert data[0].artist.images[0].url == "string"
    assert data[0].artist.images[0].coverType == ImageType.POSTER.value
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.remotePoster == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres == ["string"]
    assert data[0].artist.cleanName == "string"
    assert data[0].artist.sortName == "string"
    assert isinstance(data[0].artist.tags[0], int)
    assert data[0].artist.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data[0].artist.ratings.votes, int)
    assert isinstance(data[0].artist.ratings.value, float)
    assert isinstance(data[0].artist.statistics.albumCount, int)
    assert isinstance(data[0].artist.statistics.trackFileCount, int)
    assert isinstance(data[0].artist.statistics.trackCount, int)
    assert isinstance(data[0].artist.statistics.totalTrackCount, int)
    assert isinstance(data[0].artist.statistics.sizeOnDisk, int)
    assert isinstance(data[0].artist.statistics.percentOfTracks, float)
    assert isinstance(data[0].artist.id, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/tag/detail/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_tags_details(tagid=0)

    assert isinstance(data.id, int)
    assert data.label == "string"
    assert isinstance(data.delayProfileIds[0], int)
    assert isinstance(data.notificationIds[0], int)
    assert isinstance(data.restrictionIds[0], int)
    assert isinstance(data.importListIds[0], int)
    assert isinstance(data.artistIds[0], int)


@pytest.mark.asyncio
async def test_async_get_tracks(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting tracks."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/track?artistId=0&albumId=0&albumReleaseId=0&trackIds=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/track.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_tracks(
        artistid=0, albumid=0, albumreleaseid=0, trackids=[0]
    )
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].trackFileId, int)
    assert isinstance(data[0].albumId, int)
    assert data[0].explicit is False
    assert isinstance(data[0].absoluteTrackNumber, int)
    assert isinstance(data[0].trackNumber, int)
    assert data[0].title == "string"
    assert isinstance(data[0].duration, int)
    assert isinstance(data[0].mediumNumber, int)
    assert data[0].hasFile is False
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert isinstance(data[0].id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/track",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    with pytest.raises(ArrException):
        await lidarr_client.async_get_tracks()

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/track/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/track-details.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_tracks(trackids=0)
    assert isinstance(data.artistId, int)
    assert isinstance(data.trackFileId, int)
    assert isinstance(data.albumId, int)
    assert data.explicit is False
    assert isinstance(data.absoluteTrackNumber, int)
    assert isinstance(data.trackNumber, int)
    assert data.title == "string"
    assert isinstance(data.duration, int)
    assert isinstance(data.mediumNumber, int)
    assert data.hasFile is False
    assert data.artist.status == "string"
    assert data.artist.ended is True
    assert data.artist.artistName == "string"
    assert data.artist.foreignArtistId == "string"
    assert isinstance(data.artist.tadbId, int)
    assert isinstance(data.artist.discogsId, int)
    assert data.artist.overview == "string"
    assert data.artist.artistType == "string"
    assert data.artist.disambiguation == "string"
    assert data.artist.links[0].url == "string"
    assert data.artist.links[0].name == "string"
    assert data.artist.images[0].url == "string"
    assert data.artist.images[0].coverType == ImageType.POSTER.value
    assert data.artist.images[0].extension == "string"
    assert data.artist.path == "string"
    assert isinstance(data.artist.qualityProfileId, int)
    assert isinstance(data.artist.metadataProfileId, int)
    assert data.artist.monitored is True
    assert data.artist.genres == ["string"]
    assert data.artist.cleanName == "string"
    assert data.artist.sortName == "string"
    assert isinstance(data.artist.tags[0], int)
    assert data.artist.added == datetime(2021, 8, 21, 15, 35, 54, 398878)
    assert isinstance(data.artist.ratings.votes, int)
    assert isinstance(data.artist.ratings.value, float)
    assert isinstance(data.artist.statistics.albumCount, int)
    assert isinstance(data.artist.statistics.trackFileCount, int)
    assert isinstance(data.artist.statistics.trackCount, int)
    assert isinstance(data.artist.statistics.totalTrackCount, int)
    assert isinstance(data.artist.statistics.sizeOnDisk, int)
    assert isinstance(data.artist.statistics.percentOfTracks, float)
    assert isinstance(data.artist.id, int)
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_get_track_files(aresponses, lidarr_client: LidarrClient) -> None:
    """Test getting track files."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile?unmapped=False&artistId=0&albumId=0&trackFileIds=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/trackfile.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_track_files(
        artistid=0, albumid=0, trackfileids=[0]
    )
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert data[0].path == "string"
    assert isinstance(data[0].size, int)
    assert data[0].dateAdded == datetime(2021, 8, 21, 16, 0, 22, 10803)
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].qualityWeight, int)
    assert isinstance(data[0].mediaInfo.audioChannels, float)
    assert data[0].mediaInfo.audioBitRate == "string"
    assert data[0].mediaInfo.audioCodec == "string"
    assert data[0].mediaInfo.audioBits == "string"
    assert data[0].mediaInfo.audioSampleRate == "string"
    assert data[0].qualityCutoffNotMet is False
    assert isinstance(data[0].id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile/0?unmapped=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/trackfile-details.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_track_files(trackfileids=0)
    assert isinstance(data.artistId, int)
    assert isinstance(data.albumId, int)
    assert data.path == "string"
    assert isinstance(data.size, int)
    assert data.dateAdded == datetime(2021, 8, 21, 16, 0, 17, 930148)
    assert isinstance(data.quality.quality.id, int)
    assert data.quality.quality.name == "string"
    assert isinstance(data.quality.revision.version, int)
    assert isinstance(data.quality.revision.real, int)
    assert data.quality.revision.isRepack is False
    assert isinstance(data.qualityWeight, int)
    assert isinstance(data.mediaInfo.audioChannels, float)
    assert data.mediaInfo.audioBitRate == "string"
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioBits == "string"
    assert data.mediaInfo.audioSampleRate == "string"
    assert data.qualityCutoffNotMet is False
    assert data.audioTags.title == "string"
    assert data.audioTags.cleanTitle == "string"
    assert data.audioTags.artistTitle == "string"
    assert data.audioTags.albumTitle == "string"
    assert data.audioTags.artistTitleInfo.title == "string"
    assert isinstance(data.audioTags.artistTitleInfo.year, int)
    assert isinstance(data.audioTags.discNumber, int)
    assert isinstance(data.audioTags.discCount, int)
    assert isinstance(data.audioTags.year, int)
    assert data.audioTags.duration == "00:15:08.0093333"
    assert isinstance(data.audioTags.quality.quality.id, int)
    assert data.audioTags.quality.quality.name == "string"
    assert isinstance(data.audioTags.quality.revision.version, int)
    assert isinstance(data.audioTags.quality.revision.real, int)
    assert data.audioTags.quality.revision.isRepack is False
    assert data.audioTags.mediaInfo.audioFormat == "string"
    assert isinstance(data.audioTags.mediaInfo.audioBitrate, int)
    assert isinstance(data.audioTags.mediaInfo.audioChannels, float)
    assert isinstance(data.audioTags.mediaInfo.audioBits, int)
    assert isinstance(data.audioTags.mediaInfo.audioSampleRate, int)
    assert isinstance(data.audioTags.trackNumbers[0], int)
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile?unmapped=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/trackfile-details.json"),
        ),
        match_querystring=True,
    )
    with pytest.raises(ArrException):
        await lidarr_client.async_get_track_files()


@pytest.mark.asyncio
async def test_async_get_metadata_provider(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test getting metadata provider."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/config/metadataprovider",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/config-metadataprovider.json"),
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_get_metadata_provider()
    assert data.metadataSource == ""
    assert data.writeAudioTags == "no"
    assert data.scrubAudioTags is False
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_edit_metadata_provider(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test editing metadata provider."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/config/metadataprovider",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = LidarrMetadataProvider("test")
    data = await lidarr_client.async_edit_metadata_provider(data)
    assert isinstance(data, LidarrMetadataProvider)


@pytest.mark.asyncio
async def test_async_edit_track_files(aresponses, lidarr_client: LidarrClient) -> None:
    """Test editing track files."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await lidarr_client.async_edit_track_files(LidarrTrackFile("test"))
    assert isinstance(data, LidarrTrackFile)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile/editor",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = LidarrTrackFileEditor(
        {"trackFileIds": 0, "quality": {"quality": "test", "revision": "test"}}
    )
    await lidarr_client.async_edit_track_files(data)


@pytest.mark.asyncio
async def test_async_delete_track_files(
    aresponses, lidarr_client: LidarrClient
) -> None:
    """Test deleting track files."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_delete_track_files(0)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/trackfile/bulk",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await lidarr_client.async_delete_track_files([0])


@pytest.mark.asyncio
async def test_not_implemented(lidarr_client: LidarrClient) -> None:
    """Test methods not implemented by the API."""
    with pytest.raises(NotImplementedError):
        await lidarr_client.async_get_languages()
