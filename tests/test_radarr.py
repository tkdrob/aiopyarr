"""Tests for Radarr object models."""
from datetime import datetime

import pytest
from aiohttp.client import ClientSession

from aiopyarr.models.radarr import RadarrNamingConfig
from aiopyarr.radarr_client import RadarrClient

from . import RADARR_API, TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklisted movies."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_blocklist()

    assert data.page == 0
    assert data.pageSize == 0
    assert data.records[0].movieId == 0
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].date == "string"
    assert data.records[0].id == 0
    assert data.records[0].indexer == "string"
    assert data.records[0].protocol == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 0
    assert data.records[0].quality.quality.modifier == "string"
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is True
    assert data.records[0].languages[0].id == 0
    assert data.records[0].languages[0].name == "string"
    assert data.records[0].customFormats[0].id == 0
    assert data.records[0].customFormats[0].name == "string"
    assert data.records[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data.records[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert spec.fields[0].order == 0
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data.sortDirection == "string"
    assert data.sortKey == "string"
    assert data.totalRecords == 0


@pytest.mark.asyncio
async def test_async_get_blocklist_movie(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/blocklist/movie?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist-movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_blocklist_movie(bocklistid=0)

    assert data[0].movieId == 0
    assert data[0].sourceTitle == "string"
    assert data[0].languages[0].id == 0
    assert data[0].languages[0].name == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.quality.modifier == "string"
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is True
    assert data[0].customFormats[0].id == 0
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert spec.fields[0].order == 0
    assert spec.fields[0].name == "string"
    assert spec.fields[0].label == "string"
    assert spec.fields[0].helpText == "string"
    assert spec.fields[0].value == "string"
    assert spec.fields[0].type == "string"
    assert spec.fields[0].advanced is True
    assert data[0].date == "string"
    assert data[0].id == 0
    assert data[0].indexer == "string"
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01&unmonitored=True",
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
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_calendar(start, end)

    assert data[0].title == "string"
    assert data[0].originalTitle == "string"
    assert data[0].alternateTitles == []
    assert data[0].secondaryYearSourceId == 0
    assert data[0].sortTitle == "string"
    assert data[0].sizeOnDisk == 0
    assert data[0].status == "string"
    assert data[0].overview == "string"
    assert data[0].physicalRelease == datetime(2021, 12, 3, 0, 0)
    assert data[0].digitalRelease == datetime(2020, 8, 11, 0, 0)
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].url == "string"
    assert data[0].website == "string"
    assert data[0].year == 0
    assert data[0].hasFile is True
    assert data[0].youTubeTrailerId == "string"
    assert data[0].studio == "string"
    assert data[0].path == "string"
    assert data[0].qualityProfileId == 0
    assert data[0].monitored is True
    assert data[0].minimumAvailability == "string"
    assert data[0].isAvailable is True
    assert data[0].folderName == "string"
    assert data[0].runtime == 0
    assert data[0].cleanTitle == "string"
    assert data[0].imdbId == "string"
    assert data[0].tmdbId == 0
    assert data[0].titleSlug == "string"
    assert data[0].genres == ["string"]
    assert data[0].tags == []
    assert data[0].added == datetime(2020, 7, 16, 13, 25, 37)
    assert data[0].ratings.imdb.votes == 0
    assert data[0].ratings.imdb.value == 0.0
    assert data[0].ratings.imdb.type == "string"
    assert data[0].ratings.tmdb.votes == 0
    assert data[0].ratings.tmdb.value == 0.0
    assert data[0].ratings.tmdb.type == "string"
    assert data[0].ratings.metacritic.votes == 0
    assert data[0].ratings.metacritic.value == 0.0
    assert data[0].ratings.metacritic.type == "string"
    assert data[0].ratings.rottenTomatoes.votes == 0
    assert data[0].ratings.rottenTomatoes.value == 0.0
    assert data[0].ratings.rottenTomatoes.type == "string"
    assert data[0].movieFile.movieId == 0
    assert data[0].movieFile.relativePath == "string"
    assert data[0].movieFile.path == "string"
    assert data[0].movieFile.size == 0
    assert data[0].movieFile.dateAdded == datetime(2021, 6, 1, 4, 8, 20)
    assert data[0].movieFile.sceneName == "string"
    assert data[0].movieFile.indexerFlags == 0
    assert data[0].movieFile.quality.quality.id == 0
    assert data[0].movieFile.quality.quality.name == "string"
    assert data[0].movieFile.quality.quality.source == "string"
    assert data[0].movieFile.quality.quality.resolution == 0
    assert data[0].movieFile.quality.quality.modifier == "string"
    assert data[0].movieFile.quality.revision.version == 0
    assert data[0].movieFile.quality.revision.real == 0
    assert data[0].movieFile.quality.revision.isRepack is False
    assert data[0].movieFile.mediaInfo.audioBitrate == 0
    assert data[0].movieFile.mediaInfo.audioChannels == 0.0
    assert data[0].movieFile.mediaInfo.audioCodec == "string"
    assert data[0].movieFile.mediaInfo.audioLanguages == "string"
    assert data[0].movieFile.mediaInfo.audioStreamCount == 0
    assert data[0].movieFile.mediaInfo.videoBitDepth == 0
    assert data[0].movieFile.mediaInfo.videoBitrate == 0
    assert data[0].movieFile.mediaInfo.videoCodec == "string"
    assert data[0].movieFile.mediaInfo.videoFps == 0.0
    assert data[0].movieFile.mediaInfo.resolution == "string"
    assert data[0].movieFile.mediaInfo.runTime == "00:00:00"
    assert data[0].movieFile.mediaInfo.scanType == "string"
    assert data[0].movieFile.mediaInfo.subtitles == "string"
    assert data[0].movieFile.originalFilePath == "string"
    assert data[0].movieFile.qualityCutoffNotMet is False
    assert data[0].movieFile.languages[0].id == 0
    assert data[0].movieFile.languages[0].name == "string"
    assert data[0].movieFile.sceneName == "string"
    assert data[0].movieFile.edition == "string"
    assert data[0].movieFile.id == 0
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/naming?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: RadarrNamingConfig = await client.async_get_naming_config()

    assert data.colonReplacementFormat == "string"
    assert data.id == 0
    assert data.includeQuality is True
    assert data.movieFolderFormat == "string"
    assert data.renameMovies is True
    assert data.replaceIllegalCharacters is True
    assert data.replaceSpaces is True
    assert data.standardMovieFormat == "string"


@pytest.mark.asyncio
async def test_async_get_movie_history(aresponses):
    """Test getting movie history."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/history/movie?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/history-movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_movie_history(recordid=0)

    assert data[0].movieId == 0
    assert data[0].sourceTitle == "string"
    assert data[0].languages[0].id == 0
    assert data[0].languages[0].name == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.quality.modifier == "string"
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is True
    assert data[0].customFormats[0].id == 0
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    spec = data[0].customFormats[0].specifications[0]
    assert spec.name == "string"
    assert spec.implementation == "string"
    assert spec.implementationName == "string"
    assert spec.infoLink == "string"
    assert spec.negate is True
    assert spec.required is True
    assert spec.fields[0].order == 0
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
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_import_list(aresponses):
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/importlist/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/importlist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_import_lists(listid=0)

    assert data.enabled is True
    assert data.enableAuto is True
    assert data.shouldMonitor is True
    assert data.rootFolderPath == "string"
    assert data.qualityProfileId == 0
    assert data.searchOnAdd is True
    assert data.minimumAvailability == "string"
    assert data.listType == "string"
    assert data.listOrder == 0
    assert data.name == "string"
    assert data.fields[0].order == 0
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert data.implementationName == "string"
    assert data.implementation == "string"
    assert data.configContract == "string"
    assert data.infoLink == "string"
    assert data.tags == [0]
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_movie(aresponses):
    """Test getting movie attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/movie/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/movie.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_movies(movieid=0)

    assert data.id == 0
    assert data.title == "string"
    assert data.originalTitle == "string"
    assert data.alternateTitles[0].sourceType == "tmdb"
    assert data.alternateTitles[0].movieId == 1
    assert data.alternateTitles[0].title == "string"
    assert data.alternateTitles[0].sourceId == 0
    assert data.alternateTitles[0].votes == 0
    assert data.alternateTitles[0].voteCount == 0
    assert data.alternateTitles[0].language.id == 1
    assert data.alternateTitles[0].language.name == "string"
    assert data.alternateTitles[0].id == 1
    assert data.sortTitle == "string"
    assert data.sizeOnDisk == 0
    assert data.overview == "string"
    assert data.inCinemas == datetime(2020, 11, 6, 0, 0)
    assert data.physicalRelease == datetime(2019, 3, 19, 0, 0)
    assert data.images[0].coverType == "string"
    assert data.images[0].url == "string"
    assert data.images[0].remoteUrl == "string"
    assert data.website == "string"
    assert data.year == 0
    assert data.hasFile is True
    assert data.youTubeTrailerId == "string"
    assert data.studio == "string"
    assert data.path == "string"
    assert data.rootFolderPath == "string"
    assert data.qualityProfileId == 0
    assert data.monitored is True
    assert data.minimumAvailability == "string"
    assert data.isAvailable is True
    assert data.folderName == "string"
    assert data.runtime == 0
    assert data.cleanTitle == "string"
    assert data.imdbId == "string"
    assert data.tmdbId == 0
    assert data.titleSlug == "string"
    assert data.certification == "string"
    assert data.genres == ["string"]
    assert data.tags == [0]
    assert data.added == datetime(2018, 12, 28, 5, 56, 49)
    assert data.ratings.imdb.votes == 0
    assert data.ratings.imdb.value == 0.0
    assert data.ratings.imdb.type == "string"
    assert data.ratings.tmdb.votes == 0
    assert data.ratings.tmdb.value == 0.0
    assert data.ratings.tmdb.type == "string"
    assert data.ratings.metacritic.votes == 0
    assert data.ratings.metacritic.value == 0.0
    assert data.ratings.metacritic.type == "string"
    assert data.ratings.rottenTomatoes.votes == 0
    assert data.ratings.rottenTomatoes.value == 0.0
    assert data.ratings.rottenTomatoes.type == "string"
    assert data.movieFile.movieId == 0
    assert data.movieFile.relativePath == "string"
    assert data.movieFile.path == "string"
    assert data.movieFile.size == 0
    assert data.movieFile.dateAdded == datetime(2020, 11, 26, 2, 0, 35)
    assert data.movieFile.indexerFlags == 1
    assert data.movieFile.quality.quality.id == 0
    assert data.movieFile.quality.quality.name == "string"
    assert data.movieFile.quality.quality.source == "string"
    assert data.movieFile.quality.quality.resolution == 0
    assert data.movieFile.quality.quality.modifier == "string"
    assert data.movieFile.quality.revision.version == 0
    assert data.movieFile.quality.revision.real == 0
    assert data.movieFile.quality.revision.isRepack is False
    assert data.movieFile.mediaInfo.audioBitrate == 0
    assert data.movieFile.mediaInfo.audioChannels == 0.0
    assert data.movieFile.mediaInfo.audioCodec == "string"
    assert data.movieFile.mediaInfo.audioLanguages == "string"
    assert data.movieFile.mediaInfo.audioStreamCount == 0
    assert data.movieFile.mediaInfo.videoBitDepth == 0
    assert data.movieFile.mediaInfo.videoBitrate == 0
    assert data.movieFile.mediaInfo.videoCodec == "string"
    assert data.movieFile.mediaInfo.videoFps == 0.0
    assert data.movieFile.mediaInfo.resolution == "string"
    assert data.movieFile.mediaInfo.runTime == "00:00:00"
    assert data.movieFile.mediaInfo.scanType == "string"
    assert data.movieFile.originalFilePath == "string"
    assert data.movieFile.qualityCutoffNotMet is True
    assert data.movieFile.languages[0].id == 0
    assert data.movieFile.languages[0].name == "string"
    assert data.movieFile.edition == "string"
    assert data.movieFile.id == 0
    assert data.collection.name == "string"
    assert data.collection.tmdbId == 0
    assert data.collection.images[0].coverType == "string"
    assert data.collection.images[0].url == "string"
    assert data.collection.images[0].remoteUrl == "string"
    assert data.status == "string"


@pytest.mark.asyncio
async def test_async_get_movie_file(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/moviefile?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieid=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/moviefile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_movie_files_by_movie_id(movieid=0)

    assert data.movieId == 0
    assert data.relativePath == "string"
    assert data.path == "string"
    assert data.size == 0
    assert data.dateAdded == datetime(2018, 12, 28, 6, 35, 27)
    assert data.indexerFlags == 0
    assert data.quality.quality.id == 0
    assert data.quality.quality.name == "string"
    assert data.quality.quality.source == "string"
    assert data.quality.quality.resolution == 0
    assert data.quality.quality.modifier == "string"
    assert data.quality.revision.version == 0
    assert data.quality.revision.real == 0
    assert data.quality.revision.isRepack is True
    assert data.mediaInfo.audioAdditionalFeatures == "string"
    assert data.mediaInfo.audioBitrate == 0
    assert data.mediaInfo.audioChannels == 0.0
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioLanguages == "string"
    assert data.mediaInfo.audioStreamCount == 0
    assert data.mediaInfo.videoBitDepth == 0
    assert data.mediaInfo.videoBitrate == 0
    assert data.mediaInfo.videoCodec == "string"
    assert data.mediaInfo.videoFps == 0
    assert data.mediaInfo.resolution == "string"
    assert data.mediaInfo.runTime == "string"
    assert data.mediaInfo.scanType == "string"
    assert data.mediaInfo.subtitles == "string"
    assert data.qualityCutoffNotMet is True
    assert data.languages[0].id == 0
    assert data.languages[0].name == "string"
    assert data.sceneName == "string"
    assert data.edition == "string"
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_notification(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/notification/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/notification.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
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
    assert data.fields[0].order == 0
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert data.fields[0].selectOptions[0].value == 0
    assert data.fields[0].selectOptions[0].name == "string"
    assert data.fields[0].selectOptions[0].order == 0
    assert data.implementationName == "string"
    assert data.implementation == "string"
    assert data.configContract == "string"
    assert data.infoLink == "string"
    assert data.message.message == "string"
    assert data.message.type == "string"
    assert data.tags == [0]
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/queue?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=ascending&sortKey=timeLeft&includeUnknownMovieItems=False&includeMovie=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue()

    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "timeleft"
    assert data.sortDirection == "ascending"
    assert data.totalRecords == 1
    assert data.records[0].movieId == 0
    assert data.records[0].languages[0].id == 0
    assert data.records[0].languages[0].name == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 0
    assert data.records[0].quality.quality.modifier == "string"
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is True
    assert data.records[0].customFormats[0].id == 0
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
    assert data.records[0].customFormats[0].specifications[0].fields[0].order == 0
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
    assert data.records[0].size == 0
    assert data.records[0].title == "string"
    assert data.records[0].sizeleft == 0
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
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/queue/details?apikey=ur1234567-0abc12de3f456gh7ij89k012&includeUnknownMovieItems=False&includeMovie=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue_details()
    assert data[0].movieId == 0
    assert data[0].languages[0].id == 0
    assert data[0].languages[0].name == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.quality.modifier == "string"
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is True
    assert data[0].customFormats[0].id == 0
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is True
    assert data[0].customFormats[0].specifications[0].name == "string"
    assert data[0].customFormats[0].specifications[0].implementation == "string"
    assert data[0].customFormats[0].specifications[0].implementationName == "string"
    assert data[0].customFormats[0].specifications[0].infoLink == "string"
    assert data[0].customFormats[0].specifications[0].negate is True
    assert data[0].customFormats[0].specifications[0].required is True
    assert data[0].customFormats[0].specifications[0].fields[0].order == 0
    assert data[0].customFormats[0].specifications[0].fields[0].name == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].label == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].helpText == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].value == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].type == "string"
    assert data[0].customFormats[0].specifications[0].fields[0].advanced is True
    assert data[0].size == 0
    assert data[0].title == "string"
    assert data[0].sizeleft == 0
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
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/tag/detail/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_tags_details(tagid=0)

    assert data.id == 0
    assert data.label == "string"
    assert data.delayProfileIds == [0]
    assert data.notificationIds == [0]
    assert data.restrictionIds == [0]
    assert data.importListIds == [0]
    assert data.movieIds == [0]
    assert data.indexerIds == [0]


@pytest.mark.asyncio
async def test_async_parse(aresponses):
    """Test parsing movie file name."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/parse?apikey=ur1234567-0abc12de3f456gh7ij89k012&title=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/parse.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_parse("test")

    assert data.title == "string"
    assert data.parsedMovieInfo.movieTitles == ["string"]
    assert data.parsedMovieInfo.originalTitle == "string"
    assert data.parsedMovieInfo.releaseTitle == "string"
    assert data.parsedMovieInfo.simpleReleaseTitle == "string"
    assert data.parsedMovieInfo.quality.quality.id == 0
    assert data.parsedMovieInfo.quality.quality.name == "string"
    assert data.parsedMovieInfo.quality.quality.source == "string"
    assert data.parsedMovieInfo.quality.quality.resolution == 0
    assert data.parsedMovieInfo.quality.quality.modifier == "string"
    assert data.parsedMovieInfo.quality.revision.version == 0
    assert data.parsedMovieInfo.quality.revision.real == 0
    assert data.parsedMovieInfo.quality.revision.isRepack is False
    assert data.parsedMovieInfo.languages[0].id == 0
    assert data.parsedMovieInfo.languages[0].name == "string"
    assert data.parsedMovieInfo.releaseHash == ""
    assert data.parsedMovieInfo.edition == ""
    assert data.parsedMovieInfo.year == 0
    assert data.parsedMovieInfo.imdbId == ""
    assert data.parsedMovieInfo.tmdbId == 0
    assert data.parsedMovieInfo.extraInfo == {}
    assert data.parsedMovieInfo.movieTitle == "string"
    assert data.parsedMovieInfo.primaryMovieTitle == "string"
    assert data.movie.title == "string"
    assert data.movie.originalTitle == "string"
    assert data.movie.alternateTitles[0].sourceType == "string"
    assert data.movie.alternateTitles[0].movieId == 0
    assert data.movie.alternateTitles[0].title == "string"
    assert data.movie.alternateTitles[0].sourceId == 0
    assert data.movie.alternateTitles[0].votes == 0
    assert data.movie.alternateTitles[0].voteCount == 0
    assert data.movie.alternateTitles[0].language.id == 0
    assert data.movie.alternateTitles[0].language.name == "string"
    assert data.movie.alternateTitles[0].id == 0
    assert data.movie.secondaryYearSourceId == 0
    assert data.movie.sortTitle == "string"
    assert data.movie.sizeOnDisk == 0
    assert data.movie.status == "string"
    assert data.movie.overview == "string"
    assert data.movie.inCinemas == datetime(2000, 4, 25, 0, 0)
    assert data.movie.physicalRelease == datetime(2000, 7, 8, 0, 0)
    assert data.movie.digitalRelease == datetime(2000, 2, 1, 0, 0)
    assert data.movie.images[0].coverType == "string"
    assert data.movie.images[0].url == "string"
    assert data.movie.website == "string"
    assert data.movie.year == 0
    assert data.movie.hasFile is True
    assert data.movie.youTubeTrailerId == "string"
    assert data.movie.studio == "string"
    assert data.movie.path == "string"
    assert data.movie.qualityProfileId == 0
    assert data.movie.monitored is False
    assert data.movie.minimumAvailability == "string"
    assert data.movie.isAvailable is True
    assert data.movie.folderName == "string"
    assert data.movie.runtime == 0
    assert data.movie.cleanTitle == "string"
    assert data.movie.imdbId == "string"
    assert data.movie.tmdbId == 0
    assert data.movie.titleSlug == "string"
    assert data.movie.certification == "string"
    assert data.movie.genres == ["string"]
    assert data.movie.tags == [0]
    assert data.movie.added == datetime(2020, 11, 28, 6, 34, 25)
    assert data.movie.ratings.imdb.votes == 0
    assert data.movie.ratings.imdb.value == 0.0
    assert data.movie.ratings.imdb.type == "string"
    assert data.movie.ratings.tmdb.votes == 0
    assert data.movie.ratings.tmdb.value == 0.0
    assert data.movie.ratings.tmdb.type == "string"
    assert data.movie.ratings.metacritic.votes == 0
    assert data.movie.ratings.metacritic.value == 0.0
    assert data.movie.ratings.metacritic.type == "string"
    assert data.movie.ratings.rottenTomatoes.votes == 0
    assert data.movie.ratings.rottenTomatoes.value == 0.0
    assert data.movie.ratings.rottenTomatoes.type == "string"
    assert data.movie.movieFile.movieId == 0
    assert data.movie.movieFile.relativePath == "string"
    assert data.movie.movieFile.path == "string"
    assert data.movie.movieFile.size == 0
    assert data.movie.movieFile.dateAdded == datetime(2020, 2, 23, 12, 0, 46)
    assert data.movie.movieFile.indexerFlags == 0
    assert data.movie.movieFile.quality.quality.id == 0
    assert data.movie.movieFile.quality.quality.name == "string"
    assert data.movie.movieFile.quality.quality.source == "string"
    assert data.movie.movieFile.quality.quality.resolution == 0
    assert data.movie.movieFile.quality.quality.modifier == "string"
    assert data.movie.movieFile.quality.revision.version == 0
    assert data.movie.movieFile.quality.revision.real == 0
    assert data.movie.movieFile.quality.revision.isRepack is False
    assert data.movie.movieFile.mediaInfo.audioBitrate == 0
    assert data.movie.movieFile.mediaInfo.audioChannels == 0.0
    assert data.movie.movieFile.mediaInfo.audioCodec == "string"
    assert data.movie.movieFile.mediaInfo.audioLanguages == "string"
    assert data.movie.movieFile.mediaInfo.audioStreamCount == 0
    assert data.movie.movieFile.mediaInfo.videoBitDepth == 0
    assert data.movie.movieFile.mediaInfo.videoBitrate == 0
    assert data.movie.movieFile.mediaInfo.videoCodec == "string"
    assert data.movie.movieFile.mediaInfo.videoDynamicRangeType == "string"
    assert data.movie.movieFile.mediaInfo.videoFps == 0.0
    assert data.movie.movieFile.mediaInfo.resolution == "string"
    assert data.movie.movieFile.mediaInfo.runTime == "00:00:00"
    assert data.movie.movieFile.mediaInfo.scanType == "string"
    assert data.movie.movieFile.mediaInfo.subtitles == "string"
    assert data.movie.movieFile.qualityCutoffNotMet is False
    assert data.movie.movieFile.languages[0].id == 0
    assert data.movie.movieFile.languages[0].name == "string"
    assert data.movie.movieFile.edition == "string"
    assert data.movie.movieFile.id == 0
    assert data.movie.collection.name == "string"
    assert data.movie.collection.tmdbId == 0
    assert data.movie.collection.images[0].coverType == "string"
    assert data.movie.collection.images[0].remoteUrl == "string"
    assert data.movie.collection.images[0].url == "string"
    assert data.movie.id == 0


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
    """Test searching indexers for latest releases."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/release?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/release.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_release()

    assert data[0].guid == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.quality.modifier == "string"
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is False
    assert data[0].customFormats[0].name == "string"
    assert data[0].customFormats[0].includeCustomFormatWhenRenaming is False
    assert data[0].customFormats[0].specifications[0].implementation == "string"
    assert data[0].customFormats[0].specifications[0].negate is False
    assert data[0].customFormats[0].specifications[0].required is False
    assert data[0].customFormats[0].specifications[0].fields.value == 0
    assert data[0].customFormatScore == 0
    assert data[0].qualityWeight == 0
    assert data[0].age == 0
    assert data[0].ageHours == 0
    assert data[0].ageMinutes == 0
    assert data[0].size == 0
    assert data[0].indexerId == 0
    assert data[0].indexer == "string"
    assert data[0].releaseGroup == "string"
    assert data[0].releaseHash == "string"
    assert data[0].title == "string"
    assert data[0].sceneSource is False
    assert data[0].movieTitles == ["string"]
    assert data[0].languages[0].id == 1
    assert data[0].languages[0].name == "string"
    assert data[0].approved is True
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is False
    assert data[0].tmdbId == 0
    assert data[0].imdbId == 0
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2022, 1, 7, 4, 20, 36)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].downloadAllowed is True
    assert data[0].releaseWeight == 0
    assert data[0].indexerFlags == ["string"]
    assert data[0].edition == "string"
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert data[0].seeders == 0
    assert data[0].leechers == 0
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_rename(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/rename?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/rename.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_rename(0)
    assert data[0].movieId == 0
    assert data[0].movieFileId == 0
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"
