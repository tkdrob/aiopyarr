"""Tests for Radarr object models."""
from datetime import datetime

import pytest
from aiohttp.client import ClientSession

from aiopyarr.radarr_client import RadarrClient

from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklisted movies."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/blocklist",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist.json"),
        ),
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
        assert data.records[0].quality.revision.isRepack == True
        assert data.records[0].languages[0].id == 0
        assert data.records[0].languages[0].name == "string"
        assert data.records[0].customFormats[0].id == 0
        assert data.records[0].customFormats[0].name == "string"
        assert data.records[0].customFormats[0].includeCustomFormatWhenRenaming == True
        spec = data.records[0].customFormats[0].specifications[0]
        assert spec.name == "string"
        assert spec.implementation == "string"
        assert spec.implementationName == "string"
        assert spec.infoLink == "string"
        assert spec.negate == True
        assert spec.required == True
        assert spec.fields[0].order == 0
        assert spec.fields[0].name == "string"
        assert spec.fields[0].label == "string"
        assert spec.fields[0].helpText == "string"
        assert spec.fields[0].value == "string"
        assert spec.fields[0].type == "string"
        assert spec.fields[0].advanced == True
        assert data.sortDirection == "string"
        assert data.sortKey == "string"
        assert data.totalRecords == 0


@pytest.mark.asyncio
async def test_async_get_blocklist_movie(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/blocklist/movie",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/blocklist-movie.json"),
        ),
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
        assert data[0].quality.revision.isRepack == True
        assert data[0].customFormats[0].id == 0
        assert data[0].customFormats[0].name == "string"
        assert data[0].customFormats[0].includeCustomFormatWhenRenaming == True
        spec = data[0].customFormats[0].specifications[0]
        assert spec.name == "string"
        assert spec.implementation == "string"
        assert spec.implementationName == "string"
        assert spec.infoLink == "string"
        assert spec.negate == True
        assert spec.required == True
        assert spec.fields[0].order == 0
        assert spec.fields[0].name == "string"
        assert spec.fields[0].label == "string"
        assert spec.fields[0].helpText == "string"
        assert spec.fields[0].value == "string"
        assert spec.fields[0].type == "string"
        assert spec.fields[0].advanced == True
        assert data[0].date == "string"
        assert data[0].id == 0
        assert data[0].indexer == "string"
        assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/calendar",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/calendar.json"),
        ),
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
        assert data[0].hasFile == True
        assert data[0].youTubeTrailerId == "string"
        assert data[0].studio == "string"
        assert data[0].path == "string"
        assert data[0].qualityProfileId == 9
        assert data[0].monitored == True
        assert data[0].minimumAvailability == "inCinemas"
        assert data[0].isAvailable == True
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
        assert data[0].movieFile.quality.revision.isRepack == False
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
        assert data[0].movieFile.qualityCutoffNotMet == False
        assert data[0].movieFile.languages[0].id == 1
        assert data[0].movieFile.languages[0].name == "English"
        assert data[0].movieFile.releaseGroup == "string"
        assert data[0].movieFile.edition == ""
        assert data[0].movieFile.id == 38229
        assert data[0].id == 47353


@pytest.mark.asyncio
async def test_async_get_command(aresponses):
    """Test getting commands."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/command",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/command.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_command()

        assert data[0].name == "MessagingCleanup"
        assert data[0].commandName == "Messaging Cleanup"
        assert data[0].message == "Completed"
        assert data[0].body.sendUpdatesToClient == False
        assert data[0].body.updateScheduledTask == True
        assert data[0].body.completionMessage == "Completed"
        assert data[0].body.requiresDiskAccess == False
        assert data[0].body.isExclusive == False
        assert data[0].body.isNewMovie == False
        assert data[0].body.isTypeExclusive == False
        assert data[0].body.name == "MessagingCleanup"
        assert data[0].body.lastExecutionTime == "2021-11-29T19:57:46Z"
        assert data[0].body.lastStartTime == "2021-11-29T19:57:46Z"
        assert data[0].body.trigger == "scheduled"
        assert data[0].body.suppressMessages == False
        assert data[0].priority == "low"
        assert data[0].status == "completed"
        assert data[0].queued == "2021-11-29T20:03:16Z"
        assert data[0].started == "2021-11-29T20:03:16Z"
        assert data[0].ended == "2021-11-29T20:03:16Z"
        assert data[0].duration == "00:00:00.0102456"
        assert data[0].trigger == "scheduled"
        assert data[0].stateChangeTime == "2021-11-29T20:03:16Z"
        assert data[0].sendUpdatesToClient == False
        assert data[0].updateScheduledTask == True
        assert data[0].lastExecutionTime == "2021-11-29T19:57:46Z"
        assert data[0].id == 1987776


@pytest.mark.asyncio
async def test_async_get_host_config(aresponses):
    """Test getting host configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/host",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/config-host.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_host_config()

        assert data.analyticsEnabled == True
        assert data.apiKey == "string"
        assert data.authenticationMethod == "string"
        assert data.backupFolder == "string"
        assert data.backupInterval == 0
        assert data.backupRetention == 0
        assert data.bindAddress == "string"
        assert data.branch == "string"
        assert data.certificateValidation == "string"
        assert data.consoleLogLevel == "string"
        assert data.enableSsl == True
        assert data.id == 0
        assert data.launchBrowser == True
        assert data.logLevel == "string"
        assert data.password == "string"
        assert data.port == 0
        assert data.proxyBypassFilter == "string"
        assert data.proxyBypassLocalAddresses == True
        assert data.proxyEnabled == True
        assert data.proxyHostname == "string"
        assert data.proxyPassword == "string"
        assert data.proxyPort == 0
        assert data.proxyType == "string"
        assert data.proxyUsername == "string"
        assert data.sslCertPassword == "string"
        assert data.sslCertPath == "string"
        assert data.sslPort == 0
        assert data.urlBase == "string"
        assert data.updateAutomatically == True
        assert data.updateMechanism == "string"
        assert data.updateScriptPath == "string"
        assert data.username == "string"


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/naming",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/config-naming.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_naming_config()

        assert data.colonReplacementFormat == "string"
        assert data.id == 0
        assert data.includeQuality == True
        assert data.movieFolderFormat == "string"
        assert data.renameMovies == True
        assert data.replaceIllegalCharacters == True
        assert data.replaceSpaces == True
        assert data.standardMovieFormat == "string"


@pytest.mark.asyncio
async def test_async_get_ui_config(aresponses):
    """Test getting ui configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/ui",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/config-ui.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_ui_config()

        assert data.calendarWeekColumnHeader == "ddd M/D"
        assert data.enableColorImpairedMode == False
        assert data.firstDayOfWeek == 0
        assert data.id == 1
        assert data.longDateFormat == "dddd, MMMM D YYYY"
        assert data.movieInfoLanguage == 1
        assert data.movieRuntimeFormat == "hoursMinutes"
        assert data.shortDateFormat == "MMM D YYYY"
        assert data.showRelativeDates == True
        assert data.timeFormat == "h(:mm)a"


@pytest.mark.asyncio
async def test_async_get_custom_filters(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/customfilter",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/customfilter.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_custom_filters()

        assert data[0].id == 10
        assert data[0].type == "movieIndex"
        assert data[0].label == "Rated G"
        assert data[0].filters[0].key == "certification"
        assert data[0].filters[0].value == ["G"]
        assert data[0].filters[0].type == "equal"


@pytest.mark.asyncio
async def test_async_get_diskspace(aresponses):
    """Test getting diskspace."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/diskspace",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/diskspace.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_diskspace()

        assert data[0].freeSpace == 16187217043456
        assert data[0].label == "DrivePool"
        assert data[0].path == "D:\\"
        assert data[0].totalSpace == 56009755148288


@pytest.mark.asyncio
async def test_async_get_download_client(aresponses):
    """Test getting download client."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/downloadclient/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/downloadclient.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_download_clients(clientid=0)
        assert data.configContract == "string"
        assert data.enable == True
        assert data.fields[0].order == 0
        assert data.fields[0].name == "string"
        assert data.fields[0].label == "string"
        assert data.fields[0].helpText == "string"
        assert data.fields[0].value == "string"
        assert data.fields[0].type == "string"
        assert data.fields[0].advanced == True
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
        "/api/v3/health",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/health.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_failed_health_checks()

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
        "/api/v3/history/movie",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/history-movie.json"),
        ),
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
        assert data[0].quality.revision.isRepack == True
        assert data[0].customFormats[0].id == 0
        assert data[0].customFormats[0].name == "string"
        assert data[0].customFormats[0].includeCustomFormatWhenRenaming == True
        spec = data[0].customFormats[0].specifications[0]
        assert spec.name == "string"
        assert spec.implementation == "string"
        assert spec.implementationName == "string"
        assert spec.infoLink == "string"
        assert spec.negate == True
        assert spec.required == True
        assert spec.fields[0].order == 0
        assert spec.fields[0].name == "string"
        assert spec.fields[0].label == "string"
        assert spec.fields[0].helpText == "string"
        assert spec.fields[0].value == "string"
        assert spec.fields[0].type == "string"
        assert spec.fields[0].advanced == True
        assert data[0].qualityCutoffNotMet == True
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
        "/api/v3/importlist/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/importlist.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_import_lists(listid=0)

        assert data.enabled == True
        assert data.enableAuto == True
        assert data.shouldMonitor == True
        assert data.rootFolderPath == "string"
        assert data.qualityProfileId == 0
        assert data.searchOnAdd == True
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
        assert data.fields[0].advanced == True
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
        "/api/v3/indexer/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/indexer.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_indexers(indexerid=0)

        assert data.enableRss == True
        assert data.enableAutomaticSearch == True
        assert data.enableInteractiveSearch == True
        assert data.supportsRss == True
        assert data.supportsSearch == True
        assert data.protocol == "string"
        assert data.priority == 0
        assert data.name == "string"
        assert data.fields[0].order == 0
        assert data.fields[0].name == "string"
        assert data.fields[0].label == "string"
        assert data.fields[0].helpText == "string"
        assert data.fields[0].value == "string"
        assert data.fields[0].type == "string"
        assert data.fields[0].advanced == True
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
        "/api/v3/metadata",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/metadata.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_metadata_config()

        assert data[0].enable == True
        assert data[0].name == "string"
        assert data[0].fields[0].order == 0
        assert data[0].fields[0].name == "string"
        assert data[0].fields[0].label == "string"
        assert data[0].fields[0].helpText == "string"
        assert data[0].fields[0].value == "string"
        assert data[0].fields[0].type == "string"
        assert data[0].fields[0].advanced == True
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
        "/api/v3/movie/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/movie.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_movies(movieid=0)

        assert data[0].id == 0
        assert data[0].title == "string"
        assert data[0].originalTitle == "string"
        assert data[0].alternateTitles[0].sourceType == "tmdb"
        assert data[0].alternateTitles[0].movieId == 1
        assert data[0].alternateTitles[0].title == "string"
        assert data[0].alternateTitles[0].sourceId == 0
        assert data[0].alternateTitles[0].votes == 0
        assert data[0].alternateTitles[0].voteCount == 0
        assert data[0].alternateTitles[0].language.id == 1
        assert data[0].alternateTitles[0].language.name == "English"
        assert data[0].alternateTitles[0].id == 1
        assert data[0].sortTitle == "string"
        assert data[0].sizeOnDisk == 0
        assert data[0].overview == "string"
        assert data[0].inCinemas == "string"
        assert data[0].physicalRelease == "string"
        assert data[0].images[0].coverType == "poster"
        assert data[0].images[0].url == "string"
        assert data[0].images[0].remoteUrl == "string"
        assert data[0].website == "string"
        assert data[0].year == 0
        assert data[0].hasFile == True
        assert data[0].youTubeTrailerId == "string"
        assert data[0].studio == "string"
        assert data[0].path == "string"
        assert data[0].rootFolderPath == "string"
        assert data[0].qualityProfileId == 0
        assert data[0].monitored == True
        assert data[0].minimumAvailability == "announced"
        assert data[0].isAvailable == True
        assert data[0].folderName == "string"
        assert data[0].runtime == 0
        assert data[0].cleanTitle == "string"
        assert data[0].imdbId == "string"
        assert data[0].tmdbId == 0
        assert data[0].titleSlug == "string"
        assert data[0].certification == "string"
        assert data[0].genres == ["string"]
        assert data[0].tags == [0]
        assert data[0].added == "string"
        assert data[0].ratings.votes == 0
        assert data[0].ratings.value == 0
        assert data[0].movieFile.movieId == 0
        assert data[0].movieFile.relativePath == "string"
        assert data[0].movieFile.path == "string"
        assert data[0].movieFile.size == 916662234
        assert data[0].movieFile.dateAdded == "2020-11-26T02:00:35Z"
        assert data[0].movieFile.indexerFlags == 1
        assert data[0].movieFile.quality.quality.id == 14
        assert data[0].movieFile.quality.quality.name == "WEBRip-720p"
        assert data[0].movieFile.quality.quality.source == "webrip"
        assert data[0].movieFile.quality.quality.resolution == 720
        assert data[0].movieFile.quality.quality.modifier == "none"
        assert data[0].movieFile.quality.revision.version == 1
        assert data[0].movieFile.quality.revision.real == 0
        assert data[0].movieFile.quality.revision.isRepack == False
        assert data[0].movieFile.mediaInfo.audioBitrate == 0
        assert data[0].movieFile.mediaInfo.audioChannels == 2
        assert data[0].movieFile.mediaInfo.audioCodec == "AAC"
        assert data[0].movieFile.mediaInfo.audioLanguages == ""
        assert data[0].movieFile.mediaInfo.audioStreamCount == 1
        assert data[0].movieFile.mediaInfo.videoBitDepth == 8
        assert data[0].movieFile.mediaInfo.videoBitrate == 1000000
        assert data[0].movieFile.mediaInfo.videoCodec == "x264"
        assert data[0].movieFile.mediaInfo.videoFps == 25.000
        assert data[0].movieFile.mediaInfo.resolution == "1280x534"
        assert data[0].movieFile.mediaInfo.runTime == "1:49:06"
        assert data[0].movieFile.mediaInfo.scanType == "Progressive"
        assert data[0].movieFile.originalFilePath == "string"
        assert data[0].movieFile.qualityCutoffNotMet == True
        assert data[0].movieFile.languages[0].id == 26
        assert data[0].movieFile.languages[0].name == "Hindi"
        assert data[0].movieFile.edition == ""
        assert data[0].movieFile.id == 35361
        assert data[0].collection.name == "string"
        assert data[0].collection.tmdbId == 0
        assert data[0].collection.images[0].coverType == "poster"
        assert data[0].collection.images[0].url == "string"
        assert data[0].collection.images[0].remoteUrl == "string"
        assert data[0].status == "deleted"


@pytest.mark.asyncio
async def test_async_get_movie_file(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/moviefile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/moviefile.json"),
        ),
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
        assert data.quality.revision.isRepack == True
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
        assert data.qualityCutoffNotMet == True
        assert data.languages[0].id == 0
        assert data.languages[0].name == "string"
        assert data.releaseGroup == "string"
        assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_notification(aresponses):
    """Test getting movie file attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/notification/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/notification.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_notifications(notifyid=0)

        assert data.onGrab == True
        assert data.onDownload == True
        assert data.onUpgrade == True
        assert data.onRename == True
        assert data.onDelete == True
        assert data.onHealthIssue == True
        assert data.supportsOnGrab == True
        assert data.supportsOnDownload == True
        assert data.supportsOnUpgrade == True
        assert data.supportsOnRename == True
        assert data.supportsOnDelete == True
        assert data.supportsOnHealthIssue == True
        assert data.includeHealthWarnings == True
        assert data.name == "string"
        assert data.fields[0].order == 0
        assert data.fields[0].name == "string"
        assert data.fields[0].label == "string"
        assert data.fields[0].helpText == "string"
        assert data.fields[0].value == "string"
        assert data.fields[0].type == "string"
        assert data.fields[0].advanced == True
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
        "/api/v3/qualityProfile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/qualityProfile.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_quality_profiles()

        assert data[0].name == "Any"
        assert data[0].upgradeAllowed == True
        assert data[0].cutoff == 20
        assert data[0].items[0].quality.id == 0
        assert data[0].items[0].quality.name == "Unknown"
        assert data[0].items[0].quality.source == "unknown"
        assert data[0].items[0].quality.resolution == 0
        assert data[0].items[0].quality.modifier == "none"
        assert data[0].items[0].items == []
        assert data[0].items[0].allowed == False
        assert data[0].items[1].name == "WEB 480p"
        assert data[0].items[1].items[0].quality.id == 12
        assert data[0].items[1].items[0].quality.name == "WEBRip-480p"
        assert data[0].items[1].items[0].quality.source == "webrip"
        assert data[0].items[1].items[0].quality.resolution == 480
        assert data[0].items[1].items[0].quality.modifier == "none"
        assert data[0].items[1].items[0].items == []
        assert data[0].items[1].items[0].allowed == True
        assert data[0].items[1].allowed == True
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
        "/api/v3/queue/details",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue-details.json"),
        ),
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
        assert data[0].quality.revision.isRepack == True
        assert data[0].customFormats[0].id == 0
        assert data[0].customFormats[0].name == "string"
        assert data[0].customFormats[0].includeCustomFormatWhenRenaming == True
        assert data[0].customFormats[0].specifications[0].name == "string"
        assert data[0].customFormats[0].specifications[0].implementation == "string"
        assert data[0].customFormats[0].specifications[0].implementationName == "string"
        assert data[0].customFormats[0].specifications[0].infoLink == "string"
        assert data[0].customFormats[0].specifications[0].negate == True
        assert data[0].customFormats[0].specifications[0].required == True
        assert data[0].customFormats[0].specifications[0].fields[0].order == 0
        assert data[0].customFormats[0].specifications[0].fields[0].name == "string"
        assert data[0].customFormats[0].specifications[0].fields[0].label == "string"
        assert data[0].customFormats[0].specifications[0].fields[0].helpText == "string"
        assert data[0].customFormats[0].specifications[0].fields[0].value == "string"
        assert data[0].customFormats[0].specifications[0].fields[0].type == "string"
        assert data[0].customFormats[0].specifications[0].fields[0].advanced == True
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
        "/api/v3/queue/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/queue-status.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue_status()

        assert data.totalCount == 0
        assert data.count == 0
        assert data.unknownCount == 0
        assert data.errors == True
        assert data.warnings == True
        assert data.unknownErrors == True
        assert data.unknownWarnings == True


@pytest.mark.asyncio
async def test_async_get_remote_path_mappings(aresponses):
    """Test getting remote path mappings."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/remotePathMapping",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/remotePathMapping.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_remote_path_mappings()

        assert data[0].host == "localhost"
        assert data[0].remotePath == "C:\\"
        assert data[0].localPath == "A:\\Movies\\"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_root_folders(aresponses):
    """Test getting root folders."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/rootfolder",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/rootfolder.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_root_folders()

        assert data[0].path == "C:\\Downloads\\Movies"
        assert data[0].freeSpace == 282500063232
        assert data[0].unmappedFolders[0].name == "string"
        assert data[0].unmappedFolders[0].path == "path"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_system_status(aresponses):
    """Test getting system status."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/system-status.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_system_status()

        assert data.appData == "C:\\ProgramData\\Radarr"
        assert data.authentication == True
        assert data.branch == "nightly"
        assert data.buildTime == "2020-09-01T23:23:23.9621974Z"
        assert data.isAdmin == False
        assert data.isDebug == True
        assert data.isDocker == False
        assert data.isLinux == False
        assert data.isMono == False
        assert data.isNetCore == True
        assert data.isOsx == False
        assert data.isProduction == False
        assert data.isUserInteractive == True
        assert data.isWindows == True
        assert data.migrationVersion == 180
        assert data.mode == "console"
        assert data.osName == "Windows"
        assert data.osVersion == "10.0.18363.0"
        assert data.packageUpdateMechanism == "builtIn"
        assert data.runtimeName == "netCore"
        assert data.runtimeVersion == "3.1.10"
        assert data.sqliteVersion == "3.32.1"
        assert data.startTime == "2020-09-01T23:50:20.2415965Z"
        assert data.startupPath == "C:\\ProgramData\\Radarr"
        assert data.urlBase == ""
        assert data.version == "10.0.0.34882"


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/tag/detail/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/tag-detail.json"),
        ),
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
        "/api/v3/update",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/update.json"),
        ),
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_software_update_info()

        assert data.version == "3.0.0.3553"
        assert data.branch == "nightly"
        assert data.releaseDate == "2020-09-02T05:36:13.047313Z"
        assert data.fileName == "Radarr.nightly.3.0.0.3553.windows-core-x64.zip"
        assert data.url == "string"
        assert data.installed == False
        assert data.installed == False
        assert data.latest == False
        assert data.changes.new == []
        assert data.changes.fixed == ["string"]
        assert data.hash == "abc123"
