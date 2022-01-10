"""Tests for Sonarr object models."""
from datetime import datetime

import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient

from . import SONARR_API, TEST_HOST_CONFIGURATION, load_fixture

from aiopyarr.models.sonarr import (  # isort:skip
    SonarrNamingConfig,
    SonarrQueue,
)




@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01",
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

    assert data[0].seriesId == 0
    assert data[0].episodeFileId == 0
    assert data[0].seasonNumber == 0
    assert data[0].episodeNumber == 0
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
    assert data[0].downloading is False
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_episode_by_id(aresponses):
    """Test getting episode by ID."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episode/1?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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

    assert data.seriesId == 0
    assert data.episodeFileId == 0
    assert data.seasonNumber == 0
    assert data.episodeNumber == 0
    assert data.title == "string"
    assert data.airDate == datetime(2009, 9, 17, 0, 0)
    assert data.airDateUtc == datetime(2009, 9, 18, 2, 0)
    assert data.overview == "string"
    assert data.episodeFile.seriesId == 0
    assert data.episodeFile.seasonNumber == 0
    assert data.episodeFile.relativePath == "string"
    assert data.episodeFile.path == "string"
    assert data.episodeFile.size == 0
    assert data.episodeFile.dateAdded == datetime(2019, 6, 13, 9, 8, 3, 775081)
    assert data.episodeFile.releaseGroup == "string"
    assert data.episodeFile.language.id == 0
    assert data.episodeFile.language.name == "string"
    assert data.episodeFile.quality.quality.id == 0
    assert data.episodeFile.quality.quality.name == "string"
    assert data.episodeFile.quality.quality.source == "string"
    assert data.episodeFile.quality.quality.resolution == 0
    assert data.episodeFile.quality.revision.version == 0
    assert data.episodeFile.quality.revision.real == 0
    assert data.episodeFile.quality.revision.isRepack is False
    assert data.episodeFile.mediaInfo.audioBitrate == 0
    assert data.episodeFile.mediaInfo.audioChannels == 0.0
    assert data.episodeFile.mediaInfo.audioCodec == "string"
    assert data.episodeFile.mediaInfo.audioLanguages == "string"
    assert data.episodeFile.mediaInfo.audioStreamCount == 0
    assert data.episodeFile.mediaInfo.videoBitDepth == 0
    assert data.episodeFile.mediaInfo.videoBitrate == 0
    assert data.episodeFile.mediaInfo.videoCodec == "string"
    assert data.episodeFile.mediaInfo.videoFps == 0.0
    assert data.episodeFile.mediaInfo.resolution == "string"
    assert data.episodeFile.mediaInfo.runTime == "00:00"
    assert data.episodeFile.mediaInfo.scanType == "string"
    assert data.episodeFile.mediaInfo.subtitles == "string"
    assert data.episodeFile.qualityCutoffNotMet is False
    assert data.episodeFile.languageCutoffNotMet is False
    assert data.episodeFile.id == 0
    assert data.hasFile is True
    assert data.monitored is True
    assert data.absoluteEpisodeNumber == 0
    assert data.unverifiedSceneNumbering is False
    assert data.series.title == "string"
    assert data.series.sortTitle == "string"
    assert data.series.status == "string"
    assert data.series.ended is True
    assert data.series.overview == "string"
    assert data.series.network == "string"
    assert data.series.airTime == "00:00"
    assert data.series.images[0].coverType == "string"
    assert data.series.images[0].url == "string"
    assert data.series.seasons[0].seasonNumber == 0
    assert data.series.seasons[0].monitored is False
    assert data.series.year == 0
    assert data.series.path == "string"
    assert data.series.qualityProfileId == 0
    assert data.series.languageProfileId == 0
    assert data.series.seasonFolder is True
    assert data.series.monitored is True
    assert data.series.useSceneNumbering is False
    assert data.series.runtime == 0
    assert data.series.tvdbId == 0
    assert data.series.tvRageId == 0
    assert data.series.tvMazeId == 0
    assert data.series.firstAired == datetime(2017, 4, 5, 0, 0)
    assert data.series.seriesType == "string"
    assert data.series.cleanTitle == "string"
    assert data.series.imdbId == "string"
    assert data.series.titleSlug == "string"
    assert data.series.certification == "string"
    assert data.series.genres == ["string"]
    assert data.series.tags == [0]
    assert data.series.added == datetime(2019, 5, 19, 5, 33, 42, 243920)
    assert data.series.ratings.votes == 0
    assert data.series.ratings.value == 0.0
    assert data.series.id == 0
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_episode_files(aresponses):
    """Test getting episode files."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episodefile/1?apikey=ur1234567-0abc12de3f456gh7ij89k012&seriesId=1",
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

    assert data.seriesId == 0
    assert data.seasonNumber == 0
    assert data.relativePath == "string"
    assert data.path == "string"
    assert data.size == 0
    assert data.dateAdded == datetime(2019, 5, 19, 5, 33, 25, 295709)
    assert data.releaseGroup == "string"
    assert data.language.id == 0
    assert data.language.name == "string"
    assert data.quality.quality.id == 0
    assert data.quality.quality.name == "string"
    assert data.quality.quality.source == "string"
    assert data.quality.quality.resolution == 0
    assert data.quality.revision.version == 0
    assert data.quality.revision.real == 0
    assert data.quality.revision.isRepack is False
    assert data.mediaInfo.audioBitrate == 0
    assert data.mediaInfo.audioChannels == 0.0
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioLanguages == "string"
    assert data.mediaInfo.audioStreamCount == 0
    assert data.mediaInfo.videoBitDepth == 0
    assert data.mediaInfo.videoBitrate == 0
    assert data.mediaInfo.videoCodec == "string"
    assert data.mediaInfo.videoFps == 0.0
    assert data.mediaInfo.resolution == "string"
    assert data.mediaInfo.runTime == "00:00"
    assert data.mediaInfo.scanType == "string"
    assert data.mediaInfo.subtitles == "string"
    assert data.qualityCutoffNotMet is True
    assert data.languageCutoffNotMet is False
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/history?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortDir=desc&sortKey=date",
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
    assert data.totalRecords == 1
    assert data.records[0].episodeId == 0
    assert data.records[0].seriesId == 0
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].language.id == 0
    assert data.records[0].language.name == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 0
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].qualityCutoffNotMet is True
    assert data.records[0].languageCutoffNotMet is False
    assert data.records[0].languageCutoffNotMet is False
    assert data.records[0].date == datetime(2019, 11, 1, 9, 9, 34, 288036)
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == "string"
    assert data.records[0].data.indexer == "string"
    assert data.records[0].data.nzbInfoUrl == "string"
    assert data.records[0].data.releaseGroup == "string"
    assert data.records[0].data.age == 0
    assert data.records[0].data.ageHours == 0.0
    assert data.records[0].data.ageMinutes == 0.0
    assert data.records[0].data.publishedDate == datetime(2020, 2, 8, 13, 30, 37)
    assert data.records[0].data.fileId == 0
    assert data.records[0].data.droppedPath == "string"
    assert data.records[0].data.importedPath == "string"
    assert data.records[0].data.downloadClient == "string"
    assert data.records[0].data.downloadClientName == "string"
    assert data.records[0].data.preferredWordScore == 0
    assert data.records[0].data.size == 0
    assert data.records[0].data.downloadUrl == "string"
    assert data.records[0].data.guid == "string"
    assert data.records[0].data.tvdbId == 0
    assert data.records[0].data.tvRageId == 0
    assert data.records[0].data.protocol == 0
    assert data.records[0].data.torrentInfoHash == "string"
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_parse_title_or_path(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/parse?apikey=ur1234567-0abc12de3f456gh7ij89k012&title=Series.Title.S01E01.720p.HDTV-Sonarr&path=/",
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

    assert data.title == "string"
    assert data.parsedEpisodeInfo.releaseTitle == "string"
    assert data.parsedEpisodeInfo.seriesTitle == "string"
    assert data.parsedEpisodeInfo.seriesTitleInfo.title == "string"
    assert data.parsedEpisodeInfo.seriesTitleInfo.titleWithoutYear == "string"
    assert data.parsedEpisodeInfo.seriesTitleInfo.year == 0
    assert data.parsedEpisodeInfo.quality.quality.id == 0
    assert data.parsedEpisodeInfo.quality.quality.name == "string"
    assert data.parsedEpisodeInfo.quality.quality.source == "string"
    assert data.parsedEpisodeInfo.quality.quality.resolution == 0
    assert data.parsedEpisodeInfo.quality.revision.version == 0
    assert data.parsedEpisodeInfo.quality.revision.real == 0
    assert data.parsedEpisodeInfo.quality.revision.isRepack is False
    assert data.parsedEpisodeInfo.seasonNumber == 0
    assert data.parsedEpisodeInfo.episodeNumbers == [0]
    assert data.parsedEpisodeInfo.absoluteEpisodeNumbers == [0]
    assert data.parsedEpisodeInfo.specialAbsoluteEpisodeNumbers == [0]
    assert data.parsedEpisodeInfo.language.id == 0
    assert data.parsedEpisodeInfo.language.name == "string"
    assert data.parsedEpisodeInfo.fullSeason is False
    assert data.parsedEpisodeInfo.isPartialSeason is False
    assert data.parsedEpisodeInfo.isMultiSeason is False
    assert data.parsedEpisodeInfo.isSeasonExtra is False
    assert data.parsedEpisodeInfo.special is False
    assert data.parsedEpisodeInfo.releaseHash == "string"
    assert data.parsedEpisodeInfo.seasonPart == 0
    assert data.parsedEpisodeInfo.releaseTokens == "string"
    assert data.parsedEpisodeInfo.isDaily is False
    assert data.parsedEpisodeInfo.isAbsoluteNumbering is False
    assert data.parsedEpisodeInfo.isPossibleSpecialEpisode is False
    assert data.parsedEpisodeInfo.isPossibleSceneSeasonSpecial is False
    assert data.series.title == "string"
    assert data.series.sortTitle == "string"
    assert data.series.status == "string"
    assert data.series.ended is True
    assert data.series.overview == "string"
    assert data.series.network == "string"
    assert data.series.airTime == "00:00"
    assert data.series.images[0].coverType == "string"
    assert data.series.images[0].url == "string"
    assert data.series.seasons[0].seasonNumber == 0
    assert data.series.seasons[0].monitored is False
    assert data.series.year == 0
    assert data.series.path == "string"
    assert data.series.qualityProfileId == 0
    assert data.series.languageProfileId == 0
    assert data.series.seasonFolder is True
    assert data.series.monitored is True
    assert data.series.useSceneNumbering is False
    assert data.series.runtime == 0
    assert data.series.tvdbId == 0
    assert data.series.tvRageId == 0
    assert data.series.tvMazeId == 0
    assert data.series.firstAired == datetime(2011, 9, 26, 0, 0)
    assert data.series.seriesType == "string"
    assert data.series.cleanTitle == "string"
    assert data.series.imdbId == "string"
    assert data.series.titleSlug == "string"
    assert data.series.certification == "string"
    assert data.series.genres == ["string"]
    assert data.series.tags == [0]
    assert data.series.added == datetime(2020, 5, 19, 5, 33, 31, 868402)
    assert data.series.ratings.votes == 0
    assert data.series.ratings.value == 0.0
    assert data.series.id == 0
    assert data.episodes[0].seriesId == 0
    assert data.episodes[0].episodeFileId == 0
    assert data.episodes[0].seasonNumber == 0
    assert data.episodes[0].episodeNumber == 0
    assert data.episodes[0].title == "string"
    assert data.episodes[0].airDate == datetime(2010, 8, 26, 0, 0)
    assert data.episodes[0].airDateUtc == datetime(2006, 9, 27, 0, 0)
    assert data.episodes[0].overview == "string"
    assert data.episodes[0].hasFile is True
    assert data.episodes[0].monitored is False
    assert data.episodes[0].absoluteEpisodeNumber == 0
    assert data.episodes[0].unverifiedSceneNumbering is False
    assert data.episodes[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/queue?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=ascending&sortKey=timeLeft&includeUnknownSeriesItems=False&includeSeries=False&includeEpisode=False",
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
        data = await client.async_get_queue()

    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "timeleft"
    assert data.sortDirection == "ascending"
    assert data.totalRecords == 1
    assert data.records[0].seriesId == 0
    assert data.records[0].episodeId == 0
    assert data.records[0].series
    assert data.records[0].episode
    assert data.records[0].language.id == 0
    assert data.records[0].language.name == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 0
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].size == 0.0
    assert data.records[0].title == "string"
    assert data.records[0].sizeleft == 0.0
    assert data.records[0].timeleft == "00:00:00"
    assert data.records[0].estimatedCompletionTime == datetime(
        2020, 2, 9, 13, 14, 14, 379532
    )
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
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
    """Test getting release."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/release?apikey=ur1234567-0abc12de3f456gh7ij89k012&episodeId=0",
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
        data = await client.async_get_release(episodeid=0)

    assert data[0].guid == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is False
    assert data[0].qualityWeight == 0
    assert data[0].age == 0
    assert data[0].ageHours == 0.0
    assert data[0].ageMinutes == 0.0
    assert data[0].size == 0
    assert data[0].indexerId == 0
    assert data[0].indexer == "string"
    assert data[0].releaseGroup == "string"
    assert data[0].releaseHash == "string"
    assert data[0].title == "string"
    assert data[0].fullSeason is False
    assert data[0].sceneSource is False
    assert data[0].seasonNumber == 0
    assert data[0].language.id == 0
    assert data[0].language.name == "string"
    assert data[0].languageWeight == 0
    assert data[0].seriesTitle == "string"
    assert data[0].episodeNumbers == [0]
    assert data[0].absoluteEpisodeNumbers == [0]
    assert data[0].mappedSeasonNumber == 0
    assert data[0].mappedEpisodeNumbers == [0]
    assert data[0].mappedAbsoluteEpisodeNumbers == [0]
    assert data[0].approved is False
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is True
    assert data[0].tvdbId == 0
    assert data[0].tvRageId == 0
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2020, 1, 8, 15, 31, 3)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].episodeRequested is False
    assert data[0].downloadAllowed is True
    assert data[0].releaseWeight == 0
    assert data[0].preferredWordScore == 0
    assert data[0].sceneMapping.title == "string"
    assert data[0].sceneMapping.seasonNumber == 0
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert data[0].seeders == 0
    assert data[0].leechers == 0
    assert data[0].protocol == "string"
    assert data[0].isDaily is False
    assert data[0].isAbsoluteNumbering is False
    assert data[0].isPossibleSpecialEpisode is False
    assert data[0].special is False


@pytest.mark.asyncio
async def test_async_lookup_series(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=string",
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
        data = await client.async_lookup_series(term="string")

    assert data[0].title == "string"
    assert data[0].sortTitle == "string"
    assert data[0].status == "string"
    assert data[0].ended is False
    assert data[0].overview == "string"
    assert data[0].network == "string"
    assert data[0].airTime == "00:00"
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].url == "string"
    assert data[0].images[0].remoteUrl == "string"
    assert data[0].remotePoster == "string"
    assert data[0].seasons[0].seasonNumber == 0
    assert data[0].seasons[0].monitored is True
    assert data[0].year == 0
    assert data[0].path == "string"
    assert data[0].qualityProfileId == 0
    assert data[0].languageProfileId == 0
    assert data[0].seasonFolder is True
    assert data[0].monitored is True
    assert data[0].useSceneNumbering is False
    assert data[0].runtime == 0
    assert data[0].tvdbId == 0
    assert data[0].tvRageId == 0
    assert data[0].tvMazeId == 0
    assert data[0].firstAired == datetime(2018, 10, 12, 0, 0)
    assert data[0].seriesType == "string"
    assert data[0].cleanTitle == "string"
    assert data[0].imdbId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].folder == "string"
    assert data[0].certification == "string"
    assert data[0].genres == ["string"]
    assert data[0].tags == [0]
    assert data[0].added == datetime(2018, 10, 31, 5, 49, 55, 357150)
    assert data[0].ratings.votes == 0
    assert data[0].ratings.value == 0.0
    assert data[0].statistics.seasonCount == 0
    assert data[0].statistics.episodeFileCount == 0
    assert data[0].statistics.episodeCount == 0
    assert data[0].statistics.totalEpisodeCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfEpisodes == 0.0
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_import_lists(aresponses):
    """Test getting importlist."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/importlist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_import_lists()

    assert data[0].enableAutomaticAdd is True
    assert data[0].shouldMonitor == "string"
    assert data[0].rootFolderPath == "string"
    assert data[0].qualityProfileId == 0
    assert data[0].languageProfileId == 0
    assert data[0].seriesType == "string"
    assert data[0].seasonFolder is True
    assert data[0].listType == "string"
    assert data[0].listOrder == 0
    assert data[0].name == "string"
    assert data[0].fields[0].order == 0
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == "string"
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].hidden == "string"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert data[0].tags == [0]
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_series(aresponses):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series/3?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
    assert data.alternateTitles[0].seasonNumber == 0
    assert data.sortTitle == "string"
    assert data.status == "string"
    assert data.ended is True
    assert data.overview == "string"
    assert data.previousAiring == "string"
    assert data.network == "string"
    assert data.airTime == "00:00"
    assert data.images[0].coverType == "string"
    assert data.images[0].url == "string"
    assert data.images[0].remoteUrl == "string"
    assert data.seasons[0].seasonNumber == 0
    assert data.seasons[0].monitored is True
    assert data.seasons[0].statistics.previousAiring == datetime(2019, 7, 5, 7, 0)
    assert data.seasons[0].statistics.episodeFileCount == 0
    assert data.seasons[0].statistics.episodeCount == 0
    assert data.seasons[0].statistics.totalEpisodeCount == 0
    assert data.seasons[0].statistics.sizeOnDisk == 0
    assert data.seasons[0].statistics.percentOfEpisodes == 0.0
    assert data.year == 0
    assert data.path == "string"
    assert data.qualityProfileId == 0
    assert data.languageProfileId == 0
    assert data.seasonFolder is True
    assert data.monitored is True
    assert data.useSceneNumbering is False
    assert data.runtime == 0
    assert data.tvdbId == 0
    assert data.tvRageId == 0
    assert data.tvMazeId == 0
    assert data.firstAired == datetime(2018, 5, 31, 0, 0)
    assert data.seriesType == "string"
    assert data.cleanTitle == "string"
    assert data.imdbId == "string"
    assert data.titleSlug == "string"
    assert data.rootFolderPath == "string"
    assert data.certification == "string"
    assert data.genres == ["string"]
    assert data.tags == [0]
    assert data.added == datetime(2018, 6, 19, 5, 33, 15, 994870)
    assert data.ratings.votes == 0
    assert data.ratings.value == 0.0
    assert data.statistics.seasonCount == 0
    assert data.statistics.episodeFileCount == 0
    assert data.statistics.episodeCount == 0
    assert data.statistics.totalEpisodeCount == 0
    assert data.statistics.sizeOnDisk == 0
    assert data.statistics.percentOfEpisodes == 0.0
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses):
    """Test getting wanted."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/wanted/missing?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=airDateUtc&page=1&pageSize=10&sortDir=asc",
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
    assert data.pageSize == 10
    assert data.sortKey == "airDateUtc"
    assert data.sortDirection == "default"
    assert data.totalRecords == 1
    assert data.records[0].seriesId == 0
    assert data.records[0].episodeFileId == 0
    assert data.records[0].seasonNumber == 0
    assert data.records[0].episodeNumber == 0
    assert data.records[0].title == "string"
    assert data.records[0].airDate == datetime(2010, 3, 7, 0, 0)
    assert data.records[0].airDateUtc == datetime(2010, 3, 7, 5, 0)
    assert data.records[0].overview == "string"
    assert data.records[0].hasFile is False
    assert data.records[0].monitored is True
    assert data.records[0].absoluteEpisodeNumber == 0
    assert data.records[0].unverifiedSceneNumbering is False
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklist."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortDirection=descending&sortKey=date",
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
    assert data.records[0].language.id == 0
    assert data.records[0].language.name == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert data.records[0].quality.quality.resolution == 0
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].date == datetime(2021, 9, 19, 8, 14, 33, 582863)
    assert data.records[0].protocol == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/config/naming?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: SonarrNamingConfig = await client.async_get_naming_config()

    assert data.renameEpisodes is True
    assert data.replaceIllegalCharacters is True
    assert data.multiEpisodeStyle == 0
    assert data.standardEpisodeFormat == "string"
    assert data.dailyEpisodeFormat == "string"
    assert data.animeEpisodeFormat == "string"
    assert data.seriesFolderFormat == "string"
    assert data.seasonFolderFormat == "string"
    assert data.specialsFolderFormat == "string"
    assert data.includeSeriesTitle is False
    assert data.includeEpisodeTitle is False
    assert data.includeQuality is False
    assert data.replaceSpaces is True
    assert data.separator == "string"
    assert data.numberStyle == "string"
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_notifications(aresponses):
    """Test getting notifications."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/notification.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_notifications()

    assert data[0].onGrab is False
    assert data[0].onDownload is False
    assert data[0].onUpgrade is True
    assert data[0].onRename is False
    assert data[0].onSeriesDelete is False
    assert data[0].onEpisodeFileDelete is False
    assert data[0].onEpisodeFileDeleteForUpgrade is True
    assert data[0].onHealthIssue is True
    assert data[0].supportsOnGrab is True
    assert data[0].supportsOnDownload is True
    assert data[0].supportsOnUpgrade is True
    assert data[0].supportsOnRename is True
    assert data[0].supportsOnSeriesDelete is True
    assert data[0].supportsOnEpisodeFileDelete is True
    assert data[0].supportsOnEpisodeFileDeleteForUpgrade is True
    assert data[0].supportsOnHealthIssue is True
    assert data[0].includeHealthWarnings is True
    assert data[0].name == "string"
    assert data[0].fields[0].order == 0
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == [0]
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is True
    assert data[0].fields[0].selectOptions[0].value == 0
    assert data[0].fields[0].selectOptions[0].name == "string"
    assert data[0].fields[0].selectOptions[0].order == 0
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert data[0].tags == [0]
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/queue/details?apikey=ur1234567-0abc12de3f456gh7ij89k012&includeUnknownSeriesItems=False&includeSeries=True&includeEpisode=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue_details()
    assert data[0].seriesId == 0
    assert data[0].episodeId == 0
    assert data[0].series
    assert data[0].episode.seriesId == 0
    assert data[0].episode.episodeFileId == 0
    assert data[0].episode.seasonNumber == 0
    assert data[0].episode.episodeNumber == 0
    assert data[0].episode.title == "string"
    assert data[0].episode.airDate == datetime(2020, 7, 9, 0, 0)
    assert data[0].episode.airDateUtc == datetime(2020, 7, 10, 2, 0)
    assert data[0].episode.overview == "string"
    assert data[0].episode.hasFile is False
    assert data[0].episode.monitored is True
    assert data[0].episode.absoluteEpisodeNumber == 0
    assert data[0].episode.unverifiedSceneNumbering is False
    assert data[0].episode.id == 0
    assert data[0].language.id == 0
    assert data[0].language.name == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert data[0].quality.quality.resolution == 0
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is False
    assert data[0].size == 0.0
    assert data[0].title == "string"
    assert data[0].sizeleft == 0.0
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2022, 1, 7, 10, 40, 32, 560840)
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
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_rename(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/rename?apikey=ur1234567-0abc12de3f456gh7ij89k012&seriesId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/rename.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_rename(0)
    assert data[0].seriesId == 0
    assert data[0].seasonNumber == 0
    assert data[0].episodeNumbers == [0]
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/tag/detail/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_tags_details(tagid=0)

    assert data.id == 0
    assert data.label == "string"
    assert data.delayProfileIds == [0]
    assert data.notificationIds == [0]
    assert data.restrictionIds == [0]
    assert data.indexerIds == [0]
    assert data.importListIds == [0]
    assert data.seriesIds == [0]
