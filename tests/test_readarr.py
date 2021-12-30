"""Tests for Readarr object models."""
from datetime import datetime

from aiopyarr.readarr_client import ReadarrClient
import pytest
from aiohttp.client import ClientSession


from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_author(aresponses):
    """Test getting author info."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/author/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
    assert data.status == "continuing"
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
    assert data.nextBook.ratings.value == 0
    assert data.nextBook.ratings.popularity == 0
    assert data.nextBook.cleanTitle == "string"
    assert data.nextBook.monitored is True
    assert data.nextBook.anyEditionOk is True
    assert data.nextBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.addOptions.addType == "automatic"
    assert data.nextBook.addOptions.searchForNewBook is True
    assert data.nextBook.authorMetadata.value.id == 0
    assert data.nextBook.authorMetadata.value.foreignAuthorId == "string"
    assert data.nextBook.authorMetadata.value.titleSlug == "string"
    assert data.nextBook.authorMetadata.value.name == "string"
    assert data.nextBook.authorMetadata.value.sortName == "string"
    assert data.nextBook.authorMetadata.value.nameLastFirst == "string"
    assert data.nextBook.authorMetadata.value.sortNameLastFirst == "string"
    assert data.nextBook.authorMetadata.value.aliases[0] == "string"
    assert data.nextBook.authorMetadata.value.overview == "string"
    assert data.nextBook.authorMetadata.value.disambiguation == "string"
    assert data.nextBook.authorMetadata.value.gender == "string"
    assert data.nextBook.authorMetadata.value.hometown == "string"
    assert data.nextBook.authorMetadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.authorMetadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.authorMetadata.value.status == "continuing"
    assert data.nextBook.authorMetadata.value.images[0].url == "string"
    assert data.nextBook.authorMetadata.value.images[0].coverType == "unknown"
    assert data.nextBook.authorMetadata.value.images[0].extension == "string"
    assert data.nextBook.authorMetadata.value.links[0].url == "string"
    assert data.nextBook.authorMetadata.value.links[0].name == "string"
    assert data.nextBook.authorMetadata.value.genres[0] == "string"
    assert data.nextBook.authorMetadata.value.ratings.votes == 0
    assert data.nextBook.authorMetadata.value.ratings.value == 0
    assert data.nextBook.authorMetadata.value.ratings.popularity == 0
    assert data.nextBook.authorMetadata.isLoaded is True
    assert data.nextBook.author.value.id == 0
    assert data.nextBook.author.value.authorMetadataId == 0
    assert data.nextBook.author.value.cleanName == "string"
    assert data.nextBook.author.value.monitored is True
    assert data.nextBook.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.path == "string"
    assert data.nextBook.author.value.rootFolderPath == "string"
    assert data.nextBook.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.qualityProfileId == 0
    assert data.nextBook.author.value.metadataProfileId == 0
    assert data.nextBook.author.value.tags[0] == 0
    assert data.nextBook.author.value.addOptions.monitor == "all"
    assert data.nextBook.author.value.addOptions.booksToMonitor[0] == "string"
    assert data.nextBook.author.value.addOptions.monitored is True
    assert data.nextBook.author.value.addOptions.searchForMissingBooks is True
    assert data.nextBook.author.value.metadata.value.id == 0
    assert data.nextBook.author.value.metadata.value.foreignAuthorId == "string"
    assert data.nextBook.author.value.metadata.value.titleSlug == "string"
    assert data.nextBook.author.value.metadata.value.name == "string"
    assert data.nextBook.author.value.metadata.value.sortName == "string"
    assert data.nextBook.author.value.metadata.value.nameLastFirst == "string"
    assert data.nextBook.author.value.metadata.value.sortNameLastFirst == "string"
    assert data.nextBook.author.value.metadata.value.aliases[0] == "string"
    assert data.nextBook.author.value.metadata.value.overview == "string"
    assert data.nextBook.author.value.metadata.value.disambiguation == "string"
    assert data.nextBook.author.value.metadata.value.gender == "string"
    assert data.nextBook.author.value.metadata.value.hometown == "string"
    assert data.nextBook.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.metadata.value.status == "continuing"
    assert data.nextBook.author.value.metadata.value.images[0].url == "string"
    assert data.nextBook.author.value.metadata.value.images[0].coverType == "unknown"
    assert data.nextBook.author.value.metadata.value.images[0].extension == "string"
    assert data.nextBook.author.value.metadata.value.links[0].url == "string"
    assert data.nextBook.author.value.metadata.value.links[0].name == "string"
    assert data.nextBook.author.value.metadata.value.genres[0] == "string"
    assert data.nextBook.author.value.metadata.value.ratings.votes == 0
    assert data.nextBook.author.value.metadata.value.ratings.value == 0
    assert data.nextBook.author.value.metadata.value.ratings.popularity == 0
    assert data.nextBook.author.value.metadata.isLoaded is True
    assert data.nextBook.author.value.qualityProfileId == 0
    assert data.nextBook.author.value.metadataProfileId == 0
    assert data.nextBook.author.value.tags[0] == 0
    assert data.nextBook.author.value.addOptions.monitor == "all"
    assert data.nextBook.author.value.addOptions.booksToMonitor[0] == "string"
    assert data.nextBook.author.value.addOptions.monitored is True
    assert data.nextBook.author.value.addOptions.searchForMissingBooks is True
    assert data.nextBook.author.value.metadata.value.id == 0
    assert data.nextBook.author.value.metadata.value.foreignAuthorId == "string"
    assert data.nextBook.author.value.metadata.value.titleSlug == "string"
    assert data.nextBook.author.value.metadata.value.name == "string"
    assert data.nextBook.author.value.metadata.value.sortName == "string"
    assert data.nextBook.author.value.metadata.value.nameLastFirst == "string"
    assert data.nextBook.author.value.metadata.value.sortNameLastFirst == "string"
    assert data.nextBook.author.value.metadata.value.aliases[0] == "string"
    assert data.nextBook.author.value.metadata.value.overview == "string"
    assert data.nextBook.author.value.metadata.value.disambiguation == "string"
    assert data.nextBook.author.value.metadata.value.gender == "string"
    assert data.nextBook.author.value.metadata.value.hometown == "string"
    assert data.nextBook.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.author.value.metadata.value.status == "continuing"
    assert data.nextBook.author.value.metadata.value.images[0].url == "string"
    assert data.nextBook.author.value.metadata.value.images[0].coverType == "unknown"
    assert data.nextBook.author.value.metadata.value.images[0].extension == "string"
    assert data.nextBook.author.value.metadata.value.links[0].url == "string"
    assert data.nextBook.author.value.metadata.value.links[0].name == "string"
    assert data.nextBook.author.value.metadata.value.genres[0] == "string"
    assert data.nextBook.author.value.metadata.value.ratings.votes == 0
    assert data.nextBook.author.value.metadata.value.ratings.value == 0
    assert data.nextBook.author.value.metadata.value.ratings.popularity == 0
    assert data.nextBook.author.value.metadata.isLoaded is True
    assert data.nextBook.author.value.qualityProfile.value.id == 0
    assert data.nextBook.author.value.qualityProfile.value.name == "string"
    assert data.nextBook.author.value.qualityProfile.value.upgradeAllowed is True
    assert data.nextBook.author.value.qualityProfile.value.cutoff == 0
    item = data.nextBook.author.value.qualityProfile.value.items[0]
    assert item.id == 0
    assert item.name == "string"
    assert item.quality.id == 0
    assert item.quality.name == "string"
    assert item.items[0] == None
    assert item.allowed is True
    assert data.nextBook.author.value.qualityProfile.isLoaded is True
    assert data.nextBook.author.value.metadataProfile.value.id == 0
    assert data.nextBook.author.value.metadataProfile.value.name == "string"
    assert data.nextBook.author.value.metadataProfile.value.minPopularity == 0
    assert data.nextBook.author.value.metadataProfile.value.skipMissingDate is True
    assert data.nextBook.author.value.metadataProfile.value.skipMissingIsbn is True
    assert data.nextBook.author.value.metadataProfile.value.skipPartsAndSets is True
    assert data.nextBook.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert data.nextBook.author.value.metadataProfile.value.allowedLanguages == "string"
    assert data.nextBook.author.value.metadataProfile.value.minPages == 0
    assert data.nextBook.author.value.metadataProfile.value.ignored == "string"
    assert data.nextBook.author.value.metadataProfile.isLoaded is True
    assert data.nextBook.author.value.books.value[0] == None
    assert data.nextBook.author.value.books.isLoaded is True
    assert data.nextBook.author.value.series.value[0].id == 0
    assert data.nextBook.author.value.series.value[0].foreignSeriesId == "string"
    assert data.nextBook.author.value.series.value[0].title == "string"
    assert data.nextBook.author.value.series.value[0].description == "string"
    assert data.nextBook.author.value.series.value[0].numbered is True
    assert data.nextBook.author.value.series.value[0].workCount == 0
    assert data.nextBook.author.value.series.value[0].primaryWorkCount == 0
    assert data.nextBook.author.value.series.value[0].books.value == [None]
    assert data.nextBook.author.value.series.value[0].books.isLoaded is True
    assert data.nextBook.author.value.series.value[0].foreignAuthorId == "string"
    assert data.nextBook.author.value.name == "string"
    assert data.nextBook.author.value.foreignAuthorId == "string"
    assert data.nextBook.author.isLoaded is True
    assert data.nextBook.editions.value[0].id == 0
    assert data.nextBook.editions.value[0].bookId == 0
    assert data.nextBook.editions.value[0].foreignEditionId == "string"
    assert data.nextBook.editions.value[0].titleSlug == "string"
    assert data.nextBook.editions.value[0].isbn13 == "string"
    assert data.nextBook.editions.value[0].asin == "string"
    assert data.nextBook.editions.value[0].title == "string"
    assert data.nextBook.editions.value[0].language == "string"
    assert data.nextBook.editions.value[0].overview == "string"
    assert data.nextBook.editions.value[0].format == "string"
    assert data.nextBook.editions.value[0].isEbook is True
    assert data.nextBook.editions.value[0].disambiguation == "string"
    assert data.nextBook.editions.value[0].publisher == "string"
    assert data.nextBook.editions.value[0].pageCount == 0
    assert data.nextBook.editions.value[0].releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.editions.value[0].images[0].url == "string"
    assert data.nextBook.editions.value[0].images[0].coverType == "unknown"
    assert data.nextBook.editions.value[0].images[0].extension == "string"
    assert data.nextBook.editions.value[0].links[0].url == "string"
    assert data.nextBook.editions.value[0].links[0].name == "string"
    assert data.nextBook.editions.value[0].ratings.votes == 0
    assert data.nextBook.editions.value[0].ratings.value == 0
    assert data.nextBook.editions.value[0].ratings.popularity == 0
    assert data.nextBook.editions.value[0].monitored is True
    assert data.nextBook.editions.value[0].manualAdd is True
    assert data.nextBook.editions.value[0].book.isLoaded is True
    _value = data.nextBook.editions.value[0].bookFiles.value[0]
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert data.nextBook.bookFiles.value[0].id == 0
    assert data.nextBook.bookFiles.value[0].path == "string"
    assert data.nextBook.bookFiles.value[0].size == 0
    assert data.nextBook.bookFiles.value[0].modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.bookFiles.value[0].dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.bookFiles.value[0].sceneName == "string"
    assert data.nextBook.bookFiles.value[0].releaseGroup == "string"
    assert data.nextBook.bookFiles.value[0].quality.quality.id == 0
    assert data.nextBook.bookFiles.value[0].quality.quality.name == "string"
    assert data.nextBook.bookFiles.value[0].quality.revision.version == 0
    assert data.nextBook.bookFiles.value[0].quality.revision.isRepack is True
    assert data.nextBook.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert data.nextBook.bookFiles.value[0].mediaInfo.audioBitrate == "string"
    assert data.nextBook.bookFiles.value[0].mediaInfo.audioChannels == 0
    assert data.nextBook.bookFiles.value[0].mediaInfo.audioBits == 0
    assert data.nextBook.bookFiles.value[0].mediaInfo.audioSampleRate == "string"
    assert data.nextBook.bookFiles.value[0].editionId == 0
    assert data.nextBook.bookFiles.value[0].calibreId == 0
    assert data.nextBook.bookFiles.value[0].part == 0
    _value = data.nextBook.bookFiles.value[0].author.value
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert data.lastBook.ratings.value == 0
    assert data.lastBook.ratings.popularity == 0
    assert data.lastBook.cleanTitle == "string"
    assert data.lastBook.monitored is True
    assert data.lastBook.anyEditionOk is True
    assert data.lastBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.addOptions.addType == "automatic"
    assert data.lastBook.addOptions.searchForNewBook is True
    assert data.lastBook.authorMetadata.value.id == 0
    assert data.lastBook.authorMetadata.value.foreignAuthorId == "string"
    assert data.lastBook.authorMetadata.value.titleSlug == "string"
    assert data.lastBook.authorMetadata.value.name == "string"
    assert data.lastBook.authorMetadata.value.sortName == "string"
    assert data.lastBook.authorMetadata.value.nameLastFirst == "string"
    assert data.lastBook.authorMetadata.value.sortNameLastFirst == "string"
    assert data.lastBook.authorMetadata.value.aliases[0] == "string"
    assert data.lastBook.authorMetadata.value.overview == "string"
    assert data.lastBook.authorMetadata.value.disambiguation == "string"
    assert data.lastBook.authorMetadata.value.gender == "string"
    assert data.lastBook.authorMetadata.value.hometown == "string"
    assert data.lastBook.authorMetadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.authorMetadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.authorMetadata.value.status == "continuing"
    assert data.lastBook.authorMetadata.value.images[0].url == "string"
    assert data.lastBook.authorMetadata.value.images[0].coverType == "unknown"
    assert data.lastBook.authorMetadata.value.images[0].extension == "string"
    assert data.lastBook.authorMetadata.value.links[0].url == "string"
    assert data.lastBook.authorMetadata.value.links[0].name == "string"
    assert data.lastBook.authorMetadata.value.genres[0] == "string"
    assert data.lastBook.authorMetadata.value.ratings.votes == 0
    assert data.lastBook.authorMetadata.value.ratings.value == 0
    assert data.lastBook.authorMetadata.value.ratings.popularity == 0
    assert data.lastBook.authorMetadata.isLoaded is True
    assert data.lastBook.author.value.id == 0
    assert data.lastBook.author.value.authorMetadataId == 0
    assert data.lastBook.author.value.cleanName == "string"
    assert data.lastBook.author.value.monitored is True
    assert data.lastBook.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.path == "string"
    assert data.lastBook.author.value.rootFolderPath == "string"
    assert data.lastBook.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.qualityProfileId == 0
    assert data.lastBook.author.value.metadataProfileId == 0
    assert data.lastBook.author.value.tags[0] == 0
    assert data.lastBook.author.value.addOptions.monitor == "all"
    assert data.lastBook.author.value.addOptions.booksToMonitor[0] == "string"
    assert data.lastBook.author.value.addOptions.monitored is True
    assert data.lastBook.author.value.addOptions.searchForMissingBooks is True
    assert data.lastBook.author.value.metadata.value.id == 0
    assert data.lastBook.author.value.metadata.value.foreignAuthorId == "string"
    assert data.lastBook.author.value.metadata.value.titleSlug == "string"
    assert data.lastBook.author.value.metadata.value.name == "string"
    assert data.lastBook.author.value.metadata.value.sortName == "string"
    assert data.lastBook.author.value.metadata.value.nameLastFirst == "string"
    assert data.lastBook.author.value.metadata.value.sortNameLastFirst == "string"
    assert data.lastBook.author.value.metadata.value.aliases[0] == "string"
    assert data.lastBook.author.value.metadata.value.overview == "string"
    assert data.lastBook.author.value.metadata.value.disambiguation == "string"
    assert data.lastBook.author.value.metadata.value.gender == "string"
    assert data.lastBook.author.value.metadata.value.hometown == "string"
    assert data.lastBook.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.metadata.value.status == "continuing"
    assert data.lastBook.author.value.metadata.value.images[0].url == "string"
    assert data.lastBook.author.value.metadata.value.images[0].coverType == "unknown"
    assert data.lastBook.author.value.metadata.value.images[0].extension == "string"
    assert data.lastBook.author.value.metadata.value.links[0].url == "string"
    assert data.lastBook.author.value.metadata.value.links[0].name == "string"
    assert data.lastBook.author.value.metadata.value.genres[0] == "string"
    assert data.lastBook.author.value.metadata.value.ratings.votes == 0
    assert data.lastBook.author.value.metadata.value.ratings.value == 0
    assert data.lastBook.author.value.metadata.value.ratings.popularity == 0
    assert data.lastBook.author.value.metadata.isLoaded is True
    assert data.lastBook.author.value.qualityProfileId == 0
    assert data.lastBook.author.value.metadataProfileId == 0
    assert data.lastBook.author.value.tags[0] == 0
    assert data.lastBook.author.value.addOptions.monitor == "all"
    assert data.lastBook.author.value.addOptions.booksToMonitor[0] == "string"
    assert data.lastBook.author.value.addOptions.monitored is True
    assert data.lastBook.author.value.addOptions.searchForMissingBooks is True
    assert data.lastBook.author.value.metadata.value.id == 0
    assert data.lastBook.author.value.metadata.value.foreignAuthorId == "string"
    assert data.lastBook.author.value.metadata.value.titleSlug == "string"
    assert data.lastBook.author.value.metadata.value.name == "string"
    assert data.lastBook.author.value.metadata.value.sortName == "string"
    assert data.lastBook.author.value.metadata.value.nameLastFirst == "string"
    assert data.lastBook.author.value.metadata.value.sortNameLastFirst == "string"
    assert data.lastBook.author.value.metadata.value.aliases[0] == "string"
    assert data.lastBook.author.value.metadata.value.overview == "string"
    assert data.lastBook.author.value.metadata.value.disambiguation == "string"
    assert data.lastBook.author.value.metadata.value.gender == "string"
    assert data.lastBook.author.value.metadata.value.hometown == "string"
    assert data.lastBook.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.author.value.metadata.value.status == "continuing"
    assert data.lastBook.author.value.metadata.value.images[0].url == "string"
    assert data.lastBook.author.value.metadata.value.images[0].coverType == "unknown"
    assert data.lastBook.author.value.metadata.value.images[0].extension == "string"
    assert data.lastBook.author.value.metadata.value.links[0].url == "string"
    assert data.lastBook.author.value.metadata.value.links[0].name == "string"
    assert data.lastBook.author.value.metadata.value.genres[0] == "string"
    assert data.lastBook.author.value.metadata.value.ratings.votes == 0
    assert data.lastBook.author.value.metadata.value.ratings.value == 0
    assert data.lastBook.author.value.metadata.value.ratings.popularity == 0
    assert data.lastBook.author.value.metadata.isLoaded is True
    _value = data.lastBook.author.value.qualityProfile.value
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
    assert data.lastBook.author.value.metadataProfile.value.minPopularity == 0
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
    assert data.lastBook.editions.value[0].id == 0
    assert data.lastBook.editions.value[0].bookId == 0
    assert data.lastBook.editions.value[0].foreignEditionId == "string"
    assert data.lastBook.editions.value[0].titleSlug == "string"
    assert data.lastBook.editions.value[0].isbn13 == "string"
    assert data.lastBook.editions.value[0].asin == "string"
    assert data.lastBook.editions.value[0].title == "string"
    assert data.lastBook.editions.value[0].language == "string"
    assert data.lastBook.editions.value[0].overview == "string"
    assert data.lastBook.editions.value[0].format == "string"
    assert data.lastBook.editions.value[0].isEbook is True
    assert data.lastBook.editions.value[0].disambiguation == "string"
    assert data.lastBook.editions.value[0].publisher == "string"
    assert data.lastBook.editions.value[0].pageCount == 0
    assert data.lastBook.editions.value[0].releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.editions.value[0].images[0].url == "string"
    assert data.lastBook.editions.value[0].images[0].coverType == "unknown"
    assert data.lastBook.editions.value[0].images[0].extension == "string"
    assert data.lastBook.editions.value[0].links[0].url == "string"
    assert data.lastBook.editions.value[0].links[0].name == "string"
    assert data.lastBook.editions.value[0].ratings.votes == 0
    assert data.lastBook.editions.value[0].ratings.value == 0
    assert data.lastBook.editions.value[0].ratings.popularity == 0
    assert data.lastBook.editions.value[0].monitored is True
    assert data.lastBook.editions.value[0].manualAdd is True
    assert data.lastBook.editions.value[0].book.isLoaded is True
    _value = data.lastBook.editions.value[0].bookFiles.value[0]
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert data.images[0].coverType == "unknown"
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
    assert data.addOptions.monitor == "all"
    assert data.addOptions.booksToMonitor[0] == "string"
    assert data.addOptions.monitored is True
    assert data.addOptions.searchForMissingBooks is True
    assert data.ratings.votes == 0
    assert data.ratings.value == 0
    assert data.ratings.popularity == 0
    assert data.statistics.bookFileCount == 0
    assert data.statistics.bookCount == 0
    assert data.statistics.availableBookCount == 0
    assert data.statistics.totalBookCount == 0
    assert data.statistics.sizeOnDisk == 0
    assert data.statistics.percentOfBooks == 0


@pytest.mark.asyncio
async def test_async_author_lookup(aresponses):
    """Test getting author lookup info."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/author/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=string",
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
    assert data[0].status == "continuing"
    assert data[0].ended is False
    assert data[0].authorName == "string"
    assert data[0].authorNameLastFirst == "string"
    assert data[0].foreignAuthorId == "string"
    assert data[0].titleSlug == "string"
    assert data[0].overview == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "poster"
    assert data[0].images[0].extension == ".jpg"
    assert data[0].remotePoster == "string"
    assert data[0].path == "string"
    assert data[0].qualityProfileId == 1
    assert data[0].metadataProfileId == 1
    assert data[0].monitored is True
    assert data[0].monitorNewItems == "all"
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
    assert data[0].statistics.percentOfBooks == 0
    assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses):
    """Test getting blocklist info."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/blocklist?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=20&sortDirection=descending&sortKey=date",
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
    assert data.records[0].protocol == "unknown"
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    assert data.records[0].author.id == 0
    assert data.records[0].author.authorMetadataId == 0
    assert data.records[0].author.status == "continuing"
    assert data.records[0].author.ended is True
    assert data.records[0].author.authorName == "string"
    assert data.records[0].author.authorNameLastFirst == "string"
    assert data.records[0].author.foreignAuthorId == "string"
    assert data.records[0].author.titleSlug == "string"
    assert data.records[0].author.overview == "string"
    assert data.records[0].author.disambiguation == "string"
    assert data.records[0].author.links[0].url == "string"
    assert data.records[0].author.links[0].name == "string"
    assert data.records[0].author.nextBook.id == 0
    assert data.records[0].author.nextBook.authorMetadataId == 0
    assert data.records[0].author.nextBook.foreignBookId == "string"
    assert data.records[0].author.nextBook.titleSlug == "string"
    assert data.records[0].author.nextBook.title == "string"
    assert data.records[0].author.nextBook.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.records[0].author.nextBook.links[0].url == "string"
    assert data.records[0].author.nextBook.links[0].name == "string"
    assert data.records[0].author.nextBook.genres[0] == "string"
    assert data.records[0].author.nextBook.ratings.votes == 0
    assert data.records[0].author.nextBook.ratings.value == 0
    assert data.records[0].author.nextBook.ratings.popularity == 0
    assert data.records[0].author.nextBook.cleanTitle == "string"
    assert data.records[0].author.nextBook.monitored is True
    assert data.records[0].author.nextBook.anyEditionOk is True
    assert data.records[0].author.nextBook.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.records[0].author.nextBook.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.records[0].author.nextBook.addOptions.addType == "automatic"
    assert data.records[0].author.nextBook.addOptions.searchForNewBook is True
    _value = data.records[0].author.nextBook.authorMetadata.value
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _val.mediaInfo.audioChannels == 0
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
    assert _val.author.value.addOptions.monitor == "all"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _val = _value.bookFiles.value[0]
    assert _val.author.value.metadata.value.id == 0
    assert _val.author.value.metadata.value.foreignAuthorId == "string"
    assert _val.author.value.metadata.value.titleSlug == "string"
    assert _val.author.value.metadata.value.name == "string"
    assert _val.author.value.metadata.value.sortName == "string"
    assert _val.author.value.metadata.value.nameLastFirst == "string"
    assert _val.author.value.metadata.value.sortNameLastFirst == "string"
    assert _val.author.value.metadata.value.aliases[0] == "string"
    assert _val.author.value.metadata.value.overview == "string"
    assert _val.author.value.metadata.value.disambiguation == "string"
    assert _val.author.value.metadata.value.gender == "string"
    assert _val.author.value.metadata.value.hometown == "string"
    assert _val.author.value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.author.value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.author.value.metadata.value.status == "continuing"
    assert _val.author.value.metadata.value.images[0].url == "string"
    assert _val.author.value.metadata.value.images[0].coverType == "unknown"
    assert _val.author.value.metadata.value.images[0].extension == "string"
    assert _val.author.value.metadata.value.links[0].url == "string"
    assert _val.author.value.metadata.value.links[0].name == "string"
    assert _val.author.value.metadata.value.genres[0] == "string"
    assert _val.author.value.metadata.value.ratings.votes == 0
    assert _val.author.value.metadata.value.ratings.value == 0
    assert _val.author.value.metadata.value.ratings.popularity == 0
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
    assert _val.author.value.metadataProfile.value.minPopularity == 0
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert data.records[0].author.lastBook.id == 0
    assert data.records[0].author.lastBook.authorMetadataId == 0
    assert data.records[0].author.lastBook.foreignBookId == "string"
    assert data.records[0].author.lastBook.titleSlug == "string"
    assert data.records[0].author.lastBook.title == "string"
    assert data.records[0].author.lastBook.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert data.records[0].author.lastBook.links[0].url == "string"
    assert data.records[0].author.lastBook.links[0].name == "string"
    assert data.records[0].author.lastBook.genres[0] == "string"
    assert data.records[0].author.lastBook.ratings.votes == 0
    assert data.records[0].author.lastBook.ratings.value == 0
    assert data.records[0].author.lastBook.ratings.popularity == 0
    assert data.records[0].author.lastBook.cleanTitle == "string"
    assert data.records[0].author.lastBook.monitored is True
    assert data.records[0].author.lastBook.anyEditionOk is True
    assert data.records[0].author.lastBook.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert data.records[0].author.lastBook.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert data.records[0].author.lastBook.addOptions.addType == "automatic"
    assert data.records[0].author.lastBook.addOptions.searchForNewBook is True
    _value = data.records[0].author.lastBook.authorMetadata.value
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
    assert _value.metadata.isLoaded is True
    assert _value.qualityProfileId == 0
    assert _value.metadataProfileId == 0
    assert _value.tags[0] == 0
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _val.mediaInfo.audioChannels == 0
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
    assert _val.author.value.addOptions.monitor == "all"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    assert _val.author.value.metadata.value.id == 0
    assert _val.author.value.metadata.value.foreignAuthorId == "string"
    assert _val.author.value.metadata.value.titleSlug == "string"
    assert _val.author.value.metadata.value.name == "string"
    assert _val.author.value.metadata.value.sortName == "string"
    assert _val.author.value.metadata.value.nameLastFirst == "string"
    assert _val.author.value.metadata.value.sortNameLastFirst == "string"
    assert _val.author.value.metadata.value.aliases[0] == "string"
    assert _val.author.value.metadata.value.overview == "string"
    assert _val.author.value.metadata.value.disambiguation == "string"
    assert _val.author.value.metadata.value.gender == "string"
    assert _val.author.value.metadata.value.hometown == "string"
    assert _val.author.value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.author.value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.author.value.metadata.value.status == "continuing"
    assert _val.author.value.metadata.value.images[0].url == "string"
    assert _val.author.value.metadata.value.images[0].coverType == "unknown"
    assert _val.author.value.metadata.value.images[0].extension == "string"
    assert _val.author.value.metadata.value.links[0].url == "string"
    assert _val.author.value.metadata.value.links[0].name == "string"
    assert _val.author.value.metadata.value.genres[0] == "string"
    assert _val.author.value.metadata.value.ratings.votes == 0
    assert _val.author.value.metadata.value.ratings.value == 0
    assert _val.author.value.metadata.value.ratings.popularity == 0
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
    assert _val.author.value.metadataProfile.value.minPopularity == 0
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert data.records[0].author.images[0].coverType == "unknown"
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
    assert data.records[0].author.addOptions.monitor == "all"
    assert data.records[0].author.addOptions.booksToMonitor[0] == "string"
    assert data.records[0].author.addOptions.monitored is True
    assert data.records[0].author.addOptions.searchForMissingBooks is True
    assert data.records[0].author.ratings.votes == 0
    assert data.records[0].author.ratings.value == 0
    assert data.records[0].author.ratings.popularity == 0
    assert data.records[0].author.statistics.bookFileCount == 0
    assert data.records[0].author.statistics.bookCount == 0
    assert data.records[0].author.statistics.availableBookCount == 0
    assert data.records[0].author.statistics.totalBookCount == 0
    assert data.records[0].author.statistics.sizeOnDisk == 0
    assert data.records[0].author.statistics.percentOfBooks == 0


@pytest.mark.asyncio
async def test_async_get_book(aresponses):
    """Test getting book info."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/book/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
    assert data[0].author.status == "continuing"
    assert data[0].author.ended is True
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert data[0].author.titleSlug == "string"
    assert data[0].author.overview == "string"
    assert data[0].author.disambiguation == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    assert data[0].author.nextBook.id == 0
    assert data[0].author.nextBook.authorMetadataId == 0
    assert data[0].author.nextBook.foreignBookId == "string"
    assert data[0].author.nextBook.titleSlug == "string"
    assert data[0].author.nextBook.title == "string"
    assert data[0].author.nextBook.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert data[0].author.nextBook.links[0].url == "string"
    assert data[0].author.nextBook.links[0].name == "string"
    assert data[0].author.nextBook.genres[0] == "string"
    assert data[0].author.nextBook.ratings.votes == 0
    assert data[0].author.nextBook.ratings.value == 0
    assert data[0].author.nextBook.ratings.popularity == 0
    assert data[0].author.nextBook.cleanTitle == "string"
    assert data[0].author.nextBook.monitored is True
    assert data[0].author.nextBook.anyEditionOk is True
    assert data[0].author.nextBook.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert data[0].author.nextBook.added == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert data[0].author.nextBook.addOptions.addType == "automatic"
    assert data[0].author.nextBook.addOptions.searchForNewBook is True
    _value = data[0].author.nextBook.authorMetadata.value
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    assert _value.bookFiles.value[0].id == 0
    assert _value.bookFiles.value[0].path == "string"
    assert _value.bookFiles.value[0].size == 0
    assert _value.bookFiles.value[0].modified == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.bookFiles.value[0].dateAdded == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.bookFiles.value[0].sceneName == "string"
    assert _value.bookFiles.value[0].releaseGroup == "string"
    assert _value.bookFiles.value[0].quality.quality.id == 0
    assert _value.bookFiles.value[0].quality.quality.name == "string"
    assert _value.bookFiles.value[0].quality.revision.version == 0
    assert _value.bookFiles.value[0].quality.revision.real == 0
    assert _value.bookFiles.value[0].quality.revision.isRepack is True
    assert _value.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert _value.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _value.bookFiles.value[0].mediaInfo.audioChannels == 0
    assert _value.bookFiles.value[0].mediaInfo.audioBits == 0
    assert _value.bookFiles.value[0].mediaInfo.audioSampleRate == "string"
    assert _value.bookFiles.value[0].editionId == 0
    assert _value.bookFiles.value[0].calibreId == 0
    assert _value.bookFiles.value[0].part == 0
    _val = _value.bookFiles.value[0].author.value
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
    assert _val.addOptions.monitor == "all"
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
    assert _val.metadata.value.status == "continuing"
    assert _val.metadata.value.images[0].url == "string"
    assert _val.metadata.value.images[0].coverType == "unknown"
    assert _val.metadata.value.images[0].extension == "string"
    assert _val.metadata.value.links[0].url == "string"
    assert _val.metadata.value.links[0].name == "string"
    assert _val.metadata.value.genres[0] == "string"
    assert _val.metadata.value.ratings.votes == 0
    assert _val.metadata.value.ratings.value == 0
    assert _val.metadata.value.ratings.popularity == 0
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
    assert _val.metadataProfile.value.minPopularity == 0
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
    assert data[0].author.lastBook.id == 0
    assert data[0].author.lastBook.authorMetadataId == 0
    assert data[0].author.lastBook.foreignBookId == "string"
    assert data[0].author.lastBook.titleSlug == "string"
    assert data[0].author.lastBook.title == "string"
    assert data[0].author.lastBook.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert data[0].author.lastBook.links[0].url == "string"
    assert data[0].author.lastBook.links[0].name == "string"
    assert data[0].author.lastBook.genres[0] == "string"
    assert data[0].author.lastBook.ratings.votes == 0
    assert data[0].author.lastBook.ratings.value == 0
    assert data[0].author.lastBook.ratings.popularity == 0
    assert data[0].author.lastBook.cleanTitle == "string"
    assert data[0].author.lastBook.monitored is True
    assert data[0].author.lastBook.anyEditionOk is True
    assert data[0].author.lastBook.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert data[0].author.lastBook.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert data[0].author.lastBook.addOptions.addType == "automatic"
    assert data[0].author.lastBook.addOptions.searchForNewBook is True
    _value = data[0].author.lastBook.authorMetadata.value
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert _value.metadata.value.ratings.votes == 0
    assert _value.metadata.value.ratings.value == 0
    assert _value.metadata.value.ratings.popularity == 0
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _value.images[0].coverType == "unknown"
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.ratings.votes == 0
    assert _value.ratings.value == 0
    assert _value.ratings.popularity == 0
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
    assert _val.mediaInfo.audioChannels == 0
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
    assert _val.author.value.addOptions.monitor == "all"
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    assert _val.author.value.metadata.value.id == 0
    assert _val.author.value.metadata.value.foreignAuthorId == "string"
    assert _val.author.value.metadata.value.titleSlug == "string"
    assert _val.author.value.metadata.value.name == "string"
    assert _val.author.value.metadata.value.sortName == "string"
    assert _val.author.value.metadata.value.nameLastFirst == "string"
    assert _val.author.value.metadata.value.sortNameLastFirst == "string"
    assert _val.author.value.metadata.value.aliases[0] == "string"
    assert _val.author.value.metadata.value.overview == "string"
    assert _val.author.value.metadata.value.disambiguation == "string"
    assert _val.author.value.metadata.value.gender == "string"
    assert _val.author.value.metadata.value.hometown == "string"
    assert _val.author.value.metadata.value.born == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert _val.author.value.metadata.value.died == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert _val.author.value.metadata.value.status == "continuing"
    assert _val.author.value.metadata.value.images[0].url == "string"
    assert _val.author.value.metadata.value.images[0].coverType == "unknown"
    assert _val.author.value.metadata.value.images[0].extension == "string"
    assert _val.author.value.metadata.value.links[0].url == "string"
    assert _val.author.value.metadata.value.links[0].name == "string"
    assert _val.author.value.metadata.value.genres[0] == "string"
    assert _val.author.value.metadata.value.ratings.votes == 0
    assert _val.author.value.metadata.value.ratings.value == 0
    assert _val.author.value.metadata.value.ratings.popularity == 0
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
    assert _val.author.value.metadataProfile.value.minPopularity == 0
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
    assert data[0].author.images[0].coverType == "unknown"
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
    assert data[0].author.addOptions.monitor == "all"
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0
    assert data[0].author.ratings.popularity == 0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "unknown"
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].statistics.bookFileCount == 0
    assert data[0].statistics.bookCount == 0
    assert data[0].statistics.totalBookCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfBooks == 0
    assert data[0].added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].addOptions.addType == "automatic"
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
    assert data[0].editions[0].images[0].coverType == "unknown"
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
        "/api/v1/bookfile/0?apikey=ur1234567-0abc12de3f456gh7ij89k012&unmapped=False",
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
    assert data.mediaInfo.audioChannels == 0
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
    assert data.audioTags.mediaInfo.audioChannels == 0
    assert data.audioTags.mediaInfo.audioBits == 0
    assert data.audioTags.mediaInfo.audioSampleRate == "string"
    assert data.audioTags.trackNumbers[0] == 0
    assert data.audioTags.language == "string"
    assert data.audioTags.releaseGroup == "string"
    assert data.audioTags.releaseHash == "string"

    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/bookfile?apikey=ur1234567-0abc12de3f456gh7ij89k012&unmapped=False&authorId=0&bookId=0",
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
        "/api/v1/book/lookup?apikey=ur1234567-0abc12de3f456gh7ij89k012&term=isbn:test",
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
    assert data[0].author.status == "continuing"
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert data[0].author.titleSlug == "string"
    assert data[0].author.links == []
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == "poster"
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.qualityProfileId == 0
    assert data[0].author.metadataProfileId == 0
    assert data[0].author.monitored is False
    assert data[0].author.monitorNewItems == "all"
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
    assert data[0].author.statistics.percentOfBooks == 0
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
        "/api/v1/calendar?apikey=ur1234567-0abc12de3f456gh7ij89k012&start=2020-11-30&end=2020-12-01&unmonitored=False&includeAuthor=False",
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
    assert _value.status == "continuing"
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
    assert _value.nextBook.addOptions.addType == "automatic"
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _book.editions.value[0].id == 0
    assert _book.editions.value[0].bookId == 0
    assert _book.editions.value[0].foreignEditionId == "string"
    assert _book.editions.value[0].titleSlug == "string"
    assert _book.editions.value[0].isbn13 == "string"
    assert _book.editions.value[0].asin == "string"
    assert _book.editions.value[0].title == "string"
    assert _book.editions.value[0].language == "string"
    assert _book.editions.value[0].overview == "string"
    assert _book.editions.value[0].format == "string"
    assert _book.editions.value[0].isEbook is True
    assert _book.editions.value[0].disambiguation == "string"
    assert _book.editions.value[0].publisher == "string"
    assert _book.editions.value[0].pageCount == 0
    assert _book.editions.value[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.editions.value[0].images[0].url == "string"
    assert _book.editions.value[0].images[0].coverType == "unknown"
    assert _book.editions.value[0].images[0].extension == "string"
    assert _book.editions.value[0].links[0].url == "string"
    assert _book.editions.value[0].links[0].name == "string"
    assert _book.editions.value[0].ratings.votes == 0
    assert _book.editions.value[0].ratings.value == 0
    assert _book.editions.value[0].ratings.popularity == 0
    assert _book.editions.value[0].monitored is True
    assert _book.editions.value[0].manualAdd is True
    assert _book.editions.value[0].book.isLoaded is True
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert _book.bookFiles.value[0].id == 0
    assert _book.bookFiles.value[0].path == "string"
    assert _book.bookFiles.value[0].size == 0
    assert _book.bookFiles.value[0].modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.bookFiles.value[0].dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.bookFiles.value[0].sceneName == "string"
    assert _book.bookFiles.value[0].releaseGroup == "string"
    assert _book.bookFiles.value[0].quality.quality.id == 0
    assert _book.bookFiles.value[0].quality.quality.name == "string"
    assert _book.bookFiles.value[0].quality.revision.version == 0
    assert _book.bookFiles.value[0].quality.revision.real == 0
    assert _book.bookFiles.value[0].quality.revision.isRepack is True
    assert _book.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert _book.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _book.bookFiles.value[0].mediaInfo.audioChannels == 0
    assert _book.bookFiles.value[0].mediaInfo.audioBits == 0
    assert _book.bookFiles.value[0].mediaInfo.audioSampleRate == 0
    assert _book.bookFiles.value[0].editionId == 0
    assert _book.bookFiles.value[0].calibreId == 0
    assert _book.bookFiles.value[0].part == 0
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
    assert _author.value.addOptions.monitor == "all"
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    assert _author.value.metadata.value.id == 0
    assert _author.value.metadata.value.foreignAuthorId == "string"
    assert _author.value.metadata.value.titleSlug == "string"
    assert _author.value.metadata.value.name == "string"
    assert _author.value.metadata.value.sortName == "string"
    assert _author.value.metadata.value.nameLastFirst == "string"
    assert _author.value.metadata.value.sortNameLastFirst == "string"
    assert _author.value.metadata.value.aliases[0] == "string"
    assert _author.value.metadata.value.overview == "string"
    assert _author.value.metadata.value.disambiguation == "string"
    assert _author.value.metadata.value.gender == "string"
    assert _author.value.metadata.value.hometown == "string"
    assert _author.value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.metadata.value.status == "continuing"
    assert _author.value.metadata.value.images[0].url == "string"
    assert _author.value.metadata.value.images[0].coverType == "unknown"
    assert _author.value.metadata.value.images[0].extension == "string"
    assert _author.value.metadata.value.links[0].url == "string"
    assert _author.value.metadata.value.links[0].name == "string"
    assert _author.value.metadata.value.genres[0] == "string"
    assert _author.value.metadata.value.ratings.votes == 0
    assert _author.value.metadata.value.ratings.value == 0
    assert _author.value.metadata.value.ratings.popularity == 0
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
    assert _author.value.metadataProfile.value.minPopularity == 0
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
    assert _value.nextBook.addOptions.addType == "automatic"
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
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
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
    assert _value.addOptions.monitor == "all"
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
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _book.editions.value[0].id == 0
    assert _book.editions.value[0].bookId == 0
    assert _book.editions.value[0].foreignEditionId == "string"
    assert _book.editions.value[0].titleSlug == "string"
    assert _book.editions.value[0].isbn13 == "string"
    assert _book.editions.value[0].asin == "string"
    assert _book.editions.value[0].title == "string"
    assert _book.editions.value[0].language == "string"
    assert _book.editions.value[0].overview == "string"
    assert _book.editions.value[0].format == "string"
    assert _book.editions.value[0].isEbook is True
    assert _book.editions.value[0].disambiguation == "string"
    assert _book.editions.value[0].publisher == "string"
    assert _book.editions.value[0].pageCount == 0
    assert _book.editions.value[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.editions.value[0].images[0].url == "string"
    assert _book.editions.value[0].images[0].coverType == "unknown"
    assert _book.editions.value[0].images[0].extension == "string"
    assert _book.editions.value[0].links[0].url == "string"
    assert _book.editions.value[0].links[0].name == "string"
    assert _book.editions.value[0].ratings.votes == 0
    assert _book.editions.value[0].ratings.value == 0
    assert _book.editions.value[0].ratings.popularity == 0
    assert _book.editions.value[0].monitored is True
    assert _book.editions.value[0].manualAdd is True
    assert _book.editions.value[0].book.isLoaded is True
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
    assert _value.mediaInfo.audioChannels == 0
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
    assert _value.author.value.addOptions.monitor == "all"
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    assert _value.author.value.metadata.value.id == 0
    assert _value.author.value.metadata.value.foreignAuthorId == "string"
    assert _value.author.value.metadata.value.titleSlug == "string"
    assert _value.author.value.metadata.value.name == "string"
    assert _value.author.value.metadata.value.sortName == "string"
    assert _value.author.value.metadata.value.nameLastFirst == "string"
    assert _value.author.value.metadata.value.sortNameLastFirst == "string"
    assert _value.author.value.metadata.value.aliases[0] == "string"
    assert _value.author.value.metadata.value.overview == "string"
    assert _value.author.value.metadata.value.disambiguation == "string"
    assert _value.author.value.metadata.value.gender == "string"
    assert _value.author.value.metadata.value.hometown == "string"
    assert _value.author.value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.metadata.value.status == "continuing"
    assert _value.author.value.metadata.value.images[0].url == "string"
    assert _value.author.value.metadata.value.images[0].coverType == "unknown"
    assert _value.author.value.metadata.value.images[0].extension == "string"
    assert _value.author.value.metadata.value.links[0].url == "string"
    assert _value.author.value.metadata.value.links[0].name == "string"
    assert _value.author.value.metadata.value.genres[0] == "string"
    assert _value.author.value.metadata.value.ratings.votes == 0
    assert _value.author.value.metadata.value.ratings.value == 0
    assert _value.author.value.metadata.value.ratings.popularity == 0
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
    assert _value.author.value.metadataProfile.value.minPopularity == 0
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
    assert _book.bookFiles.value[0].id == 0
    assert _book.bookFiles.value[0].path == "string"
    assert _book.bookFiles.value[0].size == 0
    assert _book.bookFiles.value[0].modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.bookFiles.value[0].dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _book.bookFiles.value[0].sceneName == "string"
    assert _book.bookFiles.value[0].releaseGroup == "string"
    assert _book.bookFiles.value[0].quality.quality.id == 0
    assert _book.bookFiles.value[0].quality.quality.name == "string"
    assert _book.bookFiles.value[0].quality.revision.version == 0
    assert _book.bookFiles.value[0].quality.revision.real == 0
    assert _book.bookFiles.value[0].quality.revision.isRepack is True
    assert _book.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert _book.bookFiles.value[0].mediaInfo.audioBitrate == 0
    assert _book.bookFiles.value[0].mediaInfo.audioChannels == 0
    assert _book.bookFiles.value[0].mediaInfo.audioBits == 0
    assert _book.bookFiles.value[0].mediaInfo.audioSampleRate == 0
    assert _book.bookFiles.value[0].editionId == 0
    assert _book.bookFiles.value[0].calibreId == 0
    assert _book.bookFiles.value[0].part == 0
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
    assert _author.value.addOptions.monitor == "all"
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    assert _author.value.metadata.value.id == 0
    assert _author.value.metadata.value.foreignAuthorId == "string"
    assert _author.value.metadata.value.titleSlug == "string"
    assert _author.value.metadata.value.name == "string"
    assert _author.value.metadata.value.sortName == "string"
    assert _author.value.metadata.value.nameLastFirst == "string"
    assert _author.value.metadata.value.sortNameLastFirst == "string"
    assert _author.value.metadata.value.aliases[0] == "string"
    assert _author.value.metadata.value.overview == "string"
    assert _author.value.metadata.value.disambiguation == "string"
    assert _author.value.metadata.value.gender == "string"
    assert _author.value.metadata.value.hometown == "string"
    assert _author.value.metadata.value.born == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.metadata.value.died == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.metadata.value.status == "continuing"
    assert _author.value.metadata.value.images[0].url == "string"
    assert _author.value.metadata.value.images[0].coverType == "unknown"
    assert _author.value.metadata.value.images[0].extension == "string"
    assert _author.value.metadata.value.links[0].url == "string"
    assert _author.value.metadata.value.links[0].name == "string"
    assert _author.value.metadata.value.genres[0] == "string"
    assert _author.value.metadata.value.ratings.votes == 0
    assert _author.value.metadata.value.ratings.value == 0
    assert _author.value.metadata.value.ratings.popularity == 0
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
    assert _author.value.metadataProfile.value.minPopularity == 0
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
    assert data[0].author.images[0].coverType == "unknown"
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
    assert data[0].author.addOptions.monitor == "all"
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert data[0].author.ratings.votes == 0
    assert data[0].author.ratings.value == 0
    assert data[0].author.ratings.popularity == 0
    assert data[0].author.statistics.bookFileCount == 0
    assert data[0].author.statistics.bookCount == 0
    assert data[0].author.statistics.availableBookCount == 0
    assert data[0].author.statistics.totalBookCount == 0
    assert data[0].author.statistics.sizeOnDisk == 0
    assert data[0].author.statistics.percentOfBooks == 0
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "unknown"
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].statistics.bookFileCount == 0
    assert data[0].statistics.bookCount == 0
    assert data[0].statistics.totalBookCount == 0
    assert data[0].statistics.sizeOnDisk == 0
    assert data[0].statistics.percentOfBooks == 0
    assert data[0].added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].addOptions.addType == "automatic"
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
    assert data[0].editions[0].images[0].coverType == "unknown"
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
async def test_async_get_wanted_missing(aresponses):
    """Test getting wanted and missing books."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/wanted/missing?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=title&page=1&pageSize=10",
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
    assert data.records[0].ratings.value == 0
    assert data.records[0].ratings.popularity == 0
    assert data.records[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data.records[0].pageCount == 0
    assert data.records[0].genres[0] == "string"
    assert data.records[0].author.authorMetadataId == 0
    assert data.records[0].author.status == "continuing"
    assert data.records[0].author.ended is False
    assert data.records[0].author.authorName == "string"
    assert data.records[0].author.authorNameLastFirst == "string"
    assert data.records[0].author.foreignAuthorId == "string"
    assert data.records[0].author.titleSlug == "string"
    assert data.records[0].author.overview == "string"
    assert data.records[0].author.links[0].url == "string"
    assert data.records[0].author.links[0].name == "string"
    assert data.records[0].author.images[0].url == "string"
    assert data.records[0].author.images[0].coverType == "unknown"
    assert data.records[0].author.images[0].extension == "string"
    assert data.records[0].author.path == "string"
    assert data.records[0].author.qualityProfileId == 0
    assert data.records[0].author.metadataProfileId == 0
    assert data.records[0].author.monitored is True
    assert data.records[0].author.monitorNewItems == "all"
    assert data.records[0].author.genres == []
    assert data.records[0].author.cleanName == "string"
    assert data.records[0].author.sortName == "string"
    assert data.records[0].author.sortNameLastFirst == "string"
    assert data.records[0].author.tags == []
    assert data.records[0].author.added == datetime(2021, 12, 6, 22, 23, 55)
    assert data.records[0].author.ratings.votes == 0
    assert data.records[0].author.ratings.value == 0
    assert data.records[0].author.ratings.popularity == 0
    assert data.records[0].author.statistics.bookFileCount == 0
    assert data.records[0].author.statistics.bookCount == 0
    assert data.records[0].author.statistics.availableBookCount == 0
    assert data.records[0].author.statistics.totalBookCount == 0
    assert data.records[0].author.statistics.sizeOnDisk == 0
    assert data.records[0].author.statistics.percentOfBooks == 0
    assert data.records[0].author.id == 0
    assert data.records[0].images[0].url == "string"
    assert data.records[0].images[0].coverType == "unknown"
    assert data.records[0].images[0].extension == "string"
    assert data.records[0].links[0].url == "string"
    assert data.records[0].links[0].name == "string"
    assert data.records[0].statistics.bookFileCount == 0
    assert data.records[0].statistics.bookCount == 0
    assert data.records[0].statistics.totalBookCount == 0
    assert data.records[0].statistics.sizeOnDisk == 0
    assert data.records[0].statistics.percentOfBooks == 0
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
    assert data.records[0].editions[0].images[0].coverType == "unknown"
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
        "/api/v1/wanted/cutoff?apikey=ur1234567-0abc12de3f456gh7ij89k012&sortKey=title&page=1&pageSize=10",
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
async def test_async_get_metadata_profiles(aresponses):
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/metadataprofile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/metadata-profile.json"),
        ),
        #match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_metadata_profiles()
    assert data[0].id == 0
