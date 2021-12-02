"""Tests for Soanrr object models."""
import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient

from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/calendar",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/calendar.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_calendar()

        assert data[0].seriesId == 3
        assert data[0].episodeFileId == 0
        assert data[0].seasonNumber == 4
        assert data[0].episodeNumber == 11
        assert data[0].title == "string"
        assert data[0].airDate == "2017-01-26"
        assert data[0].airDateUtc == "2017-01-27T01:30:00Z"
        assert data[0].overview == "string"
        assert data[0].hasFile == False
        assert data[0].monitored == True
        assert data[0].sceneEpisodeNumber == 0
        assert data[0].sceneSeasonNumber == 0
        assert data[0].tvDbEpisodeId == 0
        assert data[0].series.tvdbId == 0
        assert data[0].series.tvRageId == 0
        assert data[0].series.imdbId == "string"
        assert data[0].series.cleanTitle == "string"
        assert data[0].series.status == "continuing"
        assert data[0].series.overview == "string"
        assert data[0].series.airTime == "5:30pm"
        assert data[0].series.monitored == True
        assert data[0].series.qualityProfileId == 1
        assert data[0].series.seasonFolder == True
        assert data[0].series.lastInfoSync == "2017-01-26T19:25:55.4555946Z"
        assert data[0].series.runtime == 30
        assert data[0].series.images[0].coverType == "banner"
        assert data[0].series.images[0].url == "string"
        assert data[0].series.seriesType == "standard"
        assert data[0].series.network == "string"
        assert data[0].series.useSceneNumbering == False
        assert data[0].series.titleSlug == "string"
        assert data[0].series.path == "string"
        assert data[0].series.year == 0
        assert data[0].series.firstAired == "2016-01-10T01:30:00Z"
        assert data[0].series.qualityProfile.value.name == "SD"
        assert data[0].series.qualityProfile.value.id == 1
        assert data[0].series.qualityProfile.value.allowed[0].id == 1
        assert data[0].series.qualityProfile.value.allowed[0].name == "SDTV"
        assert data[0].series.qualityProfile.value.allowed[0].weight == 1
        assert data[0].series.qualityProfile.value.cutoff.id == 1
        assert data[0].series.qualityProfile.value.cutoff.name == "SDTV"
        assert data[0].series.qualityProfile.value.cutoff.weight == 1
        assert data[0].series.qualityProfile.isLoaded == True
        assert data[0].series.seasons[0].seasonNumber == 0
        assert data[0].series.seasons[0].monitored == False
        assert data[0].series.id == 66
        assert data[0].downloading == False
        assert data[0].id == 14402


@pytest.mark.asyncio
async def test_async_get_commands(aresponses):
    """Test getting commands."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/command/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/command.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_commands(cmdid=0)

        assert data.name == "RescanSeries"
        assert data.startedOn == "0001-01-01T00:00:00Z"
        assert data.stateChangeTime == "2014-02-05T05:09:09.2366139Z"
        assert data.sendUpdatesToClient == True
        assert data.state == "pending"
        assert data.id == 24


@pytest.mark.asyncio
async def test_async_get_diskspace(aresponses):
    """Test getting diskspace."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/diskspace",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/diskspace.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_diskspace()

        assert data[0].path == "C:\\"
        assert data[0].label == ""
        assert data[0].freeSpace == 282500067328
        assert data[0].totalSpace == 499738734592


@pytest.mark.asyncio
async def test_async_get_episode_by_id(aresponses):
    """Test getting episode by ID."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/episode/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episode.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_episode_by_id(episodeid=1)

        assert data.seriesId == 1
        assert data.episodeFileId == 0
        assert data.seasonNumber == 1
        assert data.episodeNumber == 1
        assert data.title == "string"
        assert data.airDate == "2009-09-17"
        assert data.airDateUtc == "2009-09-18T02:00:00Z"
        assert data.overview == "string"
        assert data.episodeFile.seriesId == 1
        assert data.episodeFile.seasonNumber == 1
        assert data.episodeFile.relativePath == "string"
        assert data.episodeFile.path == "string"
        assert data.episodeFile.size == 50
        assert data.episodeFile.dateAdded == "2019-06-13T09:08:03.775081Z"
        assert data.episodeFile.sceneName == "string"
        assert data.episodeFile.releaseGroup == "string"
        assert data.episodeFile.language.id == 1
        assert data.episodeFile.language.name == "English"
        assert data.episodeFile.quality.quality.id == 4
        assert data.episodeFile.quality.quality.name == "HDTV-720p"
        assert data.episodeFile.quality.quality.source == "television"
        assert data.episodeFile.quality.quality.resolution == 720
        assert data.episodeFile.quality.revision.version == 1
        assert data.episodeFile.quality.revision.real == 0
        assert data.episodeFile.quality.revision.isRepack == False
        assert data.episodeFile.mediaInfo.audioBitrate == 384000
        assert data.episodeFile.mediaInfo.audioChannels == 5.1
        assert data.episodeFile.mediaInfo.audioCodec == "AC3"
        assert data.episodeFile.mediaInfo.audioLanguages == "English"
        assert data.episodeFile.mediaInfo.audioStreamCount == 1
        assert data.episodeFile.mediaInfo.videoBitDepth == 8
        assert data.episodeFile.mediaInfo.videoBitrate == 3055382
        assert data.episodeFile.mediaInfo.videoCodec == "x264"
        assert data.episodeFile.mediaInfo.videoFps == 23.976
        assert data.episodeFile.mediaInfo.resolution == "1280x714"
        assert data.episodeFile.mediaInfo.runTime == "22:01"
        assert data.episodeFile.mediaInfo.scanType == "Progressive"
        assert data.episodeFile.mediaInfo.subtitles == "English"
        assert data.episodeFile.qualityCutoffNotMet == False
        assert data.episodeFile.languageCutoffNotMet == False
        assert data.episodeFile.id == 18429
        assert data.hasFile == True
        assert data.monitored == True
        assert data.absoluteEpisodeNumber == 3
        assert data.unverifiedSceneNumbering == False
        assert data.series.title == "string"
        assert data.series.sortTitle == "string"
        assert data.series.status == "ended"
        assert data.series.ended == True
        assert data.series.overview == "string"
        assert data.series.network == "string"
        assert data.series.airTime == "22:00"
        assert data.series.seasons[0].seasonNumber == 0
        assert data.series.seasons[0].monitored == False
        assert data.series.year == 2017
        assert data.series.path == "string"
        assert data.series.qualityProfileId == 6
        assert data.series.languageProfileId == 1
        assert data.series.seasonFolder == True
        assert data.series.monitored == True
        assert data.series.useSceneNumbering == False
        assert data.series.runtime == 21
        assert data.series.tvdbId == 0
        assert data.series.tvRageId == 0
        assert data.series.tvMazeId == 0
        assert data.series.firstAired == "2017-04-05T00:00:00Z"
        assert data.series.seriesType == "standard"
        assert data.series.cleanTitle == "string"
        assert data.series.imdbId == "string"
        assert data.series.titleSlug == "string"
        assert data.series.certification == "TV-MA"
        assert data.series.genres == ["Comedy"]
        assert data.series.tags == []
        assert data.series.added == "2019-05-19T05:33:42.24392Z"
        assert data.series.ratings.votes == 80
        assert data.series.ratings.value == 8.7
        assert data.series.id == 15
        assert data.series.images[0].coverType == "banner"
        assert data.series.images[0].url == "string"
        assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_episode_files(aresponses):
    """Test getting episode files."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/episodefile/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episodefile.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_episode_files(1, 1)

        assert data.seriesId == 1
        assert data.seasonNumber == 1
        assert data.path == "string"
        assert data.size == 0
        assert data.dateAdded == "2013-05-29T10:42:05.1335301Z"
        assert data.sceneName == ""
        assert data.quality.quality.id == 1
        assert data.quality.quality.name == "Bluray 720p"
        assert data.quality.quality.allowed == []
        assert data.quality.proper == False
        assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/history",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/history.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_history()

        assert data.page == 1
        assert data.pageSize == 10
        assert data.sortKey == "date"
        assert data.sortDirection == "descending"
        assert data.totalRecords == 8094
        assert data.records[0].episodeId == 75118
        assert data.records[0].seriesId == 22
        assert data.records[0].sourceTitle == "string"
        assert data.records[0].language.id == 1
        assert data.records[0].language.name == "English"
        assert data.records[0].language.allowed == []
        assert data.records[0].quality.quality.id == 5
        assert data.records[0].quality.quality.name == "WEBDL-720p"
        assert data.records[0].quality.quality.source == "web"
        assert data.records[0].quality.quality.resolution == 720
        assert data.records[0].quality.revision.version == 1
        assert data.records[0].quality.revision.real == 0
        assert data.records[0].quality.revision.isRepack == False
        assert data.records[0].qualityCutoffNotMet == True
        assert data.records[0].languageCutoffNotMet == False
        assert data.records[0].languageCutoffNotMet == False
        assert data.records[0].date == "2019-11-01T09:09:34.288036Z"
        assert data.records[0].downloadId == "string"
        assert data.records[0].eventType == "downloadFolderImported"
        assert data.records[0].data.indexer == "string"
        assert data.records[0].data.nzbInfoUrl == "string"
        assert data.records[0].data.releaseGroup == "string"
        assert data.records[0].data.age == 0
        assert data.records[0].data.ageHours == 0.0
        assert data.records[0].data.ageMinutes == 0.0
        assert data.records[0].data.publishedDate == "string"
        assert data.records[0].data.fileId == 53153
        assert data.records[0].data.droppedPath == "string"
        assert data.records[0].data.importedPath == "string"
        assert data.records[0].data.downloadClient == "string"
        assert data.records[0].data.downloadClientName == "string"
        assert data.records[0].data.preferredWordScore == 0
        assert data.records[0].data.size == 184576954
        assert data.records[0].data.downloadUrl == "string"
        assert data.records[0].data.guid == "string"
        assert data.records[0].data.tvdbId == 0
        assert data.records[0].data.tvRageId == 0
        assert data.records[0].data.protocol == 2
        assert data.records[0].data.torrentInfoHash == "string"
        assert data.records[0].id == 76400


@pytest.mark.asyncio
async def test_async_get_logs(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/log",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/logs.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_logs()

        assert data.page == 1
        assert data.pageSize == 10
        assert data.sortKey == "logger"
        assert data.sortDirection == "default"
        assert data.totalRecords == 74433
        assert data.records[0].time == "2021-11-19T09:28:26.549994Z"
        assert data.records[0].level == "info"
        assert data.records[0].logger == "BackupService"
        assert data.records[0].message == "Starting Backup"
        assert data.records[0].id == 3920809


@pytest.mark.asyncio
async def test_async_parse_title_or_path(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/parse",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/parse.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_parse_title_or_path(
            title="Series.Title.S01E01.720p.HDTV-Sonarr"
        )

        assert data.title == "Series.Title.S01E01.720p.HDTV-Sonarr"
        assert (
            data.parsedEpisodeInfo.releaseTitle
            == "Series.Title.S01E01.720p.HDTV-Sonarr"
        )
        assert data.parsedEpisodeInfo.seriesTitle == "Series Title"
        assert data.parsedEpisodeInfo.seriesTitleInfo.title == "Series Title"
        assert data.parsedEpisodeInfo.seriesTitleInfo.titleWithoutYear == "Series Title"
        assert data.parsedEpisodeInfo.seriesTitleInfo.year == 0
        assert data.parsedEpisodeInfo.quality.quality.id == 4
        assert data.parsedEpisodeInfo.quality.quality.name == "HDTV-720p"
        assert data.parsedEpisodeInfo.quality.revision.version == 1
        assert data.parsedEpisodeInfo.quality.revision.real == 0
        assert data.parsedEpisodeInfo.seasonNumber == 1
        assert data.parsedEpisodeInfo.episodeNumbers == [1]
        assert data.parsedEpisodeInfo.absoluteEpisodeNumbers == []
        assert data.parsedEpisodeInfo.language == "english"
        assert data.parsedEpisodeInfo.fullSeason == False
        assert data.parsedEpisodeInfo.special == False
        assert data.parsedEpisodeInfo.releaseGroup == "Sonarr"
        assert data.parsedEpisodeInfo.releaseHash == ""
        assert data.parsedEpisodeInfo.isDaily == False
        assert data.parsedEpisodeInfo.isAbsoluteNumbering == False
        assert data.parsedEpisodeInfo.isPossibleSpecialEpisode == False
        assert data.series == {}
        assert data.episodes == []


@pytest.mark.asyncio
async def test_async_get_profiles(aresponses):
    """Test getting profiles."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/profile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/profile.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_profiles()

        assert data[0].name == "SD"
        assert data[0].cutoff.id == 1
        assert data[0].cutoff.name == "SDTV"
        assert data[0].items[0].quality.id == 1
        assert data[0].items[0].quality.name == "SDTV"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/queue",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/queue.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue()

        assert data[0].series.title == "string"
        assert data[0].series.sortTitle == "string"
        assert data[0].series.seasonCount == 2
        assert data[0].series.status == "continuing"
        assert data[0].series.overview == "string"
        assert data[0].series.network == "string"
        assert data[0].series.airTime == "21:00"
        assert data[0].series.images[0].coverType == "fanart"
        assert data[0].series.images[0].url == "string"
        assert data[0].series.seasons[0].seasonNumber == 0
        assert data[0].series.seasons[0].monitored == False
        assert data[0].series.year == 2015
        assert data[0].series.path == "string"
        assert data[0].series.profileId == 5
        assert data[0].series.seasonFolder == True
        assert data[0].series.monitored == True
        assert data[0].series.useSceneNumbering == False
        assert data[0].series.runtime == 60
        assert data[0].series.tvdbId == 0
        assert data[0].series.tvRageId == 0
        assert data[0].series.tvMazeId == 0
        assert data[0].series.firstAired == "2016-04-16T23:00:00Z"
        assert data[0].series.lastInfoSync == "2017-02-05T16:40:11.614176Z"
        assert data[0].series.seriesType == "standard"
        assert data[0].series.cleanTitle == "string"
        assert data[0].series.imdbId == "string"
        assert data[0].series.titleSlug == "string"
        assert data[0].series.certification == "TV-MA"
        assert data[0].series.genres == ["Adventure", "Drama", "Fantasy"]
        assert data[0].series.tags == []
        assert data[0].series.added == "2015-12-28T13:44:24.204583Z"
        assert data[0].series.ratings.votes == 1128
        assert data[0].series.ratings.value == 9.4
        assert data[0].series.qualityProfileId == 5
        assert data[0].series.id == 17
        assert data[0].episode.seriesId == 17
        assert data[0].episode.episodeFileId == 0
        assert data[0].episode.seasonNumber == 3
        assert data[0].episode.episodeNumber == 8
        assert data[0].episode.title == "string"
        assert data[0].episode.airDate == "2013-05-19"
        assert data[0].episode.airDateUtc == "2013-05-20T01:00:00Z"
        assert data[0].episode.overview == "string"
        assert data[0].episode.hasFile == False
        assert data[0].episode.monitored == False
        assert data[0].episode.absoluteEpisodeNumber == 28
        assert data[0].episode.unverifiedSceneNumbering == False
        assert data[0].episode.id == 889
        assert data[0].quality.quality.id == 7
        assert data[0].quality.quality.name == "Bluray-1080p"
        assert data[0].quality.revision.version == 1
        assert data[0].quality.revision.real == 0
        assert data[0].size == 4472186820
        assert data[0].title == "string"
        assert data[0].sizeleft == 0
        assert data[0].timeleft == "00:00:00"
        assert data[0].estimatedCompletionTime == "2016-02-05T22:46:52.440104Z"
        assert data[0].status == "Downloading"
        assert data[0].trackedDownloadStatus == "Ok"
        assert data[0].statusMessages == []
        assert data[0].downloadId == "string"
        assert data[0].protocol == "string"
        assert data[0].id == 1503378561


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
    """Test getting release."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/release",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/release.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_release(releaseid=0)

        assert data[0].guid == "string"
        assert data[0].quality.quality.id == 4
        assert data[0].quality.quality.name == "HDTV-720p"
        assert data[0].quality.proper == False
        assert data[0].age == 0
        assert data[0].size == 0
        assert data[0].indexerId == 5
        assert data[0].indexer == "string"
        assert data[0].releaseGroup == "string"
        assert data[0].title == "string"
        assert data[0].fullSeason == False
        assert data[0].sceneSource == False
        assert data[0].seasonNumber == 3
        assert data[0].language == "english"
        assert data[0].seriesTitle == "string"
        assert data[0].episodeNumbers == [1]
        assert data[0].approved == False
        assert data[0].tvRageId == 0
        assert data[0].rejections == ["Unknown Series"]
        assert data[0].publishDate == "2017-02-10T00:00:00Z"
        assert data[0].downloadUrl == "string"
        assert data[0].downloadAllowed == True


@pytest.mark.asyncio
async def test_async_get_root_folders(aresponses):
    """Test getting root folders."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/rootfolder",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/rootfolder.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_root_folders()

        assert data[0].path == "C:\\Downloads\\TV"
        assert data[0].freeSpace == 282500063232
        assert data[0].unmappedFolders == []
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_series_lookup(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/series/lookup",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series-lookup.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_series_lookup()

        assert data[0].title == "string"
        assert data[0].sortTitle == "string"
        assert data[0].seasonCount == 4
        assert data[0].status == "continuing"
        assert data[0].overview == "string"
        assert data[0].network == "string"
        assert data[0].airTime == "21:00"
        assert data[0].images[0].coverType == "fanart"
        assert data[0].images[0].url == "string"
        assert data[0].remotePoster == "string"
        assert data[0].seasons[0].seasonNumber == 0
        assert data[0].seasons[0].monitored == False
        assert data[0].year == 2013
        assert data[0].profileId == 0
        assert data[0].seasonFolder == False
        assert data[0].monitored == False
        assert data[0].useSceneNumbering == False
        assert data[0].runtime == 45
        assert data[0].tvdbId == 0
        assert data[0].tvRageId == 0
        assert data[0].firstAired == "2013-09-23T05:00:00Z"
        assert data[0].seriesType == "string"
        assert data[0].cleanTitle == "string"
        assert data[0].imdbId == "string"
        assert data[0].titleSlug == "string"
        assert data[0].certification == "TV-14"
        assert data[0].genres == ["Action", "Crime", "Drama", "Mystery"]
        assert data[0].tags == []
        assert data[0].added == "0001-01-01T00:00:00Z"
        assert data[0].ratings.votes == 182
        assert data[0].ratings.value == 8.6
        assert data[0].qualityProfileId == 0


@pytest.mark.asyncio
async def test_async_get_series(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/series/3",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_series(seriesid=3)

        assert data.title == "string"
        assert data.alternateTitles[0].title == "string"
        assert data.alternateTitles[0].seasonNumber == -1
        assert data.sortTitle == "string"
        assert data.seasonCount == 2
        assert data.totalEpisodeCount == 17
        assert data.episodeCount == 8
        assert data.episodeFileCount == 8
        assert data.sizeOnDisk == 0
        assert data.status == "continuing"
        assert data.overview == "string"
        assert data.previousAiring == "2019-04-29T01:00:00Z"
        assert data.network == "string"
        assert data.airTime == "21:00"
        assert data.images[0].coverType == "fanart"
        assert data.images[0].url == "string"
        assert data.seasons[0].seasonNumber == 0
        assert data.seasons[0].monitored == False
        assert data.seasons[0].statistics.previousAiring == "2019-04-29T01:00:00Z"
        assert data.seasons[0].statistics.episodeFileCount == 0
        assert data.seasons[0].statistics.episodeCount == 0
        assert data.seasons[0].statistics.totalEpisodeCount == 1
        assert data.seasons[0].statistics.sizeOnDisk == 0
        assert data.seasons[0].statistics.percentOfEpisodes == 0.0
        assert data.year == 2017
        assert data.path == "string"
        assert data.profileId == 6
        assert data.seasonFolder == True
        assert data.monitored == True
        assert data.useSceneNumbering == False
        assert data.runtime == 60
        assert data.tvdbId == 0
        assert data.tvRageId == 0
        assert data.tvMazeId == 0
        assert data.firstAired == "2019-04-29T23:00:00Z"
        assert data.lastInfoSync == "2019-12-01T17:35:41.103443Z"
        assert data.seriesType == "standard"
        assert data.cleanTitle == "string"
        assert data.imdbId == "string"
        assert data.titleSlug == "string"
        assert data.certification == "TV-MA"
        assert data.genres == ["Action", "Adventure", "Fantasy", "Suspense"]
        assert data.tags == []
        assert data.added == "2019-09-13T15:50:29.325136Z"
        assert data.ratings.votes == 0
        assert data.ratings.value == 0.0
        assert data.qualityProfileId == 6
        assert data.id == 3


@pytest.mark.asyncio
async def test_async_get_system_backup(aresponses):
    """Test getting system backup info."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/system/backup",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/system-backup.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_system_backup()

        assert data[0].name == "nzbdrone_backup_2017.08.17_22.00.00.zip"
        assert data[0].path == "/backup/update/nzbdrone_backup_2017.08.17_22.00.00.zip"
        assert data[0].type == "update"
        assert data[0].time == "2017-08-18T05:00:37Z"
        assert data[0].id == 1207435784


@pytest.mark.asyncio
async def test_async_get_system_status(aresponses):
    """Test getting system status info."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/system-status.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_system_status()

        assert data.version == "2.0.0.1121"
        assert data.buildTime == "2014-02-08T20:49:36.5560392Z"
        assert data.isDebug == False
        assert data.isProduction == True
        assert data.isAdmin == True
        assert data.isUserInteractive == False
        assert data.startupPath == "C:\\ProgramData\\NzbDrone\\bin"
        assert data.appData == "C:\\ProgramData\\NzbDrone"
        assert data.osVersion == "6.2.9200.0"
        assert data.isMono == False
        assert data.isLinux == False
        assert data.isWindows == True
        assert data.branch == "develop"
        assert data.authentication == False
        assert data.startOfWeek == 0
        assert data.urlBase == ""


@pytest.mark.asyncio
async def test_async_get_tags(aresponses):
    """Test getting tags."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/tag/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/tag.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_tags(tagid=1)

        assert data.label == "amzn"
        assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses):
    """Test getting wanted."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/wanted/missing",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/wantedmissing.json"),
        ),
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_wanted()

        assert data.page == 1
        assert data.pageSize == 15
        assert data.sortKey == "airDateUtc"
        assert data.sortDirection == "descending"
        assert data.totalRecords == 2
        assert data.records[0].seriesId == 1
        assert data.records[0].episodeFileId == 0
        assert data.records[0].seasonNumber == 5
        assert data.records[0].episodeNumber == 4
        assert data.records[0].title == "string"
        assert data.records[0].airDate == "2014-02-03"
        assert data.records[0].airDateUtc == "2014-02-04T03:00:00Z"
        assert data.records[0].overview == "string"
        assert data.records[0].hasFile == False
        assert data.records[0].monitored == True
        assert data.records[0].sceneEpisodeNumber == 0
        assert data.records[0].sceneSeasonNumber == 0
        assert data.records[0].tvDbEpisodeId == 0
        assert data.records[0].absoluteEpisodeNumber == 50
        assert data.records[0].series.tvdbId == 0
        assert data.records[0].series.tvRageId == 0
        assert data.records[0].series.imdbId == "string"
        assert data.records[0].series.title == "string"
        assert data.records[0].series.cleanTitle == "string"
        assert data.records[0].series.status == "continuing"
        assert data.records[0].series.overview == "string"
        assert data.records[0].series.airTime == "7:00pm"
        assert data.records[0].series.monitored == True
        assert data.records[0].series.qualityProfileId == 1
        assert data.records[0].series.seasonFolder == True
        assert data.records[0].series.lastInfoSync == "2014-02-05T04:39:28.550495Z"
        assert data.records[0].series.runtime == 30
        assert data.records[0].series.images[0].coverType == "banner"
        assert data.records[0].series.images[0].url == "string"
        assert data.records[0].series.seriesType == "standard"
        assert data.records[0].series.network == "string"
        assert data.records[0].series.useSceneNumbering == False
        assert data.records[0].series.titleSlug == "string"
        assert data.records[0].series.path == "string"
        assert data.records[0].series.year == 2009
        assert data.records[0].series.firstAired == "2012-09-18T02:00:00Z"
        assert data.records[0].series.qualityProfile.value.name == "SD"
        assert data.records[0].series.qualityProfile.value.cutoff.id == 1
        assert data.records[0].series.qualityProfile.value.cutoff.name == "SDTV"
        quality = data.records[0].series.qualityProfile.value.items[0].quality
        assert quality.id == 1
        assert quality.name == "SDTV"
        assert data.records[0].series.qualityProfile.value.items[0].allowed == True
        assert data.records[0].series.qualityProfile.value.id == 1
        assert data.records[0].series.qualityProfile.isLoaded == True
        assert data.records[0].series.seasons[0].seasonNumber == 5
        assert data.records[0].series.seasons[0].monitored == True
        assert data.records[0].series.id == 1
        assert data.records[0].downloading == False
        assert data.records[0].id == 55
