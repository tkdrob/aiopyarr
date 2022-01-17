"""Tests for Lidarr object models."""
# pylint:disable=line-too-long, too-many-lines, too-many-statements
import json
from datetime import datetime
from re import T
from aiopyarr.models.request import Command
from aiopyarr.exceptions import ArrException

import pytest
from aiohttp.client import ClientSession

from aiopyarr.lidarr_client import LidarrClient
from aiopyarr.models.lidarr import LidarrAlbum, LidarrAlbumEditor, LidarrAlbumHistory, LidarrAlbumStudio, LidarrArtist, LidarrCommands, LidarrEventType, LidarrImportList, LidarrMetadataProfile, LidarrRelease, LidarrWantedCutoff
from tests import LIDARR_API, TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_albums(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_albums(albumids=0)
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
    #assert data.secondaryTypes == ["string"] #TODO
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
    assert data.artist.images[0].coverType == "string"
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
    assert data.images[0].coverType == "string"
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_albums()

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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_albums(albumids=[0, 1], artistid=0, foreignalbumid=0)


@pytest.mark.asyncio
async def test_async_add_album(aresponses):
    """Test adding album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_album(LidarrAlbum("test"))
    assert isinstance(data, LidarrAlbum)


@pytest.mark.asyncio
async def test_async_edit_albums(aresponses):
    """Test editing album info."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_albums(LidarrAlbum("test"))
    assert isinstance(data, LidarrAlbum)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/album/monitor",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    editor = LidarrAlbumEditor({"albumids": [0], "monitored": True})
    # TODO lower case all params if they work and are in models
    assert isinstance(editor.albumids[0], int)
    assert editor.monitored is True
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_edit_albums(editor)


@pytest.mark.asyncio
async def test_async_delete_album(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_album(0)


@pytest.mark.asyncio
async def test_async_album_studio(aresponses):
    """Test album studio."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/albumstudio",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    editor = LidarrAlbumStudio(json.loads(load_fixture("lidarr/albumstudio.json")))
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_album_studio(editor)
    assert isinstance(editor.artist[0].id, int)
    assert editor.artist[0].monitored is True
    assert isinstance(editor.artist[0].albums[0].id, int)
    assert editor.artist[0].albums[0].title == "string"
    assert editor.artist[0].albums[0].disambiguation == "string"
    assert editor.artist[0].albums[0].overview == "string"
    assert isinstance(editor.artist[0].albums[0].artistId, int)
    assert editor.artist[0].albums[0].foreignAlbumId == "string"
    assert editor.artist[0].albums[0].monitored is True
    assert editor.artist[0].albums[0].anyReleaseOk is True
    assert isinstance(editor.artist[0].albums[0].profileId, int)
    assert isinstance(editor.artist[0].albums[0].duration, int)
    assert editor.artist[0].albums[0].albumType == "string"
    #assert editor.artist[0].albums[0].secondaryTypes == ["string"] #TODO
    assert isinstance(editor.artist[0].albums[0].ratings.votes, int)
    assert isinstance(editor.artist[0].albums[0].ratings.value, float)
    assert editor.artist[0].albums[0].releaseDate == datetime(2020, 2, 15, 14, 59, 24, 750000)
    assert isinstance(editor.artist[0].albums[0].releases[0].id, int)
    assert isinstance(editor.artist[0].albums[0].releases[0].albumId, int)
    assert editor.artist[0].albums[0].releases[0].foreignReleaseId == "string"
    assert editor.artist[0].albums[0].releases[0].title == "string"
    assert editor.artist[0].albums[0].releases[0].status == "string"
    assert isinstance(editor.artist[0].albums[0].releases[0].duration, int)
    assert isinstance(editor.artist[0].albums[0].releases[0].trackCount, int)
    assert isinstance(editor.artist[0].albums[0].releases[0].media[0].mediumNumber, int)
    assert editor.artist[0].albums[0].releases[0].media[0].mediumName == "string"
    assert editor.artist[0].albums[0].releases[0].media[0].mediumFormat == "string"
    assert editor.artist[0].albums[0].releases[0].disambiguation == "string"
    assert editor.artist[0].albums[0].releases[0].country == ["string"]
    assert editor.artist[0].albums[0].releases[0].label == ["string"]
    assert editor.artist[0].albums[0].releases[0].format == "string"
    assert editor.artist[0].albums[0].releases[0].monitored is True
    assert isinstance(editor.artist[0].albums[0].artist.id, int)
    assert isinstance(editor.artist[0].albums[0].artist.artistMetadataId, int)
    assert editor.artist[0].albums[0].artist.status == "string"
    assert editor.artist[0].albums[0].artist.artistName == "string"
    assert editor.artist[0].albums[0].artist.foreignArtistId == "string"
    assert editor.artist[0].albums[0].artist.mbId == "string"
    assert isinstance(editor.artist[0].albums[0].artist.tadbId, int)
    assert isinstance(editor.artist[0].albums[0].artist.discogsId, int)
    assert editor.artist[0].albums[0].artist.allMusicId == "string"
    assert editor.artist[0].albums[0].artist.overview == "string"
    assert editor.artist[0].albums[0].artist.artistType == "string"
    assert editor.artist[0].albums[0].artist.disambiguation == "string"
    assert editor.artist[0].albums[0].artist.links[0].url == "string"
    assert editor.artist[0].albums[0].artist.links[0].name == "string"
    #assert editor.artist[0].albums[0].artist.nextAlbum == "string" #TODO
    #assert editor.artist[0].albums[0].artist.lastAlbum == "string" #TODO
    assert editor.artist[0].albums[0].artist.images[0].url == "string"
    assert editor.artist[0].albums[0].artist.images[0].coverType == "string"
    #assert editor.artist[0].albums[0].artist.members == "string"
    #assert editor.artist[0].albums[0].artist.remotePoster == "string"
    assert editor.artist[0].albums[0].artist.path == "string"
    assert isinstance(editor.artist[0].albums[0].artist.qualityProfileId, int)
    assert isinstance(editor.artist[0].albums[0].artist.metadataProfileId, int)
    assert editor.artist[0].albums[0].artist.monitored is True
    #assert editor.artist[0].albums[0].artist.rootFolderPath == "string"
    assert editor.artist[0].albums[0].artist.genres == ["string"]
    assert editor.artist[0].albums[0].artist.cleanName == "string"
    assert editor.artist[0].albums[0].artist.sortName == "string"
    assert isinstance(editor.artist[0].albums[0].artist.tags[0], int)
    assert editor.artist[0].albums[0].artist.added == datetime(2020, 2, 15, 14, 59, 24, 751000)
    #assert editor.artist[0].albums[0].artist.addOptions
    assert isinstance(editor.artist[0].albums[0].artist.ratings.votes, int)
    assert isinstance(editor.artist[0].albums[0].artist.ratings.value, float)
    assert isinstance(editor.artist[0].albums[0].artist.statistics.albumCount, int)
    assert isinstance(editor.artist[0].albums[0].artist.statistics.trackFileCount, int)
    assert isinstance(editor.artist[0].albums[0].artist.statistics.trackCount, int)
    assert isinstance(editor.artist[0].albums[0].artist.statistics.totalTrackCount, int)
    assert isinstance(editor.artist[0].albums[0].artist.statistics.sizeOnDisk, int)
    assert editor.artist[0].albums[0].images[0].url == "string"
    assert editor.artist[0].albums[0].images[0].coverType == "string"
    assert editor.artist[0].albums[0].links[0].url == "string"
    assert editor.artist[0].albums[0].links[0].name == "string"
    assert isinstance(editor.artist[0].albums[0].statistics.trackFileCount, int)
    assert isinstance(editor.artist[0].albums[0].statistics.trackCount, int)
    assert isinstance(editor.artist[0].albums[0].statistics.totalTrackCount, int)
    assert isinstance(editor.artist[0].albums[0].statistics.sizeOnDisk, int)
    #assert editor.artist[0].albums[0].addOptions
    #assert editor.artist[0].albums[0].remoteCover
    #assert editor.artist[0].albums[0].grabbed is True
    assert editor.monitoringOptions.monitor == "string"
    assert editor.monitoringOptions.albumsToMonitor == ["string"]
    assert editor.monitoringOptions.monitored is True


@pytest.mark.asyncio
async def test_async_get_artists(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_artists(0)
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
    #assert data.lasrAlbum #TODO
    assert data.images[0].url == "string"
    assert data.images[0].coverType == "string"
    assert data.images[0].extension == "string"
    assert data.path == "string"
    assert isinstance(data.qualityProfileId, int)
    assert isinstance(data.metadataProfileId, int)
    assert data.monitored is True
    #assert data.rootFolderPath == "string"
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_artists()

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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_artists("test")


@pytest.mark.asyncio
async def test_async_add_artist(aresponses):
    """Test adding artist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_artist(LidarrArtist("test"))
    assert isinstance(data, LidarrArtist)


@pytest.mark.asyncio
async def test_async_edit_artists(aresponses):
    """Test editing artist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_artists(LidarrArtist("test"))
    assert isinstance(data, LidarrArtist)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/artist/editor",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_edit_artists("test") #TODO test for ArtistEditor instance


@pytest.mark.asyncio
async def test_async_delete_artists(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_artists(0)

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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_artists([0])


@pytest.mark.asyncio
async def test_async_album_lookup(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_album_lookup("test")
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
    #assert data[0].secondaryTypes == ["string"] #TODO
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
    assert data[0].artist.images[0].coverType == "string"
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
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].remoteCover == "string"


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklist."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/blacklist?page=1&pageSize=10&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_blocklist()
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == "date"
    assert data.sortDirection == "descending"
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
    assert data.records[0].protocol == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert data.records[0].artist.status == "string"
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
    assert data.records[0].artist.images[0].coverType == "string"
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
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/calendar?start=2020-11-30&end=2020-12-01&unmonitored=False",
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_calendar(start, end)
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
    #assert data[0].secondaryTypes[0] == "string" #TODO
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
    assert data[0].artist.images[0].coverType == "string"
    assert data[0].artist.images[0].extension == "string"
    assert data[0].artist.path == "string"
    assert isinstance(data[0].artist.qualityProfileId, int)
    assert isinstance(data[0].artist.metadataProfileId, int)
    assert data[0].artist.monitored is True
    assert data[0].artist.genres== ["string"]
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
    assert data[0].images[0].coverType == "string"
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
async def test_async_lidarr_commands(aresponses):
    """Test sending lidarr commands."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_lidarr_command(LidarrCommands.ALBUM_SEARCH)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.APP_UPDATE_CHECK)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.ARTIST_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.ALBUM_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.MISSING_ALBUM_SEARCH)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.REFRESH_ALBUM)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_lidarr_command(LidarrCommands.REFRESH_ARTIST)


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_wanted(recordid=0, missing=False)
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
    #assert data.secondaryTypes == ["string"] #TODO
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
    assert data.artist.images[0].coverType == "string"
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
    assert data.images[0].coverType == "string"
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
        f"/api/{LIDARR_API}/wanted/missing?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_wanted()
    assert isinstance(data, LidarrWantedCutoff)


@pytest.mark.asyncio
async def test_async_get_importlist(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_import_lists()
    assert data[0].enableAutomaticAdd is False
    assert data[0].shouldMonitor == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert isinstance(data[0].metadataProfileId, int)
    assert data[0].listType == "string"
    assert isinstance(data[0].listOrder, int)
    assert data[0].name == "string"
    assert isinstance(data[0].fields[0].order, int)
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == []
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].selectOptionsProviderAction =="string"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert isinstance(data[0].tags[0], int)
    assert data[0].presets[0].enableAutomaticAdd is False
    assert data[0].presets[0].shouldMonitor == "string"
    assert isinstance(data[0].presets[0].qualityProfileId, int)
    assert isinstance(data[0].presets[0].metadataProfileId, int)
    assert data[0].presets[0].listType == "string"
    assert isinstance(data[0].presets[0].listOrder, int)
    assert data[0].presets[0].name == "string"
    assert isinstance(data[0].presets[0].fields[0].order, int)
    assert data[0].presets[0].fields[0].name == "string"
    assert data[0].presets[0].fields[0].label == "string"
    assert data[0].presets[0].fields[0].value == "string"
    assert data[0].presets[0].fields[0].type == "string"
    assert data[0].presets[0].fields[0].advanced is True
    assert data[0].presets[0].implementation == "string"
    assert data[0].presets[0].configContract == "string"
    assert data[0].presets[0].infoLink == "string"
    assert isinstance(data[0].presets[0].tags[0], int)
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_import_lists(0)


@pytest.mark.asyncio
async def test_async_edit_importlist(aresponses):
    """Test editing import list."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_import_list(LidarrImportList("test"))
    assert isinstance(data, LidarrImportList)


@pytest.mark.asyncio
async def test_async_add_importlist(aresponses):
    """Test adding import list."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_import_list(LidarrImportList("test"))
    assert isinstance(data, LidarrImportList)


@pytest.mark.asyncio
async def test_async_test_import_lists(aresponses):
    """Test import list testing."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists(LidarrImportList("test")) is True

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists() is True

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists() is False


@pytest.mark.asyncio
async def test_async_importlist_action(aresponses):
    """Test performing import list action."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/importlist/action/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    data = await client.async_importlist_action(LidarrImportList({"name": "test"}))
    assert isinstance(data, LidarrImportList)


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting_history."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history?page=1&pageSize=10&sortKey=date&sortDirection=ascending&includeArtist=True&includeAlbum=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/history.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_history(artist=True, album=True)
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == "date"
    assert data.sortDirection == "descending"
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
    assert data.records[0].eventType == "string"
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
    assert isinstance(data.records[0].data.protocol, int)
    assert data.records[0].data.downloadForced is False #TODO check type hints
    assert data.records[0].data.torrentInfoHash == "string"
    assert data.records[0].album.title == "string"
    assert data.records[0].album.disambiguation == "string"
    assert data.records[0].album.overview == "string"
    assert isinstance(data.records[0].album.artistId, int)
    assert data.records[0].album.foreignAlbumId == "string"
    assert data.records[0].album.monitored is True
    assert data.records[0].album.anyReleaseOk is True
    assert isinstance(data.records[0].album.profileId, int)
    assert isinstance(data.records[0].album.duration, int)
    assert data.records[0].album.albumType == "string"
    #assert isinstance(data.records[0].album.secondaryTypes[0].id, int) #TODO
    #assert data.records[0].album.secondaryTypes[0].name == "string"
    assert isinstance(data.records[0].album.mediumCount, int)
    assert isinstance(data.records[0].album.ratings.votes, int)
    assert isinstance(data.records[0].album.ratings.value, float)
    assert data.records[0].album.releaseDate == datetime(2015, 11, 13, 0, 0)
    assert isinstance(data.records[0].album.releases[0].id, int)
    assert isinstance(data.records[0].album.releases[0].albumId, int)
    assert data.records[0].album.releases[0].foreignReleaseId == "string"
    assert data.records[0].album.releases[0].title == "string"
    assert data.records[0].album.releases[0].status == "string"
    assert isinstance(data.records[0].album.releases[0].duration, int)
    assert isinstance(data.records[0].album.releases[0].trackCount, int)
    assert isinstance(data.records[0].album.releases[0].media[0].mediumNumber, int)
    assert data.records[0].album.releases[0].media[0].mediumName == "string"
    assert data.records[0].album.releases[0].media[0].mediumFormat == "string"
    assert isinstance(data.records[0].album.releases[0].mediumCount, int)
    assert data.records[0].album.releases[0].disambiguation == "string"
    assert data.records[0].album.releases[0].country == ["string"]
    assert data.records[0].album.releases[0].label == ["string"]
    assert data.records[0].album.releases[0].format == "string"
    assert data.records[0].album.releases[0].monitored is False
    assert data.records[0].album.genres == ["string"]
    assert isinstance(data.records[0].album.media[0].mediumNumber, int)
    assert data.records[0].album.media[0].mediumName == "string"
    assert data.records[0].album.media[0].mediumFormat == "string"
    assert data.records[0].album.artist.status == "string"
    assert data.records[0].album.artist.ended is False
    assert data.records[0].album.artist.artistName == "string"
    assert data.records[0].album.artist.foreignArtistId == "string"
    assert isinstance(data.records[0].album.artist.tadbId, int)
    assert isinstance(data.records[0].album.artist.discogsId, int)
    assert data.records[0].album.artist.overview == "string"
    assert data.records[0].album.artist.artistType == "string"
    assert data.records[0].album.artist.disambiguation == "string"
    assert data.records[0].album.artist.links[0].url == "string"
    assert data.records[0].album.artist.links[0].name == "string"
    assert data.records[0].album.artist.images[0].url == "string"
    assert data.records[0].album.artist.images[0].coverType == "string"
    assert data.records[0].album.artist.images[0].extension == "string"
    assert data.records[0].album.artist.path == "string"
    assert isinstance(data.records[0].album.artist.qualityProfileId, int)
    assert isinstance(data.records[0].album.artist.metadataProfileId, int)
    assert data.records[0].album.artist.monitored is True
    assert data.records[0].album.artist.genres == ["string"]
    assert data.records[0].album.artist.cleanName == "string"
    assert data.records[0].album.artist.sortName == "string"
    assert isinstance(data.records[0].album.artist.tags[0], int)
    assert data.records[0].album.artist.added == datetime(2021, 8, 21, 15, 56, 31, 922597)
    assert isinstance(data.records[0].album.artist.ratings.votes, int)
    assert isinstance(data.records[0].album.artist.ratings.value, float)
    assert isinstance(data.records[0].album.artist.statistics.albumCount, int)
    assert isinstance(data.records[0].album.artist.statistics.trackFileCount, int)
    assert isinstance(data.records[0].album.artist.statistics.trackCount, int)
    assert isinstance(data.records[0].album.artist.statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].album.artist.statistics.percentOfTracks, float)
    assert isinstance(data.records[0].album.artist.id, int)
    assert data.records[0].album.images[0].url == "string"
    assert data.records[0].album.images[0].coverType == "string"
    assert data.records[0].album.images[0].extension == "string"
    assert data.records[0].album.links[0].url == "string"
    assert data.records[0].album.links[0].name == "string"
    assert isinstance(data.records[0].album.id, int)
    assert data.records[0].artist.status =="string"
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
    assert data.records[0].artist.images[0].coverType == "string"
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

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/since?page=1&pageSize=10&sortKey=date&sortDirection=ascending&includeArtist=False&includeAlbum=False&date=2020-11-30",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    date = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_history(date=date)
    assert isinstance(data, LidarrAlbumHistory)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/artist?page=1&pageSize=10&sortKey=date&sortDirection=ascending&artistId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_history(artist=0)
    assert isinstance(data, LidarrAlbumHistory)

    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/history/artist?page=1&pageSize=10&sortKey=date&sortDirection=ascending&eventType=downloadFailed&artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_history(artist=0, album=0, event_type=LidarrEventType.DOWNLOAD_FAILED)
    assert isinstance(data, LidarrAlbumHistory)


@pytest.mark.asyncio
async def test_async_get_metadata_profiles(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_metadata_profiles()
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
async def test_async_edit_metadata_profile(aresponses):
    """Test editing metadata profile."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/metadataprofile",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_metadata_profile(LidarrMetadataProfile("test"))
    assert isinstance(data, LidarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_add_metadata_profile(aresponses):
    """Test adding metadata profile."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/metadataprofile",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_metadata_profile(LidarrMetadataProfile("test"))
    assert isinstance(data, LidarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_queue()
    assert isinstance(data.page, int)
    assert isinstance(data.page, int)
    assert data.sortKey == "timeleft"
    assert data.sortDirection == "ascending"
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].artistId, int)
    assert isinstance(data.records[0].albumId, int)
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert isinstance(data.records[0].size, float)
    assert data.records[0].title == "string"
    assert isinstance(data.records[0].sizeleft, float)
    assert data.records[0].timeleft == "00:00:00"
    assert data.records[0].estimatedCompletionTime == datetime(2020, 2, 16, 23, 34, 44, 885649)
    assert data.records[0].status == "string"
    assert data.records[0].trackedDownloadStatus == "string"
    assert data.records[0].trackedDownloadState == "string"
    assert data.records[0].statusMessages[0].title == "string"
    assert data.records[0].statusMessages[0].messages == ["string"]
    assert data.records[0].downloadId == "string"
    assert data.records[0].protocol == "string"
    assert data.records[0].downloadClient == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].outputPath == "string"
    assert data.records[0].downloadForced is False
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_queue_details(artistid=0, albumids=[0])
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
    assert data[0].artist.images[0].coverType == "string"
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
    assert isinstance(data[0].album.secondaryTypes[0], int) 
    assert isinstance(data[0].album.mediumCount, int)
    #assert isinstance(data[0].album.ratings.votes, int) #TODO
    #assert isinstance(data[0].album.ratings.value, float)
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
    assert data[0].album.artist.images[0].coverType == "string"
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
    assert data[0].album.images[0].coverType == "string"
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
    assert isinstance(data[0].sizeleft, float)
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2020, 2, 16, 23, 49, 45, 143727)
    assert data[0].status == "string"
    assert data[0].trackedDownloadStatus == "string"
    assert data[0].trackedDownloadState == "string"
    assert data[0].statusMessages[0].title == "string"
    assert data[0].statusMessages[0].messages == ["string"]
    assert data[0].downloadId == "string"
    assert data[0].protocol == "string"
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_queue_details()


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_release(artistid=0, albumid=0)
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
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2020, 2, 16, 20, 8, 16)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoHash == "string"
    assert data[0].downloadAllowed is True
    assert isinstance(data[0].releaseWeight, int)
    assert isinstance(data[0].preferredWordScore, float)
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert isinstance(data[0].seeders, int)
    assert isinstance(data[0].leechers, int)
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_downlaod_release(aresponses):
    """Test downloading release."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/release",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_download_release("test", 0)
    assert isinstance(data, LidarrRelease)


@pytest.mark.asyncio
async def test_async_get_pushed_release(aresponses):
    """Test getting pushed release."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/release/push?id=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_pushed_release("test")
    assert isinstance(data, LidarrRelease)


@pytest.mark.asyncio
async def test_async_get_rename(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/rename?artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/rename.json")
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_rename(0, albumid=0)
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert isinstance(data[0].trackNumbers[0], int)
    assert isinstance(data[0].trackFileId, int)
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_retag(aresponses):
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/retag?artistId=0&albumId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/retag.json")
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_retag(0, albumid=0)
    assert isinstance(data[0].artistId, int)
    assert isinstance(data[0].albumId, int)
    assert isinstance(data[0].trackNumbers[0], int)
    assert isinstance(data[0].trackFileId, int)
    assert data[0].path == "string"
    assert data[0].changes[0].field == "string"
    assert data[0].changes[0].oldValue == "string"
    assert data[0].changes[0].newValue == "string"


@pytest.mark.asyncio
async def test_async_search(aresponses):
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8686",
        f"/api/{LIDARR_API}/search?term=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("lidarr/search.json")
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_search("test")
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
    assert data[0].artist.images[0].coverType == "string"
    assert data[0].artist.images[0].extension == "string"
    #assert data[0].artist.remotePoster == "string" TODO
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
async def test_async_get_tag_details(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_tags_details(tagid=0)

    assert isinstance(data.id, int)
    assert data.label == "string"
    assert isinstance(data.delayProfileIds[0], int)
    assert isinstance(data.notificationIds[0], int)
    assert isinstance(data.restrictionIds[0], int)
    assert isinstance(data.importListIds[0], int)
    assert isinstance(data.artistIds[0], int)


@pytest.mark.asyncio
async def test_async_get_tracks(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_tracks(artistid=0, albumid=0, albumreleaseid=0, trackids=[0])
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    with pytest.raises(ArrException):
        await client.async_get_tracks()

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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_tracks(trackids=0)
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
    assert data.artist.images[0].coverType == "string"
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
async def test_async_get_track_files(aresponses):
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_track_files(artistid=0, albumid=0, trackfileids=[0])
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
    async with ClientSession():
        client = LidarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_track_files(trackfileids=0)
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
