"""Tests for Radarr object models."""
from datetime import datetime
from aiopyarr.models.radarr import (
    RadarrHealth,
    RadarrMetadataConfig,
    RadarrNamingConfig,
    RadarrQualityProfile,
    RadarrQueueStatus,
    RadarrRemotePathMapping,
    RadarrUpdate,
)

import pytest
from aiohttp.client import ClientSession

from aiopyarr.radarr_client import RadarrClient

from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklisted movies."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=descending&sortKey=date",
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
        "/api/v3/blocklist/movie?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieId=0",
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
        "/api/v3/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01&unmonitored=True",
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
        assert data[0].sizeOnDisk == 1967709785
        assert data[0].status == "released"
        assert data[0].overview == "string"
        assert data[0].physicalRelease == "2021-12-03T00:00:00Z"
        assert data[0].digitalRelease == "2020-08-11T00:00:00Z"
        assert data[0].images[0].coverType == "poster"
        assert data[0].images[0].url == "string"
        assert data[0].website == "string"
        assert data[0].year == 2020
        assert data[0].hasFile is True
        assert data[0].youTubeTrailerId == "string"
        assert data[0].studio == "string"
        assert data[0].path == "string"
        assert data[0].qualityProfileId == 9
        assert data[0].monitored is True
        assert data[0].minimumAvailability == "inCinemas"
        assert data[0].isAvailable is True
        assert data[0].folderName == "string"
        assert data[0].runtime == 97
        assert data[0].cleanTitle == "string"
        assert data[0].imdbId == "string"
        assert data[0].tmdbId == 0
        assert data[0].titleSlug == "string"
        assert data[0].genres == ["Comedy", "Horror", "Music"]
        assert data[0].tags == []
        assert data[0].added == "2020-07-16T13:25:37Z"
        assert data[0].ratings.votes == 48
        assert data[0].ratings.value == 6.1
        assert data[0].movieFile.movieId == 0
        assert data[0].movieFile.relativePath == "string"
        assert data[0].movieFile.path == "string"
        assert data[0].movieFile.size == 1967709785
        assert data[0].movieFile.dateAdded == "2021-06-01T04:08:20Z"
        assert data[0].movieFile.sceneName == "string"
        assert data[0].movieFile.indexerFlags == 1
        assert data[0].movieFile.quality.quality.id == 7
        assert data[0].movieFile.quality.quality.name == "Bluray-1080p"
        assert data[0].movieFile.quality.quality.source == "bluray"
        assert data[0].movieFile.quality.quality.resolution == 1080
        assert data[0].movieFile.quality.quality.modifier == "none"
        assert data[0].movieFile.quality.revision.version == 1
        assert data[0].movieFile.quality.revision.real == 0
        assert data[0].movieFile.quality.revision.isRepack is False
        assert data[0].movieFile.mediaInfo.audioBitrate == 224000
        assert data[0].movieFile.mediaInfo.audioChannels == 5.1
        assert data[0].movieFile.mediaInfo.audioCodec == "AAC"
        assert data[0].movieFile.mediaInfo.audioLanguages == "eng"
        assert data[0].movieFile.mediaInfo.audioStreamCount == 1
        assert data[0].movieFile.mediaInfo.videoBitDepth == 8
        assert data[0].movieFile.mediaInfo.videoBitrate == 2500000
        assert data[0].movieFile.mediaInfo.videoCodec == "x264"
        assert data[0].movieFile.mediaInfo.videoFps == 23.976
        assert data[0].movieFile.mediaInfo.resolution == "1920x816"
        assert data[0].movieFile.mediaInfo.runTime == "1:36:04"
        assert data[0].movieFile.mediaInfo.scanType == "Progressive"
        assert data[0].movieFile.mediaInfo.subtitles == ""
        assert data[0].movieFile.originalFilePath == "string"
        assert data[0].movieFile.qualityCutoffNotMet is False
        assert data[0].movieFile.languages[0].id == 1
        assert data[0].movieFile.languages[0].name == "English"
        assert data[0].movieFile.releaseGroup == "string"
        assert data[0].movieFile.edition == ""
        assert data[0].movieFile.id == 38229
        assert data[0].id == 47353


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/naming?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
async def test_async_get_download_client(aresponses):
    """Test getting download client."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/downloadclient/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/downloadclient.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_download_clients(clientid=0)
        assert data.configContract == "string"
        assert data.enable is True
        assert data.fields[0].order == 0
        assert data.fields[0].name == "string"
        assert data.fields[0].label == "string"
        assert data.fields[0].helpText == "string"
        assert data.fields[0].value == "string"
        assert data.fields[0].type == "string"
        assert data.fields[0].advanced is True
        assert data.id == 0
        assert data.implementation == "string"
        assert data.implementationName == "string"
        assert data.infoLink == "string"
        assert data.name == "string"
        assert data.protocol == "string"
        assert data.priority == 0
        assert data.tags == [0]


@pytest.mark.asyncio
async def test_async_get_failed_health_checks(aresponses):
    """Test getting failed health checks."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/health?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/health.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[RadarrHealth] = await client.async_get_failed_health_checks()

        assert data[0].message == "Enable Completed Download Handling"
        assert data[0].source == "ImportMechanismCheck"
        assert data[0].type == "warning"
        assert (
            data[0].wikiUrl
            == "https://wiki.servarr.com/radarr/system#completed-failed-download-handling"
        )


@pytest.mark.asyncio
async def test_async_get_movie_history(aresponses):
    """Test getting movie history."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/history/movie?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieId=0",
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
        "/api/v3/importlist/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
async def test_async_get_indexer(aresponses):
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/indexer/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/indexer.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_indexers(indexerid=0)

        assert data.enableRss is True
        assert data.enableAutomaticSearch is True
        assert data.enableInteractiveSearch is True
        assert data.supportsRss is True
        assert data.supportsSearch is True
        assert data.protocol == "string"
        assert data.priority == 0
        assert data.name == "string"
        assert data.fields[0].order == 0
        assert data.fields[0].name == "string"
        assert data.fields[0].label == "string"
        assert data.fields[0].helpText == "string"
        assert data.fields[0].value == "string"
        assert data.fields[0].type == "string"
        assert data.fields[0].advanced is True
        assert data.implementation == "string"
        assert data.implementationName == "string"
        assert data.configContract == "string"
        assert data.infoLink == "string"
        assert data.tags == [{}]
        assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_metadata_config(aresponses):
    """Test getting metadata config."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/metadata?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/metadata.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[RadarrMetadataConfig] = await client.async_get_metadata_config()

        assert data[0].enable is True
        assert data[0].name == "string"
        assert data[0].fields[0].order == 0
        assert data[0].fields[0].name == "string"
        assert data[0].fields[0].label == "string"
        assert data[0].fields[0].helpText == "string"
        assert data[0].fields[0].value == "string"
        assert data[0].fields[0].type == "string"
        assert data[0].fields[0].advanced is True
        assert data[0].implementationName == "string"
        assert data[0].implementation == "string"
        assert data[0].configContract == "string"
        assert data[0].infoLink == "string"
        assert data[0].tags == [0]
        assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_movie(aresponses):
    """Test getting movie attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/movie/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        assert data.alternateTitles[0].language.name == "English"
        assert data.alternateTitles[0].id == 1
        assert data.sortTitle == "string"
        assert data.sizeOnDisk == 0
        assert data.overview == "string"
        assert data.inCinemas == "string"
        assert data.physicalRelease == "string"
        assert data.images[0].coverType == "poster"
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
        assert data.minimumAvailability == "announced"
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
        assert data.added == "string"
        assert data.ratings.votes == 0
        assert data.ratings.value == 0
        assert data.movieFile.movieId == 0
        assert data.movieFile.relativePath == "string"
        assert data.movieFile.path == "string"
        assert data.movieFile.size == 916662234
        assert data.movieFile.dateAdded == "2020-11-26T02:00:35Z"
        assert data.movieFile.indexerFlags == 1
        assert data.movieFile.quality.quality.id == 14
        assert data.movieFile.quality.quality.name == "WEBRip-720p"
        assert data.movieFile.quality.quality.source == "webrip"
        assert data.movieFile.quality.quality.resolution == 720
        assert data.movieFile.quality.quality.modifier == "none"
        assert data.movieFile.quality.revision.version == 1
        assert data.movieFile.quality.revision.real == 0
        assert data.movieFile.quality.revision.isRepack is False
        assert data.movieFile.mediaInfo.audioBitrate == 0
        assert data.movieFile.mediaInfo.audioChannels == 2
        assert data.movieFile.mediaInfo.audioCodec == "AAC"
        assert data.movieFile.mediaInfo.audioLanguages == ""
        assert data.movieFile.mediaInfo.audioStreamCount == 1
        assert data.movieFile.mediaInfo.videoBitDepth == 8
        assert data.movieFile.mediaInfo.videoBitrate == 1000000
        assert data.movieFile.mediaInfo.videoCodec == "x264"
        assert data.movieFile.mediaInfo.videoFps == 25.000
        assert data.movieFile.mediaInfo.resolution == "1280x534"
        assert data.movieFile.mediaInfo.runTime == "1:49:06"
        assert data.movieFile.mediaInfo.scanType == "Progressive"
        assert data.movieFile.originalFilePath == "string"
        assert data.movieFile.qualityCutoffNotMet is True
        assert data.movieFile.languages[0].id == 26
        assert data.movieFile.languages[0].name == "Hindi"
        assert data.movieFile.edition == ""
        assert data.movieFile.id == 35361
        assert data.collection.name == "string"
        assert data.collection.tmdbId == 0
        assert data.collection.images[0].coverType == "poster"
        assert data.collection.images[0].url == "string"
        assert data.collection.images[0].remoteUrl == "string"
        assert data.status == "deleted"


@pytest.mark.asyncio
async def test_async_get_movie_file(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/moviefile?apikey=ur1234567-0abc12de3f456gh7ij89k012&movieid=0",
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
        assert data.dateAdded == "string"
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
        assert data.mediaInfo.audioChannels == 0
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
        assert data.releaseGroup == "string"
        assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_notification(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/notification/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        assert data.onDelete is True
        assert data.onHealthIssue is True
        assert data.supportsOnGrab is True
        assert data.supportsOnDownload is True
        assert data.supportsOnUpgrade is True
        assert data.supportsOnRename is True
        assert data.supportsOnDelete is True
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
        assert data.implementationName == "string"
        assert data.implementation == "string"
        assert data.configContract == "string"
        assert data.infoLink == "string"
        assert data.message.message == "string"
        assert data.message.type == "string"
        assert data.tags == [0]
        assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_quality_profiles(aresponses):
    """Test getting quality profiles."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/qualityProfile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/qualityProfile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[RadarrQualityProfile] = await client.async_get_quality_profiles()

        assert data[0].name == "Any"
        assert data[0].upgradeAllowed is True
        assert data[0].cutoff == 20
        assert data[0].items[0].quality.id == 0
        assert data[0].items[0].quality.name == "Unknown"
        assert data[0].items[0].quality.source == "unknown"
        assert data[0].items[0].quality.resolution == 0
        assert data[0].items[0].quality.modifier == "none"
        assert data[0].items[0].items == []
        assert data[0].items[0].allowed is False
        assert data[0].items[1].name == "WEB 480p"
        assert data[0].items[1].items[0].quality.id == 12
        assert data[0].items[1].items[0].quality.name == "WEBRip-480p"
        assert data[0].items[1].items[0].quality.source == "webrip"
        assert data[0].items[1].items[0].quality.resolution == 480
        assert data[0].items[1].items[0].quality.modifier == "none"
        assert data[0].items[1].items[0].items == []
        assert data[0].items[1].items[0].allowed is True
        assert data[0].items[1].allowed is True
        assert data[0].items[1].id == 1000
        assert data[0].minFormatScore == 0
        assert data[0].cutoffFormatScore == 0
        assert data[0].formatItems == []
        assert data[0].language.id == 1
        assert data[0].language.name == "English"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/queue/details?apikey=ur1234567-0abc12de3f456gh7ij89k012&includeMovie=True",
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
        assert data[0].statusMessages[0].messages == [{}]
        assert data[0].errorMessage == "string"
        assert data[0].downloadId == "string"
        assert data[0].protocol == "string"
        assert data[0].downloadClient == "string"
        assert data[0].indexer == "string"
        assert data[0].outputPath == "string"
        assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue_status(aresponses):
    """Test getting queue status."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/queue/status?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue-status.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: RadarrQueueStatus = await client.async_get_queue_status()

        assert data.totalCount == 0
        assert data.count == 0
        assert data.unknownCount == 0
        assert data.errors is True
        assert data.warnings is True
        assert data.unknownErrors is True
        assert data.unknownWarnings is True


@pytest.mark.asyncio
async def test_async_get_remote_path_mappings(aresponses):
    """Test getting remote path mappings."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/remotePathMapping?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/remotePathMapping.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[
            RadarrRemotePathMapping
        ] = await client.async_get_remote_path_mappings()

        assert data[0].host == "localhost"
        assert data[0].remotePath == "C:\\"
        assert data[0].localPath == "A:\\Movies\\"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/tag/detail/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        assert data.netImportIds == [0]
        assert data.movieIds == [0]


@pytest.mark.asyncio
async def test_async_get_software_update_info(aresponses):
    """Test getting software update info."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/update?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/update.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: RadarrUpdate = await client.async_get_software_update_info()

        assert data.version == "3.0.0.3553"
        assert data.branch == "nightly"
        assert data.releaseDate == "2020-09-02T05:36:13.047313Z"
        assert data.fileName == "Radarr.nightly.3.0.0.3553.windows-core-x64.zip"
        assert data.url == "string"
        assert data.installed is False
        assert data.installed is False
        assert data.latest is False
        assert data.changes.new == []
        assert data.changes.fixed == ["string"]
        assert data.hash == "abc123"
