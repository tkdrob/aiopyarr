"""Tests for Radarr object models."""
# pylint:disable=line-too-long, too-many-lines, too-many-statements
from datetime import datetime

from aiohttp.client import ClientSession
import pytest

from aiopyarr.models.radarr import (
    RadarrCommands,
    RadarrEventType,
    RadarrImportList,
    RadarrMovie,
    RadarrMovieEditor,
    RadarrMovieFile,
    RadarrNamingConfig,
    RadarrNotification,
    RadarrRelease,
)
from aiopyarr.models.request import Command
from aiopyarr.radarr_client import RadarrClient

from . import RADARR_API, TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklisted movies."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/blocklist?page=1&pageSize=20&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_blocklist()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert isinstance(data.records[0].movieId, int)
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].date == "string"
    assert isinstance(data.records[0].id, int)
    assert data.records[0].indexer == "string"
    assert data.records[0].protocol == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert isinstance(data.records[0].quality.quality.resolution, int)
    assert data.records[0].quality.quality.modifier == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is True
    assert isinstance(data.records[0].languages[0].id, int)
    assert data.records[0].languages[0].name == "string"
    assert isinstance(data.records[0].customFormats[0].id, int)
    assert data.records[0].customFormats[0].name == "string"
    assert data.records[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data.records[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert isinstance(spec.fields[0].order, int)
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data.sortDirection == "string"
    assert data.sortKey == "string"
    assert isinstance(data.totalRecords, int)


@pytest.mark.asyncio
async def test_async_get_blocklist_movie(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/blocklist/movie?movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist-movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_blocklist_movie(bocklistid=0)

    assert isinstance(data[0].movieId, int)
    assert data[0].sourceTitle == "string"
    assert isinstance(data[0].languages[0].id, int)
    assert data[0].languages[0].name == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
    assert data[0].quality.quality.modifier == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is True
    assert isinstance(data[0].customFormats[0].id, int)
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert isinstance(spec.fields[0].order, int)
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data[0].date == "string"
    assert isinstance(data[0].id, int)
    assert data[0].indexer == "string"
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/calendar?start=2020-11-30&end=2020-12-01&unmonitored=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/calendar.json"),
        ),
        match_querystring=True,
    )
    start = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    end = datetime.strptime("Dec 1 2020  1:33PM", "%b %d %Y %I:%M%p")
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_calendar(start, end)

    assert data[0].title == "string"
    assert data[0].originalTitle == "string"
    assert data[0].alternateTitles == []
    assert isinstance(data[0].secondaryYearSourceId, int)
    assert data[0].sortTitle == "string"
    assert isinstance(data[0].sizeOnDisk, int)
    assert data[0].status == "string"
    assert data[0].overview == "string"
    assert data[0].physicalRelease == datetime(2021, 12, 3, 0, 0)
    assert data[0].digitalRelease == datetime(2020, 8, 11, 0, 0)
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].url == "string"
    assert data[0].website == "string"
    assert isinstance(data[0].year, int)
    assert data[0].hasFile is True
    assert data[0].youTubeTrailerId == "string"
    assert data[0].studio == "string"
    assert data[0].path == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert data[0].monitored is True
    assert data[0].minimumAvailability == "string"
    assert data[0].isAvailable is True
    assert data[0].folderName == "string"
    assert isinstance(data[0].runtime, int)
    assert data[0].cleanTitle == "string"
    assert data[0].imdbId == "string"
    assert isinstance(data[0].tmdbId, int)
    assert data[0].titleSlug == "string"
    assert data[0].genres == ["string"]
    assert data[0].tags == []
    assert data[0].added == datetime(2020, 7, 16, 13, 25, 37)
    assert isinstance(data[0].ratings.imdb.votes, int)
    assert isinstance(data[0].ratings.imdb.value, float)
    assert data[0].ratings.imdb.type == "string"
    assert isinstance(data[0].ratings.tmdb.votes, int)
    assert isinstance(data[0].ratings.tmdb.value, float)
    assert data[0].ratings.tmdb.type == "string"
    assert isinstance(data[0].ratings.metacritic.votes, int)
    assert isinstance(data[0].ratings.metacritic.value, int)
    assert data[0].ratings.metacritic.type == "string"
    assert isinstance(data[0].ratings.rottenTomatoes.votes, int)
    assert isinstance(data[0].ratings.rottenTomatoes.value, int)
    assert data[0].ratings.rottenTomatoes.type == "string"
    assert isinstance(data[0].movieFile.movieId, int)
    assert data[0].movieFile.relativePath == "string"
    assert data[0].movieFile.path == "string"
    assert isinstance(data[0].movieFile.size, int)
    assert data[0].movieFile.dateAdded == datetime(2021, 6, 1, 4, 8, 20)
    assert data[0].movieFile.sceneName == "string"
    assert isinstance(data[0].movieFile.indexerFlags, int)
    assert isinstance(data[0].movieFile.quality.quality.id, int)
    assert data[0].movieFile.quality.quality.name == "string"
    assert data[0].movieFile.quality.quality.source == "string"
    assert isinstance(data[0].movieFile.quality.quality.resolution, int)
    assert data[0].movieFile.quality.quality.modifier == "string"
    assert isinstance(data[0].movieFile.quality.revision.version, int)
    assert isinstance(data[0].movieFile.quality.revision.real, int)
    assert data[0].movieFile.quality.revision.isRepack is False
    assert isinstance(data[0].movieFile.mediaInfo.audioBitrate, int)
    assert isinstance(data[0].movieFile.mediaInfo.audioChannels, float)
    assert data[0].movieFile.mediaInfo.audioCodec == "string"
    assert data[0].movieFile.mediaInfo.audioLanguages == "string"
    assert isinstance(data[0].movieFile.mediaInfo.audioStreamCount, int)
    assert isinstance(data[0].movieFile.mediaInfo.videoBitDepth, int)
    assert isinstance(data[0].movieFile.mediaInfo.videoBitrate, int)
    assert data[0].movieFile.mediaInfo.videoCodec == "string"
    assert isinstance(data[0].movieFile.mediaInfo.videoFps, float)
    assert data[0].movieFile.mediaInfo.resolution == "string"
    assert data[0].movieFile.mediaInfo.runTime == "00:00:00"
    assert data[0].movieFile.mediaInfo.scanType == "string"
    assert data[0].movieFile.mediaInfo.subtitles == "string"
    assert data[0].movieFile.originalFilePath == "string"
    assert data[0].movieFile.qualityCutoffNotMet is False
    assert isinstance(data[0].movieFile.languages[0].id, int)
    assert data[0].movieFile.languages[0].name == "string"
    assert data[0].movieFile.sceneName == "string"
    assert data[0].movieFile.edition == "string"
    assert isinstance(data[0].movieFile.id, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/naming",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data: RadarrNamingConfig = await client.async_get_naming_config()

    assert data.colonReplacementFormat == "string"
    assert isinstance(data.id, int)
    assert data.includeQuality is True
    assert data.movieFolderFormat == "string"
    assert data.renameMovies is True
    assert data.replaceIllegalCharacters is True
    assert data.replaceSpaces is True
    assert data.standardMovieFormat == "string"


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/history?page=1&pageSize=20&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/history.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_history()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == "date"
    assert data.sortDirection == "descending"
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].movieId, int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].languages[0].id, int)
    assert data.records[0].languages[0].name == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert isinstance(data.records[0].quality.quality.resolution, int)
    assert data.records[0].quality.quality.modifier == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is True
    assert isinstance(data.records[0].customFormats[0].id, int)
    assert data.records[0].customFormats[0].name == "string"
    assert data.records[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data.records[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert isinstance(spec.fields[0].order, int)
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data.records[0].qualityCutoffNotMet is True
    assert data.records[0].date == "string"
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == "string"
    assert data.records[0].data.reason == "Upgrade"
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_movie_history(aresponses):
    """Test getting movie history."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/history/movie?movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/history-movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_movie_history(recordid=0)

    assert isinstance(data[0].movieId, int)
    assert data[0].sourceTitle == "string"
    assert isinstance(data[0].languages[0].id, int)
    assert data[0].languages[0].name == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
    assert data[0].quality.quality.modifier == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is True
    assert isinstance(data[0].customFormats[0].id, int)
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert isinstance(spec.fields[0].order, int)
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data[0].qualityCutoffNotMet is True
    assert data[0].date == "string"
    assert data[0].downloadId == "string"
    assert data[0].eventType == "string"
    assert data[0].data.reason == "Upgrade"
    assert isinstance(data[0].id, int)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/history/movie?movieId=0&eventType=grabbed",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_get_movie_history(
            recordid=0, event_type=RadarrEventType.GRABBED
        )


@pytest.mark.asyncio
async def test_async_get_import_list(aresponses):
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/importlist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_import_lists(listid=0)

    assert data.enabled is True
    assert data.enableAuto is True
    assert data.shouldMonitor is True
    assert data.rootFolderPath == "string"
    assert isinstance(data.qualityProfileId, int)
    assert data.searchOnAdd is True
    assert data.minimumAvailability == "string"
    assert data.listType == "string"
    assert isinstance(data.listOrder, int)
    assert data.name == "string"
    assert isinstance(data.fields[0].order, int)
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert data.fields[0].hidden
    assert isinstance(data.fields[0].selectOptions[0].value, int)
    assert data.fields[0].selectOptions[0].name == "string"
    assert isinstance(data.fields[0].selectOptions[0].order, int)
    assert data.fields[0].selectOptions[0].dividerAfter is False
    assert data.implementationName == "string"
    assert data.implementation == "string"
    assert data.configContract == "string"
    assert data.infoLink == "string"
    assert isinstance(data.tags[0], int)
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_get_movie(aresponses):
    """Test getting movie attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/0?tmdbid=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_movies(movieid=0)

    assert isinstance(data.id, int)
    assert data.title == "string"
    assert data.originalTitle == "string"
    assert data.alternateTitles[0].sourceType == "tmdb"
    assert data.alternateTitles[0].movieId == 1
    assert data.alternateTitles[0].title == "string"
    assert isinstance(data.alternateTitles[0].sourceId, int)
    assert isinstance(data.alternateTitles[0].votes, int)
    assert isinstance(data.alternateTitles[0].voteCount, int)
    assert data.alternateTitles[0].language.id == 1
    assert data.alternateTitles[0].language.name == "string"
    assert data.alternateTitles[0].id == 1
    assert data.sortTitle == "string"
    assert isinstance(data.sizeOnDisk, int)
    assert data.overview == "string"
    assert data.inCinemas == datetime(2020, 11, 6, 0, 0)
    assert data.physicalRelease == datetime(2019, 3, 19, 0, 0)
    assert data.images[0].coverType == "string"
    assert data.images[0].url == "string"
    assert data.images[0].remoteUrl == "string"
    assert data.website == "string"
    assert isinstance(data.year, int)
    assert data.hasFile is True
    assert data.youTubeTrailerId == "string"
    assert data.studio == "string"
    assert data.path == "string"
    assert data.rootFolderPath == "string"
    assert isinstance(data.qualityProfileId, int)
    assert data.monitored is True
    assert data.minimumAvailability == "string"
    assert data.isAvailable is True
    assert data.folderName == "string"
    assert isinstance(data.runtime, int)
    assert data.cleanTitle == "string"
    assert data.imdbId == "string"
    assert isinstance(data.tmdbId, int)
    assert data.titleSlug == "string"
    assert data.certification == "string"
    assert data.genres == ["string"]
    assert isinstance(data.tags[0], int)
    assert data.added == datetime(2018, 12, 28, 5, 56, 49)
    assert isinstance(data.ratings.imdb.votes, int)
    assert isinstance(data.ratings.imdb.value, float)
    assert data.ratings.imdb.type == "string"
    assert isinstance(data.ratings.tmdb.votes, int)
    assert isinstance(data.ratings.tmdb.value, float)
    assert data.ratings.tmdb.type == "string"
    assert isinstance(data.ratings.metacritic.votes, int)
    assert isinstance(data.ratings.metacritic.value, int)
    assert data.ratings.metacritic.type == "string"
    assert isinstance(data.ratings.rottenTomatoes.votes, int)
    assert isinstance(data.ratings.rottenTomatoes.value, int)
    assert data.ratings.rottenTomatoes.type == "string"
    assert isinstance(data.movieFile.movieId, int)
    assert data.movieFile.relativePath == "string"
    assert data.movieFile.path == "string"
    assert isinstance(data.movieFile.size, int)
    assert data.movieFile.dateAdded == datetime(2020, 11, 26, 2, 0, 35)
    assert data.movieFile.indexerFlags == 1
    assert isinstance(data.movieFile.quality.quality.id, int)
    assert data.movieFile.quality.quality.name == "string"
    assert data.movieFile.quality.quality.source == "string"
    assert isinstance(data.movieFile.quality.quality.resolution, int)
    assert data.movieFile.quality.quality.modifier == "string"
    assert isinstance(data.movieFile.quality.revision.version, int)
    assert isinstance(data.movieFile.quality.revision.real, int)
    assert data.movieFile.quality.revision.isRepack is False
    assert isinstance(data.movieFile.mediaInfo.audioBitrate, int)
    assert isinstance(data.movieFile.mediaInfo.audioChannels, float)
    assert data.movieFile.mediaInfo.audioCodec == "string"
    assert data.movieFile.mediaInfo.audioLanguages == "string"
    assert isinstance(data.movieFile.mediaInfo.audioStreamCount, int)
    assert isinstance(data.movieFile.mediaInfo.videoBitDepth, int)
    assert isinstance(data.movieFile.mediaInfo.videoBitrate, int)
    assert data.movieFile.mediaInfo.videoCodec == "string"
    assert isinstance(data.movieFile.mediaInfo.videoFps, float)
    assert data.movieFile.mediaInfo.resolution == "string"
    assert data.movieFile.mediaInfo.runTime == "00:00:00"
    assert data.movieFile.mediaInfo.scanType == "string"
    assert data.movieFile.originalFilePath == "string"
    assert data.movieFile.qualityCutoffNotMet is True
    assert isinstance(data.movieFile.languages[0].id, int)
    assert data.movieFile.languages[0].name == "string"
    assert data.movieFile.edition == "string"
    assert isinstance(data.movieFile.id, int)
    assert data.collection.name == "string"
    assert isinstance(data.collection.tmdbId, int)
    assert data.collection.images[0].coverType == "string"
    assert data.collection.images[0].url == "string"
    assert data.collection.images[0].remoteUrl == "string"
    assert data.status == "string"

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie?tmdbid=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_movies(movieid=0, tmdb=True)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_movies()


@pytest.mark.asyncio
async def test_async_lookup_movie(aresponses):
    """Test movie lookup."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/lookup?term=tmdb:test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/movie-import.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_lookup_movie("test")
    assert isinstance(data[0], RadarrMovie)


@pytest.mark.asyncio
async def test_async_lookup_movie_files(aresponses):
    """Test movie files lookup."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/moviefile/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/moviefile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_lookup_movie_files(0)

    assert isinstance(data.movieId, int)
    assert data.relativePath == "string"
    assert data.path == "string"
    assert isinstance(data.size, int)
    assert data.dateAdded == datetime(2018, 12, 28, 6, 35, 27)
    assert isinstance(data.indexerFlags, int)
    assert isinstance(data.quality.quality.id, int)
    assert data.quality.quality.name == "string"
    assert data.quality.quality.source == "string"
    assert isinstance(data.quality.quality.resolution, int)
    assert data.quality.quality.modifier == "string"
    assert isinstance(data.quality.revision.version, int)
    assert isinstance(data.quality.revision.real, int)
    assert data.quality.revision.isRepack is True
    assert data.mediaInfo.audioAdditionalFeatures == "string"
    assert isinstance(data.mediaInfo.audioBitrate, int)
    assert isinstance(data.mediaInfo.audioChannels, float)
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioLanguages == "string"
    assert isinstance(data.mediaInfo.audioStreamCount, int)
    assert isinstance(data.mediaInfo.videoBitDepth, int)
    assert isinstance(data.mediaInfo.videoBitrate, int)
    assert data.mediaInfo.videoCodec == "string"
    assert isinstance(data.mediaInfo.videoFps, int)
    assert data.mediaInfo.resolution == "string"
    assert data.mediaInfo.runTime == "string"
    assert data.mediaInfo.scanType == "string"
    assert data.mediaInfo.subtitles == "string"
    assert data.qualityCutoffNotMet is True
    assert isinstance(data.languages[0].id, int)
    assert data.languages[0].name == "string"
    assert data.sceneName == "string"
    assert data.edition == "string"
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/moviefile?movieFileIds=0&movieFileIds=1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/moviefile-list.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_lookup_movie_files([0, 1])
    assert isinstance(data[0], RadarrMovieFile)


@pytest.mark.asyncio
async def test_async_get_notification(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/notification.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_notifications(notifyid=0)

    assert data.onGrab is True
    assert data.onDownload is True
    assert data.onUpgrade is True
    assert data.onRename is True
    assert data.onHealthIssue is True
    assert data.supportsOnGrab is True
    assert data.supportsOnDownload is True
    assert data.supportsOnUpgrade is True
    assert data.supportsOnRename is True
    assert data.supportsOnHealthIssue is True
    assert data.includeHealthWarnings is True
    assert data.name == "string"
    assert isinstance(data.fields[0].order, int)
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert isinstance(data.fields[0].selectOptions[0].value, int)
    assert data.fields[0].selectOptions[0].name == "string"
    assert isinstance(data.fields[0].selectOptions[0].order, int)
    assert data.implementationName == "string"
    assert data.implementation == "string"
    assert data.configContract == "string"
    assert data.infoLink == "string"
    assert data.message.message == "string"
    assert data.message.type == "string"
    assert isinstance(data.tags[0], int)
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/queue?page=1&pageSize=20&sortDirection=ascending&sortKey=timeLeft&includeUnknownMovieItems=False&includeMovie=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_queue()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == "timeleft"
    assert data.sortDirection == "ascending"
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].movieId, int)
    assert isinstance(data.records[0].languages[0].id, int)
    assert data.records[0].languages[0].name == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert isinstance(data.records[0].quality.quality.resolution, int)
    assert data.records[0].quality.quality.modifier == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is True
    assert isinstance(data.records[0].customFormats[0].id, int)
    assert data.records[0].customFormats[0].name == "string"
    assert data.records[0].customFormats[0].includeCustomFormatWhenRenaming is True
    assert data.records[0].customFormats[0].specifications[0].name == "string"
    assert data.records[0].customFormats[0].specifications[0].implementation == "string"
    assert (
        data.records[0].customFormats[0].specifications[0].implementationName
        == "string"
    )
    assert data.records[0].customFormats[0].specifications[0].infoLink == "string"
    assert data.records[0].customFormats[0].specifications[0].negate is True
    assert data.records[0].customFormats[0].specifications[0].required is True
    assert isinstance(
        data.records[0].customFormats[0].specifications[0].fields[0].order, int
    )
    assert data.records[0].customFormats[0].specifications[0].fields[0].name == "string"
    assert (
        data.records[0].customFormats[0].specifications[0].fields[0].label == "string"
    )
    assert (
        data.records[0].customFormats[0].specifications[0].fields[0].helpText
        == "string"
    )
    assert (
        data.records[0].customFormats[0].specifications[0].fields[0].value == "string"
    )
    assert data.records[0].customFormats[0].specifications[0].fields[0].type == "string"
    assert data.records[0].customFormats[0].specifications[0].fields[0].advanced is True
    assert isinstance(data.records[0].size, int)
    assert data.records[0].title == "string"
    assert isinstance(data.records[0].sizeleft, int)
    assert data.records[0].timeleft == "string"
    assert data.records[0].estimatedCompletionTime == "string"
    assert data.records[0].status == "string"
    assert data.records[0].trackedDownloadStatus == "string"
    assert data.records[0].trackedDownloadState == "string"
    assert data.records[0].statusMessages[0].title == "string"
    assert data.records[0].statusMessages[0].messages == ["string"]
    assert data.records[0].errorMessage == "string"
    assert data.records[0].downloadId == "string"
    assert data.records[0].protocol == "string"
    assert data.records[0].downloadClient == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].outputPath == "string"
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/queue/details?includeUnknownMovieItems=False&includeMovie=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_queue_details()
    assert isinstance(data[0].movieId, int)
    assert isinstance(data[0].languages[0].id, int)
    assert data[0].languages[0].name == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
    assert data[0].quality.quality.modifier == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is True
    assert isinstance(data[0].customFormats[0].id, int)
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    assert data[0].customFormats[0].specifications[0].name == "string"
    assert data[0].customFormats[0].specifications[0].implementation == "string"
    assert data[0].customFormats[0].specifications[0].implementationName == "string"
    assert data[0].customFormats[0].specifications[0].infoLink == "string"
    assert data[0].customFormats[0].specifications[0].negate is True
    assert data[0].customFormats[0].specifications[0].required is True
    assert isinstance(data[0].customFormats[0].specifications[0].fields[0].order, int)
    assert data[0].customFormats[0].specifications[0].fields[0].name == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].label == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].helpText == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].value == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].type == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].advanced is True
    assert isinstance(data[0].size, int)
    assert data[0].title == "string"
    assert isinstance(data[0].sizeleft, int)
    assert data[0].timeleft == "string"
    assert data[0].estimatedCompletionTime == "string"
    assert data[0].status == "string"
    assert data[0].trackedDownloadStatus == "string"
    assert data[0].trackedDownloadState == "string"
    assert data[0].statusMessages[0].title == "string"
    assert data[0].statusMessages[0].messages == ["string"]
    assert data[0].errorMessage == "string"
    assert data[0].downloadId == "string"
    assert data[0].protocol == "string"
    assert data[0].downloadClient == "string"
    assert data[0].indexer == "string"
    assert data[0].outputPath == "string"
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/tag/detail/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_tags_details(tagid=0)

    assert isinstance(data.id, int)
    assert data.label == "string"
    assert isinstance(data.delayProfileIds[0], int)
    assert isinstance(data.notificationIds[0], int)
    assert isinstance(data.restrictionIds[0], int)
    assert isinstance(data.importListIds[0], int)
    assert isinstance(data.movieIds[0], int)
    assert isinstance(data.indexerIds[0], int)


@pytest.mark.asyncio
async def test_async_parse(aresponses):
    """Test parsing movie file name."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/parse?title=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/parse.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_parse("test")

    assert data.title == "string"
    assert data.parsedMovieInfo.movieTitles == ["string"]
    assert data.parsedMovieInfo.originalTitle == "string"
    assert data.parsedMovieInfo.releaseTitle == "string"
    assert data.parsedMovieInfo.simpleReleaseTitle == "string"
    assert isinstance(data.parsedMovieInfo.quality.quality.id, int)
    assert data.parsedMovieInfo.quality.quality.name == "string"
    assert data.parsedMovieInfo.quality.quality.source == "string"
    assert isinstance(data.parsedMovieInfo.quality.quality.resolution, int)
    assert data.parsedMovieInfo.quality.quality.modifier == "string"
    assert isinstance(data.parsedMovieInfo.quality.revision.version, int)
    assert isinstance(data.parsedMovieInfo.quality.revision.real, int)
    assert data.parsedMovieInfo.quality.revision.isRepack is False
    assert isinstance(data.parsedMovieInfo.languages[0].id, int)
    assert data.parsedMovieInfo.languages[0].name == "string"
    assert data.parsedMovieInfo.releaseHash == ""
    assert data.parsedMovieInfo.edition == ""
    assert isinstance(data.parsedMovieInfo.year, int)
    assert data.parsedMovieInfo.imdbId == ""
    assert isinstance(data.parsedMovieInfo.tmdbId, int)
    assert data.parsedMovieInfo.extraInfo == {}
    assert data.parsedMovieInfo.movieTitle == "string"
    assert data.parsedMovieInfo.primaryMovieTitle == "string"
    assert data.movie.title == "string"
    assert data.movie.originalTitle == "string"
    assert data.movie.alternateTitles[0].sourceType == "string"
    assert isinstance(data.movie.alternateTitles[0].movieId, int)
    assert data.movie.alternateTitles[0].title == "string"
    assert isinstance(data.movie.alternateTitles[0].sourceId, int)
    assert isinstance(data.movie.alternateTitles[0].votes, int)
    assert isinstance(data.movie.alternateTitles[0].voteCount, int)
    assert isinstance(data.movie.alternateTitles[0].language.id, int)
    assert data.movie.alternateTitles[0].language.name == "string"
    assert isinstance(data.movie.alternateTitles[0].id, int)
    assert isinstance(data.movie.secondaryYearSourceId, int)
    assert data.movie.sortTitle == "string"
    assert isinstance(data.movie.sizeOnDisk, int)
    assert data.movie.status == "string"
    assert data.movie.overview == "string"
    assert data.movie.inCinemas == datetime(2000, 4, 25, 0, 0)
    assert data.movie.physicalRelease == datetime(2000, 7, 8, 0, 0)
    assert data.movie.digitalRelease == datetime(2000, 2, 1, 0, 0)
    assert data.movie.images[0].coverType == "string"
    assert data.movie.images[0].url == "string"
    assert data.movie.website == "string"
    assert isinstance(data.movie.year, int)
    assert data.movie.hasFile is True
    assert data.movie.youTubeTrailerId == "string"
    assert data.movie.studio == "string"
    assert data.movie.path == "string"
    assert isinstance(data.movie.qualityProfileId, int)
    assert data.movie.monitored is False
    assert data.movie.minimumAvailability == "string"
    assert data.movie.isAvailable is True
    assert data.movie.folderName == "string"
    assert isinstance(data.movie.runtime, int)
    assert data.movie.cleanTitle == "string"
    assert data.movie.imdbId == "string"
    assert isinstance(data.movie.tmdbId, int)
    assert data.movie.titleSlug == "string"
    assert data.movie.certification == "string"
    assert data.movie.genres == ["string"]
    assert isinstance(data.movie.tags[0], int)
    assert data.movie.added == datetime(2020, 11, 28, 6, 34, 25)
    assert isinstance(data.movie.ratings.imdb.votes, int)
    assert isinstance(data.movie.ratings.imdb.value, float)
    assert data.movie.ratings.imdb.type == "string"
    assert isinstance(data.movie.ratings.tmdb.votes, int)
    assert isinstance(data.movie.ratings.tmdb.value, float)
    assert data.movie.ratings.tmdb.type == "string"
    assert isinstance(data.movie.ratings.metacritic.votes, int)
    assert isinstance(data.movie.ratings.metacritic.value, int)
    assert data.movie.ratings.metacritic.type == "string"
    assert isinstance(data.movie.ratings.rottenTomatoes.votes, int)
    assert isinstance(data.movie.ratings.rottenTomatoes.value, int)
    assert data.movie.ratings.rottenTomatoes.type == "string"
    assert isinstance(data.movie.movieFile.movieId, int)
    assert data.movie.movieFile.relativePath == "string"
    assert data.movie.movieFile.path == "string"
    assert isinstance(data.movie.movieFile.size, int)
    assert data.movie.movieFile.dateAdded == datetime(2020, 2, 23, 12, 0, 46)
    assert isinstance(data.movie.movieFile.indexerFlags, int)
    assert isinstance(data.movie.movieFile.quality.quality.id, int)
    assert data.movie.movieFile.quality.quality.name == "string"
    assert data.movie.movieFile.quality.quality.source == "string"
    assert isinstance(data.movie.movieFile.quality.quality.resolution, int)
    assert data.movie.movieFile.quality.quality.modifier == "string"
    assert isinstance(data.movie.movieFile.quality.revision.version, int)
    assert isinstance(data.movie.movieFile.quality.revision.real, int)
    assert data.movie.movieFile.quality.revision.isRepack is False
    assert isinstance(data.movie.movieFile.mediaInfo.audioBitrate, int)
    assert isinstance(data.movie.movieFile.mediaInfo.audioChannels, float)
    assert data.movie.movieFile.mediaInfo.audioCodec == "string"
    assert data.movie.movieFile.mediaInfo.audioLanguages == "string"
    assert isinstance(data.movie.movieFile.mediaInfo.audioStreamCount, int)
    assert isinstance(data.movie.movieFile.mediaInfo.videoBitDepth, int)
    assert isinstance(data.movie.movieFile.mediaInfo.videoBitrate, int)
    assert data.movie.movieFile.mediaInfo.videoCodec == "string"
    assert data.movie.movieFile.mediaInfo.videoDynamicRangeType == "string"
    assert isinstance(data.movie.movieFile.mediaInfo.videoFps, float)
    assert data.movie.movieFile.mediaInfo.resolution == "string"
    assert data.movie.movieFile.mediaInfo.runTime == "00:00:00"
    assert data.movie.movieFile.mediaInfo.scanType == "string"
    assert data.movie.movieFile.mediaInfo.subtitles == "string"
    assert data.movie.movieFile.qualityCutoffNotMet is False
    assert isinstance(data.movie.movieFile.languages[0].id, int)
    assert data.movie.movieFile.languages[0].name == "string"
    assert data.movie.movieFile.edition == "string"
    assert isinstance(data.movie.movieFile.id, int)
    assert data.movie.collection.name == "string"
    assert isinstance(data.movie.collection.tmdbId, int)
    assert data.movie.collection.images[0].coverType == "string"
    assert data.movie.collection.images[0].remoteUrl == "string"
    assert data.movie.collection.images[0].url == "string"
    assert isinstance(data.movie.id, int)


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
    """Test searching indexers for latest releases."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/release",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/release.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_release()

    assert data[0].guid == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
    assert data[0].quality.quality.modifier == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is False
    assert data[0].customFormats[0].specifications[0].implementation == "string"
    assert data[0].customFormats[0].specifications[0].negate is False
    assert data[0].customFormats[0].specifications[0].required is False
    assert isinstance(data[0].customFormats[0].specifications[0].fields.value, int)
    assert isinstance(data[0].customFormatScore, int)
    assert isinstance(data[0].qualityWeight, int)
    assert isinstance(data[0].age, int)
    assert isinstance(data[0].ageHours, float)
    assert isinstance(data[0].ageMinutes, float)
    assert isinstance(data[0].size, int)
    assert isinstance(data[0].indexerId, int)
    assert data[0].indexer == "string"
    assert data[0].releaseGroup == "string"
    assert data[0].releaseHash == "string"
    assert data[0].title == "string"
    assert data[0].sceneSource is False
    assert data[0].movieTitles == ["string"]
    assert isinstance(data[0].languages[0].id, int)
    assert data[0].languages[0].name == "string"
    assert data[0].approved is True
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is False
    assert isinstance(data[0].tmdbId, int)
    assert isinstance(data[0].imdbId, int)
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2022, 1, 7, 4, 20, 36)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].downloadAllowed is True
    assert isinstance(data[0].releaseWeight, int)
    assert data[0].indexerFlags == ["string"]
    assert data[0].edition == "string"
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert isinstance(data[0].seeders, int)
    assert isinstance(data[0].leechers, int)
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_pushed_release(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/release/push?id=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/release-push.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_pushed_release("test")
    assert isinstance(data, RadarrRelease)


@pytest.mark.asyncio
async def test_async_get_rename(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/rename?movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/rename.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_get_rename(0)
    assert isinstance(data[0].movieId, int)
    assert isinstance(data[0].movieFileId, int)
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_edit_movies(aresponses):
    """Test editing movies."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie?moveFiles=False",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_movies(RadarrMovie("test"))
    assert isinstance(data, RadarrMovie)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/editor",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_movies(RadarrMovieEditor("test"))
    assert isinstance(data, RadarrMovie)


@pytest.mark.asyncio
async def test_async_delete_movies(aresponses):
    """Test deleting movies."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/0?deleteFiles=False&addImportExclusion=False",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_movies(0)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/editor",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_movies([0, 1])


@pytest.mark.asyncio
async def test_async_import_movies(aresponses):
    """Test importing movies."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/import",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/movie-import.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_import_movies(RadarrMovie("test"))
    assert isinstance(data[0], RadarrMovie)


@pytest.mark.asyncio
async def test_async_delete_movie_file(aresponses):
    """Test deleting movie file."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/moviefile/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        await client.async_delete_movie_file(0)


@pytest.mark.asyncio
async def test_async_edit_import_list(aresponses):
    """Test editing an import list."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_import_list(RadarrImportList("test"))
    assert isinstance(data, RadarrImportList)


@pytest.mark.asyncio
async def test_async_add_import_list(aresponses):
    """Test adding an import list."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_import_list(RadarrImportList("test"))
    assert isinstance(data, RadarrImportList)


@pytest.mark.asyncio
async def test_async_test_import_lists(aresponses):
    """Test import list testing."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists(RadarrImportList("test")) is True

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists() is True

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_import_lists() is False


@pytest.mark.asyncio
async def test_async_importlist_action(aresponses):
    """Test performing import list action."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/action/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    data = await client.async_importlist_action(RadarrImportList({"name": "test"}))
    assert isinstance(data, RadarrImportList)


@pytest.mark.asyncio
async def test_async_edit_naming_config(aresponses):
    """Test adding an import list."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/naming",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_naming_config(RadarrNamingConfig("test"))
    assert isinstance(data, RadarrNamingConfig)


@pytest.mark.asyncio
async def test_async_edit_notification(aresponses):
    """Test editing notification."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification",
        "PUT",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_edit_notification(RadarrNotification("test"))
    assert isinstance(data, RadarrNotification)


@pytest.mark.asyncio
async def test_async_add_notification(aresponses):
    """Test adding notification."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_add_notification(RadarrNotification("test"))
    assert isinstance(data, RadarrNotification)


@pytest.mark.asyncio
async def test_async_test_notifications(aresponses):
    """Test notification testing."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_notifications(RadarrNotification("test")) is True

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_notifications() is True

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    assert await client.async_test_notifications() is False


@pytest.mark.asyncio
async def test_async_radarr_commands(aresponses):
    """Test Radarr commands."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_radarr_command(RadarrCommands.DOWNLOADED_MOVIES_SCAN)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_radarr_command(RadarrCommands.MISSING_MOVIES_SEARCH)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_radarr_command(RadarrCommands.REFRESH_MOVIE, [0])
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_radarr_command(RadarrCommands.RENAME_MOVIE)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_radarr_command(RadarrCommands.RESCAN_MOVIE)
    assert isinstance(data, Command)


@pytest.mark.asyncio
async def test_async_download_release(aresponses):
    """Test downloading release."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/release",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/release.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
        data = await client.async_download_release("test", 0)
    assert isinstance(data[0], RadarrRelease)


@pytest.mark.asyncio
async def test_not_implemented():
    """Test methods not implemented by the API."""
    async with ClientSession():
        client = RadarrClient(host_configuration=TEST_HOST_CONFIGURATION)
    with pytest.raises(NotImplementedError):
        await client.async_get_import_list_exclusions()

    with pytest.raises(NotImplementedError):
        await client.async_delete_import_list_exclusion(0)

    with pytest.raises(NotImplementedError):
        await client.async_edit_import_list_exclusion(0)

    with pytest.raises(NotImplementedError):
        await client.async_add_import_list_exclusion(0)

    with pytest.raises(NotImplementedError):
        await client.async_get_release_profiles(0)

    with pytest.raises(NotImplementedError):
        await client.async_edit_release_profile(0)

    with pytest.raises(NotImplementedError):
        await client.async_delete_release_profile(0)

    with pytest.raises(NotImplementedError):
        await client.async_add_release_profile(0)

    with pytest.raises(NotImplementedError):
        await client.async_delete_metadata_profile(0)
