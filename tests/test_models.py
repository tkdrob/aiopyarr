"""Tests for object models."""
from datetime import datetime
from aiopyarr.const import ATTR_DATA
from aiopyarr.models.base import BaseModel
from aiopyarr.models.common import Diskspace
from aiopyarr.models.response import PyArrResponse

from aiopyarr.readarr_client import ReadarrClient
import pytest
from aiohttp.client import ClientSession
import json

from aiopyarr.sonarr_client import SonarrClient
from aiopyarr.models.readarr import _ReadarrBookValueSeriesLinks, _ReadarrEditionsValue, ReadarrBookshelf, _ReadarrAuthorValueBooks, _ReadarrAuthorValueSeries, _ReadarrEditions, _ReadarrEditionsValueBookFiles, _ReadarrSeriesLinks


from . import TEST_HOST_CONFIGURATION, load_fixture



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
    assert item.data.authors[0].books[0].id == 0
    assert item.data.authors[0].books[0].title == "string"
    assert item.data.authors[0].books[0].authorTitle == "string"
    assert item.data.authors[0].books[0].seriesTitle == "string"
    assert item.data.authors[0].books[0].disambiguation == "string"
    assert item.data.authors[0].books[0].overview == "string"
    assert item.data.authors[0].books[0].authorId == 0
    assert item.data.authors[0].books[0].foreignBookId == "string"
    assert item.data.authors[0].books[0].titleSlug == "string"
    assert item.data.authors[0].books[0].monitored is True
    assert item.data.authors[0].books[0].anyEditionOk is True
    assert item.data.authors[0].books[0].ratings.votes == 0
    assert item.data.authors[0].books[0].ratings.value == 0
    assert item.data.authors[0].books[0].releaseDate == "2021-12-10T10:00:06.987Z"
    assert item.data.authors[0].books[0].pageCount == 0
    assert item.data.authors[0].books[0].genres[0] == "string"
    _value = item.data.authors[0].books[0].author
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
    assert _value.nextBook.releaseDate == "2021-12-10T10:00:06.987Z"
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert _value.nextBook.ratings.votes == 0
    assert _value.nextBook.ratings.value == 0
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == "2021-12-10T10:00:06.987Z"
    assert _value.nextBook.added == "2021-12-10T10:00:06.987Z"
    assert _value.nextBook.addOptions.addType == "automatic"
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
    assert _value.born == "2021-12-10T10:00:06.987Z"
    assert _value.died == "2021-12-10T10:00:06.987Z"
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
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
    assert _value.lastInfoSync == "2021-12-10T10:00:06.987Z"
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == "2021-12-10T10:00:06.987Z"
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
    assert _value.metadata.value.born == "2021-12-10T10:00:06.987Z"
    assert _value.metadata.value.died == "2021-12-10T10:00:06.987Z"
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert _book.releaseDate == "2021-12-10T10:00:06.987Z"
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert _book.ratings.votes == 0
    assert _book.ratings.value == 0
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == "2021-12-10T10:00:06.987Z"
    assert _book.added == "2021-12-10T10:00:06.987Z"
    assert _book.addOptions.addType == "automatic"
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
    assert _value.born == "2021-12-10T10:00:06.987Z"
    assert _value.died == "2021-12-10T10:00:06.987Z"
    assert _value.status == "continuing"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == "unknown"
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
    assert _value.lastInfoSync == "2021-12-10T10:00:06.987Z"
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == "2021-12-10T10:00:06.987Z"
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
    assert _value.metadata.value.born == "2021-12-10T10:00:06.987Z"
    assert _value.metadata.value.died == "2021-12-10T10:00:06.987Z"
    assert _value.metadata.value.status == "continuing"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == "unknown"
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
    assert _value.metadataProfile.value.minPopularity == 0
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
    assert item.data.authors[0].books[0].author.images[0].url == "string"
    assert item.data.authors[0].books[0].author.images[0].coverType == "unknown"
    assert item.data.authors[0].books[0].author.remotePoster == "string"
    assert item.data.authors[0].books[0].author.path == "string"
    assert item.data.authors[0].books[0].author.qualityProfileId == 0
    assert item.data.authors[0].books[0].author.metadataProfileId == 0
    assert item.data.authors[0].books[0].author.monitored is True
    assert item.data.authors[0].books[0].author.rootFolderPath == "string"
    assert item.data.authors[0].books[0].author.genres[0] == "string"
    assert item.data.authors[0].books[0].author.cleanName == "string"
    assert item.data.authors[0].books[0].author.sortName == "string"
    assert item.data.authors[0].books[0].author.sortNameLastFirst == "string"
    assert item.data.authors[0].books[0].author.tags[0] == 0
    assert item.data.authors[0].books[0].author.added == "2021-12-10T10:00:06.987Z"
    assert item.data.authors[0].books[0].author.addOptions.monitor == "all"
    assert item.data.authors[0].books[0].author.addOptions.booksToMonitor[0] == "string"
    assert item.data.authors[0].books[0].author.addOptions.monitored is True
    assert item.data.authors[0].books[0].author.addOptions.searchForMissingBooks is True
    assert item.data.authors[0].books[0].author.ratings.votes == 0
    assert item.data.authors[0].books[0].author.ratings.value == 0
    assert item.data.authors[0].books[0].author.statistics.bookFileCount == 0
    assert item.data.authors[0].books[0].author.statistics.bookCount == 0
    assert item.data.authors[0].books[0].author.statistics.availableBookCount == 0
    assert item.data.authors[0].books[0].author.statistics.totalBookCount == 0
    assert item.data.authors[0].books[0].author.statistics.sizeOnDisk == 0
    assert item.data.authors[0].books[0].images[0].url == "string"
    assert item.data.authors[0].books[0].images[0].coverType == "unknown"
    assert item.data.authors[0].books[0].links[0].url == "string"
    assert item.data.authors[0].books[0].links[0].name == "string"
    assert item.data.authors[0].books[0].statistics.bookFileCount == 0
    assert item.data.authors[0].books[0].statistics.bookCount == 0
    assert item.data.authors[0].books[0].statistics.totalBookCount == 0
    assert item.data.authors[0].books[0].statistics.sizeOnDisk == 0
    assert item.data.authors[0].books[0].added == "2021-12-10T10:00:06.987Z"
    assert item.data.authors[0].books[0].addOptions.addType == "automatic"
    assert item.data.authors[0].books[0].addOptions.searchForNewBook is True
    assert item.data.authors[0].books[0].remoteCover == "string"
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
    assert _editions.releaseDate == "2021-12-10T10:00:06.987Z"
    assert _editions.images[0].url == "string"
    assert _editions.images[0].coverType == "unknown"
    assert _editions.links[0].url == "string"
    assert _editions.links[0].name == "string"
    assert _editions.ratings.votes == 0
    assert _editions.ratings.value == 0
    assert _editions.monitored is True
    assert _editions.manualAdd is True
    assert _editions.remoteCover == "string"
    assert _editions.grabbed is True
    assert item.data.authors[0].books[0].grabbed is True
    assert item.data.monitoringOptions.monitor == "all"
    assert item.data.monitoringOptions.booksToMonitor[0] == "string"
    assert item.data.monitoringOptions.monitored is True
