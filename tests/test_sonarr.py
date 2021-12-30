"""Tests for Sonarr object models."""
from datetime import datetime
from aiopyarr.models.common import SystemBackup
from aiopyarr.models.sonarr import (
    SonarrQualityProfile,
    SonarrQueue,
    SonarrSeriesLookup,
)
import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient

from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/calendar.json"),
        ),
        match_querystring=True,
    )
    start = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    end = datetime.strptime("Dec 1 2020  1:33PM", "%b %d %Y %I:%M%p")
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_calendar(start_date=start, end_date=end)

        assert data[0].seriesId == 3
        assert data[0].episodeFileId == 0
        assert data[0].seasonNumber == 4
        assert data[0].episodeNumber == 11
        assert data[0].title == "string"
        assert data[0].airDate == datetime(2017, 1, 26, 0, 0)
        assert data[0].airDateUtc == datetime(2017, 1, 27, 1, 30)
        assert data[0].overview == "string"
        assert data[0].hasFile is False
        assert data[0].monitored is True
        assert data[0].sceneEpisodeNumber == 0
        assert data[0].sceneSeasonNumber == 0
        assert data[0].tvDbEpisodeId == 0
        assert data[0].unverifiedSceneNumbering is False
        assert data[0].series.tvdbId == 0
        assert data[0].series.tvRageId == 0
        assert data[0].series.imdbId == "string"
        assert data[0].series.cleanTitle == "string"
        assert data[0].series.status == "continuing"
        assert data[0].series.overview == "string"
        assert data[0].series.airTime == "5:30pm"
        assert data[0].series.monitored is True
        assert data[0].series.qualityProfileId == 1
        assert data[0].series.seasonFolder is True
        assert data[0].series.lastInfoSync == datetime(2017, 1, 26, 19, 25, 55, 455594)
        assert data[0].series.runtime == 30
        assert data[0].series.images[0].coverType == "banner"
        assert data[0].series.images[0].url == "string"
        assert data[0].series.seriesType == "standard"
        assert data[0].series.network == "string"
        assert data[0].series.useSceneNumbering is False
        assert data[0].series.titleSlug == "string"
        assert data[0].series.path == "string"
        assert data[0].series.year == 0
        assert data[0].series.firstAired == datetime(2016, 1, 10, 1, 30)
        assert data[0].series.qualityProfile.value.name == "SD"
        assert data[0].series.qualityProfile.value.id == 1
        assert data[0].series.qualityProfile.value.allowed[0].id == 1
        assert data[0].series.qualityProfile.value.allowed[0].name == "SDTV"
        assert data[0].series.qualityProfile.value.allowed[0].weight == 1
        assert data[0].series.qualityProfile.value.cutoff.id == 1
        assert data[0].series.qualityProfile.value.cutoff.name == "SDTV"
        assert data[0].series.qualityProfile.value.cutoff.weight == 1
        assert data[0].series.qualityProfile.isLoaded is True
        assert data[0].series.seasons[0].seasonNumber == 0
        assert data[0].series.seasons[0].monitored is False
        assert data[0].series.id == 66
        assert data[0].downloading is False
        assert data[0].id == 14402


@pytest.mark.asyncio
async def test_async_get_episode_by_id(aresponses):
    """Test getting episode by ID."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/episode/1?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episode.json"),
        ),
        match_querystring=True,
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
        assert data.airDate == datetime(2009, 9, 17, 0, 0)
        assert data.airDateUtc == datetime(2009, 9, 18, 2, 0)
        assert data.overview == "string"
        assert data.episodeFile.seriesId == 1
        assert data.episodeFile.seasonNumber == 1
        assert data.episodeFile.relativePath == "string"
        assert data.episodeFile.path == "string"
        assert data.episodeFile.size == 50
        assert data.episodeFile.dateAdded == datetime(2019, 6, 13, 9, 8, 3, 775081)
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
        assert data.episodeFile.quality.revision.isRepack is False
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
        assert data.episodeFile.qualityCutoffNotMet is False
        assert data.episodeFile.languageCutoffNotMet is False
        assert data.episodeFile.id == 18429
        assert data.hasFile is True
        assert data.monitored is True
        assert data.absoluteEpisodeNumber == 3
        assert data.unverifiedSceneNumbering is False
        assert data.series.title == "string"
        assert data.series.sortTitle == "string"
        assert data.series.status == "ended"
        assert data.series.ended is True
        assert data.series.overview == "string"
        assert data.series.network == "string"
        assert data.series.airTime == "22:00"
        assert data.series.seasons[0].seasonNumber == 0
        assert data.series.seasons[0].monitored is False
        assert data.series.year == 2017
        assert data.series.path == "string"
        assert data.series.qualityProfileId == 6
        assert data.series.languageProfileId == 1
        assert data.series.seasonFolder is True
        assert data.series.monitored is True
        assert data.series.useSceneNumbering is False
        assert data.series.runtime == 21
        assert data.series.tvdbId == 0
        assert data.series.tvRageId == 0
        assert data.series.tvMazeId == 0
        assert data.series.firstAired == datetime(2017, 4, 5, 0, 0)
        assert data.series.seriesType == "standard"
        assert data.series.cleanTitle == "string"
        assert data.series.imdbId == "string"
        assert data.series.titleSlug == "string"
        assert data.series.certification == "TV-MA"
        assert data.series.genres == ["Comedy"]
        assert data.series.tags == []
        assert data.series.added == datetime(2019, 5, 19, 5, 33, 42, 243920)
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
        "/api/v3/episodefile/1?apikey=ur1234567-0abc12de3f456gh7ij89k012&seriesId=1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episodefile.json"),
        ),
        match_querystring=True,
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
        assert data.dateAdded == datetime(2013, 5, 29, 10, 42, 5, 133530)
        assert data.sceneName == ""
        assert data.quality.quality.id == 1
        assert data.quality.quality.name == "Bluray 720p"
        assert data.quality.quality.allowed == []
        assert data.quality.proper is False
        assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/history?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortDir=desc&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/history.json"),
        ),
        match_querystring=True,
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
        assert data.records[0].quality.revision.isRepack is False
        assert data.records[0].qualityCutoffNotMet is True
        assert data.records[0].languageCutoffNotMet is False
        assert data.records[0].languageCutoffNotMet is False
        assert data.records[0].date == datetime(2019, 11, 1, 9, 9, 34, 288036)
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
async def test_async_parse_title_or_path(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/parse?apikey=ur1234567-0abc12de3f456gh7ij89k012&title=Series.Title.S01E01.720p.HDTV-Sonarr&path=/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/parse.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_parse_title_or_path(
            title="Series.Title.S01E01.720p.HDTV-Sonarr", path="/"
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
        assert data.parsedEpisodeInfo.fullSeason is False
        assert data.parsedEpisodeInfo.special is False
        assert data.parsedEpisodeInfo.releaseGroup == "Sonarr"
        assert data.parsedEpisodeInfo.releaseHash == ""
        assert data.parsedEpisodeInfo.isDaily is False
        assert data.parsedEpisodeInfo.isAbsoluteNumbering is False
        assert data.parsedEpisodeInfo.isPossibleSpecialEpisode is False
        assert data.series == {}
        assert data.episodes == []


@pytest.mark.asyncio
async def test_async_get_profiles(aresponses):
    """Test getting profiles."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/profile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/profile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[SonarrQualityProfile] = await client.async_get_profiles()

        assert data[0].name == "SD"
        assert data[0].cutoff.id == 1
        assert data[0].cutoff.name == "SDTV"
        assert data[0].items[0].quality.id == 1
        assert data[0].items[0].quality.name == "SDTV"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_queue(aresponses): # TODO fix fixture
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/queue?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/queue.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[SonarrQueue] = await client.async_get_queue()

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
        assert data[0].series.seasons[0].monitored is False
        assert data[0].series.year == 2015
        assert data[0].series.path == "string"
        assert data[0].series.profileId == 5
        assert data[0].series.seasonFolder is True
        assert data[0].series.monitored is True
        assert data[0].series.useSceneNumbering is False
        assert data[0].series.runtime == 60
        assert data[0].series.tvdbId == 0
        assert data[0].series.tvRageId == 0
        assert data[0].series.tvMazeId == 0
        assert data[0].series.firstAired == datetime(2016, 4, 16, 23, 0)
        assert data[0].series.lastInfoSync == datetime(2017, 2, 5, 16, 40, 11, 614176)
        assert data[0].series.seriesType == "standard"
        assert data[0].series.cleanTitle == "string"
        assert data[0].series.imdbId == "string"
        assert data[0].series.titleSlug == "string"
        assert data[0].series.certification == "TV-MA"
        assert data[0].series.genres == ["Adventure", "Drama", "Fantasy"]
        assert data[0].series.tags == []
        assert data[0].series.added == datetime(2015, 12, 28, 13, 44, 24, 204583)
        assert data[0].series.ratings.votes == 1128
        assert data[0].series.ratings.value == 9.4
        assert data[0].series.qualityProfileId == 5
        assert data[0].series.id == 17
        assert data[0].episode.seriesId == 17
        assert data[0].episode.episodeFileId == 0
        assert data[0].episode.seasonNumber == 3
        assert data[0].episode.episodeNumber == 8
        assert data[0].episode.title == "string"
        assert data[0].episode.airDate == datetime(2013, 5, 19, 0, 0)
        assert data[0].episode.airDateUtc == datetime(2013, 5, 20, 1, 0)
        assert data[0].episode.overview == "string"
        assert data[0].episode.hasFile is False
        assert data[0].episode.monitored is False
        assert data[0].episode.absoluteEpisodeNumber == 28
        assert data[0].episode.unverifiedSceneNumbering is False
        assert data[0].episode.id == 889
        assert data[0].quality.quality.id == 7
        assert data[0].quality.quality.name == "Bluray-1080p"
        assert data[0].quality.revision.version == 1
        assert data[0].quality.revision.real == 0
        assert data[0].size == 4472186820
        assert data[0].title == "string"
        assert data[0].sizeleft == 0
        assert data[0].timeleft == "00:00:00"
        assert data[0].estimatedCompletionTime == datetime(2016, 2, 5, 22, 46, 52, 440104)
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
        "/api/v3/release?apikey=ur1234567-0abc12de3f456gh7ij89k012&episodeId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/release.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_release(releaseid=0)

        assert data[0].guid == "string"
        assert data[0].quality.quality.id == 4
        assert data[0].quality.quality.name == "HDTV-720p"
        assert data[0].quality.proper is False
        assert data[0].age == 0
        assert data[0].size == 0
        assert data[0].indexerId == 5
        assert data[0].indexer == "string"
        assert data[0].releaseGroup == "string"
        assert data[0].title == "string"
        assert data[0].fullSeason is False
        assert data[0].sceneSource is False
        assert data[0].seasonNumber == 3
        assert data[0].language == "english"
        assert data[0].seriesTitle == "string"
        assert data[0].episodeNumbers == [1]
        assert data[0].approved is False
        assert data[0].tvRageId == 0
        assert data[0].rejections == ["Unknown Series"]
        assert data[0].publishDate == datetime(2017, 2, 10, 0, 0)
        assert data[0].downloadUrl == "string"
        assert data[0].downloadAllowed is True


@pytest.mark.asyncio
async def test_async_lookup_series(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/series/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=string",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series-lookup.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[SonarrSeriesLookup] = await client.async_lookup_series(term="string")

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
        assert data[0].seasons[0].monitored is False
        assert data[0].year == 2013
        assert data[0].profileId == 0
        assert data[0].seasonFolder is False
        assert data[0].monitored is False
        assert data[0].useSceneNumbering is False
        assert data[0].runtime == 45
        assert data[0].tvdbId == 0
        assert data[0].tvRageId == 0
        assert data[0].firstAired == datetime(2013, 9, 23, 5, 0)
        assert data[0].seriesType == "string"
        assert data[0].cleanTitle == "string"
        assert data[0].imdbId == "string"
        assert data[0].titleSlug == "string"
        assert data[0].certification == "TV-14"
        assert data[0].genres == ["Action", "Crime", "Drama", "Mystery"]
        assert data[0].tags == []
        assert data[0].added == datetime(1, 1, 1, 0, 0)
        assert data[0].ratings.votes == 182
        assert data[0].ratings.value == 8.6
        assert data[0].qualityProfileId == 0


@pytest.mark.asyncio
async def test_async_get_series(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/series/3?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series.json"),
        ),
        match_querystring=True,
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
        assert data.previousAiring == datetime(2019, 4, 29, 1, 0)
        assert data.network == "string"
        assert data.airTime == "21:00"
        assert data.images[0].coverType == "fanart"
        assert data.images[0].url == "string"
        assert data.seasons[0].seasonNumber == 0
        assert data.seasons[0].monitored is False
        assert data.seasons[0].statistics.previousAiring == datetime(2019, 4, 29, 1, 0)
        assert data.seasons[0].statistics.episodeFileCount == 0
        assert data.seasons[0].statistics.episodeCount == 0
        assert data.seasons[0].statistics.totalEpisodeCount == 1
        assert data.seasons[0].statistics.sizeOnDisk == 0
        assert data.seasons[0].statistics.percentOfEpisodes == 0.0
        assert data.year == 2017
        assert data.path == "string"
        assert data.profileId == 6
        assert data.seasonFolder is True
        assert data.monitored is True
        assert data.useSceneNumbering is False
        assert data.runtime == 60
        assert data.tvdbId == 0
        assert data.tvRageId == 0
        assert data.tvMazeId == 0
        assert data.firstAired == datetime(2019, 4, 29, 23, 0)
        assert data.lastInfoSync == datetime(2019, 12, 1, 17, 35, 41, 103443)
        assert data.seriesType == "standard"
        assert data.cleanTitle == "string"
        assert data.imdbId == "string"
        assert data.titleSlug == "string"
        assert data.certification == "TV-MA"
        assert data.genres == ["Action", "Adventure", "Fantasy", "Suspense"]
        assert data.tags == []
        assert data.added == datetime(2019, 9, 13, 15, 50, 29, 325136)
        assert data.ratings.votes == 0
        assert data.ratings.value == 0.0
        assert data.qualityProfileId == 6
        assert data.id == 3


@pytest.mark.asyncio
async def test_async_get_system_backup(aresponses):
    """Test getting system backup info."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/system/backup?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/system-backup.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[SystemBackup] = await client.async_get_system_backup()

        assert data[0].name == "nzbdrone_backup_2017.08.17_22.00.00.zip"
        assert data[0].path == "/backup/update/nzbdrone_backup_2017.08.17_22.00.00.zip"
        assert data[0].type == "update"
        assert data[0].time == datetime(2017, 8, 18, 5, 0, 37)
        assert data[0].id == 1207435784


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses):
    """Test getting wanted."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/wanted/missing?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=airDateUtc&page=1&pageSize=10&sortDir=asc",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/wantedmissing.json"),
        ),
        match_querystring=True,
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
        assert data.records[0].airDate == datetime(2014, 2, 3, 0, 0)
        assert data.records[0].airDateUtc == datetime(2014, 2, 4, 3, 0)
        assert data.records[0].overview == "string"
        assert data.records[0].hasFile is False
        assert data.records[0].monitored is True
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
        assert data.records[0].series.monitored is True
        assert data.records[0].series.qualityProfileId == 1
        assert data.records[0].series.seasonFolder is True
        assert data.records[0].series.lastInfoSync == datetime(2014, 2, 5, 4, 39, 28, 550495)
        assert data.records[0].series.runtime == 30
        assert data.records[0].series.images[0].coverType == "banner"
        assert data.records[0].series.images[0].url == "string"
        assert data.records[0].series.seriesType == "standard"
        assert data.records[0].series.network == "string"
        assert data.records[0].series.useSceneNumbering is False
        assert data.records[0].series.titleSlug == "string"
        assert data.records[0].series.path == "string"
        assert data.records[0].series.year == 2009
        assert data.records[0].series.firstAired == datetime(2012, 9, 18, 2, 0)
        assert data.records[0].series.qualityProfile.value.name == "SD"
        assert data.records[0].series.qualityProfile.value.cutoff.id == 1
        assert data.records[0].series.qualityProfile.value.cutoff.name == "SDTV"
        quality = data.records[0].series.qualityProfile.value.items[0].quality
        assert quality.id == 1
        assert quality.name == "SDTV"
        assert data.records[0].series.qualityProfile.value.items[0].allowed is True
        assert data.records[0].series.qualityProfile.value.id == 1
        assert data.records[0].series.qualityProfile.isLoaded is True
        assert data.records[0].series.seasons[0].seasonNumber == 5
        assert data.records[0].series.seasons[0].monitored is True
        assert data.records[0].series.id == 1
        assert data.records[0].downloading is False
        assert data.records[0].id == 55


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklist."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_blocklist()

    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "date"
    assert data.sortDirection == "descending"
    assert data.totalRecords == 0
    assert data.records[0].seriesId == 0
    assert data.records[0].episodeIds[0] == 0
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].language.id == 1
    assert data.records[0].language.name == "English"
    assert data.records[0].quality.quality.id == 14
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 720
    assert data.records[0].quality.revision.version == 1
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].date == datetime(2021, 9, 19, 8, 14, 33, 582863)
    assert data.records[0].protocol == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert data.records[0].id == 0
