"""Tests for Readarr object models."""
import json
from datetime import datetime

import pytest
from aiohttp.client import ClientSession

from aiopyarr.const import ATTR_DATA
from aiopyarr.models.readarr import ReadarrBookshelf, ReadarrNamingConfig
from aiopyarr.models.response import PyArrResponse
from aiopyarr.readarr_client import ReadarrClient

from . import READARR_API, TEST_HOST_CONFIGURATION, load_fixture

from aiopyarr.models.readarr_common import (  # isort:skip
    _ReadarrAuthorValueBooks,
    _ReadarrAuthorValueSeries,
    _ReadarrEditions,
    _ReadarrEditionsValueBookFiles,
    _ReadarrSeriesLinks,
)


@pytest.mark.asyncio
async def test_async_author(aresponses):
    """Test getting author info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/author.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_author(authorid=0)
    assert data.id == 0
    assert data.authorMetadataId == 0
    assert data.status == "string"
    assert data.ended is True
    assert data.authorName == "string"
    assert data.authorNameLastFirst == "string"
    assert data.foreignAuthorId == "string"
    assert data.titleSlug == "string"
    assert data.overview == "string"
    assert data.disambiguation == "string"
    assert data.links[0].url == "string"
    assert data.links[0].name == "string"
    assert data.nextBook.id == 0
    assert data.nextBook.authorMetadataId == 0
    assert data.nextBook.foreignBookId == "string"
    assert data.nextBook.titleSlug == "string"
    assert data.nextBook.title == "string"
    assert data.nextBook.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.links[0].url == "string"
    assert data.nextBook.links[0].name == "string"
    assert data.nextBook.genres[0] == "string"
    assert data.nextBook.ratings.votes == 0
    assert data.nextBook.ratings.value == 0.0
    assert data.nextBook.ratings.popularity == 0.0
    assert data.nextBook.cleanTitle == "string"
    assert data.nextBook.monitored is True
    assert data.nextBook.anyEditionOk is True
    assert data.nextBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.addOptions.addType == "string"
    assert data.nextBook.addOptions.searchForNewBook is True
    _value = data.nextBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data.nextBook.authorMetadata.isLoaded is True
    _value = data.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    item = _value.qualityProfile.value.items[0]
    assert item.id == 0
    assert item.name == "string"
    assert item.quality.id == 0
    assert item.quality.name == "string"
    assert item.items[0] == None
    assert item.allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] == None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.nextBook.author.isLoaded is True
    _value = data.nextBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.real == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert data.nextBook.editions.isLoaded is True
    _value = data.nextBook.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == "string"
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    _value = _value.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.nextBook.bookFiles.value[0].author.isLoaded is True
    assert data.nextBook.bookFiles.value[0].edition.isLoaded is True
    assert data.nextBook.bookFiles.value[0].partCount == 0
    assert data.nextBook.bookFiles.isLoaded is True
    assert data.nextBook.seriesLinks.value[0].id == 0
    assert data.nextBook.seriesLinks.value[0].position == "string"
    assert data.nextBook.seriesLinks.value[0].seriesId == 0
    assert data.nextBook.seriesLinks.value[0].bookId == 0
    assert data.nextBook.seriesLinks.value[0].isPrimary is True
    assert data.nextBook.seriesLinks.value[0].series.value.id == 0
    assert data.nextBook.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert data.nextBook.seriesLinks.value[0].series.value.title == "string"
    assert data.nextBook.seriesLinks.value[0].series.value.description == "string"
    assert data.nextBook.seriesLinks.value[0].series.value.numbered is True
    assert data.nextBook.seriesLinks.value[0].series.value.workCount == 0
    assert data.nextBook.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert data.nextBook.seriesLinks.value[0].series.value.books.value[0] is None
    assert data.nextBook.seriesLinks.value[0].series.value.books.isLoaded is True
    assert data.nextBook.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert data.nextBook.seriesLinks.value[0].series.isLoaded is True
    assert data.nextBook.seriesLinks.value[0].book.isLoaded is True
    assert data.nextBook.seriesLinks.isLoaded is True
    assert data.lastBook.id == 0
    assert data.lastBook.authorMetadataId == 0
    assert data.lastBook.foreignBookId == "string"
    assert data.lastBook.titleSlug == "string"
    assert data.lastBook.title == "string"
    assert data.lastBook.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.links[0].url == "string"
    assert data.lastBook.links[0].name == "string"
    assert data.lastBook.genres[0] == "string"
    assert data.lastBook.ratings.votes == 0
    assert data.lastBook.ratings.value == 0.0
    assert data.lastBook.ratings.popularity == 0.0
    assert data.lastBook.cleanTitle == "string"
    assert data.lastBook.monitored is True
    assert data.lastBook.anyEditionOk is True
    assert data.lastBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.addOptions.addType == "string"
    assert data.lastBook.addOptions.searchForNewBook is True
    _value = data.lastBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data.lastBook.authorMetadata.isLoaded is True
    _value = data.lastBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    _value = _value.qualityProfile.value
    assert _value.id == 0
    assert _value.name == "string"
    assert _value.upgradeAllowed is True
    assert _value.cutoff == 0
    assert _value.items[0].id == 0
    assert _value.items[0].name == "string"
    assert _value.items[0].quality.id == 0
    assert _value.items[0].quality.name == "string"
    assert _value.items[0].items[0] == None
    assert _value.items[0].allowed is True
    assert data.lastBook.author.value.qualityProfile.isLoaded is True
    assert data.lastBook.author.value.metadataProfile.value.id == 0
    assert data.lastBook.author.value.metadataProfile.value.name == "string"
    assert data.lastBook.author.value.metadataProfile.value.minPopularity == 0.0
    assert data.lastBook.author.value.metadataProfile.value.skipMissingDate is True
    assert data.lastBook.author.value.metadataProfile.value.skipMissingIsbn is True
    assert data.lastBook.author.value.metadataProfile.value.skipPartsAndSets is True
    assert data.lastBook.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert data.lastBook.author.value.metadataProfile.value.allowedLanguages == "string"
    assert data.lastBook.author.value.metadataProfile.value.minPages == 0
    assert data.lastBook.author.value.metadataProfile.value.ignored == "string"
    assert data.lastBook.author.value.metadataProfile.isLoaded is True
    assert data.lastBook.author.value.books.value[0] == None
    assert data.lastBook.author.value.books.isLoaded is True
    assert data.lastBook.author.value.series.value[0].id == 0
    assert data.lastBook.author.value.series.value[0].foreignSeriesId == "string"
    assert data.lastBook.author.value.series.value[0].title == "string"
    assert data.lastBook.author.value.series.value[0].description == "string"
    assert data.lastBook.author.value.series.value[0].numbered is True
    assert data.lastBook.author.value.series.value[0].workCount == 0
    assert data.lastBook.author.value.series.value[0].primaryWorkCount == 0
    assert data.lastBook.author.value.series.value[0].books.value == [None]
    assert data.lastBook.author.value.series.value[0].books.isLoaded is True
    assert data.lastBook.author.value.series.value[0].foreignAuthorId == "string"
    assert data.lastBook.author.value.name == "string"
    assert data.lastBook.author.value.foreignAuthorId == "string"
    assert data.lastBook.author.isLoaded is True
    _value = data.lastBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.real == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert data.lastBook.editions.isLoaded is True
    _value = data.lastBook.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert data.lastBook.bookFiles.isLoaded is True
    assert data.lastBook.seriesLinks.value[0].id == 0
    assert data.lastBook.seriesLinks.value[0].position == "string"
    assert data.lastBook.seriesLinks.value[0].seriesId == 0
    assert data.lastBook.seriesLinks.value[0].bookId == 0
    assert data.lastBook.seriesLinks.value[0].isPrimary is True
    assert data.lastBook.seriesLinks.value[0].series.value.id == 0
    assert data.lastBook.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert data.lastBook.seriesLinks.value[0].series.value.title == "string"
    assert data.lastBook.seriesLinks.value[0].series.value.description == "string"
    assert data.lastBook.seriesLinks.value[0].series.value.numbered is True
    assert data.lastBook.seriesLinks.value[0].series.value.workCount == 0
    assert data.lastBook.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert data.lastBook.seriesLinks.value[0].series.value.books.value[0] is None
    assert data.lastBook.seriesLinks.value[0].series.value.books.isLoaded is True
    assert data.lastBook.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert data.lastBook.seriesLinks.value[0].series.isLoaded is True
    assert data.lastBook.seriesLinks.value[0].book.isLoaded is True
    assert data.lastBook.seriesLinks.isLoaded is True
    assert data.images[0].url == "string"
    assert data.images[0].coverType == "string"
    assert data.images[0].extension == "string"
    assert data.remotePoster == "string"
    assert data.path == "string"
    assert data.qualityProfileId == 0
    assert data.metadataProfileId == 0
    assert data.monitored is True
    assert data.rootFolderPath == "string"
    assert data.genres[0] == "string"
    assert data.cleanName == "string"
    assert data.sortName == "string"
    assert data.sortNameLastFirst == "string"
    assert data.tags[0] == 0
    assert data.added == datetime(2021, 12, 6, 22, 12, 47, 68000)
    assert data.addOptions.monitor == "string"
    assert data.addOptions.booksToMonitor[0] == "string"
    assert data.addOptions.monitored is True
    assert data.addOptions.searchForMissingBooks is True
    assert data.ratings.votes == 0
    assert data.ratings.value == 0.0
    assert data.ratings.popularity == 0.0
    assert data.statistics.bookFileCount == 0
    assert data.statistics.bookCount == 0
    assert data.statistics.availableBookCount == 0
    assert data.statistics.totalBookCount == 0
    assert data.statistics.sizeOnDisk == 0
    assert data.statistics.percentOfBooks == 0.0


@pytest.mark.asyncio
async def test_async_author_lookup(aresponses):
    """Test getting author lookup info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=string",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/author-lookup.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_author_lookup(term="string")
    assert data[0].authorMetadataId == 1
    assert data[0].status == "string"
    assert data[0].ended is False
    assert data[0].authorName == "string"
    assert data[0].authorNameLastFirst == "string"
    assert data[0].foreignAuthorId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].overview == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].extension == ".jpg"
    assert data[0].remotePoster == "string"
    assert data[0].path == "string"
    assert data[0].qualityProfileId == 1
    assert data[0].metadataProfileId == 1
    assert data[0].monitored is True
    assert data[0].monitorNewItems == "string"
    assert data[0].genres == []
    assert data[0].cleanName == "string"
    assert data[0].sortName == "string"
    assert data[0].sortNameLastFirst == "string"
    assert data[0].tags == []
    assert data[0].added == datetime(2021, 12, 6, 22, 23, 55)
    assert data[0].ratings.votes == 16374205
    assert data[0].ratings.value == 4.05
    assert data[0].ratings.popularity == 66315530.25
    assert data[0].statistics.bookFileCount == 0
    assert data[0].statistics.bookCount == 0
    assert data[0].statistics.availableBookCount == 0
    assert data[0].statistics.totalBookCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfBooks == 0.0
    assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklist info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=descending&sortKey=date",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_blocklist()
    assert data.page == 0
    assert data.pageSize == 0
    assert data.sortKey == "string"
    assert data.sortDirection == "default"
    assert data.filters[0].key == "string"
    assert data.filters[0].value == "string"
    assert data.totalRecords == 0
    assert data.records[0].id == 0
    assert data.records[0].authorId == 0
    assert data.records[0].bookIds[0] == 0
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is True
    assert data.records[0].date == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.records[0].protocol == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    _author = data.records[0].author
    assert _author.id == 0
    assert _author.authorMetadataId == 0
    assert _author.status == "string"
    assert _author.ended is True
    assert _author.authorName == "string"
    assert _author.authorNameLastFirst == "string"
    assert _author.foreignAuthorId == "string"
    assert _author.titleSlug == "string"
    assert _author.overview == "string"
    assert _author.disambiguation == "string"
    assert _author.links[0].url == "string"
    assert _author.links[0].name == "string"
    assert _author.nextBook.id == 0
    assert _author.nextBook.authorMetadataId == 0
    assert _author.nextBook.foreignBookId == "string"
    assert _author.nextBook.titleSlug == "string"
    assert _author.nextBook.title == "string"
    assert _author.nextBook.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.links[0].url == "string"
    assert _author.nextBook.links[0].name == "string"
    assert _author.nextBook.genres[0] == "string"
    assert _author.nextBook.ratings.votes == 0
    assert _author.nextBook.ratings.value == 0.0
    assert _author.nextBook.ratings.popularity == 0.0
    assert _author.nextBook.cleanTitle == "string"
    assert _author.nextBook.monitored is True
    assert _author.nextBook.anyEditionOk is True
    assert _author.nextBook.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.addOptions.addType == "string"
    assert _author.nextBook.addOptions.searchForNewBook is True
    _value = _author.nextBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data.records[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data.records[0].author.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] == None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] == None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.records[0].author.nextBook.author.isLoaded is True
    _value = data.records[0].author.nextBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == "string"
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags[0] == 0
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _val = _value.bookFiles.value[0]
    _valu = _val.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert data.records[0].author.nextBook.editions.isLoaded is True
    _value = data.records[0].author.nextBook.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert data.records[0].author.nextBook.bookFiles.isLoaded is True
    _value = data.records[0].author.nextBook.seriesLinks.value[0]
    assert _value.id == 0
    assert _value.position == "string"
    assert _value.seriesId == 0
    assert _value.bookId == 0
    assert _value.isPrimary is True
    assert _value.series.value.id == 0
    assert _value.series.value.foreignSeriesId == "string"
    assert _value.series.value.title == "string"
    assert _value.series.value.description == "string"
    assert _value.series.value.numbered is True
    assert _value.series.value.workCount == 0
    assert _value.series.value.primaryWorkCount == 0
    assert _value.series.value.books.value[0] is None
    assert _value.series.value.books.isLoaded is True
    assert _value.series.value.foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.book.isLoaded is True
    assert data.records[0].author.nextBook.seriesLinks.isLoaded is True
    _value = data.records[0].author.lastBook
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.foreignBookId == "string"
    assert _value.titleSlug == "string"
    assert _value.title == "string"
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.cleanTitle == "string"
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.addOptions.addType == "string"
    assert _value.addOptions.searchForNewBook is True
    _value = _value.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data.records[0].author.lastBook.authorMetadata.isLoaded is True
    _value = data.records[0].author.lastBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] == None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] == None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.records[0].author.lastBook.author.isLoaded is True
    _value = data.records[0].author.lastBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == "string"
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags[0] == 0
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _valu = _val.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert data.records[0].author.lastBook.editions.isLoaded is True
    _value = data.records[0].author.lastBook.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == "string"
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert data.records[0].author.lastBook.bookFiles.isLoaded is True
    _value = data.records[0].author.lastBook.seriesLinks.value[0]
    assert _value.id == 0
    assert _value.position == "string"
    assert _value.seriesId == 0
    assert _value.bookId == 0
    assert _value.isPrimary is True
    assert _value.series.value.id == 0
    assert _value.series.value.foreignSeriesId == "string"
    assert _value.series.value.title == "string"
    assert _value.series.value.description == "string"
    assert _value.series.value.numbered is True
    assert _value.series.value.workCount == 0
    assert _value.series.value.primaryWorkCount == 0
    assert _value.series.value.books.value[0] is None
    assert _value.series.value.books.isLoaded is True
    assert _value.series.value.foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.book.isLoaded is True
    assert data.records[0].author.lastBook.seriesLinks.isLoaded is True
    assert data.records[0].author.images[0].url == "string"
    assert data.records[0].author.images[0].coverType == "string"
    assert data.records[0].author.images[0].extension == "string"
    assert data.records[0].author.remotePoster == "string"
    assert data.records[0].author.path == "string"
    assert data.records[0].author.qualityProfileId == 0
    assert data.records[0].author.metadataProfileId == 0
    assert data.records[0].author.monitored is True
    assert data.records[0].author.rootFolderPath == "string"
    assert data.records[0].author.genres[0] == "string"
    assert data.records[0].author.cleanName == "string"
    assert data.records[0].author.sortName == "string"
    assert data.records[0].author.sortNameLastFirst == "string"
    assert data.records[0].author.tags[0] == 0
    assert data.records[0].author.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert data.records[0].author.addOptions.monitor == "string"
    assert data.records[0].author.addOptions.booksToMonitor[0] == "string"
    assert data.records[0].author.addOptions.monitored is True
    assert data.records[0].author.addOptions.searchForMissingBooks is True
    assert data.records[0].author.ratings.votes == 0
    assert data.records[0].author.ratings.value == 0.0
    assert data.records[0].author.ratings.popularity == 0.0
    assert data.records[0].author.statistics.bookFileCount == 0
    assert data.records[0].author.statistics.bookCount == 0
    assert data.records[0].author.statistics.availableBookCount == 0
    assert data.records[0].author.statistics.totalBookCount == 0
    assert data.records[0].author.statistics.sizeOnDisk == 0
    assert data.records[0].author.statistics.percentOfBooks == 0.0


@pytest.mark.asyncio
async def test_async_get_book(aresponses):
    """Test getting book info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_book(bookid=0)
    assert data[0].id == 0
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert data[0].authorId == 0
    assert data[0].foreignBookId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].monitored is True
    assert data[0].anyEditionOk is True
    assert data[0].ratings.votes == 0
    assert data[0].ratings.value == 0
    assert data[0].ratings.popularity == 0
    assert data[0].releaseDate == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert data[0].pageCount == 0
    assert data[0].genres[0] == "string"
    assert data[0].author.id == 0
    assert data[0].author.authorMetadataId == 0
    assert data[0].author.status == "string"
    assert data[0].author.ended is True
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert data[0].author.titleSlug == "string"
    assert data[0].author.overview == "string"
    assert data[0].author.disambiguation == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    _book = data[0].author.nextBook
    assert _book.id == 0
    assert _book.authorMetadataId == 0
    assert _book.foreignBookId == "string"
    assert _book.titleSlug == "string"
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert _book.ratings.votes == 0
    assert _book.ratings.value == 0.0
    assert _book.ratings.popularity == 0.0
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.added == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.addOptions.addType == "string"
    assert _book.addOptions.searchForNewBook is True
    _value = _book.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _value.died == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data[0].author.nextBook.author.isLoaded is True
    _value = data[0].author.nextBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert _valu.id == 0
    assert _valu.path == "string"
    assert _valu.size == 0
    assert _valu.modified == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _valu.dateAdded == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert _valu.quality.quality.id == 0
    assert _valu.quality.quality.name == "string"
    assert _valu.quality.revision.version == 0
    assert _valu.quality.revision.real == 0
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert _valu.mediaInfo.audioBitrate == 0
    assert _valu.mediaInfo.audioChannels == 0.0
    assert _valu.mediaInfo.audioBits == 0
    assert _valu.mediaInfo.audioSampleRate == "string"
    assert _valu.editionId == 0
    assert _valu.calibreId == 0
    assert _valu.part == 0
    _val = _valu.author.value
    assert _val.id == 0
    assert _val.authorMetadataId == 0
    assert _val.cleanName == "string"
    assert _val.monitored is True
    assert _val.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.path == "string"
    assert _val.rootFolderPath == "string"
    assert _val.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.qualityProfileId == 0
    assert _val.metadataProfileId == 0
    assert _val.tags[0] == 0
    assert _val.addOptions.monitor == "string"
    assert _val.addOptions.booksToMonitor[0] == "string"
    assert _val.addOptions.monitored is True
    assert _val.addOptions.searchForMissingBooks is True
    assert _val.metadata.value.id == 0
    assert _val.metadata.value.foreignAuthorId == "string"
    assert _val.metadata.value.titleSlug == "string"
    assert _val.metadata.value.name == "string"
    assert _val.metadata.value.sortName == "string"
    assert _val.metadata.value.nameLastFirst == "string"
    assert _val.metadata.value.sortNameLastFirst == "string"
    assert _val.metadata.value.aliases[0] == "string"
    assert _val.metadata.value.overview == "string"
    assert _val.metadata.value.disambiguation == "string"
    assert _val.metadata.value.gender == "string"
    assert _val.metadata.value.hometown == "string"
    assert _val.metadata.value.born == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.metadata.value.died == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.metadata.value.status == "string"
    assert _val.metadata.value.images[0].url == "string"
    assert _val.metadata.value.images[0].coverType == "string"
    assert _val.metadata.value.images[0].extension == "string"
    assert _val.metadata.value.links[0].url == "string"
    assert _val.metadata.value.links[0].name == "string"
    assert _val.metadata.value.genres[0] == "string"
    assert _val.metadata.value.ratings.votes == 0
    assert _val.metadata.value.ratings.value == 0.0
    assert _val.metadata.value.ratings.popularity == 0.0
    assert _val.metadata.isLoaded is True
    assert _val.qualityProfile.value.id == 0
    assert _val.qualityProfile.value.name == "string"
    assert _val.qualityProfile.value.upgradeAllowed is True
    assert _val.qualityProfile.value.cutoff == 0
    assert _val.qualityProfile.value.items[0].id == 0
    assert _val.qualityProfile.value.items[0].name == "string"
    assert _val.qualityProfile.value.items[0].name == "string"
    assert _val.qualityProfile.value.items[0].quality.id == 0
    assert _val.qualityProfile.value.items[0].quality.name == "string"
    assert _val.qualityProfile.value.items[0].items[0] is None
    assert _val.qualityProfile.value.items[0].allowed is True
    assert _val.qualityProfile.isLoaded is True
    assert _val.metadataProfile.value.id == 0
    assert _val.metadataProfile.value.name == "string"
    assert _val.metadataProfile.value.minPopularity == 0.0
    assert _val.metadataProfile.value.skipMissingDate is True
    assert _val.metadataProfile.value.skipMissingIsbn is True
    assert _val.metadataProfile.value.skipPartsAndSets is True
    assert _val.metadataProfile.value.skipSeriesSecondary is True
    assert _val.metadataProfile.value.allowedLanguages == "string"
    assert _val.metadataProfile.value.minPages == 0
    assert _val.metadataProfile.value.ignored == "string"
    assert _val.metadataProfile.isLoaded is True
    assert _val.books.value[0] is None
    assert _val.books.isLoaded is True
    assert _val.series.value[0].id == 0
    assert _val.series.value[0].foreignSeriesId == "string"
    assert _val.series.value[0].title == "string"
    assert _val.series.value[0].description == "string"
    assert _val.series.value[0].numbered is True
    assert _val.series.value[0].workCount == 0
    assert _val.series.value[0].primaryWorkCount == 0
    assert _val.series.value[0].books.value[0] is None
    assert _val.series.value[0].books.isLoaded is True
    assert _val.series.value[0].foreignAuthorId == "string"
    assert _val.series.isLoaded is True
    assert _val.name == "string"
    assert _val.foreignAuthorId == "string"
    assert _value.bookFiles.value[0].author.isLoaded is True
    assert _value.bookFiles.value[0].edition.isLoaded is True
    assert _value.bookFiles.value[0].partCount == 0
    assert _value.bookFiles.isLoaded is True
    value = data[0].author.nextBook
    assert value.seriesLinks.value[0].id == 0
    assert value.seriesLinks.value[0].position == "string"
    assert value.seriesLinks.value[0].seriesId == 0
    assert value.seriesLinks.value[0].bookId == 0
    assert value.seriesLinks.value[0].isPrimary is True
    assert value.seriesLinks.value[0].series.value.id == 0
    assert value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert value.seriesLinks.value[0].series.value.title == "string"
    assert value.seriesLinks.value[0].series.value.description == "string"
    assert value.seriesLinks.value[0].series.value.numbered is True
    assert value.seriesLinks.value[0].series.value.workCount == 0
    assert value.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert value.seriesLinks.value[0].series.value.books.value[0] is None
    assert value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert value.seriesLinks.value[0].series.isLoaded is True
    assert value.seriesLinks.value[0].book.isLoaded is True
    assert value.seriesLinks.isLoaded is True
    _book = data[0].author.lastBook
    assert _book.id == 0
    assert _book.authorMetadataId == 0
    assert _book.foreignBookId == "string"
    assert _book.titleSlug == "string"
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert _book.ratings.votes == 0
    assert _book.ratings.value == 0.0
    assert _book.ratings.popularity == 0.0
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.addOptions.addType == "string"
    assert _book.addOptions.searchForNewBook is True
    _value = _book.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.died == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert data[0].author.lastBook.authorMetadata.isLoaded is True
    _value = data[0].author.lastBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0.0
    assert _value.metadata.value.ratings.popularity == 0.0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data[0].author.lastBook.author.isLoaded is True
    _value = data[0].author.lastBook.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.dateAdded == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == "string"
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags[0] == 0
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _valu = _val.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert _valu.died == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items[0] is None
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert _value.bookFiles.isLoaded is True
    value = data[0].author.lastBook
    assert value.seriesLinks.value[0].id == 0
    assert value.seriesLinks.value[0].position == "string"
    assert value.seriesLinks.value[0].seriesId == 0
    assert value.seriesLinks.value[0].bookId == 0
    assert value.seriesLinks.value[0].isPrimary is True
    assert value.seriesLinks.value[0].series.value.id == 0
    assert value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert value.seriesLinks.value[0].series.value.title == "string"
    assert value.seriesLinks.value[0].series.value.description == "string"
    assert value.seriesLinks.value[0].series.value.numbered is True
    assert value.seriesLinks.value[0].series.value.workCount == 0
    assert value.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert value.seriesLinks.value[0].series.value.books.value[0] is None
    assert value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert value.seriesLinks.value[0].series.isLoaded is True
    assert value.seriesLinks.value[0].book.isLoaded is True
    assert value.seriesLinks.isLoaded is True
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == "string"
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert data[0].author.qualityProfileId == 0
    assert data[0].author.metadataProfileId == 0
    assert data[0].author.monitored is True
    assert data[0].author.rootFolderPath == "string"
    assert data[0].author.genres[0] == "string"
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert data[0].author.tags[0] == 0
    assert data[0].author.added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].author.addOptions.monitor == "string"
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0.0
    assert data[0].author.ratings.popularity == 0.0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0.0
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].statistics.bookFileCount == 0
    assert data[0].statistics.bookCount == 0
    assert data[0].statistics.totalBookCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfBooks == 0.0
    assert data[0].added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].addOptions.addType == "string"
    assert data[0].addOptions.searchForNewBook is True
    assert data[0].remoteCover == "string"
    assert data[0].editions[0].id == 0
    assert data[0].editions[0].bookId == 0
    assert data[0].editions[0].foreignEditionId == "string"
    assert data[0].editions[0].titleSlug == "string"
    assert data[0].editions[0].isbn13 == "string"
    assert data[0].editions[0].asin == "string"
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].format == "string"
    assert data[0].editions[0].isEbook is True
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert data[0].editions[0].pageCount == 0
    assert data[0].editions[0].releaseDate == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == "string"
    assert data[0].editions[0].images[0].extension == "string"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert data[0].editions[0].ratings.votes == 0
    assert data[0].editions[0].ratings.value == 0
    assert data[0].editions[0].ratings.popularity == 0
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is True
    assert data[0].editions[0].remoteCover == "string"
    assert data[0].editions[0].grabbed is True
    assert data[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_book_file(aresponses):
    """Test getting book file info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile/0?apikey=ur1234567-0abc12de3f456gh7ij89k012&unmapped=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_book_file(fileid=0)
    assert data.id == 0
    assert data.authorId == 0
    assert data.bookId == 0
    assert data.path == "string"
    assert data.size == 0
    assert data.dateAdded == datetime(2021, 12, 9, 20, 39, 8, 79000)
    assert data.quality.quality.id == 0
    assert data.quality.quality.name == "string"
    assert data.quality.revision.version == 0
    assert data.quality.revision.real == 0
    assert data.quality.revision.isRepack is True
    assert data.qualityWeight == 0
    assert data.mediaInfo.id == 0
    assert data.mediaInfo.audioChannels == 0.0
    assert data.mediaInfo.audioBitRate == 0
    assert data.mediaInfo.audioCodec == "string"
    assert data.mediaInfo.audioBits == 0
    assert data.mediaInfo.audioSampleRate == "string"
    assert data.qualityCutoffNotMet is True
    assert data.audioTags.title == "string"
    assert data.audioTags.cleanTitle == "string"
    assert data.audioTags.authors[0] == "string"
    assert data.audioTags.authorTitle == "string"
    assert data.audioTags.bookTitle == "string"
    assert data.audioTags.seriesTitle == "string"
    assert data.audioTags.seriesIndex == "string"
    assert data.audioTags.isbn == "string"
    assert data.audioTags.asin == "string"
    assert data.audioTags.goodreadsId == "string"
    assert data.audioTags.authorMBId == "string"
    assert data.audioTags.bookMBId == "string"
    assert data.audioTags.releaseMBId == "string"
    assert data.audioTags.recordingMBId == "string"
    assert data.audioTags.trackMBId == "string"
    assert data.audioTags.trackNumbers[0] == 0
    assert data.audioTags.discNumber == 0
    assert data.audioTags.discCount == 0
    assert data.audioTags.country.twoLetterCode == "string"
    assert data.audioTags.country.name == "string"
    assert data.audioTags.year == 0
    assert data.audioTags.publisher == "string"
    assert data.audioTags.label == "string"
    assert data.audioTags.source == "string"
    assert data.audioTags.catalogNumber == "string"
    assert data.audioTags.disambiguation == "string"
    assert data.audioTags.duration.ticks == 0
    assert data.audioTags.duration.days == 0
    assert data.audioTags.duration.hours == 0
    assert data.audioTags.duration.milliseconds == 0
    assert data.audioTags.duration.minutes == 0
    assert data.audioTags.duration.seconds == 0
    assert data.audioTags.duration.totalDays == 0
    assert data.audioTags.duration.totalHours == 0
    assert data.audioTags.duration.totalMilliseconds == 0
    assert data.audioTags.duration.totalMinutes == 0
    assert data.audioTags.duration.totalSeconds == 0
    assert data.audioTags.quality.quality.id == 0
    assert data.audioTags.quality.quality.name == "string"
    assert data.audioTags.quality.revision.version == 0
    assert data.audioTags.quality.revision.real == 0
    assert data.audioTags.quality.revision.isRepack is True
    assert data.audioTags.mediaInfo.audioFormat == "string"
    assert data.audioTags.mediaInfo.audioBitrate == 0
    assert data.audioTags.mediaInfo.audioChannels == 0.0
    assert data.audioTags.mediaInfo.audioBits == 0
    assert data.audioTags.mediaInfo.audioSampleRate == "string"
    assert data.audioTags.trackNumbers[0] == 0
    assert data.audioTags.language == "string"
    assert data.audioTags.releaseGroup == "string"
    assert data.audioTags.releaseHash == "string"

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile?apikey=ur1234567-0abc12de3f456gh7ij89k012&unmapped=False&authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_book_file(authorid=0, bookid=0)


@pytest.mark.asyncio
async def test_async_book_lookup(aresponses):
    """Test getting book info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=isbn:test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-lookup.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_lookup_book(term="test")
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert data[0].authorId == 0
    assert data[0].foreignBookId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].monitored is False
    assert data[0].anyEditionOk is True
    assert data[0].ratings.votes == 0
    assert data[0].ratings.value == 0.0
    assert data[0].ratings.popularity == 0.0
    assert data[0].releaseDate == datetime(1869, 1, 1, 0, 0)
    assert data[0].pageCount == 0
    assert data[0].genres == []
    assert data[0].author.authorMetadataId == 0
    assert data[0].author.status == "string"
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert data[0].author.titleSlug == "string"
    assert data[0].author.links == []
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == "string"
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.qualityProfileId == 0
    assert data[0].author.metadataProfileId == 0
    assert data[0].author.monitored is False
    assert data[0].author.monitorNewItems == "string"
    assert data[0].author.genres == []
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert data[0].author.tags == []
    assert data[0].author.added == datetime(1, 1, 1, 4, 57)
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0.0
    assert data[0].author.ratings.popularity == 0.0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0.0
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "cover"
    assert data[0].images[0].extension == ".jpg"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].added == datetime(1, 1, 1, 4, 57)
    assert data[0].remoteCover == "string"
    assert data[0].editions[0].bookId == 0
    assert data[0].editions[0].foreignEditionId == "string"
    assert data[0].editions[0].titleSlug == "string"
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].isEbook is False
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert data[0].editions[0].pageCount == 0
    assert data[0].editions[0].releaseDate == datetime(1998, 6, 25, 0, 0)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == "cover"
    assert data[0].editions[0].images[0].extension == ".jpg"
    assert data[0].editions[0].images[0].extension == ".jpg"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert data[0].editions[0].ratings.votes == 0
    assert data[0].editions[0].ratings.value == 0.0
    assert data[0].editions[0].ratings.popularity == 0.0
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is False
    assert data[0].editions[0].grabbed is False
    assert data[0].grabbed is False


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses):
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01&unmonitored=False&includeAuthor=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/calendar.json"),
        ),
        match_querystring=True,
    )
    start = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    end = datetime.strptime("Dec 1 2020  1:33PM", "%b %d %Y %I:%M%p")
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_calendar(start, end)
    assert data[0].id == 0
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert data[0].authorId == 0
    assert data[0].foreignBookId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].monitored is True
    assert data[0].anyEditionOk is True
    assert data[0].ratings.votes == 0
    assert data[0].ratings.value == 0
    assert data[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert data[0].pageCount == 0
    assert data[0].genres[0] == "string"
    _value = data[0].author
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.status == "string"
    assert _value.authorName == "string"
    assert _value.authorNameLastFirst == "string"
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.nextBook.id == 0
    assert _value.nextBook.authorMetadataId == 0
    assert _value.nextBook.foreignBookId == "string"
    assert _value.nextBook.titleSlug == "string"
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert _value.nextBook.ratings.votes == 0
    assert _value.nextBook.ratings.value == 0
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.addOptions.addType == "string"
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = data[0].author.nextBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.died == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value == [None]
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = data[0].author.nextBook
    _valu = _book.editions.value[0]
    assert _valu.id == 0
    assert _valu.bookId == 0
    assert _valu.foreignEditionId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.disambiguation == "string"
    assert _valu.publisher == "string"
    assert _valu.pageCount == 0
    assert _valu.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _value = _book.editions.value[0].bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.real == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == 0
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert _book.editions.value[0].bookFiles.isLoaded is True
    assert _book.editions.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    _author = _book.bookFiles.value[0].author
    assert _author.value.id == 0
    assert _author.value.authorMetadataId == 0
    assert _author.value.cleanName == "string"
    assert _author.value.monitored is True
    assert _author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.path == "string"
    assert _author.value.rootFolderPath == "string"
    assert _author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.qualityProfileId == 0
    assert _author.value.metadataProfileId == 0
    assert _author.value.tags[0] == 0
    assert _author.value.addOptions.monitor == "string"
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    _val = _author.value.metadata.value
    assert _val.id == 0
    assert _val.foreignAuthorId == "string"
    assert _val.titleSlug == "string"
    assert _val.name == "string"
    assert _val.sortName == "string"
    assert _val.nameLastFirst == "string"
    assert _val.sortNameLastFirst == "string"
    assert _val.aliases[0] == "string"
    assert _val.overview == "string"
    assert _val.disambiguation == "string"
    assert _val.gender == "string"
    assert _val.hometown == "string"
    assert _val.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.status == "string"
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == "string"
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres[0] == "string"
    assert _val.ratings.votes == 0
    assert _val.ratings.value == 0.0
    assert _val.ratings.popularity == 0.0
    assert _author.value.metadata.isLoaded is True
    assert _author.value.qualityProfile.value.id == 0
    assert _author.value.qualityProfile.value.name == "string"
    assert _author.value.qualityProfile.value.upgradeAllowed is True
    assert _author.value.qualityProfile.value.cutoff == 0
    assert _author.value.qualityProfile.value.items[0].id == 0
    assert _author.value.qualityProfile.value.items[0].name == "string"
    assert _author.value.qualityProfile.value.items[0].quality.id == 0
    assert _author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _author.value.qualityProfile.value.items[0].items == [None]
    assert _author.value.qualityProfile.value.items[0].allowed is True
    assert _author.value.qualityProfile.isLoaded is True
    assert _author.value.metadataProfile.value.id == 0
    assert _author.value.metadataProfile.value.name == "string"
    assert _author.value.metadataProfile.value.minPopularity == 0.0
    assert _author.value.metadataProfile.value.skipMissingDate is True
    assert _author.value.metadataProfile.value.skipMissingIsbn is True
    assert _author.value.metadataProfile.value.skipPartsAndSets is True
    assert _author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _author.value.metadataProfile.value.allowedLanguages == "string"
    assert _author.value.metadataProfile.value.minPages == 0
    assert _author.value.metadataProfile.value.ignored == "string"
    assert _author.value.metadataProfile.isLoaded is True
    assert _author.value.books.value == [None]
    assert _author.value.books.isLoaded is True
    assert _author.value.series.value[0].id == 0
    assert _author.value.series.value[0].foreignSeriesId == "string"
    assert _author.value.series.value[0].title == "string"
    assert _author.value.series.value[0].description == "string"
    assert _author.value.series.value[0].numbered is True
    assert _author.value.series.value[0].workCount == 0
    assert _author.value.series.value[0].primaryWorkCount == 0
    assert _author.value.series.value[0].books.value == [None]
    assert _author.value.series.value[0].books.isLoaded is True
    assert _author.value.series.value[0].foreignAuthorId == "string"
    assert _author.value.series.isLoaded is True
    assert _author.value.name == "string"
    assert _author.value.foreignAuthorId == "string"
    assert _author.isLoaded is True
    assert _book.bookFiles.value[0].edition.isLoaded is True
    assert _book.bookFiles.value[0].partCount == 0
    assert _book.bookFiles.isLoaded is True
    assert _book.seriesLinks.value[0].id == 0
    assert _book.seriesLinks.value[0].position == "string"
    assert _book.seriesLinks.value[0].seriesId == 0
    assert _book.seriesLinks.value[0].bookId == 0
    assert _book.seriesLinks.value[0].isPrimary is True
    assert _book.seriesLinks.value[0].series.value.id == 0
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert _book.seriesLinks.value[0].series.value.workCount == 0
    assert _book.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    _value = data[0].author
    assert _value.nextBook.id == 0
    assert _value.nextBook.authorMetadataId == 0
    assert _value.nextBook.foreignBookId == "string"
    assert _value.nextBook.titleSlug == "string"
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert _value.nextBook.ratings.votes == 0
    assert _value.nextBook.ratings.value == 0
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.addOptions.addType == "string"
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = data[0].author.nextBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.died == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value == [None]
    assert _value.books.isLoaded is True
    assert _value.series.value[0].id == 0
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert _value.series.value[0].workCount == 0
    assert _value.series.value[0].primaryWorkCount == 0
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = data[0].author.nextBook
    _value = _book.editions.value[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert _value.id == 0
    assert _value.path == "string"
    assert _value.size == 0
    assert _value.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert _value.quality.quality.id == 0
    assert _value.quality.quality.name == "string"
    assert _value.quality.revision.version == 0
    assert _value.quality.revision.real == 0
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == 0
    assert _value.mediaInfo.audioChannels == 0.0
    assert _value.mediaInfo.audioBits == 0
    assert _value.mediaInfo.audioSampleRate == 0
    assert _value.editionId == 0
    assert _value.calibreId == 0
    assert _value.part == 0
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags[0] == 0
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert _value.partCount == 0
    assert _book.editions.value[0].bookFiles.isLoaded is True
    assert _book.editions.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    _author = _val.author
    assert _author.value.id == 0
    assert _author.value.authorMetadataId == 0
    assert _author.value.cleanName == "string"
    assert _author.value.monitored is True
    assert _author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.path == "string"
    assert _author.value.rootFolderPath == "string"
    assert _author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.qualityProfileId == 0
    assert _author.value.metadataProfileId == 0
    assert _author.value.tags[0] == 0
    assert _author.value.addOptions.monitor == "string"
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    _val = _author.value.metadata.value
    assert _val.id == 0
    assert _val.foreignAuthorId == "string"
    assert _val.titleSlug == "string"
    assert _val.name == "string"
    assert _val.sortName == "string"
    assert _val.nameLastFirst == "string"
    assert _val.sortNameLastFirst == "string"
    assert _val.aliases[0] == "string"
    assert _val.overview == "string"
    assert _val.disambiguation == "string"
    assert _val.gender == "string"
    assert _val.hometown == "string"
    assert _val.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.status == "string"
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == "string"
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres[0] == "string"
    assert _val.ratings.votes == 0
    assert _val.ratings.value == 0.0
    assert _val.ratings.popularity == 0.0
    assert _author.value.metadata.isLoaded is True
    assert _author.value.qualityProfile.value.id == 0
    assert _author.value.qualityProfile.value.name == "string"
    assert _author.value.qualityProfile.value.upgradeAllowed is True
    assert _author.value.qualityProfile.value.cutoff == 0
    assert _author.value.qualityProfile.value.items[0].id == 0
    assert _author.value.qualityProfile.value.items[0].name == "string"
    assert _author.value.qualityProfile.value.items[0].quality.id == 0
    assert _author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _author.value.qualityProfile.value.items[0].items == [None]
    assert _author.value.qualityProfile.value.items[0].allowed is True
    assert _author.value.qualityProfile.isLoaded is True
    assert _author.value.metadataProfile.value.id == 0
    assert _author.value.metadataProfile.value.name == "string"
    assert _author.value.metadataProfile.value.minPopularity == 0.0
    assert _author.value.metadataProfile.value.skipMissingDate is True
    assert _author.value.metadataProfile.value.skipMissingIsbn is True
    assert _author.value.metadataProfile.value.skipPartsAndSets is True
    assert _author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _author.value.metadataProfile.value.allowedLanguages == "string"
    assert _author.value.metadataProfile.value.minPages == 0
    assert _author.value.metadataProfile.value.ignored == "string"
    assert _author.value.metadataProfile.isLoaded is True
    assert _author.value.books.value == [None]
    assert _author.value.books.isLoaded is True
    assert _author.value.series.value[0].id == 0
    assert _author.value.series.value[0].foreignSeriesId == "string"
    assert _author.value.series.value[0].title == "string"
    assert _author.value.series.value[0].description == "string"
    assert _author.value.series.value[0].numbered is True
    assert _author.value.series.value[0].workCount == 0
    assert _author.value.series.value[0].primaryWorkCount == 0
    assert _author.value.series.value[0].books.value == [None]
    assert _author.value.series.value[0].books.isLoaded is True
    assert _author.value.series.value[0].foreignAuthorId == "string"
    assert _author.value.series.isLoaded is True
    assert _author.value.name == "string"
    assert _author.value.foreignAuthorId == "string"
    assert _author.isLoaded is True
    assert _book.bookFiles.value[0].edition.isLoaded is True
    assert _book.bookFiles.value[0].partCount == 0
    assert _book.bookFiles.isLoaded is True
    assert _book.seriesLinks.value[0].id == 0
    assert _book.seriesLinks.value[0].position == "string"
    assert _book.seriesLinks.value[0].seriesId == 0
    assert _book.seriesLinks.value[0].bookId == 0
    assert _book.seriesLinks.value[0].isPrimary is True
    assert _book.seriesLinks.value[0].series.value.id == 0
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert _book.seriesLinks.value[0].series.value.workCount == 0
    assert _book.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == "string"
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert data[0].author.qualityProfileId == 0
    assert data[0].author.metadataProfileId == 0
    assert data[0].author.monitored is True
    assert data[0].author.rootFolderPath == "string"
    assert data[0].author.genres[0] == "string"
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert data[0].author.tags[0] == 0
    assert data[0].author.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].author.addOptions.monitor == "string"
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0.0
    assert data[0].author.ratings.popularity == 0.0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0.0
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "string"
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].statistics.bookFileCount == 0
    assert data[0].statistics.bookCount == 0
    assert data[0].statistics.totalBookCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfBooks == 0.0
    assert data[0].added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].addOptions.addType == "string"
    assert data[0].addOptions.searchForNewBook is True
    assert data[0].remoteCover == "string"
    assert data[0].editions[0].id == 0
    assert data[0].editions[0].bookId == 0
    assert data[0].editions[0].foreignEditionId == "string"
    assert data[0].editions[0].titleSlug == "string"
    assert data[0].editions[0].isbn13 == "string"
    assert data[0].editions[0].asin == "string"
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].format == "string"
    assert data[0].editions[0].isEbook is True
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert data[0].editions[0].pageCount == 0
    assert data[0].editions[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == "string"
    assert data[0].editions[0].images[0].extension == "string"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert data[0].editions[0].ratings.votes == 0
    assert data[0].editions[0].ratings.value == 0.0
    assert data[0].editions[0].ratings.popularity == 0.0
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is True
    assert data[0].editions[0].remoteCover == "string"
    assert data[0].editions[0].grabbed is True
    assert data[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_wanted_missing(aresponses):
    """Test getting wanted and missing books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/wanted/missing?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/wanted-missing.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_wanted_missing()
    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "string"
    assert data.sortDirection == "default"
    assert data.totalRecords == 0
    assert data.records[0].title == "string"
    assert data.records[0].authorTitle == "string"
    assert data.records[0].seriesTitle == "string"
    assert data.records[0].disambiguation == "string"
    assert data.records[0].overview == "string"
    assert data.records[0].authorId == 0
    assert data.records[0].foreignBookId == "string"
    assert data.records[0].titleSlug == "string"
    assert data.records[0].monitored is True
    assert data.records[0].anyEditionOk is True
    assert data.records[0].ratings.votes == 0
    assert data.records[0].ratings.value == 0.0
    assert data.records[0].ratings.popularity == 0.0
    assert data.records[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data.records[0].pageCount == 0
    assert data.records[0].genres[0] == "string"
    assert data.records[0].author.authorMetadataId == 0
    assert data.records[0].author.status == "string"
    assert data.records[0].author.ended is False
    assert data.records[0].author.authorName == "string"
    assert data.records[0].author.authorNameLastFirst == "string"
    assert data.records[0].author.foreignAuthorId == "string"
    assert data.records[0].author.titleSlug == "string"
    assert data.records[0].author.overview == "string"
    assert data.records[0].author.links[0].url == "string"
    assert data.records[0].author.links[0].name == "string"
    assert data.records[0].author.images[0].url == "string"
    assert data.records[0].author.images[0].coverType == "string"
    assert data.records[0].author.images[0].extension == "string"
    assert data.records[0].author.path == "string"
    assert data.records[0].author.qualityProfileId == 0
    assert data.records[0].author.metadataProfileId == 0
    assert data.records[0].author.monitored is True
    assert data.records[0].author.monitorNewItems == "string"
    assert data.records[0].author.genres == []
    assert data.records[0].author.cleanName == "string"
    assert data.records[0].author.sortName == "string"
    assert data.records[0].author.sortNameLastFirst == "string"
    assert data.records[0].author.tags == []
    assert data.records[0].author.added == datetime(2021, 12, 6, 22, 23, 55)
    assert data.records[0].author.ratings.votes == 0
    assert data.records[0].author.ratings.value == 0.0
    assert data.records[0].author.ratings.popularity == 0.0
    assert data.records[0].author.statistics.bookFileCount == 0
    assert data.records[0].author.statistics.bookCount == 0
    assert data.records[0].author.statistics.availableBookCount == 0
    assert data.records[0].author.statistics.totalBookCount == 0
    assert data.records[0].author.statistics.sizeOnDisk == 0
    assert data.records[0].author.statistics.percentOfBooks == 0.0
    assert data.records[0].author.id == 0
    assert data.records[0].images[0].url == "string"
    assert data.records[0].images[0].coverType == "string"
    assert data.records[0].images[0].extension == "string"
    assert data.records[0].links[0].url == "string"
    assert data.records[0].links[0].name == "string"
    assert data.records[0].statistics.bookFileCount == 0
    assert data.records[0].statistics.bookCount == 0
    assert data.records[0].statistics.totalBookCount == 0
    assert data.records[0].statistics.sizeOnDisk == 0
    assert data.records[0].statistics.percentOfBooks == 0.0
    assert data.records[0].added == datetime(2021, 12, 6, 22, 23, 58)
    assert data.records[0].editions[0].bookId == 0
    assert data.records[0].editions[0].foreignEditionId == "string"
    assert data.records[0].editions[0].titleSlug == "string"
    assert data.records[0].editions[0].asin == "string"
    assert data.records[0].editions[0].title == "string"
    assert data.records[0].editions[0].language == "string"
    assert data.records[0].editions[0].overview == "string"
    assert data.records[0].editions[0].format == "string"
    assert data.records[0].editions[0].isEbook is True
    assert data.records[0].editions[0].disambiguation == "string"
    assert data.records[0].editions[0].publisher == "string"
    assert data.records[0].editions[0].pageCount == 0
    assert data.records[0].editions[0].releaseDate == datetime(2017, 3, 15, 0, 0)
    assert data.records[0].editions[0].images[0].url == "string"
    assert data.records[0].editions[0].images[0].coverType == "string"
    assert data.records[0].editions[0].images[0].extension == "string"
    assert data.records[0].editions[0].links[0].url == "string"
    assert data.records[0].editions[0].links[0].name == "string"
    assert data.records[0].editions[0].ratings.votes == 0
    assert data.records[0].editions[0].ratings.value == 0
    assert data.records[0].editions[0].ratings.popularity == 0
    assert data.records[0].editions[0].monitored is False
    assert data.records[0].editions[0].manualAdd is False
    assert data.records[0].editions[0].grabbed is False
    assert data.records[0].editions[0].id == 0
    assert data.records[0].grabbed is False
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_wanted_cutoff(aresponses):
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/wanted/cutoff?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/wanted-cutoff.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_wanted_cutoff()
    assert data.filters[0].key == "string"
    assert data.filters[0].value == "string"


@pytest.mark.asyncio
async def test_async_get_delay_profiles(aresponses):
    """Test getting delay profile."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/delayprofile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/delayprofile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_delay_profiles()
    assert data[0].enableUsenet is True
    assert data[0].enableTorrent is True
    assert data[0].preferredProtocol == "usenet"
    assert data[0].usenetDelay == 0
    assert data[0].torrentDelay == 0
    assert data[0].order == 2147483647
    assert data[0].tags == []
    assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_history(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/history?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/history.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_history()
    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "date"
    assert data.sortDirection == "descending"
    assert data.totalRecords == 5
    assert data.records[0].bookId == 0
    assert data.records[0].authorId == 0
    assert data.records[0].sourceTitle == "string"
    assert data.records[0].quality.quality.id == 3
    assert data.records[0].quality.quality.name == "EPUB"
    assert data.records[0].quality.revision.version == 1
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].qualityCutoffNotMet is False
    assert data.records[0].date == datetime(2021, 12, 31, 1, 13, 38)
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == "grabbed"
    assert data.records[0].data.indexer == "string"
    assert data.records[0].data.nzbInfoUrl == "string"
    assert data.records[0].data.releaseGroup is None
    assert data.records[0].data.age == 0.0
    assert data.records[0].data.ageHours == 0.0
    assert data.records[0].data.ageMinutes == 0.0
    assert data.records[0].data.publishedDate == datetime(2020, 6, 6, 4, 0)
    assert data.records[0].data.downloadClient == "string"
    assert data.records[0].data.size == 0
    assert data.records[0].data.downloadUrl == "string"
    assert data.records[0].data.guid == "string"
    assert data.records[0].data.protocol == 2
    assert data.records[0].data.downloadForced is False
    assert data.records[0].data.torrentInfoHash == "string"
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_import_lists(aresponses):
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/importlist.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_import_lists()
    assert data[0].enableAutomaticAdd is True
    assert data[0].shouldMonitor == "entireAuthor"
    assert data[0].shouldMonitorExisting is False
    assert data[0].rootFolderPath == "/books/"
    assert data[0].monitorNewItems == "string"
    assert data[0].qualityProfileId == 1
    assert data[0].listType == "string"
    assert data[0].listOrder == 1
    assert data[0].name == "string"
    assert data[0].fields[0].order == 0
    assert data[0].fields[0].name == "accessToken"
    assert data[0].fields[0].label == "Access Token"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == ["string", "string"]
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].hidden == "hidden"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert data[0].tags == []
    assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_metadata_profiles(aresponses):
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/metadataprofile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/metadata-profile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_metadata_profiles()
    assert data[0].id == 0
    assert data[0].name == "string"
    assert data[0].minPages == 0
    assert data[0].skipMissingDate is True
    assert data[0].skipMissingIsbn is True
    assert data[0].skipPartsAndSets is True
    assert data[0].skipSeriesSecondary is True
    assert data[0].allowedLanguages == "string"
    assert data[0].minPages == 0
    assert data[0].ignored == "string"


@pytest.mark.asyncio
async def test_async_get_metadata_provider_configs(aresponses):
    """Test getting metadata provider configs."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/metadataprovider?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/config-metadataprovider.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_metadata_provider_configs()
    assert data.writeAudioTags == "no"
    assert data.scrubAudioTags is False
    assert data.writeBookTags == "newFiles"
    assert data.updateCovers is True
    assert data.embedMetadata is False
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_naming_config(aresponses):
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/naming?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: ReadarrNamingConfig = await client.async_get_naming_config()

    assert data.renameBooks is False
    assert data.replaceIllegalCharacters is True
    assert data.standardBookFormat == "string"
    assert data.authorFolderFormat == "string"
    assert data.includeAuthorName is False
    assert data.includeBookTitle is False
    assert data.includeQuality is False
    assert data.replaceSpaces is False
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_notifications(aresponses):
    """Test getting notifications."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/notification.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_notifications()

    assert data[0].onGrab is True
    assert data[0].onReleaseImport is True
    assert data[0].onUpgrade is True
    assert data[0].onRename is True
    assert data[0].onHealthIssue is True
    assert data[0].onDownloadFailure is True
    assert data[0].onImportFailure is True
    assert data[0].onBookRetag is True
    assert data[0].supportsOnGrab is True
    assert data[0].supportsOnReleaseImport is True
    assert data[0].supportsOnUpgrade is True
    assert data[0].supportsOnRename is True
    assert data[0].supportsOnHealthIssue is True
    assert data[0].includeHealthWarnings is False
    assert data[0].supportsOnDownloadFailure is True
    assert data[0].supportsOnImportFailure is True
    assert data[0].supportsOnBookRetag is True
    assert data[0].name == "string"
    assert data[0].fields[0].order == 0
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == "string"
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert data[0].tags == [0]
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_parse(aresponses):
    """Test parsing book file name."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/parse?apikey=ur1234567-0abc12de3f456gh7ij89k012&title=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/parse.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_parse("test")

    assert data.id == 0
    assert data.title == "string"
    assert data.parsedBookInfo.bookTitle == "string"
    assert data.parsedBookInfo.authorName == "string"
    assert data.parsedBookInfo.authorTitleInfo.title == "string"
    assert data.parsedBookInfo.authorTitleInfo.titleWithoutYear == "string"
    assert data.parsedBookInfo.authorTitleInfo.year == 0
    assert data.parsedBookInfo.quality.quality.id == 0
    assert data.parsedBookInfo.quality.quality.name == "string"
    assert data.parsedBookInfo.quality.revision.version == 0
    assert data.parsedBookInfo.quality.revision.real == 0
    assert data.parsedBookInfo.quality.revision.isRepack is True
    assert data.parsedBookInfo.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.parsedBookInfo.discography is True
    assert data.parsedBookInfo.discographyStart == 0
    assert data.parsedBookInfo.discographyEnd == 0
    assert data.parsedBookInfo.releaseGroup == "string"
    assert data.parsedBookInfo.releaseHash == "string"
    assert data.parsedBookInfo.releaseVersion == "string"
    assert data.author.id == 0
    assert data.author.authorMetadataId == 0
    assert data.author.status == "string"
    assert data.author.ended is True
    assert data.author.authorName == "string"
    assert data.author.authorNameLastFirst == "string"
    assert data.author.foreignAuthorId == "string"
    assert data.author.titleSlug == "string"
    assert data.author.overview == "string"
    assert data.author.disambiguation == "string"
    assert data.author.links[0].url == "string"
    assert data.author.links[0].name == "string"
    _value = data.author.nextBook
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.foreignBookId == "string"
    assert _value.titleSlug == "string"
    assert _value.title == "string"
    assert _value.releaseDate == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.cleanTitle == "string"
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert _value.lastInfoSync == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.added == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.addOptions.addType == "string"
    assert _value.addOptions.searchForNewBook is True
    assert _value.authorMetadata.value.id == 0
    assert _value.authorMetadata.value.foreignAuthorId == "string"
    assert _value.authorMetadata.value.titleSlug == "string"
    assert _value.authorMetadata.value.name == "string"
    assert _value.authorMetadata.value.sortName == "string"
    assert _value.authorMetadata.value.nameLastFirst == "string"
    assert _value.authorMetadata.value.sortNameLastFirst == "string"
    assert _value.authorMetadata.value.aliases == ["string"]
    assert _value.authorMetadata.value.overview == "string"
    assert _value.authorMetadata.value.disambiguation == "string"
    assert _value.authorMetadata.value.gender == "string"
    assert _value.authorMetadata.value.hometown == "string"
    assert _value.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.authorMetadata.value.status == "string"
    assert _value.authorMetadata.value.images[0].url == "string"
    assert _value.authorMetadata.value.images[0].coverType == "string"
    assert _value.authorMetadata.value.images[0].extension == "string"
    assert _value.authorMetadata.value.links[0].url == "string"
    assert _value.authorMetadata.value.links[0].name == "string"
    assert _value.authorMetadata.value.genres == ["string"]
    assert _value.authorMetadata.value.ratings.votes == 0
    assert _value.authorMetadata.value.ratings.value == 0.0
    assert _value.authorMetadata.value.ratings.popularity == 0.0
    assert _value.authorMetadata.isLoaded is True
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags == [0]
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor == ["string"]
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _val = _value.author.value.metadata
    assert _val.value.id == 0
    assert _val.value.foreignAuthorId == "string"
    assert _val.value.titleSlug == "string"
    assert _val.value.name == "string"
    assert _val.value.nameLastFirst == "string"
    assert _val.value.sortNameLastFirst == "string"
    assert _val.value.aliases == ["string"]
    assert _val.value.overview == "string"
    assert _val.value.disambiguation == "string"
    assert _val.value.gender == "string"
    assert _val.value.hometown == "string"
    assert _val.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.value.status == "string"
    assert _val.value.images[0].url == "string"
    assert _val.value.images[0].coverType == "string"
    assert _val.value.images[0].extension == "string"
    assert _val.value.links[0].url == "string"
    assert _val.value.links[0].name == "string"
    assert _val.value.genres == ["string"]
    assert _val.value.ratings.votes == 0
    assert _val.value.ratings.value == 0.0
    assert _val.value.ratings.popularity == 0.0
    assert _val.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    _val = _value.editions.value[0]
    assert _val.id == 0
    assert _val.bookId == 0
    assert _val.foreignEditionId == "string"
    assert _val.titleSlug == "string"
    assert _val.isbn13 == "string"
    assert _val.asin == "string"
    assert _val.title == "string"
    assert _val.language == "string"
    assert _val.overview == "string"
    assert _val.format == "string"
    assert _val.isEbook is True
    assert _val.disambiguation == "string"
    assert _val.publisher == "string"
    assert _val.pageCount == 0
    assert _val.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == "string"
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.ratings.votes == 0
    assert _val.ratings.value == 0.0
    assert _val.ratings.popularity == 0.0
    assert _val.monitored is True
    assert _val.manualAdd is True
    assert _val.book.isLoaded is True
    assert _val.bookFiles.value[0].id == 0
    assert _val.bookFiles.value[0].path == "string"
    assert _val.bookFiles.value[0].size == 0
    assert _val.bookFiles.value[0].modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.bookFiles.value[0].dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.bookFiles.value[0].sceneName == "string"
    assert _val.bookFiles.value[0].releaseGroup == "string"
    assert _val.bookFiles.value[0].quality.quality.id == 0
    assert _val.bookFiles.value[0].quality.quality.name == "string"
    assert _val.bookFiles.value[0].quality.revision.version == 0
    assert _val.bookFiles.value[0].quality.revision.real == 0
    assert _val.bookFiles.value[0].quality.revision.isRepack is True
    assert _val.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert _val.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _val.bookFiles.value[0].mediaInfo.audioChannels == 0.0
    assert _val.bookFiles.value[0].mediaInfo.audioBits == 0
    assert _val.bookFiles.value[0].mediaInfo.audioSampleRate == 0
    assert _val.bookFiles.value[0].editionId == 0
    assert _val.bookFiles.value[0].calibreId == 0
    assert _val.bookFiles.value[0].part == 0
    _valu = _val.bookFiles.value[0].author.value
    assert _valu.id == 0
    assert _valu.authorMetadataId == 0
    assert _valu.cleanName == "string"
    assert _valu.monitored is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.path == "string"
    assert _valu.rootFolderPath == "string"
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.qualityProfileId == 0
    assert _valu.metadataProfileId == 0
    assert _valu.tags == [0]
    assert _valu.addOptions.monitor == "string"
    assert _valu.addOptions.booksToMonitor == ["string"]
    assert _valu.addOptions.monitored is True
    assert _valu.addOptions.searchForMissingBooks is True
    assert _valu.metadata.value.id == 0
    assert _valu.metadata.value.foreignAuthorId == "string"
    assert _valu.metadata.value.titleSlug == "string"
    assert _valu.metadata.value.name == "string"
    assert _valu.metadata.value.sortName == "string"
    assert _valu.metadata.value.nameLastFirst == "string"
    assert _valu.metadata.value.sortNameLastFirst == "string"
    assert _valu.metadata.value.aliases == ["string"]
    assert _valu.metadata.value.overview == "string"
    assert _valu.metadata.value.disambiguation == "string"
    assert _valu.metadata.value.gender == "string"
    assert _valu.metadata.value.hometown == "string"
    assert _valu.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.status == "string"
    assert _valu.metadata.value.images[0].url == "string"
    assert _valu.metadata.value.images[0].coverType == "string"
    assert _valu.metadata.value.images[0].extension == "string"
    assert _valu.metadata.value.links[0].url == "string"
    assert _valu.metadata.value.links[0].name == "string"
    assert _valu.metadata.value.genres == ["string"]
    assert _valu.metadata.value.ratings.votes == 0
    assert _valu.metadata.value.ratings.value == 0.0
    assert _valu.metadata.value.ratings.popularity == 0.0
    assert _valu.metadata.isLoaded is True
    assert _valu.qualityProfile.value.id == 0
    assert _valu.qualityProfile.value.name == "string"
    assert _valu.qualityProfile.value.upgradeAllowed is True
    assert _valu.qualityProfile.value.cutoff == 0
    assert _valu.qualityProfile.value.items[0].id == 0
    assert _valu.qualityProfile.value.items[0].name == "string"
    assert _valu.qualityProfile.value.items[0].quality.id == 0
    assert _valu.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.qualityProfile.value.items[0].items == [None]
    assert _valu.qualityProfile.value.items[0].allowed is True
    assert _valu.qualityProfile.isLoaded is True
    assert _valu.metadataProfile.value.id == 0
    assert _valu.metadataProfile.value.name == "string"
    assert _valu.metadataProfile.value.minPopularity == 0.0
    assert _valu.metadataProfile.value.skipMissingDate is True
    assert _valu.metadataProfile.value.skipMissingIsbn is True
    assert _valu.metadataProfile.value.skipPartsAndSets is True
    assert _valu.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.metadataProfile.value.allowedLanguages == "string"
    assert _valu.metadataProfile.value.minPages == 0
    assert _valu.metadataProfile.value.ignored == "string"
    assert _valu.metadataProfile.isLoaded is True
    assert _valu.books.value == [None]
    assert _valu.books.isLoaded is True
    assert _valu.series.value[0].id == 0
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert _valu.series.value[0].workCount == 0
    assert _valu.series.value[0].primaryWorkCount == 0
    assert _valu.series.value[0].books.value == [None]
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.isLoaded is True
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert _val.bookFiles.value[0].author.isLoaded is True
    assert _val.bookFiles.value[0].edition.isLoaded is True
    assert _val.bookFiles.value[0].partCount == 0
    assert _val.bookFiles.isLoaded is True
    assert _value.editions.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert _valu.id == 0
    assert _valu.path == "string"
    assert _valu.size == 0
    assert _valu.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert _valu.quality.quality.id == 0
    assert _valu.quality.quality.name == "string"
    assert _valu.quality.revision.version == 0
    assert _valu.quality.revision.real == 0
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert _valu.mediaInfo.audioBitrate == 0
    assert _valu.mediaInfo.audioChannels == 0.0
    assert _valu.mediaInfo.audioBits == 0
    assert _valu.mediaInfo.audioSampleRate == 0
    assert _valu.editionId == 0
    assert _valu.calibreId == 0
    assert _valu.part == 0
    _valu = _value.bookFiles.value[0].author.value
    assert _valu.id == 0
    assert _valu.authorMetadataId == 0
    assert _valu.cleanName == "string"
    assert _valu.monitored is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.path == "string"
    assert _valu.rootFolderPath == "string"
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.qualityProfileId == 0
    assert _valu.metadataProfileId == 0
    assert _valu.tags == [0]
    assert _valu.addOptions.monitor == "string"
    assert _valu.addOptions.booksToMonitor == ["string"]
    assert _valu.addOptions.monitored is True
    assert _valu.addOptions.searchForMissingBooks is True
    assert _valu.metadata.value.id == 0
    assert _valu.metadata.value.foreignAuthorId == "string"
    assert _valu.metadata.value.titleSlug == "string"
    assert _valu.metadata.value.name == "string"
    assert _valu.metadata.value.sortName == "string"
    assert _valu.metadata.value.nameLastFirst == "string"
    assert _valu.metadata.value.sortNameLastFirst == "string"
    assert _valu.metadata.value.aliases == ["string"]
    assert _valu.metadata.value.overview == "string"
    assert _valu.metadata.value.disambiguation == "string"
    assert _valu.metadata.value.gender == "string"
    assert _valu.metadata.value.hometown == "string"
    assert _valu.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.status == "string"
    assert _valu.metadata.value.images[0].url == "string"
    assert _valu.metadata.value.images[0].coverType == "string"
    assert _valu.metadata.value.images[0].extension == "string"
    assert _valu.metadata.value.links[0].url == "string"
    assert _valu.metadata.value.links[0].name == "string"
    assert _valu.metadata.value.genres == ["string"]
    assert _valu.metadata.value.ratings.votes == 0
    assert _valu.metadata.value.ratings.value == 0.0
    assert _valu.metadata.value.ratings.popularity == 0.0
    assert _valu.metadata.isLoaded is True
    assert _valu.qualityProfile.value.id == 0
    assert _valu.qualityProfile.value.name == "string"
    assert _valu.qualityProfile.value.upgradeAllowed is True
    assert _valu.qualityProfile.value.cutoff == 0
    assert _valu.qualityProfile.value.items[0].id == 0
    assert _valu.qualityProfile.value.items[0].name == "string"
    assert _valu.qualityProfile.value.items[0].quality.id == 0
    assert _valu.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.qualityProfile.value.items[0].items == [None]
    assert _valu.qualityProfile.value.items[0].allowed is True
    assert _valu.qualityProfile.isLoaded is True
    assert _valu.metadataProfile.value.id == 0
    assert _valu.metadataProfile.value.name == "string"
    assert _valu.metadataProfile.value.minPopularity == 0.0
    assert _valu.metadataProfile.value.skipMissingDate is True
    assert _valu.metadataProfile.value.skipMissingIsbn is True
    assert _valu.metadataProfile.value.skipPartsAndSets is True
    assert _valu.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.metadataProfile.value.allowedLanguages == "string"
    assert _valu.metadataProfile.value.minPages == 0
    assert _valu.metadataProfile.value.ignored == "string"
    assert _valu.metadataProfile.isLoaded is True
    assert _valu.books.value == [None]
    assert _valu.books.isLoaded is True
    assert _valu.series.value[0].id == 0
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert _valu.series.value[0].workCount == 0
    assert _valu.series.value[0].primaryWorkCount == 0
    assert _valu.series.value[0].books.value == [None]
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.isLoaded is True
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert _value.bookFiles.value[0].author.isLoaded is True
    assert _value.bookFiles.value[0].edition.isLoaded is True
    assert _value.bookFiles.value[0].partCount == 0
    assert _value.bookFiles.isLoaded is True
    assert _value.seriesLinks.value[0].id == 0
    assert _value.seriesLinks.value[0].position == "string"
    assert _value.seriesLinks.value[0].seriesId == 0
    assert _value.seriesLinks.value[0].bookId == 0
    assert _value.seriesLinks.value[0].isPrimary is True
    assert _value.seriesLinks.value[0].series.value.id == 0
    assert _value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _value.seriesLinks.value[0].series.value.title == "string"
    assert _value.seriesLinks.value[0].series.value.description == "string"
    assert _value.seriesLinks.value[0].series.value.numbered is True
    assert _value.seriesLinks.value[0].series.value.workCount == 0
    assert _value.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _value.seriesLinks.value[0].series.value.books.value == [None]
    assert _value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _value.seriesLinks.value[0].series.isLoaded is True
    assert _value.seriesLinks.value[0].book.isLoaded is True
    assert _value.seriesLinks.isLoaded is True
    assert data.author.lastBook.id == 0
    assert data.author.lastBook.authorMetadataId == 0
    assert data.author.lastBook.foreignBookId == "string"
    assert data.author.lastBook.titleSlug == "string"
    assert data.author.lastBook.title == "string"
    assert data.author.lastBook.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.links[0].url == "string"
    assert data.author.lastBook.links[0].name == "string"
    assert data.author.lastBook.genres[0] == "string"
    assert data.author.lastBook.ratings.votes == 0
    assert data.author.lastBook.ratings.value == 0.0
    assert data.author.lastBook.ratings.popularity == 0.0
    assert data.author.lastBook.cleanTitle == "string"
    assert data.author.lastBook.monitored is True
    assert data.author.lastBook.anyEditionOk is True
    assert data.author.lastBook.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.addOptions.addType == "string"
    assert data.author.lastBook.addOptions.searchForNewBook is True
    _value = data.author.lastBook
    assert _value.authorMetadata.value.id == 0
    assert _value.authorMetadata.value.foreignAuthorId == "string"
    assert _value.authorMetadata.value.titleSlug == "string"
    assert _value.authorMetadata.value.name == "string"
    assert _value.authorMetadata.value.sortName == "string"
    assert _value.authorMetadata.value.nameLastFirst == "string"
    assert _value.authorMetadata.value.sortNameLastFirst == "string"
    assert _value.authorMetadata.value.aliases == ["string"]
    assert _value.authorMetadata.value.overview == "string"
    assert _value.authorMetadata.value.disambiguation == "string"
    assert _value.authorMetadata.value.gender == "string"
    assert _value.authorMetadata.value.hometown == "string"
    assert _value.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.authorMetadata.value.status == "string"
    assert _value.authorMetadata.value.images[0].url == "string"
    assert _value.authorMetadata.value.images[0].coverType == "string"
    assert _value.authorMetadata.value.images[0].extension == "string"
    assert _value.authorMetadata.value.links[0].url == "string"
    assert _value.authorMetadata.value.links[0].name == "string"
    assert _value.authorMetadata.value.genres == ["string"]
    assert _value.authorMetadata.value.ratings.votes == 0
    assert _value.authorMetadata.value.ratings.value == 0.0
    assert _value.authorMetadata.value.ratings.popularity == 0.0
    assert _value.authorMetadata.isLoaded is True
    assert _value.author.value.id == 0
    assert _value.author.value.authorMetadataId == 0
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.author.value.qualityProfileId == 0
    assert _value.author.value.metadataProfileId == 0
    assert _value.author.value.tags == [0]
    assert _value.author.value.addOptions.monitor == "string"
    assert _value.author.value.addOptions.booksToMonitor == ["string"]
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases == ["string"]
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 00.0
    assert _value.author.value.metadata.isLoaded is True
    assert _value.author.value.qualityProfile.value.id == 0
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert _value.author.value.qualityProfile.value.cutoff == 0
    assert _value.author.value.qualityProfile.value.items[0].id == 0
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert _value.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert _value.author.value.metadataProfile.value.id == 0
    assert _value.author.value.metadataProfile.value.name == "string"
    assert _value.author.value.metadataProfile.value.minPopularity == 0.0
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _value.author.value.metadataProfile.value.minPages == 0
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert _value.author.value.series.value[0].id == 0
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert _value.author.value.series.value[0].workCount == 0
    assert _value.author.value.series.value[0].primaryWorkCount == 0
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    _valu = _value.editions.value[0]
    assert _valu.id == 0
    assert _valu.bookId == 0
    assert _valu.foreignEditionId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.disambiguation == "string"
    assert _valu.publisher == "string"
    assert _valu.pageCount == 0
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags == [0]
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert _va.id == 0
    assert _va.foreignAuthorId == "string"
    assert _va.titleSlug == "string"
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.disambiguation == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == "string"
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert _va.ratings.votes == 0
    assert _va.ratings.value == 0.0
    assert _va.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value == [None]
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert _valu.bookFiles.isLoaded is True
    assert _value.editions.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert _valu.id == 0
    assert _valu.path == "string"
    assert _valu.size == 0
    assert _valu.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert _valu.quality.quality.id == 0
    assert _valu.quality.quality.name == "string"
    assert _valu.quality.revision.version == 0
    assert _valu.quality.revision.real == 0
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert _valu.mediaInfo.audioBitrate == 0
    assert _valu.mediaInfo.audioChannels == 0.0
    assert _valu.mediaInfo.audioBits == 0
    assert _valu.mediaInfo.audioSampleRate == 0
    assert _valu.editionId == 0
    assert _valu.calibreId == 0
    assert _valu.part == 0
    _val = _valu.author.value
    assert _val.id == 0
    assert _val.authorMetadataId == 0
    assert _val.cleanName == "string"
    assert _val.monitored is True
    assert _val.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.path == "string"
    assert _val.rootFolderPath == "string"
    assert _val.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.qualityProfileId == 0
    assert _val.metadataProfileId == 0
    assert _val.tags == [0]
    assert _val.addOptions.monitor == "string"
    assert _val.addOptions.booksToMonitor == ["string"]
    assert _val.addOptions.monitored is True
    assert _val.addOptions.searchForMissingBooks is True
    assert _val.metadata.value.id == 0
    assert _val.metadata.value.foreignAuthorId == "string"
    assert _val.metadata.value.titleSlug == "string"
    assert _val.metadata.value.name == "string"
    assert _val.metadata.value.sortName == "string"
    assert _val.metadata.value.nameLastFirst == "string"
    assert _val.metadata.value.sortNameLastFirst == "string"
    assert _val.metadata.value.aliases == ["string"]
    assert _val.metadata.value.overview == "string"
    assert _val.metadata.value.disambiguation == "string"
    assert _val.metadata.value.gender == "string"
    assert _val.metadata.value.hometown == "string"
    assert _val.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.metadata.value.status == "string"
    assert _val.metadata.value.images[0].url == "string"
    assert _val.metadata.value.images[0].coverType == "string"
    assert _val.metadata.value.images[0].extension == "string"
    assert _val.metadata.value.links[0].url == "string"
    assert _val.metadata.value.links[0].name == "string"
    assert _val.metadata.value.genres == ["string"]
    assert _val.metadata.value.ratings.votes == 0
    assert _val.metadata.value.ratings.value == 0.0
    assert _val.metadata.value.ratings.popularity == 0.0
    assert _val.metadata.isLoaded is True
    assert _val.qualityProfile.value.id == 0
    assert _val.qualityProfile.value.name == "string"
    assert _val.qualityProfile.value.upgradeAllowed is True
    assert _val.qualityProfile.value.cutoff == 0
    assert _val.qualityProfile.value.items[0].id == 0
    assert _val.qualityProfile.value.items[0].name == "string"
    assert _val.qualityProfile.value.items[0].quality.id == 0
    assert _val.qualityProfile.value.items[0].quality.name == "string"
    assert _val.qualityProfile.value.items[0].items == [None]
    assert _val.qualityProfile.value.items[0].allowed is True
    assert _val.qualityProfile.isLoaded is True
    assert _val.metadataProfile.value.id == 0
    assert _val.metadataProfile.value.name == "string"
    assert _val.metadataProfile.value.minPopularity == 0.0
    assert _val.metadataProfile.value.skipMissingDate is True
    assert _val.metadataProfile.value.skipMissingIsbn is True
    assert _val.metadataProfile.value.skipPartsAndSets is True
    assert _val.metadataProfile.value.skipSeriesSecondary is True
    assert _val.metadataProfile.value.allowedLanguages == "string"
    assert _val.metadataProfile.value.minPages == 0
    assert _val.metadataProfile.value.ignored == "string"
    assert _val.metadataProfile.isLoaded is True
    assert _val.books.value == [None]
    assert _val.books.isLoaded is True
    assert _val.series.value[0].id == 0
    assert _val.series.value[0].foreignSeriesId == "string"
    assert _val.series.value[0].title == "string"
    assert _val.series.value[0].description == "string"
    assert _val.series.value[0].numbered is True
    assert _val.series.value[0].workCount == 0
    assert _val.series.value[0].primaryWorkCount == 0
    assert _val.series.value[0].books.value == [None]
    assert _val.series.value[0].books.isLoaded is True
    assert _val.series.value[0].foreignAuthorId == "string"
    assert _val.series.isLoaded is True
    assert _val.name == "string"
    assert _val.foreignAuthorId == "string"
    assert _valu.author.isLoaded is True
    assert _valu.edition.isLoaded is True
    assert _valu.partCount == 0
    assert _value.bookFiles.isLoaded is True
    assert _value.seriesLinks.value[0].id == 0
    assert _value.seriesLinks.value[0].position == "string"
    assert _value.seriesLinks.value[0].seriesId == 0
    assert _value.seriesLinks.value[0].bookId == 0
    assert _value.seriesLinks.value[0].isPrimary is True
    assert _value.seriesLinks.value[0].series.value.id == 0
    assert _value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _value.seriesLinks.value[0].series.value.title == "string"
    assert _value.seriesLinks.value[0].series.value.description == "string"
    assert _value.seriesLinks.value[0].series.value.numbered is True
    assert _value.seriesLinks.value[0].series.value.workCount == 0
    assert _value.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _value.seriesLinks.value[0].series.value.books.value == [None]
    assert _value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _value.seriesLinks.value[0].series.isLoaded is True
    assert _value.seriesLinks.value[0].book.isLoaded is True
    assert _value.seriesLinks.isLoaded is True
    assert data.author.images[0].url == "string"
    assert data.author.images[0].coverType == "string"
    assert data.author.images[0].extension == "string"
    assert data.author.remotePoster == "string"
    assert data.author.path == "string"
    assert data.author.qualityProfileId == 0
    assert data.author.metadataProfileId == 0
    assert data.author.monitored is True
    assert data.author.rootFolderPath == "string"
    assert data.author.genres == ["string"]
    assert data.author.cleanName == "string"
    assert data.author.sortName == "string"
    assert data.author.sortNameLastFirst == "string"
    assert data.author.tags == [0]
    assert data.author.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.addOptions.monitor == "string"
    assert data.author.addOptions.booksToMonitor == ["string"]
    assert data.author.addOptions.monitored is True
    assert data.author.addOptions.searchForMissingBooks is True
    assert data.author.ratings.votes == 0
    assert data.author.ratings.value == 0.0
    assert data.author.ratings.popularity == 0.0
    assert data.author.statistics.bookFileCount == 0
    assert data.author.statistics.bookCount == 0
    assert data.author.statistics.availableBookCount == 0
    assert data.author.statistics.totalBookCount == 0
    assert data.author.statistics.sizeOnDisk == 0
    assert data.author.statistics.percentOfBooks == 0.0
    assert data.books[0].id == 0
    assert data.books[0].title == "string"
    assert data.books[0].authorTitle == "string"
    assert data.books[0].seriesTitle == "string"
    assert data.books[0].disambiguation == "string"
    assert data.books[0].overview == "string"
    assert data.books[0].authorId == 0
    assert data.books[0].foreignBookId == "string"
    assert data.books[0].titleSlug == "string"
    assert data.books[0].monitored is True
    assert data.books[0].anyEditionOk is True
    assert data.books[0].ratings.votes == 0
    assert data.books[0].ratings.value == 0.0
    assert data.books[0].ratings.popularity == 0.0
    assert data.books[0].releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.books[0].pageCount == 0
    assert data.books[0].genres == ["string"]
    assert data.books[0].author.id == 0
    assert data.books[0].author.authorMetadataId == 0
    assert data.books[0].author.status == "string"
    assert data.books[0].author.ended is True
    assert data.books[0].author.authorName == "string"
    assert data.books[0].author.authorNameLastFirst == "string"
    assert data.books[0].author.foreignAuthorId == "string"
    assert data.books[0].author.titleSlug == "string"
    assert data.books[0].author.overview == "string"
    assert data.books[0].author.disambiguation == "string"
    assert data.books[0].author.links[0].url == "string"
    assert data.books[0].author.links[0].name == "string"
    _book = data.books[0].author.nextBook
    assert _book.id == 0
    assert _book.authorMetadataId == 0
    assert _book.foreignBookId == "string"
    assert _book.titleSlug == "string"
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres == ["string"]
    assert _book.ratings.votes == 0
    assert _book.ratings.value == 0.0
    assert _book.ratings.popularity == 0.0
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.addOptions.addType == "string"
    assert _book.addOptions.searchForNewBook is True
    assert _book.authorMetadata.value.id == 0
    assert _book.authorMetadata.value.foreignAuthorId == "string"
    assert _book.authorMetadata.value.titleSlug == "string"
    assert _book.authorMetadata.value.name == "string"
    assert _book.authorMetadata.value.sortName == "string"
    assert _book.authorMetadata.value.sortNameLastFirst == "string"
    assert _book.authorMetadata.value.aliases == ["string"]
    assert _book.authorMetadata.value.overview == "string"
    assert _book.authorMetadata.value.disambiguation == "string"
    assert _book.authorMetadata.value.gender == "string"
    assert _book.authorMetadata.value.hometown == "string"
    assert _book.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.authorMetadata.value.status == "string"
    assert _book.authorMetadata.value.images[0].url == "string"
    assert _book.authorMetadata.value.images[0].coverType == "string"
    assert _book.authorMetadata.value.images[0].extension == "string"
    assert _book.authorMetadata.value.links[0].url == "string"
    assert _book.authorMetadata.value.links[0].name == "string"
    assert _book.authorMetadata.value.genres == ["string"]
    assert _book.authorMetadata.value.ratings.votes == 0
    assert _book.authorMetadata.value.ratings.value == 0.0
    assert _book.authorMetadata.value.ratings.popularity == 0.0
    assert _book.authorMetadata.isLoaded is True
    assert _book.author.value.id == 0
    assert _book.author.value.authorMetadataId == 0
    assert _book.author.value.cleanName == "string"
    assert _book.author.value.monitored is True
    assert _book.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.author.value.path == "string"
    assert _book.author.value.rootFolderPath == "string"
    assert _book.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.author.value.qualityProfileId == 0
    assert _book.author.value.metadataProfileId == 0
    assert _book.author.value.tags == [0]
    assert _book.author.value.addOptions.monitor == "string"
    assert _book.author.value.addOptions.booksToMonitor == ["string"]
    assert _book.author.value.addOptions.monitored is True
    assert _book.author.value.addOptions.searchForMissingBooks is True
    _valu = _book.author.value.metadata.value
    assert _valu.id == 0
    assert _valu.foreignAuthorId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases == ["string"]
    assert _valu.overview == "string"
    assert _valu.disambiguation == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _book.author.value.metadata.isLoaded is True
    assert _book.author.value.qualityProfile.value.id == 0
    assert _book.author.value.qualityProfile.value.name == "string"
    assert _book.author.value.qualityProfile.value.upgradeAllowed is True
    assert _book.author.value.qualityProfile.value.cutoff == 0
    assert _book.author.value.qualityProfile.value.items[0].id == 0
    assert _book.author.value.qualityProfile.value.items[0].name == "string"
    assert _book.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _book.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _book.author.value.qualityProfile.value.items[0].items == [None]
    assert _book.author.value.qualityProfile.value.items[0].allowed is True
    assert _book.author.value.qualityProfile.isLoaded is True
    assert _book.author.value.metadataProfile.value.id == 0
    assert _book.author.value.metadataProfile.value.name == "string"
    assert _book.author.value.metadataProfile.value.minPopularity == 0.0
    assert _book.author.value.metadataProfile.value.skipMissingDate is True
    assert _book.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _book.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _book.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _book.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _book.author.value.metadataProfile.value.minPages == 0
    assert _book.author.value.metadataProfile.value.ignored == "string"
    assert _book.author.value.metadataProfile.isLoaded is True
    assert _book.author.value.books.value == [None]
    assert _book.author.value.books.isLoaded is True
    assert _book.author.value.series.value[0].id == 0
    assert _book.author.value.series.value[0].foreignSeriesId == "string"
    assert _book.author.value.series.value[0].title == "string"
    assert _book.author.value.series.value[0].description == "string"
    assert _book.author.value.series.value[0].numbered is True
    assert _book.author.value.series.value[0].workCount == 0
    assert _book.author.value.series.value[0].primaryWorkCount == 0
    assert _book.author.value.series.value[0].books.value == [None]
    assert _book.author.value.series.value[0].books.isLoaded is True
    assert _book.author.value.series.value[0].foreignAuthorId == "string"
    assert _book.author.value.series.isLoaded is True
    assert _book.author.value.name == "string"
    assert _book.author.value.foreignAuthorId == "string"
    assert _book.author.isLoaded is True
    _valu = _book.editions.value[0]
    assert _valu.id == 0
    assert _valu.bookId == 0
    assert _valu.foreignEditionId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.disambiguation == "string"
    assert _valu.publisher == "string"
    assert _valu.pageCount == 0
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == "string"
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags == [0]
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert _va.id == 0
    assert _va.foreignAuthorId == "string"
    assert _va.titleSlug == "string"
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.disambiguation == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == "string"
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert _va.ratings.votes == 0
    assert _va.ratings.value == 0.0
    assert _va.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value == [None]
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert _valu.bookFiles.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags == [0]
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert _va.id == 0
    assert _va.foreignAuthorId == "string"
    assert _va.titleSlug == "string"
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.disambiguation == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == "string"
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert _va.ratings.votes == 0
    assert _va.ratings.value == 0.0
    assert _va.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert _book.bookFiles.isLoaded is True
    assert _book.seriesLinks.value[0].id == 0
    assert _book.seriesLinks.value[0].position == "string"
    assert _book.seriesLinks.value[0].seriesId == 0
    assert _book.seriesLinks.value[0].bookId == 0
    assert _book.seriesLinks.value[0].isPrimary is True
    assert _book.seriesLinks.value[0].series.value.id == 0
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert _book.seriesLinks.value[0].series.value.workCount == 0
    assert _book.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    _valu = data.books[0].author.lastBook
    assert _valu.id == 0
    assert _valu.authorMetadataId == 0
    assert _valu.foreignBookId == "string"
    assert _valu.titleSlug == "string"
    assert _valu.title == "string"
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert _valu.ratings.votes == 0
    assert _valu.ratings.value == 0.0
    assert _valu.ratings.popularity == 0.0
    assert _valu.cleanTitle == "string"
    assert _valu.monitored is True
    assert _valu.anyEditionOk is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.addOptions.addType == "string"
    assert _valu.addOptions.searchForNewBook is True
    assert _valu.authorMetadata.value.id == 0
    assert _valu.authorMetadata.value.foreignAuthorId == "string"
    assert _valu.authorMetadata.value.titleSlug == "string"
    assert _valu.authorMetadata.value.name == "string"
    assert _valu.authorMetadata.value.sortName == "string"
    assert _valu.authorMetadata.value.sortNameLastFirst == "string"
    assert _valu.authorMetadata.value.aliases == ["string"]
    assert _valu.authorMetadata.value.overview == "string"
    assert _valu.authorMetadata.value.disambiguation == "string"
    assert _valu.authorMetadata.value.gender == "string"
    assert _valu.authorMetadata.value.hometown == "string"
    assert _valu.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.authorMetadata.value.status == "string"
    assert _valu.authorMetadata.value.images[0].url == "string"
    assert _valu.authorMetadata.value.images[0].coverType == "string"
    assert _valu.authorMetadata.value.images[0].extension == "string"
    assert _valu.authorMetadata.value.links[0].url == "string"
    assert _valu.authorMetadata.value.links[0].name == "string"
    assert _valu.authorMetadata.value.genres == ["string"]
    assert _valu.authorMetadata.value.ratings.votes == 0
    assert _valu.authorMetadata.value.ratings.value == 0.0
    assert _valu.authorMetadata.value.ratings.popularity == 0.0
    assert _valu.authorMetadata.isLoaded is True
    assert _valu.author.value.id == 0
    assert _valu.author.value.authorMetadataId == 0
    assert _valu.author.value.cleanName == "string"
    assert _valu.author.value.monitored is True
    assert _valu.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.author.value.path == "string"
    assert _valu.author.value.rootFolderPath == "string"
    assert _valu.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.author.value.qualityProfileId == 0
    assert _valu.author.value.metadataProfileId == 0
    assert _valu.author.value.tags == [0]
    assert _valu.author.value.addOptions.monitor == "string"
    assert _valu.author.value.addOptions.booksToMonitor == ["string"]
    assert _valu.author.value.addOptions.monitored is True
    assert _valu.author.value.addOptions.searchForMissingBooks is True
    _val = _valu.author.value.metadata.value
    assert _val.id == 0
    assert _val.foreignAuthorId == "string"
    assert _val.titleSlug == "string"
    assert _val.name == "string"
    assert _val.sortName == "string"
    assert _val.nameLastFirst == "string"
    assert _val.sortNameLastFirst == "string"
    assert _val.aliases == ["string"]
    assert _val.overview == "string"
    assert _val.disambiguation == "string"
    assert _val.gender == "string"
    assert _val.hometown == "string"
    assert _val.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.status == "string"
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == "string"
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres == ["string"]
    assert _val.ratings.votes == 0
    assert _val.ratings.value == 0.0
    assert _val.ratings.popularity == 0.0
    assert _valu.author.value.metadata.isLoaded is True
    assert _valu.author.value.qualityProfile.value.id == 0
    assert _valu.author.value.qualityProfile.value.name == "string"
    assert _valu.author.value.qualityProfile.value.upgradeAllowed is True
    assert _valu.author.value.qualityProfile.value.cutoff == 0
    assert _valu.author.value.qualityProfile.value.items[0].id == 0
    assert _valu.author.value.qualityProfile.value.items[0].name == "string"
    assert _valu.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _valu.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.author.value.qualityProfile.value.items[0].items == [None]
    assert _valu.author.value.qualityProfile.value.items[0].allowed is True
    assert _valu.author.value.qualityProfile.isLoaded is True
    assert _valu.author.value.metadataProfile.value.id == 0
    assert _valu.author.value.metadataProfile.value.name == "string"
    assert _valu.author.value.metadataProfile.value.minPopularity == 0.0
    assert _valu.author.value.metadataProfile.value.skipMissingDate is True
    assert _valu.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _valu.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _valu.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _valu.author.value.metadataProfile.value.minPages == 0
    assert _valu.author.value.metadataProfile.value.ignored == "string"
    assert _valu.author.value.metadataProfile.isLoaded is True
    assert _valu.author.value.books.value == [None]
    assert _valu.author.value.books.isLoaded is True
    assert _valu.author.value.series.value[0].id == 0
    assert _valu.author.value.series.value[0].foreignSeriesId == "string"
    assert _valu.author.value.series.value[0].title == "string"
    assert _valu.author.value.series.value[0].description == "string"
    assert _valu.author.value.series.value[0].numbered is True
    assert _valu.author.value.series.value[0].workCount == 0
    assert _valu.author.value.series.value[0].primaryWorkCount == 0
    assert _valu.author.value.series.value[0].books.value == [None]
    assert _valu.author.value.series.value[0].books.isLoaded is True
    assert _valu.author.value.series.value[0].foreignAuthorId == "string"
    assert _valu.author.value.series.isLoaded is True
    assert _valu.author.value.name == "string"
    assert _valu.author.value.foreignAuthorId == "string"
    assert _valu.author.isLoaded is True
    _val = _valu.editions.value[0]
    assert _val.id == 0
    assert _val.bookId == 0
    assert _val.foreignEditionId == "string"
    assert _val.titleSlug == "string"
    assert _val.isbn13 == "string"
    assert _val.asin == "string"
    assert _val.title == "string"
    assert _val.language == "string"
    assert _val.overview == "string"
    assert _val.format == "string"
    assert _val.isEbook is True
    assert _val.disambiguation == "string"
    assert _val.publisher == "string"
    assert _val.pageCount == 0
    assert _val.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == "string"
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.ratings.votes == 0
    assert _val.ratings.value == 0.0
    assert _val.ratings.popularity == 0.0
    assert _val.monitored is True
    assert _val.manualAdd is True
    assert _val.book.isLoaded is True
    assert _val.bookFiles.value[0].id == 0
    assert _val.bookFiles.value[0].path == "string"
    assert _val.bookFiles.value[0].size == 0
    assert _val.bookFiles.value[0].modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.bookFiles.value[0].dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.bookFiles.value[0].sceneName == "string"
    assert _val.bookFiles.value[0].releaseGroup == "string"
    assert _val.bookFiles.value[0].quality.quality.id == 0
    assert _val.bookFiles.value[0].quality.quality.name == "string"
    assert _val.bookFiles.value[0].quality.revision.version == 0
    assert _val.bookFiles.value[0].quality.revision.real == 0
    assert _val.bookFiles.value[0].quality.revision.isRepack is True
    assert _val.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert _val.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _val.bookFiles.value[0].mediaInfo.audioChannels == 0.0
    assert _val.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _val.bookFiles.value[0].mediaInfo.audioSampleRate == 0
    assert _val.bookFiles.value[0].editionId == 0
    assert _val.bookFiles.value[0].calibreId == 0
    assert _val.bookFiles.value[0].part == 0
    _va = _val.bookFiles.value[0].author.value
    assert _va.id == 0
    assert _va.authorMetadataId == 0
    assert _va.cleanName == "string"
    assert _va.monitored is True
    assert _va.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.path == "string"
    assert _va.rootFolderPath == "string"
    assert _va.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.qualityProfileId == 0
    assert _va.metadataProfileId == 0
    assert _va.tags == [0]
    assert _va.addOptions.monitor == "string"
    assert _va.addOptions.booksToMonitor == ["string"]
    assert _va.addOptions.monitored is True
    assert _va.addOptions.searchForMissingBooks is True
    assert _va.metadata.value.id == 0
    assert _va.metadata.value.foreignAuthorId == "string"
    assert _va.metadata.value.titleSlug == "string"
    assert _va.metadata.value.name == "string"
    assert _va.metadata.value.sortName == "string"
    assert _va.metadata.value.nameLastFirst == "string"
    assert _va.metadata.value.sortNameLastFirst == "string"
    assert _va.metadata.value.aliases == ["string"]
    assert _va.metadata.value.overview == "string"
    assert _va.metadata.value.disambiguation == "string"
    assert _va.metadata.value.gender == "string"
    assert _va.metadata.value.hometown == "string"
    assert _va.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.metadata.value.status == "string"
    assert _va.metadata.value.images[0].url == "string"
    assert _va.metadata.value.images[0].coverType == "string"
    assert _va.metadata.value.images[0].extension == "string"
    assert _va.metadata.value.links[0].url == "string"
    assert _va.metadata.value.links[0].name == "string"
    assert _va.metadata.value.genres == ["string"]
    assert _va.metadata.value.ratings.votes == 0
    assert _va.metadata.value.ratings.value == 0.0
    assert _va.metadata.value.ratings.popularity == 0.0
    assert _va.metadata.isLoaded is True
    assert _va.qualityProfile.value.id == 0
    assert _va.qualityProfile.value.name == "string"
    assert _va.qualityProfile.value.upgradeAllowed is True
    assert _va.qualityProfile.value.cutoff == 0
    assert _va.qualityProfile.value.items[0].id == 0
    assert _va.qualityProfile.value.items[0].name == "string"
    assert _va.qualityProfile.value.items[0].quality.id == 0
    assert _va.qualityProfile.value.items[0].quality.name == "string"
    assert _va.qualityProfile.value.items[0].items == [None]
    assert _va.qualityProfile.value.items[0].allowed is True
    assert _va.qualityProfile.isLoaded is True
    assert _va.metadataProfile.value.id == 0
    assert _va.metadataProfile.value.name == "string"
    assert _va.metadataProfile.value.minPopularity == 0.0
    assert _va.metadataProfile.value.skipMissingDate is True
    assert _va.metadataProfile.value.skipMissingIsbn is True
    assert _va.metadataProfile.value.skipPartsAndSets is True
    assert _va.metadataProfile.value.skipSeriesSecondary is True
    assert _va.metadataProfile.value.allowedLanguages == "string"
    assert _va.metadataProfile.value.minPages == 0
    assert _va.metadataProfile.value.ignored == "string"
    assert _va.metadataProfile.isLoaded is True
    assert _va.books.value == [None]
    assert _va.books.isLoaded is True
    assert _va.series.value[0].id == 0
    assert _va.series.value[0].foreignSeriesId == "string"
    assert _va.series.value[0].title == "string"
    assert _va.series.value[0].description == "string"
    assert _va.series.value[0].numbered is True
    assert _va.series.value[0].workCount == 0
    assert _va.series.value[0].primaryWorkCount == 0
    assert _va.series.value[0].books.value == [None]
    assert _va.series.value[0].books.isLoaded is True
    assert _va.series.value[0].foreignAuthorId == "string"
    assert _va.series.isLoaded is True
    assert _va.name == "string"
    assert _va.foreignAuthorId == "string"
    assert _val.bookFiles.value[0].author.isLoaded is True
    assert _val.bookFiles.value[0].edition.isLoaded is True
    assert _val.bookFiles.value[0].partCount == 0
    assert _val.bookFiles.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert _val.id == 0
    assert _val.path == "string"
    assert _val.size == 0
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert _val.quality.quality.id == 0
    assert _val.quality.quality.name == "string"
    assert _val.quality.revision.version == 0
    assert _val.quality.revision.real == 0
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert _val.mediaInfo.audioBitrate == 0
    assert _val.mediaInfo.audioChannels == 0.0
    assert _val.mediaInfo.audioBits == 0
    assert _val.mediaInfo.audioSampleRate == 0
    assert _val.editionId == 0
    assert _val.calibreId == 0
    assert _val.part == 0
    assert _val.author.value.id == 0
    assert _val.author.value.authorMetadataId == 0
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.qualityProfileId == 0
    assert _val.author.value.metadataProfileId == 0
    assert _val.author.value.tags == [0]
    assert _val.author.value.addOptions.monitor == "string"
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert _va.id == 0
    assert _va.foreignAuthorId == "string"
    assert _va.titleSlug == "string"
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.disambiguation == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == "string"
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert _va.ratings.votes == 0
    assert _va.ratings.value == 0.0
    assert _va.ratings.popularity == 0.0
    assert _val.author.value.metadata.isLoaded is True
    assert _val.author.value.qualityProfile.value.id == 0
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert _val.author.value.qualityProfile.value.cutoff == 0
    assert _val.author.value.qualityProfile.value.items[0].id == 0
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].quality.id == 0
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert _val.author.value.metadataProfile.value.id == 0
    assert _val.author.value.metadataProfile.value.name == "string"
    assert _val.author.value.metadataProfile.value.minPopularity == 0.0
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert _val.author.value.metadataProfile.value.minPages == 0
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert _val.author.value.series.value[0].id == 0
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert _val.author.value.series.value[0].workCount == 0
    assert _val.author.value.series.value[0].primaryWorkCount == 0
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert _val.partCount == 0
    assert _valu.bookFiles.isLoaded is True
    assert _valu.seriesLinks.value[0].id == 0
    assert _valu.seriesLinks.value[0].position == "string"
    assert _valu.seriesLinks.value[0].seriesId == 0
    assert _valu.seriesLinks.value[0].bookId == 0
    assert _valu.seriesLinks.value[0].isPrimary is True
    assert _valu.seriesLinks.value[0].series.value.id == 0
    assert _valu.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _valu.seriesLinks.value[0].series.value.title == "string"
    assert _valu.seriesLinks.value[0].series.value.description == "string"
    assert _valu.seriesLinks.value[0].series.value.numbered is True
    assert _valu.seriesLinks.value[0].series.value.workCount == 0
    assert _valu.seriesLinks.value[0].series.value.primaryWorkCount == 0
    assert _valu.seriesLinks.value[0].series.value.books.value == [None]
    assert _valu.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _valu.seriesLinks.value[0].series.isLoaded is True
    assert _valu.seriesLinks.value[0].book.isLoaded is True
    assert _valu.seriesLinks.isLoaded is True
    assert data.books[0].author.images[0].url == "string"
    assert data.books[0].author.images[0].coverType == "string"
    assert data.books[0].author.images[0].extension == "string"
    assert data.books[0].author.remotePoster == "string"
    assert data.books[0].author.path == "string"
    assert data.books[0].author.qualityProfileId == 0
    assert data.books[0].author.metadataProfileId == 0
    assert data.books[0].author.monitored is True
    assert data.books[0].author.rootFolderPath == "string"
    assert data.books[0].author.genres == ["string"]
    assert data.books[0].author.cleanName == "string"
    assert data.books[0].author.sortName == "string"
    assert data.books[0].author.sortNameLastFirst == "string"
    assert data.books[0].author.tags == [0]
    assert data.books[0].author.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert data.books[0].author.addOptions.monitor == "string"
    assert data.books[0].author.addOptions.booksToMonitor == ["string"]
    assert data.books[0].author.addOptions.monitored is True
    assert data.books[0].author.addOptions.searchForMissingBooks is True
    assert data.books[0].author.ratings.votes == 0
    assert data.books[0].author.ratings.value == 0.0
    assert data.books[0].author.ratings.popularity == 0.0
    assert data.books[0].author.statistics.bookFileCount == 0
    assert data.books[0].author.statistics.bookCount == 0
    assert data.books[0].author.statistics.availableBookCount == 0
    assert data.books[0].author.statistics.totalBookCount == 0
    assert data.books[0].author.statistics.sizeOnDisk == 0
    assert data.books[0].author.statistics.percentOfBooks == 0.0
    assert data.books[0].images[0].url == "string"
    assert data.books[0].images[0].coverType == "string"
    assert data.books[0].images[0].extension == "string"
    assert data.books[0].links[0].url == "string"
    assert data.books[0].links[0].name == "string"
    assert data.books[0].statistics.bookFileCount == 0
    assert data.books[0].statistics.bookCount == 0
    assert data.books[0].statistics.totalBookCount == 0
    assert data.books[0].statistics.sizeOnDisk == 0
    assert data.books[0].statistics.percentOfBooks == 0.0
    assert data.books[0].added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert data.books[0].addOptions.addType == "string"
    assert data.books[0].addOptions.searchForNewBook is True
    assert data.books[0].remoteCover == "string"
    assert data.books[0].remoteCover == "string"
    _value = data.books[0].editions[0]
    assert _value.id == 0
    assert _value.bookId == 0
    assert _value.foreignEditionId == "string"
    assert _value.titleSlug == "string"
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert _value.pageCount == 0
    assert _value.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0.0
    assert _value.ratings.popularity == 0.0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.remoteCover == "string"
    assert _value.grabbed is True
    assert data.books[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_queue(aresponses):
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/queue?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortDirection=ascending&sortKey=timeleft&includeUnknownAuthorItems=False&includeAuthor=False&includeBook=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/queue.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue()
    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == "timeleft"
    assert data.sortDirection == "ascending"
    assert data.totalRecords == 1
    assert data.records[0].authorId == 0
    assert data.records[0].bookId == 0
    assert data.records[0].author
    assert data.records[0].book
    assert data.records[0].quality.quality.id == 0
    assert data.records[0].quality.quality.name == "string"
    assert data.records[0].quality.revision.version == 0
    assert data.records[0].quality.revision.real == 0
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].size == 0
    assert data.records[0].title == "string"
    assert data.records[0].sizeleft == 0
    assert data.records[0].timeleft == "00:00:00"
    assert data.records[0].estimatedCompletionTime == datetime(2020, 2, 9, 23, 22, 30)
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
    assert data.records[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue_details(aresponses):
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/queue/details?apikey=ur1234567-0abc12de3f456gh7ij89k012&includeUnknownAuthorItems=False&includeAuthor=False&includeBook=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_queue_details()
    assert data[0].authorId == 0
    assert data[0].bookId == 0
    assert data[0].author
    assert data[0].book
    assert data[0].book.title == "string"
    assert data[0].book.authorTitle == "string"
    assert data[0].book.seriesTitle == "string"
    assert data[0].book.disambiguation == "string"
    assert data[0].book.overview == "string"
    assert data[0].book.authorId == 0
    assert data[0].book.foreignBookId == "0"
    assert data[0].book.titleSlug == "0"
    assert data[0].book.monitored is True
    assert data[0].book.anyEditionOk is True
    assert data[0].book.ratings.votes == 0
    assert data[0].book.ratings.value == 0.0
    assert data[0].book.ratings.popularity == 0.0
    assert data[0].book.releaseDate == datetime(2021, 11, 22, 0, 0)
    assert data[0].book.pageCount == 0
    assert data[0].book.genres == ["string"]
    assert data[0].book.author.authorMetadataId == 0
    assert data[0].book.author.status == "string"
    assert data[0].book.author.ended is False
    assert data[0].book.author.authorName == "string"
    assert data[0].book.author.authorNameLastFirst == "string"
    assert data[0].book.author.foreignAuthorId == "0"
    assert data[0].book.author.titleSlug == "0"
    assert data[0].book.author.overview == "string"
    assert data[0].book.author.links[0].url == "string"
    assert data[0].book.author.links[0].name == "string"
    assert data[0].book.author.images[0].url == "string"
    assert data[0].book.author.images[0].coverType == "string"
    assert data[0].book.author.images[0].extension == "string"
    assert data[0].book.author.path == "string"
    assert data[0].book.author.qualityProfileId == 0
    assert data[0].book.author.metadataProfileId == 0
    assert data[0].book.author.monitored is True
    assert data[0].book.author.monitorNewItems == "string"
    assert data[0].book.author.genres == ["string"]
    assert data[0].book.author.cleanName == "string"
    assert data[0].book.author.sortName == "string"
    assert data[0].book.author.sortNameLastFirst == "string"
    assert data[0].book.author.tags == [0]
    assert data[0].book.author.added == datetime(2021, 12, 6, 23, 38, 3)
    assert data[0].book.author.ratings.votes == 0
    assert data[0].book.author.ratings.value == 0.0
    assert data[0].book.author.ratings.popularity == 0.0
    assert data[0].book.author.statistics.bookFileCount == 0
    assert data[0].book.author.statistics.bookCount == 0
    assert data[0].book.author.statistics.availableBookCount == 0
    assert data[0].book.author.statistics.totalBookCount == 0
    assert data[0].book.author.statistics.sizeOnDisk == 0
    assert data[0].book.author.statistics.percentOfBooks == 0.0
    assert data[0].book.author.id == 0
    assert data[0].book.images[0].url == "string"
    assert data[0].book.images[0].coverType == "string"
    assert data[0].book.images[0].extension == "string"
    assert data[0].book.links[0].url == "string"
    assert data[0].book.links[0].name == "string"
    assert data[0].book.added == datetime(2021, 12, 6, 23, 53, 58)
    assert data[0].book.editions[0].bookId == 0
    assert data[0].book.editions[0].foreignEditionId == 0
    assert data[0].book.editions[0].titleSlug == 0
    assert data[0].book.editions[0].isbn13 == 0
    assert data[0].book.editions[0].title == "string"
    assert data[0].book.editions[0].language == "string"
    assert data[0].book.editions[0].overview == "string"
    assert data[0].book.editions[0].format == "string"
    assert data[0].book.editions[0].isEbook is False
    assert data[0].book.editions[0].disambiguation == "string"
    assert data[0].book.editions[0].publisher == "string"
    assert data[0].book.editions[0].pageCount == 0
    assert data[0].book.editions[0].releaseDate == datetime(2021, 11, 25, 0, 0)
    assert data[0].book.editions[0].images[0].url == "string"
    assert data[0].book.editions[0].images[0].coverType == "string"
    assert data[0].book.editions[0].images[0].extension == "string"
    assert data[0].book.editions[0].links[0].url == "string"
    assert data[0].book.editions[0].links[0].name == "string"
    assert data[0].book.editions[0].ratings.votes == 0
    assert data[0].book.editions[0].ratings.value == 0.0
    assert data[0].book.editions[0].ratings.popularity == 0.0
    assert data[0].book.editions[0].monitored is False
    assert data[0].book.editions[0].manualAdd is False
    assert data[0].book.editions[0].grabbed is False
    assert data[0].book.editions[0].id == 0
    assert data[0].book.grabbed is False
    assert data[0].book.id == 0
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
    assert data[0].quality.revision.version == 0
    assert data[0].quality.revision.real == 0
    assert data[0].quality.revision.isRepack is False
    assert data[0].size == 0
    assert data[0].title == "string"
    assert data[0].sizeleft == 0
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2020, 2, 7, 11, 27, 27)
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
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_release(aresponses):
    """Test searching indexers for specified fields."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/release?apikey=ur1234567-0abc12de3f456gh7ij89k012&authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/release.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_release(authorid=0, bookid=0)
    assert data[0].guid == "string"
    assert data[0].quality.quality.id == 0
    assert data[0].quality.quality.name == "string"
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
    assert data[0].title == "string"
    assert data[0].discography is False
    assert data[0].sceneSource is False
    assert data[0].authorName == "string"
    assert data[0].bookTitle == "string"
    assert data[0].approved is False
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is True
    assert data[0].rejections == ["string"]
    assert data[0].publishDate == datetime(2021, 11, 23, 5, 0)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].downloadAllowed is True
    assert data[0].releaseWeight == 0
    assert data[0].preferredWordScore == 0
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert data[0].seeders == 0
    assert data[0].leechers == 0
    assert data[0].protocol == "string"


@pytest.mark.asyncio
async def test_async_get_rename(aresponses):
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/rename?apikey=ur1234567-0abc12de3f456gh7ij89k012&authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/rename.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_rename()
    assert data[0].authorId == 0
    assert data[0].bookId == 0
    assert data[0].bookFileId == 0
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_retag(aresponses):
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/retag?apikey=ur1234567-0abc12de3f456gh7ij89k012&authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/retag.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_retag()
    assert data[0].authorId == 0
    assert data[0].bookId == 0
    assert data[0].trackNumbers == [0]
    assert data[0].bookFileId == 0
    assert data[0].path == "string"
    assert data[0].changes[0].field == "string"
    assert data[0].changes[0].oldValue == "string"
    assert data[0].changes[0].newValue == "string"


@pytest.mark.asyncio
async def test_async_search(aresponses):
    """Test search."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/search?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/search.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_search("test")
    assert data[0].foreignId == "0"
    assert data[0].author.authorMetadataId == 0
    assert data[0].author.status == "string"
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "0"
    assert data[0].author.titleSlug == "0"
    assert data[0].author.overview == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == "string"
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert data[0].author.qualityProfileId == 0
    assert data[0].author.metadataProfileId == 0
    assert data[0].author.monitored is True
    assert data[0].author.monitorNewItems == "string"
    assert data[0].author.genres == ["string"]
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert data[0].author.tags == [0]
    assert data[0].author.added == datetime(2021, 10, 6, 23, 38, 49)
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0.0
    assert data[0].author.ratings.popularity == 0.0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0.0
    assert data[0].author.id == 0
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_series(aresponses):
    """Test search."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/series?apikey=ur1234567-0abc12de3f456gh7ij89k012&authorId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/series.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_series(0)
    assert data[0].title == "string"
    assert data[0].description == "string"
    assert data[0].links[0].position == "string"
    assert data[0].links[0].seriesPosition == 0
    assert data[0].links[0].seriesId == 0
    assert data[0].links[0].bookId == 0
    assert data[0].links[0].id == 0
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses):
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/tag/detail/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_tags_details(tagid=0)

    assert data.id == 0
    assert data.label == "string"
    assert data.delayProfileIds == [0]
    assert data.notificationIds == [0]
    assert data.restrictionIds == [0]
    assert data.importListIds == [0]
    assert data.authorIds == [0]


@pytest.mark.asyncio
async def test_readarr_bookshelf():
    """Test readarr bookshelf model."""
    item = PyArrResponse(
        data={ATTR_DATA: json.loads(load_fixture("readarr/bookshelf.json"))},
        datatype=ReadarrBookshelf,
    )
    assert isinstance(item.data, ReadarrBookshelf)
    assert item.data.authors[0].id == 0
    assert item.data.authors[0].monitored is True
    _value = item.data.authors[0].books[0]
    assert _value.id == 0
    assert _value.title == "string"
    assert _value.authorTitle == "string"
    assert _value.seriesTitle == "string"
    assert _value.disambiguation == "string"
    assert _value.overview == "string"
    assert _value.authorId == 0
    assert _value.foreignBookId == "string"
    assert _value.titleSlug == "string"
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.pageCount == 0
    assert _value.genres[0] == "string"
    _value = item.data.authors[0].books[0].author
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.status == "string"
    assert _value.authorName == "string"
    assert _value.authorNameLastFirst == "string"
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.nextBook.id == 0
    assert _value.nextBook.authorMetadataId == 0
    assert _value.nextBook.foreignBookId == "string"
    assert _value.nextBook.titleSlug == "string"
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert _value.nextBook.ratings.votes == 0
    assert _value.nextBook.ratings.value == 0
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.addOptions.addType == "string"
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = item.data.authors[0].books[0].author.nextBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    _value = item.data.authors[0].books[0].author.nextBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert isinstance(_value.books, _ReadarrAuthorValueBooks)
    assert isinstance(_value.series, _ReadarrAuthorValueSeries)
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = item.data.authors[0].books[0].author.nextBook
    assert isinstance(_book.editions, _ReadarrEditions)
    assert isinstance(_book.bookFiles, _ReadarrEditionsValueBookFiles)
    assert isinstance(_book.seriesLinks, _ReadarrSeriesLinks)
    _book = _book
    assert _book.id == 0
    assert _book.authorMetadataId == 0
    assert _book.foreignBookId == "string"
    assert _book.titleSlug == "string"
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert _book.ratings.votes == 0
    assert _book.ratings.value == 0
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.addOptions.addType == "string"
    assert _book.addOptions.searchForNewBook is True
    _value = item.data.authors[0].books[0].author.lastBook.authorMetadata.value
    assert _value.id == 0
    assert _value.foreignAuthorId == "string"
    assert _value.titleSlug == "string"
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    _value = item.data.authors[0].books[0].author.lastBook.author.value
    assert _value.id == 0
    assert _value.authorMetadataId == 0
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "string"
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert _value.metadata.value.id == 0
    assert _value.metadata.value.foreignAuthorId == "string"
    assert _value.metadata.value.titleSlug == "string"
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.disambiguation == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.qualityProfile.value.id == 0
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert _value.qualityProfile.value.cutoff == 0
    assert _value.qualityProfile.value.items[0].id == 0
    assert _value.qualityProfile.value.items[0].name == "string"
    assert _value.qualityProfile.value.items[0].quality.id == 0
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.metadataProfile.value.id == 0
    assert _value.metadataProfile.value.name == "string"
    assert _value.metadataProfile.value.minPopularity == 0.0
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert _value.metadataProfile.value.minPages == 0
    assert _value.metadataProfile.value.ignored == "string"
    assert isinstance(_value.books, _ReadarrAuthorValueBooks)
    assert isinstance(_value.series, _ReadarrAuthorValueSeries)
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = item.data.authors[0].books[0].author.lastBook
    assert isinstance(_book.editions, _ReadarrEditions)
    assert isinstance(_book.bookFiles, _ReadarrEditionsValueBookFiles)
    assert isinstance(_book.seriesLinks, _ReadarrSeriesLinks)
    _value = item.data.authors[0].books[0]
    assert _value.author.images[0].url == "string"
    assert _value.author.images[0].coverType == "string"
    assert _value.author.remotePoster == "string"
    assert _value.author.path == "string"
    assert _value.author.qualityProfileId == 0
    assert _value.author.metadataProfileId == 0
    assert _value.author.monitored is True
    assert _value.author.rootFolderPath == "string"
    assert _value.author.genres[0] == "string"
    assert _value.author.cleanName == "string"
    assert _value.author.sortName == "string"
    assert _value.author.sortNameLastFirst == "string"
    assert _value.author.tags[0] == 0
    assert _value.author.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.author.addOptions.monitor == "string"
    assert _value.author.addOptions.booksToMonitor[0] == "string"
    assert _value.author.addOptions.monitored is True
    assert _value.author.addOptions.searchForMissingBooks is True
    assert _value.author.ratings.votes == 0
    assert _value.author.ratings.value == 0
    assert _value.author.statistics.bookFileCount == 0
    assert _value.author.statistics.bookCount == 0
    assert _value.author.statistics.availableBookCount == 0
    assert _value.author.statistics.totalBookCount == 0
    assert _value.author.statistics.sizeOnDisk == 0
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.statistics.bookFileCount == 0
    assert _value.statistics.bookCount == 0
    assert _value.statistics.totalBookCount == 0
    assert _value.statistics.sizeOnDisk == 0
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.addOptions.addType == "string"
    assert _value.addOptions.searchForNewBook is True
    assert _value.remoteCover == "string"
    _editions = item.data.authors[0].books[0].editions[0]
    assert _editions.id == 0
    assert _editions.bookId == 0
    assert _editions.foreignEditionId == "string"
    assert _editions.titleSlug == "string"
    assert _editions.isbn13 == "string"
    assert _editions.asin == "string"
    assert _editions.title == "string"
    assert _editions.language == "string"
    assert _editions.overview == "string"
    assert _editions.format == "string"
    assert _editions.isEbook is True
    assert _editions.disambiguation == "string"
    assert _editions.publisher == "string"
    assert _editions.pageCount == 0
    assert _editions.pageCount == 0
    assert _editions.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _editions.images[0].url == "string"
    assert _editions.images[0].coverType == "string"
    assert _editions.links[0].url == "string"
    assert _editions.links[0].name == "string"
    assert _editions.ratings.votes == 0
    assert _editions.ratings.value == 0
    assert _editions.monitored is True
    assert _editions.manualAdd is True
    assert _editions.remoteCover == "string"
    assert _editions.grabbed is True
    assert item.data.authors[0].books[0].grabbed is True
    assert item.data.monitoringOptions.monitor == "string"
    assert item.data.monitoringOptions.booksToMonitor[0] == "string"
    assert item.data.monitoringOptions.monitored is True
