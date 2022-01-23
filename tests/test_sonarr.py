"""Tests for Sonarr object models."""
# pylint:disable=line-too-long, too-many-lines, too-many-statements
from datetime import datetime

import pytest

from aiopyarr.exceptions import ArrException
from aiopyarr.models.const import ProtocolType
from aiopyarr.models.request import Command, ImageType, SortDirection
from aiopyarr.models.sonarr import (
    SonarrCommands,
    SonarrEpisode,
    SonarrEpisodeFile,
    SonarrEventType,
    SonarrImportList,
    SonarrNamingConfig,
    SonarrNotification,
    SonarrRelease,
    SonarrSeries,
    SonarrSeriesAdd,
    SonarrSortKeys,
)
from aiopyarr.sonarr_client import SonarrClient

from . import SONARR_API, load_fixture


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses, sonarr_client: SonarrClient):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/calendar?start=2020-11-30&end=2020-12-01",
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
    data = await sonarr_client.async_get_calendar(start_date=start, end_date=end)

    assert isinstance(data[0].seriesId, int)
    assert isinstance(data[0].episodeFileId, int)
    assert isinstance(data[0].seasonNumber, int)
    assert isinstance(data[0].episodeNumber, int)
    assert data[0].title == "string"
    assert data[0].airDate == datetime(2017, 1, 26, 0, 0)
    assert data[0].airDateUtc == datetime(2017, 1, 27, 1, 30)
    assert data[0].overview == "string"
    assert data[0].hasFile is False
    assert data[0].monitored is True
    assert isinstance(data[0].sceneEpisodeNumber, int)
    assert isinstance(data[0].sceneSeasonNumber, int)
    assert isinstance(data[0].tvDbEpisodeId, int)
    assert data[0].unverifiedSceneNumbering is False
    assert data[0].downloading is False
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_episodes(aresponses, sonarr_client: SonarrClient):
    """Test getting episodes."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episode/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episode.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_episodes(0)

    assert isinstance(data.seriesId, int)
    assert isinstance(data.episodeFileId, int)
    assert isinstance(data.seasonNumber, int)
    assert isinstance(data.episodeNumber, int)
    assert data.title == "string"
    assert data.airDate == datetime(2009, 9, 17, 0, 0)
    assert data.airDateUtc == datetime(2009, 9, 18, 2, 0)
    assert data.overview == "string"
    assert isinstance(data.episodeFile.seriesId, int)
    assert isinstance(data.episodeFile.seasonNumber, int)
    assert data.episodeFile.relativePath == "string"
    assert data.episodeFile.path == "string"
    assert isinstance(data.episodeFile.size, int)
    assert data.episodeFile.dateAdded == datetime(2019, 6, 13, 9, 8, 3, 775081)
    assert data.episodeFile.releaseGroup == "string"
    assert isinstance(data.episodeFile.language.id, int)
    assert data.episodeFile.language.name == "string"
    assert isinstance(data.episodeFile.quality.quality.id, int)
    assert data.episodeFile.quality.quality.name == "string"
    assert data.episodeFile.quality.quality.source == "string"
    assert isinstance(data.episodeFile.quality.quality.resolution, int)
    assert isinstance(data.episodeFile.quality.revision.version, int)
    assert isinstance(data.episodeFile.quality.revision.real, int)
    assert data.episodeFile.quality.revision.isRepack is False
    assert isinstance(data.episodeFile.mediaInfo.audioBitrate, int)
    assert isinstance(data.episodeFile.mediaInfo.audioChannels, float)
    assert data.episodeFile.mediaInfo.audioCodec == "string"
    assert data.episodeFile.mediaInfo.audioLanguages == "string"
    assert isinstance(data.episodeFile.mediaInfo.audioStreamCount, int)
    assert isinstance(data.episodeFile.mediaInfo.videoBitDepth, int)
    assert isinstance(data.episodeFile.mediaInfo.videoBitrate, int)
    assert data.episodeFile.mediaInfo.videoCodec == "string"
    assert isinstance(data.episodeFile.mediaInfo.videoFps, float)
    assert data.episodeFile.mediaInfo.resolution == "string"
    assert data.episodeFile.mediaInfo.runTime == "00:00"
    assert data.episodeFile.mediaInfo.scanType == "string"
    assert data.episodeFile.mediaInfo.subtitles == "string"
    assert data.episodeFile.qualityCutoffNotMet is False
    assert data.episodeFile.languageCutoffNotMet is False
    assert isinstance(data.episodeFile.id, int)
    assert data.hasFile is True
    assert data.monitored is True
    assert isinstance(data.absoluteEpisodeNumber, int)
    assert data.unverifiedSceneNumbering is False
    assert data.series.title == "string"
    assert data.series.sortTitle == "string"
    assert data.series.status == "string"
    assert data.series.ended is True
    assert data.series.overview == "string"
    assert data.series.network == "string"
    assert data.series.airTime == "00:00"
    assert data.series.images[0].coverType == ImageType.POSTER.value
    assert data.series.images[0].url == "string"
    assert isinstance(data.series.seasons[0].seasonNumber, int)
    assert data.series.seasons[0].monitored is False
    assert isinstance(data.series.year, int)
    assert data.series.path == "string"
    assert isinstance(data.series.qualityProfileId, int)
    assert isinstance(data.series.languageProfileId, int)
    assert data.series.seasonFolder is True
    assert data.series.monitored is True
    assert data.series.useSceneNumbering is False
    assert isinstance(data.series.runtime, int)
    assert isinstance(data.series.tvdbId, int)
    assert isinstance(data.series.tvRageId, int)
    assert isinstance(data.series.tvMazeId, int)
    assert data.series.firstAired == datetime(2017, 4, 5, 0, 0)
    assert data.series.seriesType == "string"
    assert data.series.cleanTitle == "string"
    assert data.series.imdbId == "string"
    assert data.series.titleSlug == "string"
    assert data.series.certification == "string"
    assert data.series.genres == ["string"]
    assert data.series.tags == [0]
    assert data.series.added == datetime(2019, 5, 19, 5, 33, 42, 243920)
    assert isinstance(data.series.ratings.votes, int)
    assert isinstance(data.series.ratings.value, float)
    assert isinstance(data.series.id, int)
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episode?seriesId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_episodes(0, series=True)
    assert isinstance(data, SonarrEpisode)


@pytest.mark.asyncio
async def test_async_get_episode_files(aresponses, sonarr_client: SonarrClient):
    """Test getting episode files."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episodefile/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episodefile.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_episode_files(0)

    assert isinstance(data.seriesId, int)
    assert isinstance(data.seasonNumber, int)
    assert data.relativePath == "string"
    assert data.path == "string"
    assert isinstance(data.size, int)
    assert data.dateAdded == datetime(2019, 5, 19, 5, 33, 25, 295709)
    assert data.releaseGroup == "string"
    assert isinstance(data.language.id, int)
    assert data.language.name == "string"
    assert isinstance(data.quality.quality.id, int)
    assert data.quality.quality.name == "string"
    assert data.quality.quality.source == "string"
    assert isinstance(data.quality.quality.resolution, int)
    assert isinstance(data.quality.revision.version, int)
    assert isinstance(data.quality.revision.real, int)
    assert data.quality.revision.isRepack is False
    assert isinstance(data.mediaInfo.audioBitrate, int)
    assert isinstance(data.mediaInfo.audioChannels, float)
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioLanguages == "string"
    assert isinstance(data.mediaInfo.audioStreamCount, int)
    assert isinstance(data.mediaInfo.videoBitDepth, int)
    assert isinstance(data.mediaInfo.videoBitrate, int)
    assert data.mediaInfo.videoCodec == "string"
    assert isinstance(data.mediaInfo.videoFps, float)
    assert data.mediaInfo.resolution == "string"
    assert data.mediaInfo.runTime == "00:00"
    assert data.mediaInfo.scanType == "string"
    assert data.mediaInfo.subtitles == "string"
    assert data.qualityCutoffNotMet is True
    assert data.languageCutoffNotMet is False
    assert isinstance(data.id, int)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episodefile?seriesId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/episodefile.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_episode_files(0, series=True)


@pytest.mark.asyncio
async def test_async_get_history(aresponses, sonarr_client: SonarrClient):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/history?page=1&pageSize=10&sortKey=date&eventType=grabbed&episodeId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/history.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_history(
        recordid=0, event_type=SonarrEventType.GRABBED
    )

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == SonarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DESCENDING.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].episodeId, int)
    assert isinstance(data.records[0].seriesId, int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].language.id, int)
    assert data.records[0].language.name == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert isinstance(data.records[0].quality.quality.resolution, int)
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].qualityCutoffNotMet is True
    assert data.records[0].languageCutoffNotMet is False
    assert data.records[0].languageCutoffNotMet is False
    assert data.records[0].date == datetime(2019, 11, 1, 9, 9, 34, 288036)
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == SonarrEventType.GRABBED.value
    assert data.records[0].data.indexer == "string"
    assert data.records[0].data.nzbInfoUrl == "string"
    assert data.records[0].data.releaseGroup == "string"
    assert isinstance(data.records[0].data.age, int)
    assert isinstance(data.records[0].data.ageHours, float)
    assert isinstance(data.records[0].data.ageMinutes, float)
    assert data.records[0].data.publishedDate == datetime(2020, 2, 8, 13, 30, 37)
    assert isinstance(data.records[0].data.fileId, int)
    assert data.records[0].data.droppedPath == "string"
    assert data.records[0].data.importedPath == "string"
    assert data.records[0].data.downloadClient == "string"
    assert data.records[0].data.downloadClientName == "string"
    assert isinstance(data.records[0].data.preferredWordScore, int)
    assert isinstance(data.records[0].data.size, int)
    assert data.records[0].data.downloadUrl == "string"
    assert data.records[0].data.guid == "string"
    assert isinstance(data.records[0].data.tvdbId, int)
    assert isinstance(data.records[0].data.tvRageId, int)
    assert data.records[0].data.protocol is ProtocolType.UNKNOWN
    assert data.records[0].data.torrentInfoHash == "string"
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_parse_title_or_path(aresponses, sonarr_client: SonarrClient):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/parse?title=Series.Title.S01E01.720p.HDTV-Sonarr&path=/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/parse.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_parse_title_or_path(
        title="Series.Title.S01E01.720p.HDTV-Sonarr", path="/"
    )

    assert data.title == "string"
    assert data.parsedEpisodeInfo.releaseTitle == "string"
    assert data.parsedEpisodeInfo.seriesTitle == "string"
    assert data.parsedEpisodeInfo.seriesTitleInfo.title == "string"
    assert data.parsedEpisodeInfo.seriesTitleInfo.titleWithoutYear == "string"
    assert isinstance(data.parsedEpisodeInfo.seriesTitleInfo.year, int)
    assert isinstance(data.parsedEpisodeInfo.quality.quality.id, int)
    assert data.parsedEpisodeInfo.quality.quality.name == "string"
    assert data.parsedEpisodeInfo.quality.quality.source == "string"
    assert isinstance(data.parsedEpisodeInfo.quality.quality.resolution, int)
    assert isinstance(data.parsedEpisodeInfo.quality.revision.version, int)
    assert isinstance(data.parsedEpisodeInfo.quality.revision.real, int)
    assert data.parsedEpisodeInfo.quality.revision.isRepack is False
    assert isinstance(data.parsedEpisodeInfo.seasonNumber, int)
    assert isinstance(data.parsedEpisodeInfo.episodeNumbers[0], int)
    assert isinstance(data.parsedEpisodeInfo.absoluteEpisodeNumbers[0], int)
    assert isinstance(data.parsedEpisodeInfo.specialAbsoluteEpisodeNumbers[0], int)
    assert isinstance(data.parsedEpisodeInfo.language.id, int)
    assert data.parsedEpisodeInfo.language.name == "string"
    assert data.parsedEpisodeInfo.fullSeason is False
    assert data.parsedEpisodeInfo.isPartialSeason is False
    assert data.parsedEpisodeInfo.isMultiSeason is False
    assert data.parsedEpisodeInfo.isSeasonExtra is False
    assert data.parsedEpisodeInfo.special is False
    assert data.parsedEpisodeInfo.releaseHash == "string"
    assert isinstance(data.parsedEpisodeInfo.seasonPart, int)
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
    assert data.series.images[0].coverType == ImageType.POSTER.value
    assert data.series.images[0].url == "string"
    assert isinstance(data.series.seasons[0].seasonNumber, int)
    assert data.series.seasons[0].monitored is False
    assert isinstance(data.series.year, int)
    assert data.series.path == "string"
    assert isinstance(data.series.qualityProfileId, int)
    assert isinstance(data.series.languageProfileId, int)
    assert data.series.seasonFolder is True
    assert data.series.monitored is True
    assert data.series.useSceneNumbering is False
    assert isinstance(data.series.runtime, int)
    assert isinstance(data.series.tvdbId, int)
    assert isinstance(data.series.tvRageId, int)
    assert isinstance(data.series.tvMazeId, int)
    assert data.series.firstAired == datetime(2011, 9, 26, 0, 0)
    assert data.series.seriesType == "string"
    assert data.series.cleanTitle == "string"
    assert data.series.imdbId == "string"
    assert data.series.titleSlug == "string"
    assert data.series.certification == "string"
    assert data.series.genres == ["string"]
    assert isinstance(data.series.tags[0], int)
    assert data.series.added == datetime(2020, 5, 19, 5, 33, 31, 868402)
    assert isinstance(data.series.ratings.votes, int)
    assert isinstance(data.series.ratings.value, float)
    assert isinstance(data.series.id, int)
    assert isinstance(data.episodes[0].seriesId, int)
    assert isinstance(data.episodes[0].episodeFileId, int)
    assert isinstance(data.episodes[0].seasonNumber, int)
    assert isinstance(data.episodes[0].episodeNumber, int)
    assert data.episodes[0].title == "string"
    assert data.episodes[0].airDate == datetime(2010, 8, 26, 0, 0)
    assert data.episodes[0].airDateUtc == datetime(2006, 9, 27, 0, 0)
    assert data.episodes[0].overview == "string"
    assert data.episodes[0].hasFile is True
    assert data.episodes[0].monitored is False
    assert isinstance(data.episodes[0].absoluteEpisodeNumber, int)
    assert data.episodes[0].unverifiedSceneNumbering is False
    assert isinstance(data.episodes[0].id, int)

    with pytest.raises(ArrException):
        await sonarr_client.async_parse_title_or_path()


@pytest.mark.asyncio
async def test_async_get_queue(aresponses, sonarr_client: SonarrClient):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/queue?page=1&pageSize=20&sortDirection=default&sortKey=timeleft&includeUnknownSeriesItems=False&includeSeries=False&includeEpisode=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/queue.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_queue()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == SonarrSortKeys.TIMELEFT.value
    assert data.sortDirection == SortDirection.ASCENDING.value
    assert isinstance(data.totalRecords, int)
    _value = data.records[0]
    assert isinstance(_value.seriesId, int)
    assert isinstance(_value.episodeId, int)
    assert _value.series
    assert _value.episode
    assert isinstance(_value.language.id, int)
    assert _value.language.name == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert _value.quality.quality.source == "string"
    assert isinstance(_value.quality.quality.resolution, int)
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is False
    assert isinstance(_value.size, int)
    assert _value.title == "string"
    assert isinstance(_value.sizeleft, int)
    assert _value.timeleft == "00:00:00"
    assert _value.estimatedCompletionTime == datetime(2020, 2, 9, 13, 14, 14, 379532)
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
    assert isinstance(_value.id, int)


@pytest.mark.asyncio
async def test_async_get_release(aresponses, sonarr_client: SonarrClient):
    """Test getting release."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/release",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/release.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_release()

    assert data[0].guid == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
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
    assert data[0].releaseGroup == "string"
    assert data[0].releaseHash == "string"
    assert data[0].title == "string"
    assert data[0].fullSeason is False
    assert data[0].sceneSource is False
    assert isinstance(data[0].seasonNumber, int)
    assert isinstance(data[0].language.id, int)
    assert data[0].language.name == "string"
    assert isinstance(data[0].languageWeight, int)
    assert data[0].seriesTitle == "string"
    assert isinstance(data[0].episodeNumbers[0], int)
    assert isinstance(data[0].absoluteEpisodeNumbers[0], int)
    assert isinstance(data[0].mappedSeasonNumber, int)
    assert isinstance(data[0].mappedEpisodeNumbers[0], int)
    assert isinstance(data[0].mappedAbsoluteEpisodeNumbers[0], int)
    assert data[0].approved is False
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is True
    assert isinstance(data[0].tvdbId, int)
    assert isinstance(data[0].tvRageId, int)
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2020, 1, 8, 15, 31, 3)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].episodeRequested is False
    assert data[0].downloadAllowed is True
    assert isinstance(data[0].releaseWeight, int)
    assert isinstance(data[0].preferredWordScore, int)
    assert data[0].sceneMapping.title == "string"
    assert isinstance(data[0].sceneMapping.seasonNumber, int)
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert isinstance(data[0].seeders, int)
    assert isinstance(data[0].leechers, int)
    assert data[0].protocol is ProtocolType.UNKNOWN
    assert data[0].isDaily is False
    assert data[0].isAbsoluteNumbering is False
    assert data[0].isPossibleSpecialEpisode is False
    assert data[0].special is False


@pytest.mark.asyncio
async def test_async_lookup_series(aresponses, sonarr_client: SonarrClient):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series/lookup?term=string",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series-lookup.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_lookup_series(term="string")

    assert data[0].title == "string"
    assert data[0].sortTitle == "string"
    assert data[0].status == "string"
    assert data[0].ended is False
    assert data[0].overview == "string"
    assert data[0].network == "string"
    assert data[0].airTime == "00:00"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].url == "string"
    assert data[0].images[0].remoteUrl == "string"
    assert data[0].remotePoster == "string"
    assert isinstance(data[0].seasons[0].seasonNumber, int)
    assert data[0].seasons[0].monitored is True
    assert isinstance(data[0].year, int)
    assert data[0].path == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert isinstance(data[0].languageProfileId, int)
    assert data[0].seasonFolder is True
    assert data[0].monitored is True
    assert data[0].useSceneNumbering is False
    assert isinstance(data[0].runtime, int)
    assert isinstance(data[0].tvdbId, int)
    assert isinstance(data[0].tvRageId, int)
    assert isinstance(data[0].tvMazeId, int)
    assert data[0].firstAired == datetime(2018, 10, 12, 0, 0)
    assert data[0].seriesType == "string"
    assert data[0].cleanTitle == "string"
    assert data[0].imdbId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].folder == "string"
    assert data[0].certification == "string"
    assert data[0].genres == ["string"]
    assert isinstance(data[0].tags[0], int)
    assert data[0].added == datetime(2018, 10, 31, 5, 49, 55, 357150)
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert isinstance(data[0].statistics.seasonCount, int)
    assert isinstance(data[0].statistics.episodeFileCount, int)
    assert isinstance(data[0].statistics.episodeCount, int)
    assert isinstance(data[0].statistics.totalEpisodeCount, int)
    assert isinstance(data[0].statistics.sizeOnDisk, int)
    assert isinstance(data[0].statistics.percentOfEpisodes, float)
    assert isinstance(data[0].id, int)

    with pytest.raises(ArrException):
        await sonarr_client.async_lookup_series()


@pytest.mark.asyncio
async def test_async_get_import_lists(aresponses, sonarr_client: SonarrClient):
    """Test getting importlist."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/importlist.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_import_lists()

    assert data[0].enableAutomaticAdd is True
    assert data[0].shouldMonitor == "string"
    assert data[0].rootFolderPath == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert isinstance(data[0].languageProfileId, int)
    assert data[0].seriesType == "string"
    assert data[0].seasonFolder is True
    assert data[0].listType == "string"
    assert isinstance(data[0].listOrder, int)
    assert data[0].name == "string"
    assert isinstance(data[0].fields[0].order, int)
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == "string"
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].hidden == "string"
    assert isinstance(data[0].fields[0].selectOptions[0].value, int)
    assert data[0].fields[0].selectOptions[0].name == "string"
    assert isinstance(data[0].fields[0].selectOptions[0].order, int)
    assert data[0].fields[0].selectOptions[0].dividerAfter is False
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert isinstance(data[0].tags[0], int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_series(aresponses, sonarr_client: SonarrClient):
    """Test getting series lookup data."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series/3",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/series.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_series(seriesid=3)

    assert data.title == "string"
    assert data.alternateTitles[0].title == "string"
    assert isinstance(data.alternateTitles[0].seasonNumber, int)
    assert data.sortTitle == "string"
    assert data.status == "string"
    assert data.ended is True
    assert data.overview == "string"
    assert data.previousAiring == "string"
    assert data.network == "string"
    assert data.airTime == "00:00"
    assert data.images[0].coverType == ImageType.POSTER.value
    assert data.images[0].url == "string"
    assert data.images[0].remoteUrl == "string"
    assert isinstance(data.seasons[0].seasonNumber, int)
    assert data.seasons[0].monitored is True
    assert data.seasons[0].statistics.previousAiring == datetime(2019, 7, 5, 7, 0)
    assert isinstance(data.seasons[0].statistics.episodeFileCount, int)
    assert isinstance(data.seasons[0].statistics.episodeCount, int)
    assert isinstance(data.seasons[0].statistics.totalEpisodeCount, int)
    assert isinstance(data.seasons[0].statistics.sizeOnDisk, int)
    assert isinstance(data.seasons[0].statistics.percentOfEpisodes, float)
    assert isinstance(data.year, int)
    assert data.path == "string"
    assert isinstance(data.qualityProfileId, int)
    assert isinstance(data.languageProfileId, int)
    assert data.seasonFolder is True
    assert data.monitored is True
    assert data.useSceneNumbering is False
    assert isinstance(data.runtime, int)
    assert isinstance(data.tvdbId, int)
    assert isinstance(data.tvRageId, int)
    assert isinstance(data.tvMazeId, int)
    assert data.firstAired == datetime(2018, 5, 31, 0, 0)
    assert data.seriesType == "string"
    assert data.cleanTitle == "string"
    assert data.imdbId == "string"
    assert data.titleSlug == "string"
    assert data.rootFolderPath == "string"
    assert data.certification == "string"
    assert data.genres == ["string"]
    assert isinstance(data.tags[0], int)
    assert data.added == datetime(2018, 6, 19, 5, 33, 15, 994870)
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert isinstance(data.statistics.seasonCount, int)
    assert isinstance(data.statistics.episodeFileCount, int)
    assert isinstance(data.statistics.episodeCount, int)
    assert isinstance(data.statistics.totalEpisodeCount, int)
    assert isinstance(data.statistics.sizeOnDisk, int)
    assert isinstance(data.statistics.percentOfEpisodes, float)
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_get_wanted(aresponses, sonarr_client: SonarrClient):
    """Test getting wanted."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/wanted/missing?sortKey=airDateUtc&page=1&pageSize=10&sortDirection=default",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/wantedmissing.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_wanted()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == SonarrSortKeys.AIR_DATE_UTC.value
    assert data.sortDirection == SortDirection.DEFAULT.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].seriesId, int)
    assert isinstance(data.records[0].episodeFileId, int)
    assert isinstance(data.records[0].seasonNumber, int)
    assert isinstance(data.records[0].episodeNumber, int)
    assert data.records[0].title == "string"
    assert data.records[0].airDate == datetime(2010, 3, 7, 0, 0)
    assert data.records[0].airDateUtc == datetime(2010, 3, 7, 5, 0)
    assert data.records[0].overview == "string"
    assert data.records[0].hasFile is False
    assert data.records[0].monitored is True
    assert isinstance(data.records[0].absoluteEpisodeNumber, int)
    assert data.records[0].unverifiedSceneNumbering is False
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses, sonarr_client: SonarrClient):
    """Test getting blocklist."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/blocklist?page=1&pageSize=10&sortDirection=default&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_blocklist()

    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == SonarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DESCENDING.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].seriesId, int)
    assert isinstance(data.records[0].episodeIds[0], int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].language.id, int)
    assert data.records[0].language.name == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.quality.source == "string"
    assert isinstance(data.records[0].quality.quality.resolution, int)
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].date == datetime(2021, 9, 19, 8, 14, 33, 582863)
    assert data.records[0].protocol is ProtocolType.UNKNOWN
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses, sonarr_client: SonarrClient):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/config/naming",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_naming_config()

    assert data.renameEpisodes is True
    assert data.replaceIllegalCharacters is True
    assert isinstance(data.multiEpisodeStyle, int)
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
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_get_notifications(aresponses, sonarr_client: SonarrClient):
    """Test getting notifications."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/notification.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_notifications()

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
    assert isinstance(data[0].fields[0].order, int)
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert isinstance(data[0].fields[0].value[0], int)
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is True
    assert isinstance(data[0].fields[0].selectOptions[0].value, int)
    assert data[0].fields[0].selectOptions[0].name == "string"
    assert isinstance(data[0].fields[0].selectOptions[0].order, int)
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert isinstance(data[0].tags[0], int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses, sonarr_client: SonarrClient):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/queue/details?includeUnknownSeriesItems=False&includeSeries=True&includeEpisode=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_queue_details()
    assert isinstance(data[0].seriesId, int)
    assert isinstance(data[0].episodeId, int)
    assert isinstance(data[0].episode.seriesId, int)
    assert isinstance(data[0].episode.episodeFileId, int)
    assert isinstance(data[0].episode.seasonNumber, int)
    assert isinstance(data[0].episode.episodeNumber, int)
    assert data[0].episode.title == "string"
    assert data[0].episode.airDate == datetime(2020, 7, 9, 0, 0)
    assert data[0].episode.airDateUtc == datetime(2020, 7, 10, 2, 0)
    assert data[0].episode.overview == "string"
    assert data[0].episode.hasFile is False
    assert data[0].episode.monitored is True
    assert isinstance(data[0].episode.absoluteEpisodeNumber, int)
    assert data[0].episode.unverifiedSceneNumbering is False
    assert isinstance(data[0].episode.id, int)
    assert isinstance(data[0].language.id, int)
    assert data[0].language.name == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.quality.source == "string"
    assert isinstance(data[0].quality.quality.resolution, int)
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].size, int)
    assert data[0].title == "string"
    assert isinstance(data[0].sizeleft, int)
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2022, 1, 7, 10, 40, 32, 560840)
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
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_rename(aresponses, sonarr_client: SonarrClient):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/rename?seriesId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/rename.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_rename(0)
    assert isinstance(data[0].seriesId, int)
    assert isinstance(data[0].seasonNumber, int)
    assert isinstance(data[0].episodeNumbers[0], int)
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses, sonarr_client: SonarrClient):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/tag/detail/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("sonarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_get_tags_details(tagid=0)

    assert isinstance(data.id, int)
    assert data.label == "string"
    assert isinstance(data.delayProfileIds[0], int)
    assert isinstance(data.notificationIds[0], int)
    assert isinstance(data.restrictionIds[0], int)
    assert isinstance(data.indexerIds[0], int)
    assert isinstance(data.importListIds[0], int)
    assert isinstance(data.seriesIds[0], int)


@pytest.mark.asyncio
async def test_async_sonarr_commands(aresponses, sonarr_client: SonarrClient):
    """Test Sonarr commands."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_sonarr_command(
        SonarrCommands.DOWNLOADED_EPISODES_SCAN, clientid=0, path="test"
    )
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(
        SonarrCommands.EPISODE_SEARCH, episodeids=[0]
    )

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(SonarrCommands.REFRESH_SERIES)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(
        SonarrCommands.RENAME_SERIES, files=[0], seriesid=[0]
    )

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(SonarrCommands.RESCAN_SERIES)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(SonarrCommands.SEASON_SEARCH, season=0)

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/command",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_sonarr_command(SonarrCommands.SERIES_SEARCH, seriesid=0)


@pytest.mark.asyncio
async def test_async_edit_episode(aresponses, sonarr_client: SonarrClient):
    """Test editing episode."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episode/0",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_edit_episode(SonarrEpisode({"id": 0}))
    assert isinstance(data, SonarrEpisode)


@pytest.mark.asyncio
async def test_async_edit_episode_file_quality(aresponses, sonarr_client: SonarrClient):
    """Test editing episode file."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episodefile",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = SonarrEpisodeFile("test")
    data = await sonarr_client.async_edit_episode_file_quality(data)
    assert isinstance(data, SonarrEpisodeFile)


@pytest.mark.asyncio
async def test_async_delete_episode_file(aresponses, sonarr_client: SonarrClient):
    """Test deleting episode file."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/episodefile/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_delete_episode_file(0)


@pytest.mark.asyncio
async def test_async_download_release(aresponses, sonarr_client: SonarrClient):
    """Test downloading release."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/release",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_download_release(SonarrRelease("test"))
    assert isinstance(data, SonarrRelease)


@pytest.mark.asyncio
async def test_async_push_release(aresponses, sonarr_client: SonarrClient):
    """Test downloading release."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/release/push",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_push_release(SonarrRelease("test"))
    assert isinstance(data, SonarrRelease)


@pytest.mark.asyncio
async def test_async_add_series(aresponses, sonarr_client: SonarrClient):
    """Test adding series."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = SonarrSeriesAdd("test")
    assert data.addOptions.ignoreEpisodesWithFiles is None
    assert data.addOptions.ignoreEpisodesWithoutFiles is None
    assert data.addOptions.searchForMissingEpisodes is None
    data = await sonarr_client.async_add_series(data)
    assert isinstance(data, SonarrSeries)


@pytest.mark.asyncio
async def test_async_edit_series(aresponses, sonarr_client: SonarrClient):
    """Test editing series."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_edit_series(SonarrSeries({"id": 0}))
    assert isinstance(data, SonarrSeries)


@pytest.mark.asyncio
async def test_async_delete_series(aresponses, sonarr_client: SonarrClient):
    """Test deleting series."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/series/0?deleteFiles=False",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await sonarr_client.async_delete_series(0)


@pytest.mark.asyncio
async def test_async_edit_import_list(aresponses, sonarr_client: SonarrClient):
    """Test editing import list."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_edit_import_list(SonarrImportList({"id": 0}))
    assert isinstance(data, SonarrImportList)


@pytest.mark.asyncio
async def test_async_add_import_list(aresponses, sonarr_client: SonarrClient):
    """Test adding import list."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_add_import_list(SonarrImportList("test"))
    assert isinstance(data, SonarrImportList)


@pytest.mark.asyncio
async def test_async_test_import_lists(aresponses, sonarr_client: SonarrClient):
    """Test import list testing."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    data = SonarrImportList("test")
    assert await sonarr_client.async_test_import_lists(data) is True

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    assert await sonarr_client.async_test_import_lists() is True

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    assert await sonarr_client.async_test_import_lists() is False


@pytest.mark.asyncio
async def test_async_importlist_action(aresponses, sonarr_client: SonarrClient):
    """Test performing import list action."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/importlist/action/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = SonarrImportList({"name": "test"})
    data = await sonarr_client.async_importlist_action(data)
    assert isinstance(data, SonarrImportList)


@pytest.mark.asyncio
async def test_async_edit_naming_config(aresponses, sonarr_client: SonarrClient):
    """Test editing naming config."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/config/naming",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_edit_naming_config(SonarrNamingConfig("test"))
    assert isinstance(data, SonarrNamingConfig)


@pytest.mark.asyncio
async def test_async_edit_notification(aresponses, sonarr_client: SonarrClient):
    """Test editing notification."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_edit_notification(SonarrNotification("test"))
    assert isinstance(data, SonarrNotification)


@pytest.mark.asyncio
async def test_async_add_notification(aresponses, sonarr_client: SonarrClient):
    """Test adding notification."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await sonarr_client.async_add_notification(SonarrNotification("test"))
    assert isinstance(data, SonarrNotification)


@pytest.mark.asyncio
async def test_async_test_notifications(aresponses, sonarr_client: SonarrClient):
    """Test notification testing."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification/test",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    data = SonarrNotification("test")
    assert await sonarr_client.async_test_notifications(data) is True

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    assert await sonarr_client.async_test_notifications() is True

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    assert await sonarr_client.async_test_notifications() is False


@pytest.mark.asyncio
async def test_not_implemented(sonarr_client: SonarrClient):
    """Test methods not implemented by the API."""
    with pytest.raises(NotImplementedError):
        await sonarr_client.async_get_localization()

    with pytest.raises(NotImplementedError):
        await sonarr_client.async_get_languages()

    with pytest.raises(NotImplementedError):
        await sonarr_client.async_delete_metadata_profile(0)
