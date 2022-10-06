"""Tests for Readarr object models."""
# pylint:disable=line-too-long, too-many-lines, too-many-statements
from datetime import datetime
import json

import pytest

from aiopyarr.const import ATTR_DATA
from aiopyarr.exceptions import ArrException
from aiopyarr.models.base import BaseModel
from aiopyarr.models.const import ProtocolType
from aiopyarr.models.readarr import (
    ReadarrAuthor,
    ReadarrAuthorEditor,
    ReadarrBook,
    ReadarrBookFile,
    ReadarrBookFileEditor,
    ReadarrBookHistory,
    ReadarrBookshelf,
    ReadarrCommands,
    ReadarrDevelopmentConfig,
    ReadarrEventType,
    ReadarrImportList,
    ReadarrManualImport,
    ReadarrMetadataProfile,
    ReadarrMetadataProvider,
    ReadarrNamingConfig,
    ReadarrNotification,
    ReadarrRelease,
    ReadarrRootFolder,
    ReadarrSortKeys,
    ReadarrWantedCutoff,
)
from aiopyarr.models.readarr_common import (
    _ReadarrAuthorValueBooks,
    _ReadarrAuthorValueSeries,
    _ReadarrEditions,
    _ReadarrEditionsValueBookFiles,
    _ReadarrSeriesLinks,
)
from aiopyarr.models.request import (
    AddTypes,
    Command,
    ImageType,
    MonitoringOptionsType,
    SortDirection,
    StatusType,
)
from aiopyarr.readarr_client import ReadarrClient

from . import READARR_API, load_fixture


@pytest.mark.asyncio
async def test_async_get_authors(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting author info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/author.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_authors(authorid=0)
    assert isinstance(data.id, int)
    assert isinstance(data.authorMetadataId, int)
    assert data.status == "string"
    assert data.ended is True
    assert data.authorName == "string"
    assert data.authorNameLastFirst == "string"
    assert data.foreignAuthorId == "string"
    assert isinstance(data.titleSlug, int)
    assert data.overview == "string"
    assert data.links[0].url == "string"
    assert data.links[0].name == "string"
    assert isinstance(data.nextBook.id, int)
    assert isinstance(data.nextBook.authorMetadataId, int)
    assert data.nextBook.foreignBookId == "string"
    assert isinstance(data.nextBook.titleSlug, int)
    assert data.nextBook.title == "string"
    assert data.nextBook.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.links[0].url == "string"
    assert data.nextBook.links[0].name == "string"
    assert data.nextBook.genres[0] == "string"
    assert isinstance(data.nextBook.ratings.votes, int)
    assert isinstance(data.nextBook.ratings.value, float)
    assert isinstance(data.nextBook.ratings.popularity, int)
    assert data.nextBook.cleanTitle == "string"
    assert data.nextBook.monitored is True
    assert data.nextBook.anyEditionOk is True
    assert data.nextBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.nextBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.nextBook.addOptions.searchForNewBook is True
    _value = data.nextBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data.nextBook.authorMetadata.isLoaded is True
    _value = data.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    item = _value.qualityProfile.value.items[0]
    assert isinstance(item.id, int)
    assert item.name == "string"
    assert isinstance(item.quality.id, int)
    assert item.quality.name == "string"
    assert item.items[0] is None
    assert item.allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.nextBook.author.isLoaded is True
    _value = data.nextBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    _valu = _value.author.value
    assert _valu.metadata.isLoaded is True
    assert isinstance(_valu.qualityProfile.value.id, int)
    assert _valu.qualityProfile.value.name == "string"
    assert _valu.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_valu.qualityProfile.value.cutoff, int)
    assert isinstance(_valu.qualityProfile.value.items[0].id, int)
    assert _valu.qualityProfile.value.items[0].name == "string"
    assert isinstance(_valu.qualityProfile.value.items[0].quality.id, int)
    assert _valu.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.qualityProfile.value.items[0].items == [None]
    assert _valu.qualityProfile.value.items[0].allowed is True
    assert isinstance(_valu.metadataProfile.value.id, int)
    assert _valu.metadataProfile.value.name == "string"
    assert isinstance(_valu.metadataProfile.value.minPopularity, int)
    assert _valu.metadataProfile.value.skipMissingDate is True
    assert _valu.metadataProfile.value.skipMissingIsbn is True
    assert _valu.metadataProfile.value.skipPartsAndSets is True
    assert _valu.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_valu.metadataProfile.value.minPages, int)
    assert _valu.metadataProfile.value.ignored == "string"
    assert _valu.metadataProfile.isLoaded is True
    assert _valu.books.value[0] is None
    assert _valu.books.isLoaded is True
    assert isinstance(_valu.series.value[0].id, int)
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert isinstance(_valu.series.value[0].workCount, int)
    assert isinstance(_valu.series.value[0].primaryWorkCount, int)
    assert _valu.series.value[0].books.value[0] is None
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert isinstance(_valu.series.value[0].workCount, int)
    assert isinstance(_valu.series.value[0].primaryWorkCount, int)
    assert _valu.series.value[0].books.value[0] is None
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.isLoaded is True
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert data.nextBook.editions.isLoaded is True
    _value = data.nextBook.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert _value.mediaInfo.audioBitrate == "string"
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    _value = _value.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _valu = data.nextBook
    assert _valu.bookFiles.value[0].author.isLoaded is True
    assert _valu.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_valu.bookFiles.value[0].partCount, int)
    assert _valu.bookFiles.isLoaded is True
    _val = _valu.seriesLinks
    assert isinstance(_val.value[0].id, int)
    assert _val.value[0].position == "string"
    assert isinstance(_val.value[0].seriesId, int)
    assert isinstance(_val.value[0].bookId, int)
    assert _val.value[0].isPrimary is True
    assert isinstance(_val.value[0].series.value.id, int)
    assert _val.value[0].series.value.foreignSeriesId == "string"
    assert _val.value[0].series.value.title == "string"
    assert _val.value[0].series.value.description == "string"
    assert _val.value[0].series.value.numbered is True
    assert isinstance(_val.value[0].series.value.workCount, int)
    assert isinstance(_val.value[0].series.value.primaryWorkCount, int)
    assert _val.value[0].series.value.books.value[0] is None
    assert _val.value[0].series.value.books.isLoaded is True
    assert _val.value[0].series.value.foreignAuthorId == "string"
    assert _val.value[0].series.isLoaded is True
    assert _val.value[0].book.isLoaded is True
    assert _val.isLoaded is True
    assert isinstance(data.lastBook.id, int)
    assert isinstance(data.lastBook.authorMetadataId, int)
    assert data.lastBook.foreignBookId == "string"
    assert isinstance(data.lastBook.titleSlug, int)
    assert data.lastBook.title == "string"
    assert data.lastBook.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.links[0].url == "string"
    assert data.lastBook.links[0].name == "string"
    assert data.lastBook.genres[0] == "string"
    assert isinstance(data.lastBook.ratings.votes, int)
    assert isinstance(data.lastBook.ratings.value, float)
    assert isinstance(data.lastBook.ratings.popularity, int)
    assert data.lastBook.cleanTitle == "string"
    assert data.lastBook.monitored is True
    assert data.lastBook.anyEditionOk is True
    assert data.lastBook.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert data.lastBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.lastBook.addOptions.searchForNewBook is True
    _value = data.lastBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data.lastBook.authorMetadata.isLoaded is True
    _value = data.lastBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    _value = _value.qualityProfile.value
    assert isinstance(_value.id, int)
    assert _value.name == "string"
    assert _value.upgradeAllowed is True
    assert isinstance(_value.cutoff, int)
    assert isinstance(_value.items[0].id, int)
    assert _value.items[0].name == "string"
    assert isinstance(_value.items[0].quality.id, int)
    assert _value.items[0].quality.name == "string"
    assert _value.items[0].items[0] is None
    assert _value.items[0].allowed is True
    _valu = data.lastBook.author.value
    assert _valu.qualityProfile.isLoaded is True
    _val = _valu.metadataProfile
    assert isinstance(_val.value.id, int)
    assert _val.value.name == "string"
    assert isinstance(_val.value.minPopularity, int)
    assert _val.value.skipMissingDate is True
    assert _val.value.skipMissingIsbn is True
    assert _val.value.skipPartsAndSets is True
    assert _val.value.skipSeriesSecondary is True
    assert _val.value.allowedLanguages == "string"
    assert isinstance(_val.value.minPages, int)
    assert _val.value.ignored == "string"
    assert _val.isLoaded is True
    assert _valu.books.value[0] is None
    assert _valu.books.isLoaded is True
    assert isinstance(_valu.series.value[0].id, int)
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert isinstance(_valu.series.value[0].workCount, int)
    assert isinstance(_valu.series.value[0].primaryWorkCount, int)
    assert _valu.series.value[0].books.value == [None]
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert data.lastBook.author.isLoaded is True
    _value = data.lastBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert data.lastBook.editions.isLoaded is True
    _value = data.lastBook.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.dateAdded == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 6, 22, 12, 47, 67000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert data.lastBook.bookFiles.isLoaded is True
    _valu = data.lastBook.seriesLinks
    assert isinstance(_valu.value[0].id, int)
    assert _valu.value[0].position == "string"
    assert isinstance(_valu.value[0].seriesId, int)
    assert isinstance(_valu.value[0].bookId, int)
    assert _valu.value[0].isPrimary is True
    assert isinstance(_valu.value[0].series.value.id, int)
    assert _valu.value[0].series.value.foreignSeriesId == "string"
    assert _valu.value[0].series.value.title == "string"
    assert _valu.value[0].series.value.description == "string"
    assert _valu.value[0].series.value.numbered is True
    assert isinstance(_valu.value[0].series.value.workCount, int)
    assert isinstance(_valu.value[0].series.value.primaryWorkCount, int)
    assert _valu.value[0].series.value.books.value[0] is None
    assert _valu.value[0].series.value.books.isLoaded is True
    assert _valu.value[0].series.value.foreignAuthorId == "string"
    assert _valu.value[0].series.isLoaded is True
    assert _valu.value[0].book.isLoaded is True
    assert _valu.isLoaded is True
    assert data.images[0].url == "string"
    assert data.images[0].coverType == ImageType.POSTER.value
    assert data.images[0].extension == "string"
    assert data.remotePoster == "string"
    assert data.path == "string"
    assert isinstance(data.qualityProfileId, int)
    assert isinstance(data.metadataProfileId, int)
    assert data.monitored is True
    assert data.rootFolderPath == "string"
    assert data.genres[0] == "string"
    assert data.cleanName == "string"
    assert data.sortName == "string"
    assert data.sortNameLastFirst == "string"
    assert isinstance(data.tags[0], int)
    assert data.added == datetime(2021, 12, 6, 22, 12, 47, 68000)
    assert data.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data.addOptions.booksToMonitor[0] == "string"
    assert data.addOptions.monitored is True
    assert data.addOptions.searchForMissingBooks is True
    assert isinstance(data.ratings.votes, int)
    assert isinstance(data.ratings.value, float)
    assert isinstance(data.ratings.popularity, int)
    assert isinstance(data.statistics.bookFileCount, int)
    assert isinstance(data.statistics.bookCount, int)
    assert isinstance(data.statistics.availableBookCount, int)
    assert isinstance(data.statistics.totalBookCount, int)
    assert isinstance(data.statistics.sizeOnDisk, int)
    assert isinstance(data.statistics.percentOfBooks, float)


@pytest.mark.asyncio
async def test_async_author_lookup(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting author lookup info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/lookup?term=string",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/author-lookup.json"),
        ),
        match_querystring=True,
    )

    data = await readarr_client.async_author_lookup(term="string")
    assert isinstance(data[0].authorMetadataId, int)
    assert data[0].status == "string"
    assert data[0].ended is False
    assert data[0].authorName == "string"
    assert data[0].authorNameLastFirst == "string"
    assert data[0].foreignAuthorId == "string"
    assert isinstance(data[0].titleSlug, int)
    assert data[0].overview == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].extension == ".jpg"
    assert data[0].remotePoster == "string"
    assert data[0].path == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert isinstance(data[0].metadataProfileId, int)
    assert data[0].monitored is True
    assert data[0].monitorNewItems == "string"
    assert data[0].genres == ["string"]
    assert data[0].cleanName == "string"
    assert data[0].sortName == "string"
    assert data[0].sortNameLastFirst == "string"
    assert isinstance(data[0].tags[0], int)
    assert data[0].added == datetime(2021, 12, 6, 22, 23, 55)
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert isinstance(data[0].ratings.popularity, float)
    assert isinstance(data[0].statistics.bookFileCount, int)
    assert isinstance(data[0].statistics.bookCount, int)
    assert isinstance(data[0].statistics.availableBookCount, int)
    assert isinstance(data[0].statistics.totalBookCount, int)
    assert isinstance(data[0].statistics.sizeOnDisk, int)
    assert isinstance(data[0].statistics.percentOfBooks, float)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_blocklist(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting blocklist info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/blocklist?page=1&pageSize=20&sortDirection=default&sortKey=books.releaseDate",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/blocklist.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_blocklist()
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == ReadarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DEFAULT.value
    assert data.filters[0].key == "string"
    assert data.filters[0].value == "string"
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].id, int)
    assert isinstance(data.records[0].authorId, int)
    assert isinstance(data.records[0].bookIds[0], int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is True
    assert data.records[0].date == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.records[0].protocol is ProtocolType.UNKNOWN
    assert data.records[0].indexer == "string"
    assert data.records[0].message == "string"
    _author = data.records[0].author
    assert isinstance(_author.id, int)
    assert isinstance(_author.authorMetadataId, int)
    assert _author.status == "string"
    assert _author.ended is True
    assert _author.authorName == "string"
    assert _author.authorNameLastFirst == "string"
    assert _author.foreignAuthorId == "string"
    assert isinstance(_author.titleSlug, int)
    assert _author.overview == "string"
    assert _author.links[0].url == "string"
    assert _author.links[0].name == "string"
    assert isinstance(_author.nextBook.id, int)
    assert isinstance(_author.nextBook.authorMetadataId, int)
    assert _author.nextBook.foreignBookId == "string"
    assert isinstance(_author.nextBook.titleSlug, int)
    assert _author.nextBook.title == "string"
    assert _author.nextBook.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.links[0].url == "string"
    assert _author.nextBook.links[0].name == "string"
    assert _author.nextBook.genres[0] == "string"
    assert isinstance(_author.nextBook.ratings.votes, int)
    assert isinstance(_author.nextBook.ratings.value, float)
    assert isinstance(_author.nextBook.ratings.popularity, int)
    assert _author.nextBook.cleanTitle == "string"
    assert _author.nextBook.monitored is True
    assert _author.nextBook.anyEditionOk is True
    assert _author.nextBook.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _author.nextBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _author.nextBook.addOptions.searchForNewBook is True
    _value = _author.nextBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data.records[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data.records[0].author.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.records[0].author.nextBook.author.isLoaded is True
    _value = data.records[0].author.nextBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert _val.mediaInfo.audioSampleRate == "string"
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _val = _value.bookFiles.value[0]
    _valu = _val.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert data.records[0].author.nextBook.editions.isLoaded is True
    _value = data.records[0].author.nextBook.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert data.records[0].author.nextBook.bookFiles.isLoaded is True
    _value = data.records[0].author.nextBook.seriesLinks.value[0]
    assert isinstance(_value.id, int)
    assert _value.position == "string"
    assert isinstance(_value.seriesId, int)
    assert isinstance(_value.bookId, int)
    assert _value.isPrimary is True
    assert isinstance(_value.series.value.id, int)
    assert _value.series.value.foreignSeriesId == "string"
    assert _value.series.value.title == "string"
    assert _value.series.value.description == "string"
    assert _value.series.value.numbered is True
    assert isinstance(_value.series.value.workCount, int)
    assert isinstance(_value.series.value.primaryWorkCount, int)
    assert _value.series.value.books.value[0] is None
    assert _value.series.value.books.isLoaded is True
    assert _value.series.value.foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.book.isLoaded is True
    assert data.records[0].author.nextBook.seriesLinks.isLoaded is True
    _value = data.records[0].author.lastBook
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.foreignBookId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.title == "string"
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.cleanTitle == "string"
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.addOptions.searchForNewBook is True
    _value = _value.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.nameLastFirst == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data.records[0].author.lastBook.authorMetadata.isLoaded is True
    _value = data.records[0].author.lastBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data.records[0].author.lastBook.author.isLoaded is True
    _value = data.records[0].author.lastBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert _val.mediaInfo.audioSampleRate == "string"
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _valu = _val.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert data.records[0].author.lastBook.editions.isLoaded is True
    _value = data.records[0].author.lastBook.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.dateAdded == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert _value.mediaInfo.audioSampleRate == "string"
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases[0] == "string"
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.died == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items[0] is None
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value[0] is None
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value[0] is None
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert data.records[0].author.lastBook.bookFiles.isLoaded is True
    _value = data.records[0].author.lastBook.seriesLinks.value[0]
    assert isinstance(_value.id, int)
    assert _value.position == "string"
    assert isinstance(_value.seriesId, int)
    assert isinstance(_value.bookId, int)
    assert _value.isPrimary is True
    assert isinstance(_value.series.value.id, int)
    assert _value.series.value.foreignSeriesId == "string"
    assert _value.series.value.title == "string"
    assert _value.series.value.description == "string"
    assert _value.series.value.numbered is True
    assert isinstance(_value.series.value.workCount, int)
    assert isinstance(_value.series.value.primaryWorkCount, int)
    assert _value.series.value.books.value[0] is None
    assert _value.series.value.books.isLoaded is True
    assert _value.series.value.foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.book.isLoaded is True
    assert data.records[0].author.lastBook.seriesLinks.isLoaded is True
    assert data.records[0].author.images[0].url == "string"
    assert data.records[0].author.images[0].coverType == ImageType.POSTER.value
    assert data.records[0].author.images[0].extension == "string"
    assert data.records[0].author.remotePoster == "string"
    assert data.records[0].author.path == "string"
    assert isinstance(data.records[0].author.qualityProfileId, int)
    assert isinstance(data.records[0].author.metadataProfileId, int)
    assert data.records[0].author.monitored is True
    assert data.records[0].author.rootFolderPath == "string"
    assert data.records[0].author.genres[0] == "string"
    assert data.records[0].author.cleanName == "string"
    assert data.records[0].author.sortName == "string"
    assert data.records[0].author.sortNameLastFirst == "string"
    assert isinstance(data.records[0].author.tags[0], int)
    assert data.records[0].author.added == datetime(2021, 12, 7, 8, 55, 41, 227000)
    assert data.records[0].author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data.records[0].author.addOptions.booksToMonitor[0] == "string"
    assert data.records[0].author.addOptions.monitored is True
    assert data.records[0].author.addOptions.searchForMissingBooks is True
    assert isinstance(data.records[0].author.ratings.votes, int)
    assert isinstance(data.records[0].author.ratings.value, float)
    assert isinstance(data.records[0].author.ratings.popularity, int)
    assert isinstance(data.records[0].author.statistics.bookFileCount, int)
    assert isinstance(data.records[0].author.statistics.bookCount, int)
    assert isinstance(data.records[0].author.statistics.availableBookCount, int)
    assert isinstance(data.records[0].author.statistics.totalBookCount, int)
    assert isinstance(data.records[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].author.statistics.percentOfBooks, float)


@pytest.mark.asyncio
async def test_async_get_book(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting book info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_book(bookid=0)
    assert isinstance(data[0].id, int)
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert isinstance(data[0].authorId, int)
    assert data[0].foreignBookId == "string"
    assert isinstance(data[0].titleSlug, int)
    assert data[0].monitored is True
    assert data[0].anyEditionOk is True
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert isinstance(data[0].ratings.popularity, int)
    assert data[0].releaseDate == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert isinstance(data[0].pageCount, int)
    assert data[0].genres[0] == "string"
    assert isinstance(data[0].author.id, int)
    assert isinstance(data[0].author.authorMetadataId, int)
    assert data[0].author.status == "string"
    assert data[0].author.ended is True
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert isinstance(data[0].author.titleSlug, int)
    assert data[0].author.overview == "string"
    assert data[0].author.disambiguation == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    _book = data[0].author.nextBook
    assert isinstance(_book.id, int)
    assert isinstance(_book.authorMetadataId, int)
    assert _book.foreignBookId == "string"
    assert isinstance(_book.titleSlug, int)
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert isinstance(_book.ratings.votes, int)
    assert isinstance(_book.ratings.value, float)
    assert isinstance(_book.ratings.popularity, int)
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.added == datetime(2021, 12, 7, 9, 7, 35, 508000)
    assert _book.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _book.addOptions.searchForNewBook is True
    _value = _book.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data[0].author.nextBook.author.isLoaded is True
    _value = data[0].author.nextBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert isinstance(_valu.id, int)
    assert _valu.path == "string"
    assert isinstance(_valu.size, int)
    assert _valu.modified == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _valu.dateAdded == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert isinstance(_valu.quality.quality.id, int)
    assert _valu.quality.quality.name == "string"
    assert isinstance(_valu.quality.revision.version, int)
    assert isinstance(_valu.quality.revision.real, int)
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert isinstance(_valu.mediaInfo.audioBitrate, int)
    assert isinstance(_valu.mediaInfo.audioChannels, float)
    assert isinstance(_valu.mediaInfo.audioBits, int)
    assert _valu.mediaInfo.audioSampleRate == "string"
    assert isinstance(_valu.editionId, int)
    assert isinstance(_valu.calibreId, int)
    assert isinstance(_valu.part, int)
    _val = _valu.author.value
    assert isinstance(_val.id, int)
    assert isinstance(_val.authorMetadataId, int)
    assert _val.cleanName == "string"
    assert _val.monitored is True
    assert _val.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.path == "string"
    assert _val.rootFolderPath == "string"
    assert _val.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert isinstance(_val.qualityProfileId, int)
    assert isinstance(_val.metadataProfileId, int)
    assert isinstance(_val.tags[0], int)
    assert _val.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.addOptions.booksToMonitor[0] == "string"
    assert _val.addOptions.monitored is True
    assert _val.addOptions.searchForMissingBooks is True
    assert isinstance(_val.metadata.value.id, int)
    assert _val.metadata.value.foreignAuthorId == "string"
    assert isinstance(_val.metadata.value.titleSlug, int)
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
    assert _val.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _val.metadata.value.images[0].extension == "string"
    assert _val.metadata.value.links[0].url == "string"
    assert _val.metadata.value.links[0].name == "string"
    assert _val.metadata.value.genres[0] == "string"
    assert isinstance(_val.metadata.value.ratings.votes, int)
    assert isinstance(_val.metadata.value.ratings.value, float)
    assert isinstance(_val.metadata.value.ratings.popularity, int)
    assert _val.metadata.isLoaded is True
    assert isinstance(_val.qualityProfile.value.id, int)
    assert _val.qualityProfile.value.name == "string"
    assert _val.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.qualityProfile.value.cutoff, int)
    assert isinstance(_val.qualityProfile.value.items[0].id, int)
    assert _val.qualityProfile.value.items[0].name == "string"
    assert _val.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.qualityProfile.value.items[0].quality.id, int)
    assert _val.qualityProfile.value.items[0].quality.name == "string"
    assert _val.qualityProfile.value.items[0].items[0] is None
    assert _val.qualityProfile.value.items[0].allowed is True
    assert _val.qualityProfile.isLoaded is True
    assert isinstance(_val.metadataProfile.value.id, int)
    assert _val.metadataProfile.value.name == "string"
    assert isinstance(_val.metadataProfile.value.minPopularity, int)
    assert _val.metadataProfile.value.skipMissingDate is True
    assert _val.metadataProfile.value.skipMissingIsbn is True
    assert _val.metadataProfile.value.skipPartsAndSets is True
    assert _val.metadataProfile.value.skipSeriesSecondary is True
    assert _val.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.metadataProfile.value.minPages, int)
    assert _val.metadataProfile.value.ignored == "string"
    assert _val.metadataProfile.isLoaded is True
    assert _val.books.value[0] is None
    assert _val.books.isLoaded is True
    assert isinstance(_val.series.value[0].id, int)
    assert _val.series.value[0].foreignSeriesId == "string"
    assert _val.series.value[0].title == "string"
    assert _val.series.value[0].description == "string"
    assert _val.series.value[0].numbered is True
    assert isinstance(_val.series.value[0].workCount, int)
    assert isinstance(_val.series.value[0].primaryWorkCount, int)
    assert _val.series.value[0].books.value[0] is None
    assert _val.series.value[0].books.isLoaded is True
    assert _val.series.value[0].foreignAuthorId == "string"
    assert _val.series.isLoaded is True
    assert _val.name == "string"
    assert _val.foreignAuthorId == "string"
    assert _value.bookFiles.value[0].author.isLoaded is True
    assert _value.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_value.bookFiles.value[0].partCount, int)
    assert _value.bookFiles.isLoaded is True
    value = data[0].author.nextBook
    assert isinstance(value.seriesLinks.value[0].id, int)
    assert value.seriesLinks.value[0].position == "string"
    assert isinstance(value.seriesLinks.value[0].seriesId, int)
    assert isinstance(value.seriesLinks.value[0].bookId, int)
    assert value.seriesLinks.value[0].isPrimary is True
    assert isinstance(value.seriesLinks.value[0].series.value.id, int)
    assert value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert value.seriesLinks.value[0].series.value.title == "string"
    assert value.seriesLinks.value[0].series.value.description == "string"
    assert value.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(value.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(value.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert value.seriesLinks.value[0].series.value.books.value[0] is None
    assert value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert value.seriesLinks.value[0].series.isLoaded is True
    assert value.seriesLinks.value[0].book.isLoaded is True
    assert value.seriesLinks.isLoaded is True
    _book = data[0].author.lastBook
    assert isinstance(_book.id, int)
    assert isinstance(_book.authorMetadataId, int)
    assert _book.foreignBookId == "string"
    assert isinstance(_book.titleSlug, int)
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert isinstance(_book.ratings.votes, int)
    assert isinstance(_book.ratings.value, float)
    assert isinstance(_book.ratings.popularity, int)
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _book.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _book.addOptions.searchForNewBook is True
    _value = _book.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert data[0].author.lastBook.authorMetadata.isLoaded is True
    _value = data[0].author.lastBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.images[0].extension == "string"
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.metadata.value.ratings.popularity, int)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items[0] is None
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value[0] is None
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value[0] is None
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    assert data[0].author.lastBook.author.isLoaded is True
    _value = data[0].author.lastBook.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _val = _value.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.dateAdded == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert _val.mediaInfo.audioSampleRate == "string"
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2021, 12, 7, 9, 7, 35, 509000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor[0] == "string"
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _valu = _val.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items[0] is None
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value[0] is None
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert _value.bookFiles.isLoaded is True
    value = data[0].author.lastBook
    assert isinstance(value.seriesLinks.value[0].id, int)
    assert value.seriesLinks.value[0].position == "string"
    assert isinstance(value.seriesLinks.value[0].seriesId, int)
    assert isinstance(value.seriesLinks.value[0].bookId, int)
    assert value.seriesLinks.value[0].isPrimary is True
    assert isinstance(value.seriesLinks.value[0].series.value.id, int)
    assert value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert value.seriesLinks.value[0].series.value.title == "string"
    assert value.seriesLinks.value[0].series.value.description == "string"
    assert value.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(value.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(value.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert value.seriesLinks.value[0].series.value.books.value[0] is None
    assert value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert value.seriesLinks.value[0].series.isLoaded is True
    assert value.seriesLinks.value[0].book.isLoaded is True
    assert value.seriesLinks.isLoaded is True
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == ImageType.POSTER.value
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert isinstance(data[0].author.qualityProfileId, int)
    assert isinstance(data[0].author.metadataProfileId, int)
    assert data[0].author.monitored is True
    assert data[0].author.rootFolderPath == "string"
    assert data[0].author.genres[0] == "string"
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert isinstance(data[0].author.tags[0], int)
    assert data[0].author.added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert isinstance(data[0].author.ratings.votes, int)
    assert isinstance(data[0].author.ratings.value, float)
    assert isinstance(data[0].author.ratings.popularity, int)
    assert isinstance(data[0].author.statistics.bookFileCount, int)
    assert isinstance(data[0].author.statistics.bookCount, int)
    assert isinstance(data[0].author.statistics.availableBookCount, int)
    assert isinstance(data[0].author.statistics.totalBookCount, int)
    assert isinstance(data[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].author.statistics.percentOfBooks, float)
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert isinstance(data[0].statistics.bookFileCount, int)
    assert isinstance(data[0].statistics.bookCount, int)
    assert isinstance(data[0].statistics.totalBookCount, int)
    assert isinstance(data[0].statistics.sizeOnDisk, int)
    assert isinstance(data[0].statistics.percentOfBooks, float)
    assert data[0].added == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].addOptions.addType == AddTypes.AUTOMATIC.value
    assert data[0].addOptions.searchForNewBook is True
    assert data[0].remoteCover == "string"
    assert isinstance(data[0].editions[0].id, int)
    assert isinstance(data[0].editions[0].bookId, int)
    assert data[0].editions[0].foreignEditionId == "string"
    assert isinstance(data[0].editions[0].titleSlug, int)
    assert data[0].editions[0].isbn13 == "string"
    assert data[0].editions[0].asin == "string"
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].format == "string"
    assert data[0].editions[0].isEbook is True
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert isinstance(data[0].editions[0].pageCount, int)
    assert data[0].editions[0].releaseDate == datetime(2021, 12, 7, 9, 7, 35, 510000)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].editions[0].images[0].extension == "string"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert isinstance(data[0].editions[0].ratings.votes, int)
    assert isinstance(data[0].editions[0].ratings.value, float)
    assert isinstance(data[0].editions[0].ratings.popularity, int)
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is True
    assert data[0].editions[0].remoteCover == "string"
    assert data[0].editions[0].grabbed is True
    assert data[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_book_file(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting book file info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile?unmapped=False&bookFileIds=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-file.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_book_file(fileid=[0])
    assert isinstance(data.id, int)
    assert isinstance(data.authorId, int)
    assert isinstance(data.bookId, int)
    assert data.path == "string"
    assert isinstance(data.size, int)
    assert data.dateAdded == datetime(2021, 12, 9, 20, 39, 8, 79000)
    assert isinstance(data.quality.quality.id, int)
    assert data.quality.quality.name == "string"
    assert isinstance(data.quality.revision.version, int)
    assert isinstance(data.quality.revision.real, int)
    assert data.quality.revision.isRepack is True
    assert isinstance(data.qualityWeight, int)
    assert isinstance(data.mediaInfo.id, int)
    assert isinstance(data.mediaInfo.audioChannels, float)
    assert isinstance(data.mediaInfo.audioBitRate, int)
    assert data.mediaInfo.audioCodec == "string"
    assert isinstance(data.mediaInfo.audioBits, int)
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
    assert isinstance(data.audioTags.trackNumbers[0], int)
    assert isinstance(data.audioTags.discNumber, int)
    assert isinstance(data.audioTags.discCount, int)
    assert data.audioTags.country.twoLetterCode == "string"
    assert data.audioTags.country.name == "string"
    assert isinstance(data.audioTags.year, int)
    assert data.audioTags.publisher == "string"
    assert data.audioTags.label == "string"
    assert data.audioTags.source == "string"
    assert data.audioTags.catalogNumber == "string"
    assert data.audioTags.disambiguation == "string"
    assert data.audioTags.duration == "00:00:00"
    assert isinstance(data.audioTags.quality.quality.id, int)
    assert data.audioTags.quality.quality.name == "string"
    assert isinstance(data.audioTags.quality.revision.version, int)
    assert isinstance(data.audioTags.quality.revision.real, int)
    assert data.audioTags.quality.revision.isRepack is True
    assert data.audioTags.mediaInfo.audioFormat == "string"
    assert isinstance(data.audioTags.mediaInfo.audioBitrate, int)
    assert isinstance(data.audioTags.mediaInfo.audioChannels, float)
    assert isinstance(data.audioTags.mediaInfo.audioBits, int)
    assert data.audioTags.mediaInfo.audioSampleRate == "string"
    assert isinstance(data.audioTags.trackNumbers[0], int)
    assert data.audioTags.language == "string"
    assert data.audioTags.releaseGroup == "string"
    assert data.audioTags.releaseHash == "string"

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile?unmapped=False&authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-file.json"),
        ),
        match_querystring=True,
    )
    await readarr_client.async_get_book_file(authorid=0, bookid=0)


@pytest.mark.asyncio
async def test_async_book_lookup(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting book info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book/lookup?term=isbn:test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/book-lookup.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_lookup_book(term="test")
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert isinstance(data[0].authorId, int)
    assert data[0].foreignBookId == "string"
    assert isinstance(data[0].titleSlug, int)
    assert data[0].monitored is False
    assert data[0].anyEditionOk is True
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert isinstance(data[0].ratings.popularity, float)
    assert data[0].releaseDate == datetime(1869, 1, 1, 0, 0)
    assert isinstance(data[0].pageCount, int)
    assert data[0].genres == ["string"]
    assert isinstance(data[0].author.authorMetadataId, int)
    assert data[0].author.status == "string"
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert data[0].author.foreignAuthorId == "string"
    assert isinstance(data[0].author.titleSlug, int)
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == ImageType.POSTER.value
    assert data[0].author.images[0].extension == "string"
    assert isinstance(data[0].author.qualityProfileId, int)
    assert isinstance(data[0].author.metadataProfileId, int)
    assert data[0].author.monitored is False
    assert data[0].author.monitorNewItems == "string"
    assert data[0].author.genres[0] == "string"
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert isinstance(data[0].author.tags[0], int)
    assert data[0].author.added == datetime(1, 1, 1, 4, 57)
    assert isinstance(data[0].author.ratings.votes, int)
    assert isinstance(data[0].author.ratings.value, float)
    assert isinstance(data[0].author.ratings.popularity, float)
    assert isinstance(data[0].author.statistics.bookFileCount, int)
    assert isinstance(data[0].author.statistics.bookCount, int)
    assert isinstance(data[0].author.statistics.availableBookCount, int)
    assert isinstance(data[0].author.statistics.totalBookCount, int)
    assert isinstance(data[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].author.statistics.percentOfBooks, float)
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == "cover"
    assert data[0].images[0].extension == ".jpg"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert data[0].added == datetime(1, 1, 1, 4, 57)
    assert data[0].remoteCover == "string"
    assert isinstance(data[0].editions[0].bookId, int)
    assert data[0].editions[0].foreignEditionId == "string"
    assert isinstance(data[0].editions[0].titleSlug, int)
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].isEbook is False
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert isinstance(data[0].editions[0].pageCount, int)
    assert data[0].editions[0].releaseDate == datetime(1998, 6, 25, 0, 0)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == "cover"
    assert data[0].editions[0].images[0].extension == ".jpg"
    assert data[0].editions[0].images[0].extension == ".jpg"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert isinstance(data[0].editions[0].ratings.votes, int)
    assert isinstance(data[0].editions[0].ratings.value, float)
    assert isinstance(data[0].editions[0].ratings.popularity, float)
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is False
    assert data[0].editions[0].grabbed is False
    assert data[0].grabbed is False


@pytest.mark.asyncio
async def test_async_get_calendar(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting calendar."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/calendar?unmonitored=False&includeAuthor=False&start=2020-11-30&end=2020-12-01",
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
    data = await readarr_client.async_get_calendar(start, end)
    assert isinstance(data[0].id, int)
    assert data[0].title == "string"
    assert data[0].authorTitle == "string"
    assert data[0].seriesTitle == "string"
    assert data[0].disambiguation == "string"
    assert data[0].overview == "string"
    assert isinstance(data[0].authorId, int)
    assert data[0].foreignBookId == "string"
    assert isinstance(data[0].titleSlug, int)
    assert data[0].monitored is True
    assert data[0].anyEditionOk is True
    assert isinstance(data[0].ratings.votes, int)
    assert isinstance(data[0].ratings.value, float)
    assert data[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert isinstance(data[0].pageCount, int)
    assert data[0].genres[0] == "string"
    _value = data[0].author
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.status == "string"
    assert _value.authorName == "string"
    assert _value.authorNameLastFirst == "string"
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.overview == "string"
    assert _value.disambiguation == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.nextBook.id, int)
    assert isinstance(_value.nextBook.authorMetadataId, int)
    assert _value.nextBook.foreignBookId == "string"
    assert isinstance(_value.nextBook.titleSlug, int)
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert isinstance(_value.nextBook.ratings.votes, int)
    assert isinstance(_value.nextBook.ratings.value, float)
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = data[0].author.nextBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value == [None]
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = data[0].author.nextBook
    _valu = _book.editions.value[0]
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.bookId, int)
    assert _valu.foreignEditionId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.disambiguation == "string"
    assert _valu.publisher == "string"
    assert isinstance(_valu.pageCount, int)
    assert _valu.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _value = _book.editions.value[0].bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert isinstance(_value.mediaInfo.audioSampleRate, int)
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert _book.editions.value[0].bookFiles.isLoaded is True
    assert _book.editions.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    _author = _book.bookFiles.value[0].author
    assert isinstance(_author.value.id, int)
    assert isinstance(_author.value.authorMetadataId, int)
    assert _author.value.cleanName == "string"
    assert _author.value.monitored is True
    assert _author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.path == "string"
    assert _author.value.rootFolderPath == "string"
    assert _author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert isinstance(_author.value.qualityProfileId, int)
    assert isinstance(_author.value.metadataProfileId, int)
    assert isinstance(_author.value.tags[0], int)
    assert _author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    _val = _author.value.metadata.value
    assert isinstance(_val.id, int)
    assert _val.foreignAuthorId == "string"
    assert isinstance(_val.titleSlug, int)
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
    assert _val.images[0].coverType == ImageType.POSTER.value
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres[0] == "string"
    assert isinstance(_val.ratings.votes, int)
    assert isinstance(_val.ratings.value, float)
    assert isinstance(_val.ratings.popularity, int)
    assert _author.value.metadata.isLoaded is True
    assert isinstance(_author.value.qualityProfile.value.id, int)
    assert _author.value.qualityProfile.value.name == "string"
    assert _author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_author.value.qualityProfile.value.items[0].id, int)
    assert _author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_author.value.qualityProfile.value.items[0].quality.id, int)
    assert _author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _author.value.qualityProfile.value.items[0].items == [None]
    assert _author.value.qualityProfile.value.items[0].allowed is True
    assert _author.value.qualityProfile.isLoaded is True
    assert isinstance(_author.value.metadataProfile.value.id, int)
    assert _author.value.metadataProfile.value.name == "string"
    assert isinstance(_author.value.metadataProfile.value.minPopularity, int)
    assert _author.value.metadataProfile.value.skipMissingDate is True
    assert _author.value.metadataProfile.value.skipMissingIsbn is True
    assert _author.value.metadataProfile.value.skipPartsAndSets is True
    assert _author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_author.value.metadataProfile.value.minPages, int)
    assert _author.value.metadataProfile.value.ignored == "string"
    assert _author.value.metadataProfile.isLoaded is True
    assert _author.value.books.value == [None]
    assert _author.value.books.isLoaded is True
    assert isinstance(_author.value.series.value[0].id, int)
    assert _author.value.series.value[0].foreignSeriesId == "string"
    assert _author.value.series.value[0].title == "string"
    assert _author.value.series.value[0].description == "string"
    assert _author.value.series.value[0].numbered is True
    assert isinstance(_author.value.series.value[0].workCount, int)
    assert isinstance(_author.value.series.value[0].primaryWorkCount, int)
    assert _author.value.series.value[0].books.value == [None]
    assert _author.value.series.value[0].books.isLoaded is True
    assert _author.value.series.value[0].foreignAuthorId == "string"
    assert _author.value.series.isLoaded is True
    assert _author.value.name == "string"
    assert _author.value.foreignAuthorId == "string"
    assert _author.isLoaded is True
    assert _book.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_book.bookFiles.value[0].partCount, int)
    assert _book.bookFiles.isLoaded is True
    assert isinstance(_book.seriesLinks.value[0].id, int)
    assert _book.seriesLinks.value[0].position == "string"
    assert isinstance(_book.seriesLinks.value[0].seriesId, int)
    assert isinstance(_book.seriesLinks.value[0].bookId, int)
    assert _book.seriesLinks.value[0].isPrimary is True
    assert isinstance(_book.seriesLinks.value[0].series.value.id, int)
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_book.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_book.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    _value = data[0].author
    assert isinstance(_value.nextBook.id, int)
    assert isinstance(_value.nextBook.authorMetadataId, int)
    assert _value.nextBook.foreignBookId == "string"
    assert isinstance(_value.nextBook.titleSlug, int)
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert isinstance(_value.nextBook.ratings.votes, int)
    assert isinstance(_value.nextBook.ratings.value, float)
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.nextBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = data[0].author.nextBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
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
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert data[0].author.nextBook.authorMetadata.isLoaded is True
    _value = data[0].author.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 11, 9, 30, 28, 338000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
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
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert _value.metadata.isLoaded is True
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert _value.qualityProfile.isLoaded is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert _value.metadataProfile.isLoaded is True
    assert _value.books.value == [None]
    assert _value.books.isLoaded is True
    assert isinstance(_value.series.value[0].id, int)
    assert _value.series.value[0].foreignSeriesId == "string"
    assert _value.series.value[0].title == "string"
    assert _value.series.value[0].description == "string"
    assert _value.series.value[0].numbered is True
    assert isinstance(_value.series.value[0].workCount, int)
    assert isinstance(_value.series.value[0].primaryWorkCount, int)
    assert _value.series.value[0].books.value == [None]
    assert _value.series.value[0].books.isLoaded is True
    assert _value.series.value[0].foreignAuthorId == "string"
    assert _value.series.isLoaded is True
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = data[0].author.nextBook
    _value = _book.editions.value[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.disambiguation == "string"
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, int)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.book.isLoaded is True
    _value = _value.bookFiles.value[0]
    assert isinstance(_value.id, int)
    assert _value.path == "string"
    assert isinstance(_value.size, int)
    assert _value.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.sceneName == "string"
    assert _value.releaseGroup == "string"
    assert isinstance(_value.quality.quality.id, int)
    assert _value.quality.quality.name == "string"
    assert isinstance(_value.quality.revision.version, int)
    assert isinstance(_value.quality.revision.real, int)
    assert _value.quality.revision.isRepack is True
    assert _value.mediaInfo.audioFormat == "string"
    assert isinstance(_value.mediaInfo.audioBitrate, int)
    assert isinstance(_value.mediaInfo.audioChannels, float)
    assert isinstance(_value.mediaInfo.audioBits, int)
    assert isinstance(_value.mediaInfo.audioSampleRate, int)
    assert isinstance(_value.editionId, int)
    assert isinstance(_value.calibreId, int)
    assert isinstance(_value.part, int)
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor[0] == "string"
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
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
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres[0] == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, int)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.isLoaded is True
    assert _value.edition.isLoaded is True
    assert isinstance(_value.partCount, int)
    assert _book.editions.value[0].bookFiles.isLoaded is True
    assert _book.editions.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.dateAdded == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    _author = _val.author
    assert isinstance(_author.value.id, int)
    assert isinstance(_author.value.authorMetadataId, int)
    assert _author.value.cleanName == "string"
    assert _author.value.monitored is True
    assert _author.value.lastInfoSync == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert _author.value.path == "string"
    assert _author.value.rootFolderPath == "string"
    assert _author.value.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert isinstance(_author.value.qualityProfileId, int)
    assert isinstance(_author.value.metadataProfileId, int)
    assert isinstance(_author.value.tags[0], int)
    assert _author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _author.value.addOptions.booksToMonitor[0] == "string"
    assert _author.value.addOptions.monitored is True
    assert _author.value.addOptions.searchForMissingBooks is True
    _val = _author.value.metadata.value
    assert isinstance(_val.id, int)
    assert _val.foreignAuthorId == "string"
    assert isinstance(_val.titleSlug, int)
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
    assert _val.images[0].coverType == ImageType.POSTER.value
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres[0] == "string"
    assert isinstance(_val.ratings.votes, int)
    assert isinstance(_val.ratings.value, float)
    assert isinstance(_val.ratings.popularity, int)
    assert _author.value.metadata.isLoaded is True
    assert isinstance(_author.value.qualityProfile.value.id, int)
    assert _author.value.qualityProfile.value.name == "string"
    assert _author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_author.value.qualityProfile.value.items[0].id, int)
    assert _author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_author.value.qualityProfile.value.items[0].quality.id, int)
    assert _author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _author.value.qualityProfile.value.items[0].items == [None]
    assert _author.value.qualityProfile.value.items[0].allowed is True
    assert _author.value.qualityProfile.isLoaded is True
    assert isinstance(_author.value.metadataProfile.value.id, int)
    assert _author.value.metadataProfile.value.name == "string"
    assert isinstance(_author.value.metadataProfile.value.minPopularity, int)
    assert _author.value.metadataProfile.value.skipMissingDate is True
    assert _author.value.metadataProfile.value.skipMissingIsbn is True
    assert _author.value.metadataProfile.value.skipPartsAndSets is True
    assert _author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_author.value.metadataProfile.value.minPages, int)
    assert _author.value.metadataProfile.value.ignored == "string"
    assert _author.value.metadataProfile.isLoaded is True
    assert _author.value.books.value == [None]
    assert _author.value.books.isLoaded is True
    assert isinstance(_author.value.series.value[0].id, int)
    assert _author.value.series.value[0].foreignSeriesId == "string"
    assert _author.value.series.value[0].title == "string"
    assert _author.value.series.value[0].description == "string"
    assert _author.value.series.value[0].numbered is True
    assert isinstance(_author.value.series.value[0].workCount, int)
    assert isinstance(_author.value.series.value[0].primaryWorkCount, int)
    assert _author.value.series.value[0].books.value == [None]
    assert _author.value.series.value[0].books.isLoaded is True
    assert _author.value.series.value[0].foreignAuthorId == "string"
    assert _author.value.series.isLoaded is True
    assert _author.value.name == "string"
    assert _author.value.foreignAuthorId == "string"
    assert _author.isLoaded is True
    assert _book.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_book.bookFiles.value[0].partCount, int)
    assert _book.bookFiles.isLoaded is True
    assert isinstance(_book.seriesLinks.value[0].id, int)
    assert _book.seriesLinks.value[0].position == "string"
    assert isinstance(_book.seriesLinks.value[0].seriesId, int)
    assert isinstance(_book.seriesLinks.value[0].bookId, int)
    assert _book.seriesLinks.value[0].isPrimary is True
    assert isinstance(_book.seriesLinks.value[0].series.value.id, int)
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_book.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_book.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == ImageType.POSTER.value
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert isinstance(data[0].author.qualityProfileId, int)
    assert isinstance(data[0].author.metadataProfileId, int)
    assert data[0].author.monitored is True
    assert data[0].author.rootFolderPath == "string"
    assert data[0].author.genres[0] == "string"
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert isinstance(data[0].author.tags[0], int)
    assert data[0].author.added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data[0].author.addOptions.booksToMonitor[0] == "string"
    assert data[0].author.addOptions.monitored is True
    assert data[0].author.addOptions.searchForMissingBooks is True
    assert isinstance(data[0].author.ratings.votes, int)
    assert isinstance(data[0].author.ratings.value, float)
    assert isinstance(data[0].author.ratings.popularity, int)
    assert isinstance(data[0].author.statistics.bookFileCount, int)
    assert isinstance(data[0].author.statistics.bookCount, int)
    assert isinstance(data[0].author.statistics.availableBookCount, int)
    assert isinstance(data[0].author.statistics.totalBookCount, int)
    assert isinstance(data[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].author.statistics.percentOfBooks, float)
    assert data[0].images[0].url == "string"
    assert data[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].images[0].extension == "string"
    assert data[0].links[0].url == "string"
    assert data[0].links[0].name == "string"
    assert isinstance(data[0].statistics.bookFileCount, int)
    assert isinstance(data[0].statistics.bookCount, int)
    assert isinstance(data[0].statistics.totalBookCount, int)
    assert isinstance(data[0].statistics.sizeOnDisk, int)
    assert isinstance(data[0].statistics.percentOfBooks, float)
    assert data[0].added == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].addOptions.addType == AddTypes.AUTOMATIC.value
    assert data[0].addOptions.searchForNewBook is True
    assert data[0].remoteCover == "string"
    assert isinstance(data[0].editions[0].id, int)
    assert isinstance(data[0].editions[0].bookId, int)
    assert data[0].editions[0].foreignEditionId == "string"
    assert isinstance(data[0].editions[0].titleSlug, int)
    assert data[0].editions[0].isbn13 == "string"
    assert data[0].editions[0].asin == "string"
    assert data[0].editions[0].title == "string"
    assert data[0].editions[0].language == "string"
    assert data[0].editions[0].overview == "string"
    assert data[0].editions[0].format == "string"
    assert data[0].editions[0].isEbook is True
    assert data[0].editions[0].disambiguation == "string"
    assert data[0].editions[0].publisher == "string"
    assert isinstance(data[0].editions[0].pageCount, int)
    assert data[0].editions[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert data[0].editions[0].images[0].url == "string"
    assert data[0].editions[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].editions[0].images[0].extension == "string"
    assert data[0].editions[0].links[0].url == "string"
    assert data[0].editions[0].links[0].name == "string"
    assert isinstance(data[0].editions[0].ratings.votes, int)
    assert isinstance(data[0].editions[0].ratings.value, float)
    assert isinstance(data[0].editions[0].ratings.popularity, int)
    assert data[0].editions[0].monitored is True
    assert data[0].editions[0].manualAdd is True
    assert data[0].editions[0].remoteCover == "string"
    assert data[0].editions[0].grabbed is True
    assert data[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_wanted_missing(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting wanted and missing books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/wanted/missing?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/wanted-missing.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_wanted_missing()
    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == ReadarrSortKeys.BOOK_ID.value
    assert data.sortDirection == SortDirection.DEFAULT.value
    assert isinstance(data.totalRecords, int)
    assert data.records[0].title == "string"
    assert data.records[0].authorTitle == "string"
    assert data.records[0].seriesTitle == "string"
    assert data.records[0].disambiguation == "string"
    assert data.records[0].overview == "string"
    assert isinstance(data.records[0].authorId, int)
    assert data.records[0].foreignBookId == "string"
    assert isinstance(data.records[0].titleSlug, int)
    assert data.records[0].monitored is True
    assert data.records[0].anyEditionOk is True
    assert isinstance(data.records[0].ratings.votes, int)
    assert isinstance(data.records[0].ratings.value, float)
    assert isinstance(data.records[0].ratings.popularity, float)
    assert data.records[0].releaseDate == datetime(2021, 12, 11, 9, 30, 28, 339000)
    assert isinstance(data.records[0].pageCount, int)
    assert data.records[0].genres[0] == "string"
    assert isinstance(data.records[0].author.authorMetadataId, int)
    assert data.records[0].author.status == "string"
    assert data.records[0].author.ended is False
    assert data.records[0].author.authorName == "string"
    assert data.records[0].author.authorNameLastFirst == "string"
    assert data.records[0].author.foreignAuthorId == "string"
    assert isinstance(data.records[0].author.titleSlug, int)
    assert data.records[0].author.overview == "string"
    assert data.records[0].author.links[0].url == "string"
    assert data.records[0].author.links[0].name == "string"
    assert data.records[0].author.images[0].url == "string"
    assert data.records[0].author.images[0].coverType == ImageType.POSTER.value
    assert data.records[0].author.images[0].extension == "string"
    assert data.records[0].author.path == "string"
    assert isinstance(data.records[0].author.qualityProfileId, int)
    assert isinstance(data.records[0].author.metadataProfileId, int)
    assert data.records[0].author.monitored is True
    assert data.records[0].author.monitorNewItems == "string"
    assert data.records[0].author.genres == ["string"]
    assert data.records[0].author.cleanName == "string"
    assert data.records[0].author.sortName == "string"
    assert data.records[0].author.sortNameLastFirst == "string"
    assert isinstance(data.records[0].author.tags[0], int)
    assert data.records[0].author.added == datetime(2021, 12, 6, 22, 23, 55)
    assert isinstance(data.records[0].author.ratings.votes, int)
    assert isinstance(data.records[0].author.ratings.value, float)
    assert isinstance(data.records[0].author.ratings.popularity, float)
    assert isinstance(data.records[0].author.statistics.bookFileCount, int)
    assert isinstance(data.records[0].author.statistics.bookCount, int)
    assert isinstance(data.records[0].author.statistics.availableBookCount, int)
    assert isinstance(data.records[0].author.statistics.totalBookCount, int)
    assert isinstance(data.records[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].author.statistics.percentOfBooks, float)
    assert isinstance(data.records[0].author.id, int)
    assert data.records[0].images[0].url == "string"
    assert data.records[0].images[0].coverType == ImageType.POSTER.value
    assert data.records[0].images[0].extension == "string"
    assert data.records[0].links[0].url == "string"
    assert data.records[0].links[0].name == "string"
    assert isinstance(data.records[0].statistics.bookFileCount, int)
    assert isinstance(data.records[0].statistics.bookCount, int)
    assert isinstance(data.records[0].statistics.totalBookCount, int)
    assert isinstance(data.records[0].statistics.sizeOnDisk, int)
    assert isinstance(data.records[0].statistics.percentOfBooks, float)
    assert data.records[0].added == datetime(2021, 12, 6, 22, 23, 58)
    assert isinstance(data.records[0].editions[0].bookId, int)
    assert data.records[0].editions[0].foreignEditionId == "string"
    assert isinstance(data.records[0].editions[0].titleSlug, int)
    assert data.records[0].editions[0].asin == "string"
    assert data.records[0].editions[0].title == "string"
    assert data.records[0].editions[0].language == "string"
    assert data.records[0].editions[0].overview == "string"
    assert data.records[0].editions[0].format == "string"
    assert data.records[0].editions[0].isEbook is True
    assert data.records[0].editions[0].disambiguation == "string"
    assert data.records[0].editions[0].publisher == "string"
    assert isinstance(data.records[0].editions[0].pageCount, int)
    assert data.records[0].editions[0].releaseDate == datetime(2017, 3, 15, 0, 0)
    assert data.records[0].editions[0].images[0].url == "string"
    assert data.records[0].editions[0].images[0].coverType == ImageType.POSTER.value
    assert data.records[0].editions[0].images[0].extension == "string"
    assert data.records[0].editions[0].links[0].url == "string"
    assert data.records[0].editions[0].links[0].name == "string"
    assert isinstance(data.records[0].editions[0].ratings.votes, int)
    assert isinstance(data.records[0].editions[0].ratings.value, float)
    assert isinstance(data.records[0].editions[0].ratings.popularity, float)
    assert data.records[0].editions[0].monitored is False
    assert data.records[0].editions[0].manualAdd is False
    assert data.records[0].editions[0].grabbed is False
    assert isinstance(data.records[0].editions[0].id, int)
    assert data.records[0].grabbed is False
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_wanted_cutoff(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/wanted/cutoff?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/wanted-cutoff.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_wanted_cutoff()
    assert isinstance(data, ReadarrWantedCutoff)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/wanted/cutoff/0?sortKey=title&page=1&pageSize=10",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_wanted_cutoff(0)
    assert isinstance(data, ReadarrBook)


@pytest.mark.asyncio
async def test_async_get_history(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/history?page=1&pageSize=20&sortDirection=default&sortKey=books.releaseDate&eventType=1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/history.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_history(event_type=ReadarrEventType.GRABBED)
    assert isinstance(data.page, int)
    assert isinstance(data.pageSize, int)
    assert data.sortKey == ReadarrSortKeys.DATE.value
    assert data.sortDirection == SortDirection.DESCENDING.value
    assert isinstance(data.totalRecords, int)
    assert isinstance(data.records[0].bookId, int)
    assert isinstance(data.records[0].authorId, int)
    assert data.records[0].sourceTitle == "string"
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "EPUB"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert data.records[0].qualityCutoffNotMet is False
    assert data.records[0].date == datetime(2021, 12, 31, 1, 13, 38)
    assert data.records[0].downloadId == "string"
    assert data.records[0].eventType == ReadarrEventType.GRABBED.name.lower()
    assert data.records[0].data.indexer == "string"
    assert data.records[0].data.nzbInfoUrl == "string"
    assert data.records[0].data.releaseGroup is None
    assert isinstance(data.records[0].data.age, int)
    assert isinstance(data.records[0].data.ageHours, float)
    assert isinstance(data.records[0].data.ageMinutes, float)
    assert data.records[0].data.publishedDate == datetime(2020, 6, 6, 4, 0)
    assert data.records[0].data.downloadClient == "string"
    assert isinstance(data.records[0].data.size, int)
    assert data.records[0].data.downloadUrl == "string"
    assert data.records[0].data.guid == "string"
    assert data.records[0].data.protocol is ProtocolType.UNKNOWN
    assert data.records[0].data.downloadForced is False
    assert data.records[0].data.torrentInfoHash == "string"
    assert isinstance(data.records[0].data.fileId, int)
    assert data.records[0].data.reason == "string"
    assert data.records[0].data.droppedPath == "string"
    assert data.records[0].data.importedPath == "string"
    assert data.records[0].data.downloadClientName == "string"
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_history_since(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/history/since?eventType=1&date=2020-11-30",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    date = datetime.strptime("Nov 30 2020  1:33PM", "%b %d %Y %I:%M%p")
    data = await readarr_client.async_get_history_since(
        event_type=ReadarrEventType.GRABBED, date=date
    )
    assert isinstance(data, ReadarrBookHistory)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/history/author?authorId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_get_history_since(authorid=0)

    with pytest.raises(ArrException):
        await readarr_client.async_get_history_since()


@pytest.mark.asyncio
async def test_async_get_import_lists(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/importlist.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_import_lists()
    assert data[0].enableAutomaticAdd is True
    assert data[0].shouldMonitor == MonitoringOptionsType.ALL.value
    assert data[0].shouldMonitorExisting is False
    assert data[0].rootFolderPath == "string"
    assert data[0].monitorNewItems == "string"
    assert isinstance(data[0].qualityProfileId, int)
    assert data[0].listType == "string"
    assert isinstance(data[0].listOrder, int)
    assert data[0].name == "string"
    assert isinstance(data[0].fields[0].order, int)
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == ["string"]
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is False
    assert data[0].fields[0].hidden == "string"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert isinstance(data[0].tags[0], int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_metadata_profiles(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting wanted cutoff books."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/metadataprofile",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/metadata-profile.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_metadata_profiles()
    assert isinstance(data[0].id, int)
    assert data[0].name == "string"
    assert isinstance(data[0].minPages, int)
    assert data[0].skipMissingDate is True
    assert data[0].skipMissingIsbn is True
    assert data[0].skipPartsAndSets is True
    assert data[0].skipSeriesSecondary is True
    assert data[0].allowedLanguages == "string"
    assert isinstance(data[0].minPages, int)
    assert data[0].ignored == "string"


@pytest.mark.asyncio
async def test_async_get_metadata_provider(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting metadata provider."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/metadataprovider",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/config-metadataprovider.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_metadata_provider()
    assert data.scrubAudioTags is False
    assert data.writeBookTags == "newFiles"
    assert data.updateCovers is True
    assert data.embedMetadata is False
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_naming_config(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting naming configuration."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/naming",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/config-naming.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_naming_config()

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
async def test_async_get_notifications(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting notifications."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/notification.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_notifications()

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
    assert isinstance(data[0].fields[0].order, int)
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
    assert isinstance(data[0].tags[0], int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_parse(aresponses, readarr_client: ReadarrClient) -> None:
    """Test parsing book file name."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/parse?title=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/parse.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_parse("test")

    assert isinstance(data.id, int)
    assert data.title == "string"
    assert data.parsedBookInfo.bookTitle == "string"
    assert data.parsedBookInfo.authorName == "string"
    assert data.parsedBookInfo.authorTitleInfo.title == "string"
    assert data.parsedBookInfo.authorTitleInfo.titleWithoutYear == "string"
    assert isinstance(data.parsedBookInfo.authorTitleInfo.year, int)
    assert isinstance(data.parsedBookInfo.quality.quality.id, int)
    assert data.parsedBookInfo.quality.quality.name == "string"
    assert isinstance(data.parsedBookInfo.quality.revision.version, int)
    assert isinstance(data.parsedBookInfo.quality.revision.real, int)
    assert data.parsedBookInfo.quality.revision.isRepack is True
    assert data.parsedBookInfo.releaseDate == datetime(2021, 12, 7, 8, 55, 41, 226000)
    assert data.parsedBookInfo.discography is True
    assert isinstance(data.parsedBookInfo.discographyStart, int)
    assert isinstance(data.parsedBookInfo.discographyEnd, int)
    assert data.parsedBookInfo.releaseGroup == "string"
    assert data.parsedBookInfo.releaseHash == "string"
    assert data.parsedBookInfo.releaseVersion == "string"
    assert isinstance(data.author.id, int)
    assert isinstance(data.author.authorMetadataId, int)
    assert data.author.status == "string"
    assert data.author.ended is True
    assert data.author.authorName == "string"
    assert data.author.authorNameLastFirst == "string"
    assert data.author.foreignAuthorId == "string"
    assert isinstance(data.author.titleSlug, int)
    assert data.author.overview == "string"
    assert data.author.links[0].url == "string"
    assert data.author.links[0].name == "string"
    _value = data.author.nextBook
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.foreignBookId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.title == "string"
    assert _value.releaseDate == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, float)
    assert _value.cleanTitle == "string"
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert _value.lastInfoSync == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.added == datetime(2020, 2, 6, 12, 49, 48, 602000)
    assert _value.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.addOptions.searchForNewBook is True
    assert isinstance(_value.authorMetadata.value.id, int)
    assert _value.authorMetadata.value.foreignAuthorId == "string"
    assert isinstance(_value.authorMetadata.value.titleSlug, int)
    assert _value.authorMetadata.value.name == "string"
    assert _value.authorMetadata.value.sortName == "string"
    assert _value.authorMetadata.value.nameLastFirst == "string"
    assert _value.authorMetadata.value.sortNameLastFirst == "string"
    assert _value.authorMetadata.value.aliases == ["string"]
    assert _value.authorMetadata.value.overview == "string"
    assert _value.authorMetadata.value.gender == "string"
    assert _value.authorMetadata.value.hometown == "string"
    assert _value.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.authorMetadata.value.status == "string"
    assert _value.authorMetadata.value.images[0].url == "string"
    assert _value.authorMetadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.authorMetadata.value.images[0].extension == "string"
    assert _value.authorMetadata.value.links[0].url == "string"
    assert _value.authorMetadata.value.links[0].name == "string"
    assert _value.authorMetadata.value.genres == ["string"]
    assert isinstance(_value.authorMetadata.value.ratings.votes, int)
    assert isinstance(_value.authorMetadata.value.ratings.value, float)
    assert isinstance(_value.authorMetadata.value.ratings.popularity, float)
    assert _value.authorMetadata.isLoaded is True
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 602000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor == ["string"]
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _val = _value.author.value.metadata
    assert isinstance(_val.value.id, int)
    assert _val.value.foreignAuthorId == "string"
    assert isinstance(_val.value.titleSlug, int)
    assert _val.value.name == "string"
    assert _val.value.nameLastFirst == "string"
    assert _val.value.sortNameLastFirst == "string"
    assert _val.value.aliases == ["string"]
    assert _val.value.overview == "string"
    assert _val.value.gender == "string"
    assert _val.value.hometown == "string"
    assert _val.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.value.status == "string"
    assert _val.value.images[0].url == "string"
    assert _val.value.images[0].coverType == ImageType.POSTER.value
    assert _val.value.images[0].extension == "string"
    assert _val.value.links[0].url == "string"
    assert _val.value.links[0].name == "string"
    assert _val.value.genres == ["string"]
    assert isinstance(_val.value.ratings.votes, int)
    assert isinstance(_val.value.ratings.value, float)
    assert isinstance(_val.value.ratings.popularity, float)
    assert _val.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    _val = _value.editions.value[0]
    assert isinstance(_val.id, int)
    assert isinstance(_val.bookId, int)
    assert _val.foreignEditionId == "string"
    assert isinstance(_val.titleSlug, int)
    assert _val.isbn13 == "string"
    assert _val.asin == "string"
    assert _val.title == "string"
    assert _val.language == "string"
    assert _val.overview == "string"
    assert _val.format == "string"
    assert _val.isEbook is True
    assert _val.publisher == "string"
    assert isinstance(_val.pageCount, int)
    assert _val.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == ImageType.POSTER.value
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert isinstance(_val.ratings.votes, int)
    assert isinstance(_val.ratings.value, float)
    assert isinstance(_val.ratings.popularity, float)
    assert _val.monitored is True
    assert _val.manualAdd is True
    assert _val.book.isLoaded is True
    assert isinstance(_val.bookFiles.value[0].id, int)
    assert _val.bookFiles.value[0].path == "string"
    assert isinstance(_val.bookFiles.value[0].size, int)
    assert _val.bookFiles.value[0].modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.bookFiles.value[0].dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.bookFiles.value[0].sceneName == "string"
    assert _val.bookFiles.value[0].releaseGroup == "string"
    assert isinstance(_val.bookFiles.value[0].quality.quality.id, int)
    assert _val.bookFiles.value[0].quality.quality.name == "string"
    assert isinstance(_val.bookFiles.value[0].quality.revision.version, int)
    assert isinstance(_val.bookFiles.value[0].quality.revision.real, int)
    assert _val.bookFiles.value[0].quality.revision.isRepack is True
    assert _val.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioBitrate, int)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioChannels, float)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioBits, int)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioSampleRate, int)
    assert isinstance(_val.bookFiles.value[0].editionId, int)
    assert isinstance(_val.bookFiles.value[0].calibreId, int)
    assert isinstance(_val.bookFiles.value[0].part, int)
    _valu = _val.bookFiles.value[0].author.value
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.authorMetadataId, int)
    assert _valu.cleanName == "string"
    assert _valu.monitored is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.path == "string"
    assert _valu.rootFolderPath == "string"
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_valu.qualityProfileId, int)
    assert isinstance(_valu.metadataProfileId, int)
    assert isinstance(_valu.tags[0], int)
    assert _valu.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _valu.addOptions.booksToMonitor == ["string"]
    assert _valu.addOptions.monitored is True
    assert _valu.addOptions.searchForMissingBooks is True
    assert isinstance(_valu.metadata.value.id, int)
    assert _valu.metadata.value.foreignAuthorId == "string"
    assert isinstance(_valu.metadata.value.titleSlug, int)
    assert _valu.metadata.value.name == "string"
    assert _valu.metadata.value.sortName == "string"
    assert _valu.metadata.value.nameLastFirst == "string"
    assert _valu.metadata.value.sortNameLastFirst == "string"
    assert _valu.metadata.value.aliases == ["string"]
    assert _valu.metadata.value.overview == "string"
    assert _valu.metadata.value.gender == "string"
    assert _valu.metadata.value.hometown == "string"
    assert _valu.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.status == "string"
    assert _valu.metadata.value.images[0].url == "string"
    assert _valu.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _valu.metadata.value.images[0].extension == "string"
    assert _valu.metadata.value.links[0].url == "string"
    assert _valu.metadata.value.links[0].name == "string"
    assert _valu.metadata.value.genres == ["string"]
    assert isinstance(_valu.metadata.value.ratings.votes, int)
    assert isinstance(_valu.metadata.value.ratings.value, float)
    assert isinstance(_valu.metadata.value.ratings.popularity, float)
    assert _valu.metadata.isLoaded is True
    assert isinstance(_valu.qualityProfile.value.id, int)
    assert _valu.qualityProfile.value.name == "string"
    assert _valu.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_valu.qualityProfile.value.cutoff, int)
    assert isinstance(_valu.qualityProfile.value.items[0].id, int)
    assert _valu.qualityProfile.value.items[0].name == "string"
    assert isinstance(_valu.qualityProfile.value.items[0].quality.id, int)
    assert _valu.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.qualityProfile.value.items[0].items == [None]
    assert _valu.qualityProfile.value.items[0].allowed is True
    assert _valu.qualityProfile.isLoaded is True
    assert isinstance(_valu.metadataProfile.value.id, int)
    assert _valu.metadataProfile.value.name == "string"
    assert isinstance(_valu.metadataProfile.value.minPopularity, int)
    assert _valu.metadataProfile.value.skipMissingDate is True
    assert _valu.metadataProfile.value.skipMissingIsbn is True
    assert _valu.metadataProfile.value.skipPartsAndSets is True
    assert _valu.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_valu.metadataProfile.value.minPages, int)
    assert _valu.metadataProfile.value.ignored == "string"
    assert _valu.metadataProfile.isLoaded is True
    assert _valu.books.value == [None]
    assert _valu.books.isLoaded is True
    assert isinstance(_valu.series.value[0].id, int)
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert isinstance(_valu.series.value[0].workCount, int)
    assert isinstance(_valu.series.value[0].primaryWorkCount, int)
    assert _valu.series.value[0].books.value == [None]
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.isLoaded is True
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert _val.bookFiles.value[0].author.isLoaded is True
    assert _val.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_val.bookFiles.value[0].partCount, int)
    assert _val.bookFiles.isLoaded is True
    assert _value.editions.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert isinstance(_valu.id, int)
    assert _valu.path == "string"
    assert isinstance(_valu.size, int)
    assert _valu.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert isinstance(_valu.quality.quality.id, int)
    assert _valu.quality.quality.name == "string"
    assert isinstance(_valu.quality.revision.version, int)
    assert isinstance(_valu.quality.revision.real, int)
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert isinstance(_valu.mediaInfo.audioBitrate, int)
    assert isinstance(_valu.mediaInfo.audioChannels, float)
    assert isinstance(_valu.mediaInfo.audioBits, int)
    assert isinstance(_valu.mediaInfo.audioSampleRate, int)
    assert isinstance(_valu.editionId, int)
    assert isinstance(_valu.calibreId, int)
    assert isinstance(_valu.part, int)
    _valu = _value.bookFiles.value[0].author.value
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.authorMetadataId, int)
    assert _valu.cleanName == "string"
    assert _valu.monitored is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.path == "string"
    assert _valu.rootFolderPath == "string"
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_valu.qualityProfileId, int)
    assert isinstance(_valu.metadataProfileId, int)
    assert isinstance(_valu.tags[0], int)
    assert _valu.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _valu.addOptions.booksToMonitor == ["string"]
    assert _valu.addOptions.monitored is True
    assert _valu.addOptions.searchForMissingBooks is True
    assert isinstance(_valu.metadata.value.id, int)
    assert _valu.metadata.value.foreignAuthorId == "string"
    assert isinstance(_valu.metadata.value.titleSlug, int)
    assert _valu.metadata.value.name == "string"
    assert _valu.metadata.value.sortName == "string"
    assert _valu.metadata.value.nameLastFirst == "string"
    assert _valu.metadata.value.sortNameLastFirst == "string"
    assert _valu.metadata.value.aliases == ["string"]
    assert _valu.metadata.value.overview == "string"
    assert _valu.metadata.value.gender == "string"
    assert _valu.metadata.value.hometown == "string"
    assert _valu.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.metadata.value.status == "string"
    assert _valu.metadata.value.images[0].url == "string"
    assert _valu.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _valu.metadata.value.images[0].extension == "string"
    assert _valu.metadata.value.links[0].url == "string"
    assert _valu.metadata.value.links[0].name == "string"
    assert _valu.metadata.value.genres == ["string"]
    assert isinstance(_valu.metadata.value.ratings.votes, int)
    assert isinstance(_valu.metadata.value.ratings.value, float)
    assert isinstance(_valu.metadata.value.ratings.popularity, float)
    assert _valu.metadata.isLoaded is True
    assert isinstance(_valu.qualityProfile.value.id, int)
    assert _valu.qualityProfile.value.name == "string"
    assert _valu.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_valu.qualityProfile.value.cutoff, int)
    assert isinstance(_valu.qualityProfile.value.items[0].id, int)
    assert _valu.qualityProfile.value.items[0].name == "string"
    assert isinstance(_valu.qualityProfile.value.items[0].quality.id, int)
    assert _valu.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.qualityProfile.value.items[0].items == [None]
    assert _valu.qualityProfile.value.items[0].allowed is True
    assert _valu.qualityProfile.isLoaded is True
    assert isinstance(_valu.metadataProfile.value.id, int)
    assert _valu.metadataProfile.value.name == "string"
    assert isinstance(_valu.metadataProfile.value.minPopularity, int)
    assert _valu.metadataProfile.value.skipMissingDate is True
    assert _valu.metadataProfile.value.skipMissingIsbn is True
    assert _valu.metadataProfile.value.skipPartsAndSets is True
    assert _valu.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_valu.metadataProfile.value.minPages, int)
    assert _valu.metadataProfile.value.ignored == "string"
    assert _valu.metadataProfile.isLoaded is True
    assert _valu.books.value == [None]
    assert _valu.books.isLoaded is True
    assert isinstance(_valu.series.value[0].id, int)
    assert _valu.series.value[0].foreignSeriesId == "string"
    assert _valu.series.value[0].title == "string"
    assert _valu.series.value[0].description == "string"
    assert _valu.series.value[0].numbered is True
    assert isinstance(_valu.series.value[0].workCount, int)
    assert isinstance(_valu.series.value[0].primaryWorkCount, int)
    assert _valu.series.value[0].books.value == [None]
    assert _valu.series.value[0].books.isLoaded is True
    assert _valu.series.value[0].foreignAuthorId == "string"
    assert _valu.series.isLoaded is True
    assert _valu.name == "string"
    assert _valu.foreignAuthorId == "string"
    assert _value.bookFiles.value[0].author.isLoaded is True
    assert _value.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_value.bookFiles.value[0].partCount, int)
    assert _value.bookFiles.isLoaded is True
    assert isinstance(_value.seriesLinks.value[0].id, int)
    assert _value.seriesLinks.value[0].position == "string"
    assert isinstance(_value.seriesLinks.value[0].seriesId, int)
    assert isinstance(_value.seriesLinks.value[0].bookId, int)
    assert _value.seriesLinks.value[0].isPrimary is True
    assert isinstance(_value.seriesLinks.value[0].series.value.id, int)
    assert _value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _value.seriesLinks.value[0].series.value.title == "string"
    assert _value.seriesLinks.value[0].series.value.description == "string"
    assert _value.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_value.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_value.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _value.seriesLinks.value[0].series.value.books.value == [None]
    assert _value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _value.seriesLinks.value[0].series.isLoaded is True
    assert _value.seriesLinks.value[0].book.isLoaded is True
    assert _value.seriesLinks.isLoaded is True
    assert isinstance(data.author.lastBook.id, int)
    assert isinstance(data.author.lastBook.authorMetadataId, int)
    assert data.author.lastBook.foreignBookId == "string"
    assert isinstance(data.author.lastBook.titleSlug, int)
    assert data.author.lastBook.title == "string"
    assert data.author.lastBook.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.links[0].url == "string"
    assert data.author.lastBook.links[0].name == "string"
    assert data.author.lastBook.genres[0] == "string"
    assert isinstance(data.author.lastBook.ratings.votes, int)
    assert isinstance(data.author.lastBook.ratings.value, float)
    assert isinstance(data.author.lastBook.ratings.popularity, float)
    assert data.author.lastBook.cleanTitle == "string"
    assert data.author.lastBook.monitored is True
    assert data.author.lastBook.anyEditionOk is True
    assert data.author.lastBook.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.lastBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.author.lastBook.addOptions.searchForNewBook is True
    _value = data.author.lastBook
    assert isinstance(_value.authorMetadata.value.id, int)
    assert _value.authorMetadata.value.foreignAuthorId == "string"
    assert isinstance(_value.authorMetadata.value.titleSlug, int)
    assert _value.authorMetadata.value.name == "string"
    assert _value.authorMetadata.value.sortName == "string"
    assert _value.authorMetadata.value.nameLastFirst == "string"
    assert _value.authorMetadata.value.sortNameLastFirst == "string"
    assert _value.authorMetadata.value.aliases == ["string"]
    assert _value.authorMetadata.value.overview == "string"
    assert _value.authorMetadata.value.gender == "string"
    assert _value.authorMetadata.value.hometown == "string"
    assert _value.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.authorMetadata.value.status == "string"
    assert _value.authorMetadata.value.images[0].url == "string"
    assert _value.authorMetadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.authorMetadata.value.images[0].extension == "string"
    assert _value.authorMetadata.value.links[0].url == "string"
    assert _value.authorMetadata.value.links[0].name == "string"
    assert _value.authorMetadata.value.genres == ["string"]
    assert isinstance(_value.authorMetadata.value.ratings.votes, int)
    assert isinstance(_value.authorMetadata.value.ratings.value, float)
    assert isinstance(_value.authorMetadata.value.ratings.popularity, float)
    assert _value.authorMetadata.isLoaded is True
    assert isinstance(_value.author.value.id, int)
    assert isinstance(_value.author.value.authorMetadataId, int)
    assert _value.author.value.cleanName == "string"
    assert _value.author.value.monitored is True
    assert _value.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _value.author.value.path == "string"
    assert _value.author.value.rootFolderPath == "string"
    assert _value.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_value.author.value.qualityProfileId, int)
    assert isinstance(_value.author.value.metadataProfileId, int)
    assert isinstance(_value.author.value.tags[0], int)
    assert _value.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.value.addOptions.booksToMonitor == ["string"]
    assert _value.author.value.addOptions.monitored is True
    assert _value.author.value.addOptions.searchForMissingBooks is True
    _valu = _value.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases == ["string"]
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, float)
    assert _value.author.value.metadata.isLoaded is True
    assert isinstance(_value.author.value.qualityProfile.value.id, int)
    assert _value.author.value.qualityProfile.value.name == "string"
    assert _value.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.author.value.qualityProfile.value.items[0].id, int)
    assert _value.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _value.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.author.value.qualityProfile.value.items[0].items == [None]
    assert _value.author.value.qualityProfile.value.items[0].allowed is True
    assert _value.author.value.qualityProfile.isLoaded is True
    assert isinstance(_value.author.value.metadataProfile.value.id, int)
    assert _value.author.value.metadataProfile.value.name == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPopularity, int)
    assert _value.author.value.metadataProfile.value.skipMissingDate is True
    assert _value.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _value.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _value.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.author.value.metadataProfile.value.minPages, int)
    assert _value.author.value.metadataProfile.value.ignored == "string"
    assert _value.author.value.metadataProfile.isLoaded is True
    assert _value.author.value.books.value == [None]
    assert _value.author.value.books.isLoaded is True
    assert isinstance(_value.author.value.series.value[0].id, int)
    assert _value.author.value.series.value[0].foreignSeriesId == "string"
    assert _value.author.value.series.value[0].title == "string"
    assert _value.author.value.series.value[0].description == "string"
    assert _value.author.value.series.value[0].numbered is True
    assert isinstance(_value.author.value.series.value[0].workCount, int)
    assert isinstance(_value.author.value.series.value[0].primaryWorkCount, int)
    assert _value.author.value.series.value[0].books.value == [None]
    assert _value.author.value.series.value[0].books.isLoaded is True
    assert _value.author.value.series.value[0].foreignAuthorId == "string"
    assert _value.author.value.series.isLoaded is True
    assert _value.author.value.name == "string"
    assert _value.author.value.foreignAuthorId == "string"
    assert _value.author.isLoaded is True
    _valu = _value.editions.value[0]
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.bookId, int)
    assert _valu.foreignEditionId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.publisher == "string"
    assert isinstance(_valu.pageCount, int)
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, float)
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert isinstance(_va.id, int)
    assert _va.foreignAuthorId == "string"
    assert isinstance(_va.titleSlug, int)
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == ImageType.POSTER.value
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert isinstance(_va.ratings.votes, int)
    assert isinstance(_va.ratings.value, float)
    assert isinstance(_va.ratings.popularity, float)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value == [None]
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert _valu.bookFiles.isLoaded is True
    assert _value.editions.isLoaded is True
    _valu = _value.bookFiles.value[0]
    assert isinstance(_valu.id, int)
    assert _valu.path == "string"
    assert isinstance(_valu.size, int)
    assert _valu.modified == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.sceneName == "string"
    assert _valu.releaseGroup == "string"
    assert isinstance(_valu.quality.quality.id, int)
    assert _valu.quality.quality.name == "string"
    assert isinstance(_valu.quality.revision.version, int)
    assert isinstance(_valu.quality.revision.real, int)
    assert _valu.quality.revision.isRepack is True
    assert _valu.mediaInfo.audioFormat == "string"
    assert isinstance(_valu.mediaInfo.audioBitrate, int)
    assert isinstance(_valu.mediaInfo.audioChannels, float)
    assert isinstance(_valu.mediaInfo.audioBits, int)
    assert isinstance(_valu.mediaInfo.audioSampleRate, int)
    assert isinstance(_valu.editionId, int)
    assert isinstance(_valu.calibreId, int)
    assert isinstance(_valu.part, int)
    _val = _valu.author.value
    assert isinstance(_val.id, int)
    assert isinstance(_val.authorMetadataId, int)
    assert _val.cleanName == "string"
    assert _val.monitored is True
    assert _val.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.path == "string"
    assert _val.rootFolderPath == "string"
    assert _val.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_val.qualityProfileId, int)
    assert isinstance(_val.metadataProfileId, int)
    assert isinstance(_val.tags[0], int)
    assert _val.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.addOptions.booksToMonitor == ["string"]
    assert _val.addOptions.monitored is True
    assert _val.addOptions.searchForMissingBooks is True
    assert isinstance(_val.metadata.value.id, int)
    assert _val.metadata.value.foreignAuthorId == "string"
    assert isinstance(_val.metadata.value.titleSlug, int)
    assert _val.metadata.value.name == "string"
    assert _val.metadata.value.sortName == "string"
    assert _val.metadata.value.nameLastFirst == "string"
    assert _val.metadata.value.sortNameLastFirst == "string"
    assert _val.metadata.value.aliases == ["string"]
    assert _val.metadata.value.overview == "string"
    assert _val.metadata.value.gender == "string"
    assert _val.metadata.value.hometown == "string"
    assert _val.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _val.metadata.value.status == "string"
    assert _val.metadata.value.images[0].url == "string"
    assert _val.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _val.metadata.value.images[0].extension == "string"
    assert _val.metadata.value.links[0].url == "string"
    assert _val.metadata.value.links[0].name == "string"
    assert _val.metadata.value.genres == ["string"]
    assert isinstance(_val.metadata.value.ratings.votes, int)
    assert isinstance(_val.metadata.value.ratings.value, float)
    assert isinstance(_val.metadata.value.ratings.popularity, float)
    assert _val.metadata.isLoaded is True
    assert isinstance(_val.qualityProfile.value.id, int)
    assert _val.qualityProfile.value.name == "string"
    assert _val.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.qualityProfile.value.cutoff, int)
    assert isinstance(_val.qualityProfile.value.items[0].id, int)
    assert _val.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.qualityProfile.value.items[0].quality.id, int)
    assert _val.qualityProfile.value.items[0].quality.name == "string"
    assert _val.qualityProfile.value.items[0].items == [None]
    assert _val.qualityProfile.value.items[0].allowed is True
    assert _val.qualityProfile.isLoaded is True
    assert isinstance(_val.metadataProfile.value.id, int)
    assert _val.metadataProfile.value.name == "string"
    assert isinstance(_val.metadataProfile.value.minPopularity, int)
    assert _val.metadataProfile.value.skipMissingDate is True
    assert _val.metadataProfile.value.skipMissingIsbn is True
    assert _val.metadataProfile.value.skipPartsAndSets is True
    assert _val.metadataProfile.value.skipSeriesSecondary is True
    assert _val.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.metadataProfile.value.minPages, int)
    assert _val.metadataProfile.value.ignored == "string"
    assert _val.metadataProfile.isLoaded is True
    assert _val.books.value == [None]
    assert _val.books.isLoaded is True
    assert isinstance(_val.series.value[0].id, int)
    assert _val.series.value[0].foreignSeriesId == "string"
    assert _val.series.value[0].title == "string"
    assert _val.series.value[0].description == "string"
    assert _val.series.value[0].numbered is True
    assert isinstance(_val.series.value[0].workCount, int)
    assert isinstance(_val.series.value[0].primaryWorkCount, int)
    assert _val.series.value[0].books.value == [None]
    assert _val.series.value[0].books.isLoaded is True
    assert _val.series.value[0].foreignAuthorId == "string"
    assert _val.series.isLoaded is True
    assert _val.name == "string"
    assert _val.foreignAuthorId == "string"
    assert _valu.author.isLoaded is True
    assert _valu.edition.isLoaded is True
    assert isinstance(_valu.partCount, int)
    assert _value.bookFiles.isLoaded is True
    assert isinstance(_value.seriesLinks.value[0].id, int)
    assert _value.seriesLinks.value[0].position == "string"
    assert isinstance(_value.seriesLinks.value[0].seriesId, int)
    assert isinstance(_value.seriesLinks.value[0].bookId, int)
    assert _value.seriesLinks.value[0].isPrimary is True
    assert isinstance(_value.seriesLinks.value[0].series.value.id, int)
    assert _value.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _value.seriesLinks.value[0].series.value.title == "string"
    assert _value.seriesLinks.value[0].series.value.description == "string"
    assert _value.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_value.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_value.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _value.seriesLinks.value[0].series.value.books.value == [None]
    assert _value.seriesLinks.value[0].series.value.books.isLoaded is True
    assert _value.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _value.seriesLinks.value[0].series.isLoaded is True
    assert _value.seriesLinks.value[0].book.isLoaded is True
    assert _value.seriesLinks.isLoaded is True
    assert data.author.images[0].url == "string"
    assert data.author.images[0].coverType == ImageType.POSTER.value
    assert data.author.images[0].extension == "string"
    assert data.author.remotePoster == "string"
    assert data.author.path == "string"
    assert isinstance(data.author.qualityProfileId, int)
    assert isinstance(data.author.metadataProfileId, int)
    assert data.author.monitored is True
    assert data.author.rootFolderPath == "string"
    assert data.author.genres == ["string"]
    assert data.author.cleanName == "string"
    assert data.author.sortName == "string"
    assert data.author.sortNameLastFirst == "string"
    assert isinstance(data.author.tags[0], int)
    assert data.author.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert data.author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data.author.addOptions.booksToMonitor == ["string"]
    assert data.author.addOptions.monitored is True
    assert data.author.addOptions.searchForMissingBooks is True
    assert isinstance(data.author.ratings.votes, int)
    assert isinstance(data.author.ratings.value, float)
    assert isinstance(data.author.ratings.popularity, float)
    assert isinstance(data.author.statistics.bookFileCount, int)
    assert isinstance(data.author.statistics.bookCount, int)
    assert isinstance(data.author.statistics.availableBookCount, int)
    assert isinstance(data.author.statistics.totalBookCount, int)
    assert isinstance(data.author.statistics.sizeOnDisk, int)
    assert isinstance(data.author.statistics.percentOfBooks, float)
    assert isinstance(data.books[0].id, int)
    assert data.books[0].title == "string"
    assert data.books[0].authorTitle == "string"
    assert data.books[0].seriesTitle == "string"
    assert data.books[0].overview == "string"
    assert isinstance(data.books[0].authorId, int)
    assert data.books[0].foreignBookId == "string"
    assert isinstance(data.books[0].titleSlug, int)
    assert data.books[0].monitored is True
    assert data.books[0].anyEditionOk is True
    assert isinstance(data.books[0].ratings.votes, int)
    assert isinstance(data.books[0].ratings.value, float)
    assert isinstance(data.books[0].ratings.popularity, float)
    assert data.books[0].releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(data.books[0].pageCount, int)
    assert data.books[0].genres == ["string"]
    assert isinstance(data.books[0].author.id, int)
    assert isinstance(data.books[0].author.authorMetadataId, int)
    assert data.books[0].author.status == "string"
    assert data.books[0].author.ended is True
    assert data.books[0].author.authorName == "string"
    assert data.books[0].author.authorNameLastFirst == "string"
    assert data.books[0].author.foreignAuthorId == "string"
    assert isinstance(data.books[0].author.titleSlug, int)
    assert data.books[0].author.overview == "string"
    assert data.books[0].author.links[0].url == "string"
    assert data.books[0].author.links[0].name == "string"
    _book = data.books[0].author.nextBook
    assert isinstance(_book.id, int)
    assert isinstance(_book.authorMetadataId, int)
    assert _book.foreignBookId == "string"
    assert isinstance(_book.titleSlug, int)
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres == ["string"]
    assert isinstance(_book.ratings.votes, int)
    assert isinstance(_book.ratings.value, float)
    assert isinstance(_book.ratings.popularity, float)
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _book.addOptions.searchForNewBook is True
    assert isinstance(_book.authorMetadata.value.id, int)
    assert _book.authorMetadata.value.foreignAuthorId == "string"
    assert isinstance(_book.authorMetadata.value.titleSlug, int)
    assert _book.authorMetadata.value.name == "string"
    assert _book.authorMetadata.value.sortName == "string"
    assert _book.authorMetadata.value.sortNameLastFirst == "string"
    assert _book.authorMetadata.value.aliases == ["string"]
    assert _book.authorMetadata.value.overview == "string"
    assert _book.authorMetadata.value.gender == "string"
    assert _book.authorMetadata.value.hometown == "string"
    assert _book.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.authorMetadata.value.status == "string"
    assert _book.authorMetadata.value.images[0].url == "string"
    assert _book.authorMetadata.value.images[0].coverType == ImageType.POSTER.value
    assert _book.authorMetadata.value.images[0].extension == "string"
    assert _book.authorMetadata.value.links[0].url == "string"
    assert _book.authorMetadata.value.links[0].name == "string"
    assert _book.authorMetadata.value.genres == ["string"]
    assert isinstance(_book.authorMetadata.value.ratings.votes, int)
    assert isinstance(_book.authorMetadata.value.ratings.value, float)
    assert isinstance(_book.authorMetadata.value.ratings.popularity, float)
    assert _book.authorMetadata.isLoaded is True
    assert isinstance(_book.author.value.id, int)
    assert isinstance(_book.author.value.authorMetadataId, int)
    assert _book.author.value.cleanName == "string"
    assert _book.author.value.monitored is True
    assert _book.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _book.author.value.path == "string"
    assert _book.author.value.rootFolderPath == "string"
    assert _book.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert isinstance(_book.author.value.qualityProfileId, int)
    assert isinstance(_book.author.value.metadataProfileId, int)
    assert isinstance(_book.author.value.tags[0], int)
    assert _book.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _book.author.value.addOptions.booksToMonitor == ["string"]
    assert _book.author.value.addOptions.monitored is True
    assert _book.author.value.addOptions.searchForMissingBooks is True
    _valu = _book.author.value.metadata.value
    assert isinstance(_valu.id, int)
    assert _valu.foreignAuthorId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.name == "string"
    assert _valu.sortName == "string"
    assert _valu.nameLastFirst == "string"
    assert _valu.sortNameLastFirst == "string"
    assert _valu.aliases == ["string"]
    assert _valu.overview == "string"
    assert _valu.gender == "string"
    assert _valu.hometown == "string"
    assert _valu.born == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.died == datetime(2020, 1, 6, 12, 49, 48, 603000)
    assert _valu.status == "string"
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, float)
    assert _book.author.value.metadata.isLoaded is True
    assert isinstance(_book.author.value.qualityProfile.value.id, int)
    assert _book.author.value.qualityProfile.value.name == "string"
    assert _book.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_book.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_book.author.value.qualityProfile.value.items[0].id, int)
    assert _book.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_book.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _book.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _book.author.value.qualityProfile.value.items[0].items == [None]
    assert _book.author.value.qualityProfile.value.items[0].allowed is True
    assert _book.author.value.qualityProfile.isLoaded is True
    assert isinstance(_book.author.value.metadataProfile.value.id, int)
    assert _book.author.value.metadataProfile.value.name == "string"
    assert isinstance(_book.author.value.metadataProfile.value.minPopularity, int)
    assert _book.author.value.metadataProfile.value.skipMissingDate is True
    assert _book.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _book.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _book.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _book.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_book.author.value.metadataProfile.value.minPages, int)
    assert _book.author.value.metadataProfile.value.ignored == "string"
    assert _book.author.value.metadataProfile.isLoaded is True
    assert _book.author.value.books.value == [None]
    assert _book.author.value.books.isLoaded is True
    assert isinstance(_book.author.value.series.value[0].id, int)
    assert _book.author.value.series.value[0].foreignSeriesId == "string"
    assert _book.author.value.series.value[0].title == "string"
    assert _book.author.value.series.value[0].description == "string"
    assert _book.author.value.series.value[0].numbered is True
    assert isinstance(_book.author.value.series.value[0].workCount, int)
    assert isinstance(_book.author.value.series.value[0].primaryWorkCount, int)
    assert _book.author.value.series.value[0].books.value == [None]
    assert _book.author.value.series.value[0].books.isLoaded is True
    assert _book.author.value.series.value[0].foreignAuthorId == "string"
    assert _book.author.value.series.isLoaded is True
    assert _book.author.value.name == "string"
    assert _book.author.value.foreignAuthorId == "string"
    assert _book.author.isLoaded is True
    _valu = _book.editions.value[0]
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.bookId, int)
    assert _valu.foreignEditionId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.isbn13 == "string"
    assert _valu.asin == "string"
    assert _valu.title == "string"
    assert _valu.language == "string"
    assert _valu.overview == "string"
    assert _valu.format == "string"
    assert _valu.isEbook is True
    assert _valu.publisher == "string"
    assert isinstance(_valu.pageCount, int)
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.images[0].url == "string"
    assert _valu.images[0].coverType == ImageType.POSTER.value
    assert _valu.images[0].extension == "string"
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, float)
    assert _valu.monitored is True
    assert _valu.manualAdd is True
    assert _valu.book.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert isinstance(_va.id, int)
    assert _va.foreignAuthorId == "string"
    assert isinstance(_va.titleSlug, int)
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == ImageType.POSTER.value
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert isinstance(_va.ratings.votes, int)
    assert isinstance(_va.ratings.value, float)
    assert isinstance(_va.ratings.popularity, float)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value == [None]
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert _valu.bookFiles.isLoaded is True
    _val = _book.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert isinstance(_va.id, int)
    assert _va.foreignAuthorId == "string"
    assert isinstance(_va.titleSlug, int)
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == ImageType.POSTER.value
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert isinstance(_va.ratings.votes, int)
    assert isinstance(_va.ratings.value, float)
    assert isinstance(_va.ratings.popularity, float)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert _book.bookFiles.isLoaded is True
    assert isinstance(_book.seriesLinks.value[0].id, int)
    assert _book.seriesLinks.value[0].position == "string"
    assert isinstance(_book.seriesLinks.value[0].seriesId, int)
    assert isinstance(_book.seriesLinks.value[0].bookId, int)
    assert _book.seriesLinks.value[0].isPrimary is True
    assert isinstance(_book.seriesLinks.value[0].series.value.id, int)
    assert _book.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _book.seriesLinks.value[0].series.value.title == "string"
    assert _book.seriesLinks.value[0].series.value.description == "string"
    assert _book.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_book.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_book.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _book.seriesLinks.value[0].series.value.books.value == [None]
    assert _book.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _book.seriesLinks.value[0].series.isLoaded is True
    assert _book.seriesLinks.value[0].book.isLoaded is True
    assert _book.seriesLinks.isLoaded is True
    _valu = data.books[0].author.lastBook
    assert isinstance(_valu.id, int)
    assert isinstance(_valu.authorMetadataId, int)
    assert _valu.foreignBookId == "string"
    assert isinstance(_valu.titleSlug, int)
    assert _valu.title == "string"
    assert _valu.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.links[0].url == "string"
    assert _valu.links[0].name == "string"
    assert _valu.genres == ["string"]
    assert isinstance(_valu.ratings.votes, int)
    assert isinstance(_valu.ratings.value, float)
    assert isinstance(_valu.ratings.popularity, float)
    assert _valu.cleanTitle == "string"
    assert _valu.monitored is True
    assert _valu.anyEditionOk is True
    assert _valu.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _valu.addOptions.searchForNewBook is True
    assert isinstance(_valu.authorMetadata.value.id, int)
    assert _valu.authorMetadata.value.foreignAuthorId == "string"
    assert isinstance(_valu.authorMetadata.value.titleSlug, int)
    assert _valu.authorMetadata.value.name == "string"
    assert _valu.authorMetadata.value.sortName == "string"
    assert _valu.authorMetadata.value.sortNameLastFirst == "string"
    assert _valu.authorMetadata.value.aliases == ["string"]
    assert _valu.authorMetadata.value.overview == "string"
    assert _valu.authorMetadata.value.gender == "string"
    assert _valu.authorMetadata.value.hometown == "string"
    assert _valu.authorMetadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.authorMetadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.authorMetadata.value.status == "string"
    assert _valu.authorMetadata.value.images[0].url == "string"
    assert _valu.authorMetadata.value.images[0].coverType == ImageType.POSTER.value
    assert _valu.authorMetadata.value.images[0].extension == "string"
    assert _valu.authorMetadata.value.links[0].url == "string"
    assert _valu.authorMetadata.value.links[0].name == "string"
    assert _valu.authorMetadata.value.genres == ["string"]
    assert isinstance(_valu.authorMetadata.value.ratings.votes, int)
    assert isinstance(_valu.authorMetadata.value.ratings.value, float)
    assert isinstance(_valu.authorMetadata.value.ratings.popularity, float)
    assert _valu.authorMetadata.isLoaded is True
    assert isinstance(_valu.author.value.id, int)
    assert isinstance(_valu.author.value.authorMetadataId, int)
    assert _valu.author.value.cleanName == "string"
    assert _valu.author.value.monitored is True
    assert _valu.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _valu.author.value.path == "string"
    assert _valu.author.value.rootFolderPath == "string"
    assert _valu.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert isinstance(_valu.author.value.qualityProfileId, int)
    assert isinstance(_valu.author.value.metadataProfileId, int)
    assert isinstance(_valu.author.value.tags[0], int)
    assert _valu.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _valu.author.value.addOptions.booksToMonitor == ["string"]
    assert _valu.author.value.addOptions.monitored is True
    assert _valu.author.value.addOptions.searchForMissingBooks is True
    _val = _valu.author.value.metadata.value
    assert isinstance(_val.id, int)
    assert _val.foreignAuthorId == "string"
    assert isinstance(_val.titleSlug, int)
    assert _val.name == "string"
    assert _val.sortName == "string"
    assert _val.nameLastFirst == "string"
    assert _val.sortNameLastFirst == "string"
    assert _val.aliases == ["string"]
    assert _val.overview == "string"
    assert _val.gender == "string"
    assert _val.hometown == "string"
    assert _val.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.status == "string"
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == ImageType.POSTER.value
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert _val.genres == ["string"]
    assert isinstance(_val.ratings.votes, int)
    assert isinstance(_val.ratings.value, float)
    assert isinstance(_val.ratings.popularity, float)
    assert _valu.author.value.metadata.isLoaded is True
    assert isinstance(_valu.author.value.qualityProfile.value.id, int)
    assert _valu.author.value.qualityProfile.value.name == "string"
    assert _valu.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_valu.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_valu.author.value.qualityProfile.value.items[0].id, int)
    assert _valu.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_valu.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _valu.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _valu.author.value.qualityProfile.value.items[0].items == [None]
    assert _valu.author.value.qualityProfile.value.items[0].allowed is True
    assert _valu.author.value.qualityProfile.isLoaded is True
    assert isinstance(_valu.author.value.metadataProfile.value.id, int)
    assert _valu.author.value.metadataProfile.value.name == "string"
    assert isinstance(_valu.author.value.metadataProfile.value.minPopularity, int)
    assert _valu.author.value.metadataProfile.value.skipMissingDate is True
    assert _valu.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _valu.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _valu.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _valu.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_valu.author.value.metadataProfile.value.minPages, int)
    assert _valu.author.value.metadataProfile.value.ignored == "string"
    assert _valu.author.value.metadataProfile.isLoaded is True
    assert _valu.author.value.books.value == [None]
    assert _valu.author.value.books.isLoaded is True
    assert isinstance(_valu.author.value.series.value[0].id, int)
    assert _valu.author.value.series.value[0].foreignSeriesId == "string"
    assert _valu.author.value.series.value[0].title == "string"
    assert _valu.author.value.series.value[0].description == "string"
    assert _valu.author.value.series.value[0].numbered is True
    assert isinstance(_valu.author.value.series.value[0].workCount, int)
    assert isinstance(_valu.author.value.series.value[0].primaryWorkCount, int)
    assert _valu.author.value.series.value[0].books.value == [None]
    assert _valu.author.value.series.value[0].books.isLoaded is True
    assert _valu.author.value.series.value[0].foreignAuthorId == "string"
    assert _valu.author.value.series.isLoaded is True
    assert _valu.author.value.name == "string"
    assert _valu.author.value.foreignAuthorId == "string"
    assert _valu.author.isLoaded is True
    _val = _valu.editions.value[0]
    assert isinstance(_val.id, int)
    assert isinstance(_val.bookId, int)
    assert _val.foreignEditionId == "string"
    assert isinstance(_val.titleSlug, int)
    assert _val.isbn13 == "string"
    assert _val.asin == "string"
    assert _val.title == "string"
    assert _val.language == "string"
    assert _val.overview == "string"
    assert _val.format == "string"
    assert _val.isEbook is True
    assert _val.publisher == "string"
    assert isinstance(_val.pageCount, int)
    assert _val.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.images[0].url == "string"
    assert _val.images[0].coverType == ImageType.POSTER.value
    assert _val.images[0].extension == "string"
    assert _val.links[0].url == "string"
    assert _val.links[0].name == "string"
    assert isinstance(_val.ratings.votes, int)
    assert isinstance(_val.ratings.value, float)
    assert isinstance(_val.ratings.popularity, float)
    assert _val.monitored is True
    assert _val.manualAdd is True
    assert _val.book.isLoaded is True
    assert isinstance(_val.bookFiles.value[0].id, int)
    assert _val.bookFiles.value[0].path == "string"
    assert isinstance(_val.bookFiles.value[0].size, int)
    assert _val.bookFiles.value[0].modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.bookFiles.value[0].dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.bookFiles.value[0].sceneName == "string"
    assert _val.bookFiles.value[0].releaseGroup == "string"
    assert isinstance(_val.bookFiles.value[0].quality.quality.id, int)
    assert _val.bookFiles.value[0].quality.quality.name == "string"
    assert isinstance(_val.bookFiles.value[0].quality.revision.version, int)
    assert isinstance(_val.bookFiles.value[0].quality.revision.real, int)
    assert _val.bookFiles.value[0].quality.revision.isRepack is True
    assert _val.bookFiles.value[0].mediaInfo.audioFormat == "string"
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioBitrate, int)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioChannels, float)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioBitrate, int)
    assert isinstance(_val.bookFiles.value[0].mediaInfo.audioSampleRate, int)
    assert isinstance(_val.bookFiles.value[0].editionId, int)
    assert isinstance(_val.bookFiles.value[0].calibreId, int)
    assert isinstance(_val.bookFiles.value[0].part, int)
    _va = _val.bookFiles.value[0].author.value
    assert isinstance(_va.id, int)
    assert isinstance(_va.authorMetadataId, int)
    assert _va.cleanName == "string"
    assert _va.monitored is True
    assert _va.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.path == "string"
    assert _va.rootFolderPath == "string"
    assert _va.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert isinstance(_va.qualityProfileId, int)
    assert isinstance(_va.metadataProfileId, int)
    assert isinstance(_va.tags[0], int)
    assert _va.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _va.addOptions.booksToMonitor == ["string"]
    assert _va.addOptions.monitored is True
    assert _va.addOptions.searchForMissingBooks is True
    assert isinstance(_va.metadata.value.id, int)
    assert _va.metadata.value.foreignAuthorId == "string"
    assert isinstance(_va.metadata.value.titleSlug, int)
    assert _va.metadata.value.name == "string"
    assert _va.metadata.value.sortName == "string"
    assert _va.metadata.value.nameLastFirst == "string"
    assert _va.metadata.value.sortNameLastFirst == "string"
    assert _va.metadata.value.aliases == ["string"]
    assert _va.metadata.value.overview == "string"
    assert _va.metadata.value.gender == "string"
    assert _va.metadata.value.hometown == "string"
    assert _va.metadata.value.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.metadata.value.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.metadata.value.status == "string"
    assert _va.metadata.value.images[0].url == "string"
    assert _va.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _va.metadata.value.images[0].extension == "string"
    assert _va.metadata.value.links[0].url == "string"
    assert _va.metadata.value.links[0].name == "string"
    assert _va.metadata.value.genres == ["string"]
    assert isinstance(_va.metadata.value.ratings.votes, int)
    assert isinstance(_va.metadata.value.ratings.value, float)
    assert isinstance(_va.metadata.value.ratings.popularity, float)
    assert _va.metadata.isLoaded is True
    assert isinstance(_va.qualityProfile.value.id, int)
    assert _va.qualityProfile.value.name == "string"
    assert _va.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_va.qualityProfile.value.cutoff, int)
    assert isinstance(_va.qualityProfile.value.items[0].id, int)
    assert _va.qualityProfile.value.items[0].name == "string"
    assert isinstance(_va.qualityProfile.value.items[0].quality.id, int)
    assert _va.qualityProfile.value.items[0].quality.name == "string"
    assert _va.qualityProfile.value.items[0].items == [None]
    assert _va.qualityProfile.value.items[0].allowed is True
    assert _va.qualityProfile.isLoaded is True
    assert isinstance(_va.metadataProfile.value.id, int)
    assert _va.metadataProfile.value.name == "string"
    assert isinstance(_va.metadataProfile.value.minPopularity, int)
    assert _va.metadataProfile.value.skipMissingDate is True
    assert _va.metadataProfile.value.skipMissingIsbn is True
    assert _va.metadataProfile.value.skipPartsAndSets is True
    assert _va.metadataProfile.value.skipSeriesSecondary is True
    assert _va.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_va.metadataProfile.value.minPages, int)
    assert _va.metadataProfile.value.ignored == "string"
    assert _va.metadataProfile.isLoaded is True
    assert _va.books.value == [None]
    assert _va.books.isLoaded is True
    assert isinstance(_va.series.value[0].id, int)
    assert _va.series.value[0].foreignSeriesId == "string"
    assert _va.series.value[0].title == "string"
    assert _va.series.value[0].description == "string"
    assert _va.series.value[0].numbered is True
    assert isinstance(_va.series.value[0].workCount, int)
    assert isinstance(_va.series.value[0].primaryWorkCount, int)
    assert _va.series.value[0].books.value == [None]
    assert _va.series.value[0].books.isLoaded is True
    assert _va.series.value[0].foreignAuthorId == "string"
    assert _va.series.isLoaded is True
    assert _va.name == "string"
    assert _va.foreignAuthorId == "string"
    assert _val.bookFiles.value[0].author.isLoaded is True
    assert _val.bookFiles.value[0].edition.isLoaded is True
    assert isinstance(_val.bookFiles.value[0].partCount, int)
    assert _val.bookFiles.isLoaded is True
    _val = _valu.bookFiles.value[0]
    assert isinstance(_val.id, int)
    assert _val.path == "string"
    assert isinstance(_val.size, int)
    assert _val.modified == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.dateAdded == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.sceneName == "string"
    assert _val.releaseGroup == "string"
    assert isinstance(_val.quality.quality.id, int)
    assert _val.quality.quality.name == "string"
    assert isinstance(_val.quality.revision.version, int)
    assert isinstance(_val.quality.revision.real, int)
    assert _val.quality.revision.isRepack is True
    assert _val.mediaInfo.audioFormat == "string"
    assert isinstance(_val.mediaInfo.audioBitrate, int)
    assert isinstance(_val.mediaInfo.audioChannels, float)
    assert isinstance(_val.mediaInfo.audioBits, int)
    assert isinstance(_val.mediaInfo.audioSampleRate, int)
    assert isinstance(_val.editionId, int)
    assert isinstance(_val.calibreId, int)
    assert isinstance(_val.part, int)
    assert isinstance(_val.author.value.id, int)
    assert isinstance(_val.author.value.authorMetadataId, int)
    assert _val.author.value.cleanName == "string"
    assert _val.author.value.monitored is True
    assert _val.author.value.lastInfoSync == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _val.author.value.path == "string"
    assert _val.author.value.rootFolderPath == "string"
    assert _val.author.value.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert isinstance(_val.author.value.qualityProfileId, int)
    assert isinstance(_val.author.value.metadataProfileId, int)
    assert isinstance(_val.author.value.tags[0], int)
    assert _val.author.value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _val.author.value.addOptions.booksToMonitor == ["string"]
    assert _val.author.value.addOptions.monitored is True
    assert _val.author.value.addOptions.searchForMissingBooks is True
    _va = _val.author.value.metadata.value
    assert isinstance(_va.id, int)
    assert _va.foreignAuthorId == "string"
    assert isinstance(_va.titleSlug, int)
    assert _va.name == "string"
    assert _va.sortName == "string"
    assert _va.nameLastFirst == "string"
    assert _va.sortNameLastFirst == "string"
    assert _va.aliases == ["string"]
    assert _va.overview == "string"
    assert _va.gender == "string"
    assert _va.hometown == "string"
    assert _va.born == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.died == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _va.status == "string"
    assert _va.images[0].url == "string"
    assert _va.images[0].coverType == ImageType.POSTER.value
    assert _va.images[0].extension == "string"
    assert _va.links[0].url == "string"
    assert _va.links[0].name == "string"
    assert _va.genres == ["string"]
    assert isinstance(_va.ratings.votes, int)
    assert isinstance(_va.ratings.value, float)
    assert isinstance(_va.ratings.popularity, float)
    assert _val.author.value.metadata.isLoaded is True
    assert isinstance(_val.author.value.qualityProfile.value.id, int)
    assert _val.author.value.qualityProfile.value.name == "string"
    assert _val.author.value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_val.author.value.qualityProfile.value.cutoff, int)
    assert isinstance(_val.author.value.qualityProfile.value.items[0].id, int)
    assert _val.author.value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_val.author.value.qualityProfile.value.items[0].quality.id, int)
    assert _val.author.value.qualityProfile.value.items[0].quality.name == "string"
    assert _val.author.value.qualityProfile.value.items[0].items == [None]
    assert _val.author.value.qualityProfile.value.items[0].allowed is True
    assert _val.author.value.qualityProfile.isLoaded is True
    assert isinstance(_val.author.value.metadataProfile.value.id, int)
    assert _val.author.value.metadataProfile.value.name == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPopularity, int)
    assert _val.author.value.metadataProfile.value.skipMissingDate is True
    assert _val.author.value.metadataProfile.value.skipMissingIsbn is True
    assert _val.author.value.metadataProfile.value.skipPartsAndSets is True
    assert _val.author.value.metadataProfile.value.skipSeriesSecondary is True
    assert _val.author.value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_val.author.value.metadataProfile.value.minPages, int)
    assert _val.author.value.metadataProfile.value.ignored == "string"
    assert _val.author.value.metadataProfile.isLoaded is True
    assert _val.author.value.books.value == [None]
    assert _val.author.value.books.isLoaded is True
    assert isinstance(_val.author.value.series.value[0].id, int)
    assert _val.author.value.series.value[0].foreignSeriesId == "string"
    assert _val.author.value.series.value[0].title == "string"
    assert _val.author.value.series.value[0].description == "string"
    assert _val.author.value.series.value[0].numbered is True
    assert isinstance(_val.author.value.series.value[0].workCount, int)
    assert isinstance(_val.author.value.series.value[0].primaryWorkCount, int)
    assert _val.author.value.series.value[0].books.value[0] is None
    assert _val.author.value.series.value[0].books.isLoaded is True
    assert _val.author.value.series.value[0].foreignAuthorId == "string"
    assert _val.author.value.series.isLoaded is True
    assert _val.author.value.name == "string"
    assert _val.author.value.foreignAuthorId == "string"
    assert _val.author.isLoaded is True
    assert _val.edition.isLoaded is True
    assert isinstance(_val.partCount, int)
    assert _valu.bookFiles.isLoaded is True
    assert isinstance(_valu.seriesLinks.value[0].id, int)
    assert _valu.seriesLinks.value[0].position == "string"
    assert isinstance(_valu.seriesLinks.value[0].seriesId, int)
    assert isinstance(_valu.seriesLinks.value[0].bookId, int)
    assert _valu.seriesLinks.value[0].isPrimary is True
    assert isinstance(_valu.seriesLinks.value[0].series.value.id, int)
    assert _valu.seriesLinks.value[0].series.value.foreignSeriesId == "string"
    assert _valu.seriesLinks.value[0].series.value.title == "string"
    assert _valu.seriesLinks.value[0].series.value.description == "string"
    assert _valu.seriesLinks.value[0].series.value.numbered is True
    assert isinstance(_valu.seriesLinks.value[0].series.value.workCount, int)
    assert isinstance(_valu.seriesLinks.value[0].series.value.primaryWorkCount, int)
    assert _valu.seriesLinks.value[0].series.value.books.value == [None]
    assert _valu.seriesLinks.value[0].series.value.foreignAuthorId == "string"
    assert _valu.seriesLinks.value[0].series.isLoaded is True
    assert _valu.seriesLinks.value[0].book.isLoaded is True
    assert _valu.seriesLinks.isLoaded is True
    assert data.books[0].author.images[0].url == "string"
    assert data.books[0].author.images[0].coverType == ImageType.POSTER.value
    assert data.books[0].author.images[0].extension == "string"
    assert data.books[0].author.remotePoster == "string"
    assert data.books[0].author.path == "string"
    assert isinstance(data.books[0].author.qualityProfileId, int)
    assert isinstance(data.books[0].author.metadataProfileId, int)
    assert data.books[0].author.monitored is True
    assert data.books[0].author.rootFolderPath == "string"
    assert data.books[0].author.genres == ["string"]
    assert data.books[0].author.cleanName == "string"
    assert data.books[0].author.sortName == "string"
    assert data.books[0].author.sortNameLastFirst == "string"
    assert isinstance(data.books[0].author.tags[0], int)
    assert data.books[0].author.added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert data.books[0].author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert data.books[0].author.addOptions.booksToMonitor == ["string"]
    assert data.books[0].author.addOptions.monitored is True
    assert data.books[0].author.addOptions.searchForMissingBooks is True
    assert isinstance(data.books[0].author.ratings.votes, int)
    assert isinstance(data.books[0].author.ratings.value, float)
    assert isinstance(data.books[0].author.ratings.popularity, float)
    assert isinstance(data.books[0].author.statistics.bookFileCount, int)
    assert isinstance(data.books[0].author.statistics.bookCount, int)
    assert isinstance(data.books[0].author.statistics.availableBookCount, int)
    assert isinstance(data.books[0].author.statistics.totalBookCount, int)
    assert isinstance(data.books[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data.books[0].author.statistics.percentOfBooks, float)
    assert data.books[0].images[0].url == "string"
    assert data.books[0].images[0].coverType == ImageType.POSTER.value
    assert data.books[0].images[0].extension == "string"
    assert data.books[0].links[0].url == "string"
    assert data.books[0].links[0].name == "string"
    assert isinstance(data.books[0].statistics.bookFileCount, int)
    assert isinstance(data.books[0].statistics.bookCount, int)
    assert isinstance(data.books[0].statistics.totalBookCount, int)
    assert isinstance(data.books[0].statistics.sizeOnDisk, int)
    assert isinstance(data.books[0].statistics.percentOfBooks, float)
    assert data.books[0].added == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert data.books[0].addOptions.addType == AddTypes.AUTOMATIC.value
    assert data.books[0].addOptions.searchForNewBook is True
    assert data.books[0].remoteCover == "string"
    assert data.books[0].remoteCover == "string"
    _value = data.books[0].editions[0]
    assert isinstance(_value.id, int)
    assert isinstance(_value.bookId, int)
    assert _value.foreignEditionId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.isbn13 == "string"
    assert _value.asin == "string"
    assert _value.title == "string"
    assert _value.language == "string"
    assert _value.overview == "string"
    assert _value.format == "string"
    assert _value.isEbook is True
    assert _value.publisher == "string"
    assert isinstance(_value.pageCount, int)
    assert _value.releaseDate == datetime(2020, 1, 6, 12, 49, 48, 604000)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.images[0].extension == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert isinstance(_value.ratings.popularity, float)
    assert _value.monitored is True
    assert _value.manualAdd is True
    assert _value.remoteCover == "string"
    assert _value.grabbed is True
    assert data.books[0].grabbed is True


@pytest.mark.asyncio
async def test_async_get_queue(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting queue."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/queue?page=1&pageSize=10&sortKey=timeleft&includeUnknownAuthorItems=False&includeAuthor=False&includeBook=False",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/queue.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_queue()
    assert data.page == 1
    assert data.pageSize == 10
    assert data.sortKey == ReadarrSortKeys.TIMELEFT.value
    assert data.sortDirection == SortDirection.ASCENDING.value
    assert data.totalRecords == 1
    assert isinstance(data.records[0].authorId, int)
    assert isinstance(data.records[0].bookId, int)
    assert data.records[0].author
    assert data.records[0].book
    assert isinstance(data.records[0].quality.quality.id, int)
    assert data.records[0].quality.quality.name == "string"
    assert isinstance(data.records[0].quality.revision.version, int)
    assert isinstance(data.records[0].quality.revision.real, int)
    assert data.records[0].quality.revision.isRepack is False
    assert isinstance(data.records[0].size, int)
    assert data.records[0].title == "string"
    assert isinstance(data.records[0].sizeleft, int)
    assert data.records[0].timeleft == "00:00:10"
    assert data.records[0].estimatedCompletionTime == datetime(2020, 2, 9, 23, 22, 30)
    assert data.records[0].status == "string"
    assert data.records[0].trackedDownloadStatus == "string"
    assert data.records[0].trackedDownloadState == "downloading"
    assert data.records[0].statusMessages[0].title == "string"
    assert data.records[0].statusMessages[0].messages == ["string"]
    assert data.records[0].downloadId == "string"
    assert data.records[0].protocol is ProtocolType.UNKNOWN
    assert data.records[0].downloadClient == "string"
    assert data.records[0].indexer == "string"
    assert data.records[0].outputPath == "string"
    assert data.records[0].downloadForced is False
    assert isinstance(data.records[0].id, int)


@pytest.mark.asyncio
async def test_async_get_queue_details(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting queue details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/queue/details?includeUnknownAuthorItems=False&includeAuthor=False&includeBook=True&authorId=0&bookIds=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/queue-details.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_queue_details(authorid=0, bookids=[0])
    assert isinstance(data[0].authorId, int)
    assert isinstance(data[0].bookId, int)
    assert data[0].author
    assert data[0].book
    assert data[0].book.title == "string"
    assert data[0].book.authorTitle == "string"
    assert data[0].book.seriesTitle == "string"
    assert data[0].book.disambiguation == "string"
    assert data[0].book.overview == "string"
    assert isinstance(data[0].book.authorId, int)
    assert data[0].book.foreignBookId == "0"
    assert isinstance(data[0].book.titleSlug, int)
    assert data[0].book.monitored is True
    assert data[0].book.anyEditionOk is True
    assert isinstance(data[0].book.ratings.votes, int)
    assert isinstance(data[0].book.ratings.value, float)
    assert isinstance(data[0].book.ratings.popularity, float)
    assert data[0].book.releaseDate == datetime(2021, 11, 22, 0, 0)
    assert isinstance(data[0].book.pageCount, int)
    assert data[0].book.genres == ["string"]
    assert isinstance(data[0].book.author.authorMetadataId, int)
    assert data[0].book.author.status == "string"
    assert data[0].book.author.ended is False
    assert data[0].book.author.authorName == "string"
    assert data[0].book.author.authorNameLastFirst == "string"
    assert isinstance(data[0].book.author.foreignAuthorId, int)
    assert isinstance(data[0].book.author.titleSlug, int)
    assert data[0].book.author.overview == "string"
    assert data[0].book.author.links[0].url == "string"
    assert data[0].book.author.links[0].name == "string"
    assert data[0].book.author.images[0].url == "string"
    assert data[0].book.author.images[0].coverType == ImageType.POSTER.value
    assert data[0].book.author.images[0].extension == "string"
    assert data[0].book.author.path == "string"
    assert isinstance(data[0].book.author.qualityProfileId, int)
    assert isinstance(data[0].book.author.metadataProfileId, int)
    assert data[0].book.author.monitored is True
    assert data[0].book.author.monitorNewItems == "string"
    assert data[0].book.author.genres == ["string"]
    assert data[0].book.author.cleanName == "string"
    assert data[0].book.author.sortName == "string"
    assert data[0].book.author.sortNameLastFirst == "string"
    assert isinstance(data[0].book.author.tags[0], int)
    assert data[0].book.author.added == datetime(2021, 12, 6, 23, 38, 3)
    assert isinstance(data[0].book.author.ratings.votes, int)
    assert isinstance(data[0].book.author.ratings.value, float)
    assert isinstance(data[0].book.author.ratings.popularity, float)
    assert isinstance(data[0].book.author.statistics.bookFileCount, int)
    assert isinstance(data[0].book.author.statistics.bookCount, int)
    assert isinstance(data[0].book.author.statistics.availableBookCount, int)
    assert isinstance(data[0].book.author.statistics.totalBookCount, int)
    assert isinstance(data[0].book.author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].book.author.statistics.percentOfBooks, float)
    assert isinstance(data[0].book.author.id, int)
    assert data[0].book.images[0].url == "string"
    assert data[0].book.images[0].coverType == ImageType.POSTER.value
    assert data[0].book.images[0].extension == "string"
    assert data[0].book.links[0].url == "string"
    assert data[0].book.links[0].name == "string"
    assert data[0].book.added == datetime(2021, 12, 6, 23, 53, 58)
    assert isinstance(data[0].book.editions[0].bookId, int)
    assert isinstance(data[0].book.editions[0].foreignEditionId, int)
    assert isinstance(data[0].book.editions[0].titleSlug, int)
    assert isinstance(data[0].book.editions[0].isbn13, int)
    assert data[0].book.editions[0].title == "string"
    assert data[0].book.editions[0].language == "string"
    assert data[0].book.editions[0].overview == "string"
    assert data[0].book.editions[0].format == "string"
    assert data[0].book.editions[0].isEbook is False
    assert data[0].book.editions[0].disambiguation == "string"
    assert data[0].book.editions[0].publisher == "string"
    assert isinstance(data[0].book.editions[0].pageCount, int)
    assert data[0].book.editions[0].releaseDate == datetime(2021, 11, 25, 0, 0)
    assert data[0].book.editions[0].images[0].url == "string"
    assert data[0].book.editions[0].images[0].coverType == ImageType.POSTER.value
    assert data[0].book.editions[0].images[0].extension == "string"
    assert data[0].book.editions[0].links[0].url == "string"
    assert data[0].book.editions[0].links[0].name == "string"
    assert isinstance(data[0].book.editions[0].ratings.votes, int)
    assert isinstance(data[0].book.editions[0].ratings.value, float)
    assert isinstance(data[0].book.editions[0].ratings.popularity, float)
    assert data[0].book.editions[0].monitored is False
    assert data[0].book.editions[0].manualAdd is False
    assert data[0].book.editions[0].grabbed is False
    assert isinstance(data[0].book.editions[0].id, int)
    assert data[0].book.grabbed is False
    assert isinstance(data[0].book.id, int)
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].size, int)
    assert data[0].title == "string"
    assert isinstance(data[0].sizeleft, int)
    assert data[0].timeleft == "00:00:00"
    assert data[0].estimatedCompletionTime == datetime(2020, 2, 7, 11, 27, 27)
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
    assert data[0].downloadForced is False
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_release(aresponses, readarr_client: ReadarrClient) -> None:
    """Test searching indexers for specified fields."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/release?authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/release.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_release(authorid=0, bookid=0)
    assert data[0].guid == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
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
    assert data[0].title == "string"
    assert data[0].discography is False
    assert data[0].sceneSource is False
    assert data[0].authorName == "string"
    assert data[0].bookTitle == "string"
    assert data[0].approved is False
    assert data[0].temporarilyRejected is False
    assert data[0].rejected is True
    assert data[0].rejections[0].reason == "string"
    assert data[0].rejections[0].type == "permanent"
    assert data[0].publishDate == datetime(2021, 11, 23, 5, 0)
    assert data[0].commentUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].infoUrl == "string"
    assert data[0].downloadAllowed is True
    assert isinstance(data[0].releaseWeight, int)
    assert isinstance(data[0].preferredWordScore, int)
    assert data[0].magnetUrl == "string"
    assert data[0].infoHash == "string"
    assert isinstance(data[0].seeders, int)
    assert isinstance(data[0].leechers, int)
    assert data[0].protocol is ProtocolType.UNKNOWN


@pytest.mark.asyncio
async def test_async_push_release(aresponses, readarr_client: ReadarrClient) -> None:
    """Test pushing release."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/release/push",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_push_release("test")
    assert isinstance(data, ReadarrRelease)


@pytest.mark.asyncio
async def test_async_get_rename(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting rename details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/rename?authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/rename.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_rename()
    assert isinstance(data[0].authorId, int)
    assert isinstance(data[0].bookId, int)
    assert isinstance(data[0].bookFileId, int)
    assert data[0].existingPath == "string"
    assert data[0].newPath == "string"


@pytest.mark.asyncio
async def test_async_get_manual_import(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting manual import."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/manualimport?authorId=0&downloadId=abc123&filterExistingFiles=True&folder=&replaceExistingFiles=True",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/manualimport.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_manual_import("abc123")
    assert data[0].path == "string"
    assert data[0].name == "string"
    assert isinstance(data[0].size, int)
    assert isinstance(data[0].author.authorMetadataId, int)
    assert data[0].author.status == StatusType.CONTINUING.value
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert isinstance(data[0].author.foreignAuthorId, int)
    assert isinstance(data[0].author.titleSlug, int)
    assert data[0].author.overview == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == ImageType.POSTER.value
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.path == "string"
    assert isinstance(data[0].author.qualityProfileId, int)
    assert isinstance(data[0].author.metadataProfileId, int)
    assert data[0].author.monitored is True
    assert data[0].author.monitorNewItems == MonitoringOptionsType.ALL.value
    assert data[0].author.genres == ["string"]
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert isinstance(data[0].author.tags[0], int)
    assert data[0].author.added == datetime(2021, 12, 6, 23, 38, 3)
    assert isinstance(data[0].author.ratings.votes, int)
    assert isinstance(data[0].author.ratings.value, float)
    assert isinstance(data[0].author.ratings.popularity, float)
    assert isinstance(data[0].author.statistics.bookFileCount, int)
    assert isinstance(data[0].author.statistics.bookCount, int)
    assert isinstance(data[0].author.statistics.availableBookCount, int)
    assert isinstance(data[0].author.statistics.totalBookCount, int)
    assert isinstance(data[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].author.statistics.percentOfBooks, int)
    assert isinstance(data[0].author.id, int)
    assert data[0].book.title == "string"
    assert data[0].book.authorTitle == "string"
    assert data[0].book.seriesTitle == "string"
    assert data[0].book.disambiguation == "string"
    assert data[0].book.overview == "string"
    assert isinstance(data[0].book.authorId, int)
    assert isinstance(data[0].book.foreignBookId, str)
    assert isinstance(data[0].book.titleSlug, int)
    assert data[0].book.monitored is True
    assert data[0].book.anyEditionOk is True
    assert isinstance(data[0].book.ratings.votes, int)
    assert isinstance(data[0].book.ratings.value, float)
    assert isinstance(data[0].book.ratings.popularity, float)
    assert data[0].book.releaseDate == datetime(2020, 9, 21, 0, 0)
    assert isinstance(data[0].book.pageCount, int)
    assert data[0].book.genres == ["string"]
    assert isinstance(data[0].book.author.authorMetadataId, int)
    assert data[0].book.author.status == StatusType.CONTINUING.value
    assert data[0].book.author.ended is False
    assert data[0].book.author.authorName == "string"
    assert data[0].book.author.authorNameLastFirst == "string"
    assert isinstance(data[0].book.author.foreignAuthorId, int)
    assert isinstance(data[0].book.author.titleSlug, int)
    assert data[0].book.author.overview == "string"
    assert data[0].book.author.links[0].url == "string"
    assert data[0].book.author.links[0].name == "Goodreads"
    assert data[0].book.author.images[0].url == "string"
    assert data[0].book.author.images[0].coverType == ImageType.POSTER.value
    assert data[0].book.author.images[0].extension == "string"
    assert data[0].book.author.path == "string"
    assert isinstance(data[0].book.author.qualityProfileId, int)
    assert isinstance(data[0].book.author.metadataProfileId, int)
    assert data[0].book.author.monitored is True
    assert data[0].book.author.monitorNewItems == MonitoringOptionsType.ALL.value
    assert data[0].book.author.genres == ["string"]
    assert data[0].book.author.cleanName == "string"
    assert data[0].book.author.sortName == "string"
    assert data[0].book.author.sortNameLastFirst == "string"
    assert isinstance(data[0].book.author.tags[0], int)
    assert data[0].book.author.added == datetime(2021, 12, 6, 23, 38, 3)
    assert isinstance(data[0].book.author.ratings.votes, int)
    assert isinstance(data[0].book.author.ratings.value, float)
    assert isinstance(data[0].book.author.ratings.popularity, float)
    assert isinstance(data[0].book.author.statistics.bookFileCount, int)
    assert isinstance(data[0].book.author.statistics.bookCount, int)
    assert isinstance(data[0].book.author.statistics.availableBookCount, int)
    assert isinstance(data[0].book.author.statistics.totalBookCount, int)
    assert isinstance(data[0].book.author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].book.author.statistics.percentOfBooks, int)
    assert isinstance(data[0].book.author.id, int)
    assert data[0].book.images[0].url == "string"
    assert data[0].book.images[0].coverType == ImageType.COVER.value
    assert data[0].book.images[0].extension == "string"
    assert data[0].book.links[0].url == "string"
    assert data[0].book.links[0].name == "string"
    assert data[0].book.added == datetime(2021, 12, 6, 23, 53, 58)
    assert isinstance(data[0].book.editions[0].bookId, int)
    assert isinstance(data[0].book.editions[0].foreignEditionId, int)
    assert isinstance(data[0].book.editions[0].titleSlug, int)
    assert isinstance(data[0].book.editions[0].isbn13, int)
    assert data[0].book.editions[0].asin == "string"
    assert data[0].book.editions[0].title == "string"
    assert data[0].book.editions[0].overview == "string"
    assert data[0].book.editions[0].format == "string"
    assert data[0].book.editions[0].isEbook is False
    assert data[0].book.editions[0].disambiguation == "string"
    assert data[0].book.editions[0].publisher == "string"
    assert isinstance(data[0].book.editions[0].pageCount, int)
    assert data[0].book.editions[0].releaseDate == datetime(2020, 8, 27, 0, 0)
    assert data[0].book.editions[0].images[0].url == "string"
    assert data[0].book.editions[0].images[0].coverType == ImageType.COVER.value
    assert data[0].book.editions[0].images[0].extension == "string"
    assert data[0].book.editions[0].links[0].url == "string"
    assert data[0].book.editions[0].links[0].name == "string"
    assert isinstance(data[0].book.editions[0].ratings.votes, int)
    assert isinstance(data[0].book.editions[0].ratings.value, float)
    assert isinstance(data[0].book.editions[0].ratings.popularity, float)
    assert data[0].book.editions[0].monitored is False
    assert data[0].book.editions[0].manualAdd is False
    assert data[0].book.editions[0].grabbed is False
    assert isinstance(data[0].book.editions[0].id, int)
    assert data[0].book.foreignBookId == "string"
    assert isinstance(data[0].quality.quality.id, int)
    assert data[0].quality.quality.name == "string"
    assert isinstance(data[0].quality.revision.version, int)
    assert isinstance(data[0].quality.revision.real, int)
    assert data[0].quality.revision.isRepack is False
    assert isinstance(data[0].qualityWeight, int)
    assert data[0].downloadId == "string"
    assert data[0].rejections[0].reason == "string"
    assert data[0].rejections[0].type == "permanent"
    assert data[0].audioTags.authors == ["string"]
    assert data[0].audioTags.authorTitle == "string"
    assert data[0].audioTags.bookTitle == "string"
    assert isinstance(data[0].audioTags.isbn, int)
    assert isinstance(data[0].audioTags.discNumber, int)
    assert isinstance(data[0].audioTags.discCount, int)
    assert isinstance(data[0].audioTags.year, int)
    assert data[0].audioTags.publisher == "string"
    assert data[0].audioTags.disambiguation == "string"
    assert data[0].audioTags.duration == "00:00:00"
    assert isinstance(data[0].audioTags.quality.quality.id, int)
    assert data[0].audioTags.quality.quality.name == "EPUB"
    assert isinstance(data[0].audioTags.quality.revision.version, int)
    assert isinstance(data[0].audioTags.quality.revision.real, int)
    assert data[0].audioTags.quality.revision.isRepack is False
    assert isinstance(data[0].audioTags.trackNumbers[0], int)
    assert data[0].audioTags.language == "en"
    assert data[0].additionalFile is False
    assert data[0].replaceExistingFiles is True
    assert data[0].disableReleaseSwitching is False
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_edit_manual_import(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing manual import."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/manualimport",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_manual_import(ReadarrManualImport("test"))
    assert isinstance(data, ReadarrManualImport)


@pytest.mark.asyncio
async def test_async_get_retag(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting retag details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/retag?authorId=0&bookId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/retag.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_retag()
    assert isinstance(data[0].authorId, int)
    assert isinstance(data[0].bookId, int)
    assert isinstance(data[0].trackNumbers[0], int)
    assert isinstance(data[0].bookFileId, int)
    assert data[0].path == "string"
    assert data[0].changes[0].field == "string"
    assert data[0].changes[0].oldValue == "string"
    assert data[0].changes[0].newValue == "string"


@pytest.mark.asyncio
async def test_async_search(aresponses, readarr_client: ReadarrClient) -> None:
    """Test search."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/search?term=test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/search.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_search("test")
    assert data[0].foreignId == "0"
    assert isinstance(data[0].author.authorMetadataId, int)
    assert data[0].author.status == "string"
    assert data[0].author.ended is False
    assert data[0].author.authorName == "string"
    assert data[0].author.authorNameLastFirst == "string"
    assert isinstance(data[0].author.foreignAuthorId, int)
    assert isinstance(data[0].author.titleSlug, int)
    assert data[0].author.overview == "string"
    assert data[0].author.links[0].url == "string"
    assert data[0].author.links[0].name == "string"
    assert data[0].author.images[0].url == "string"
    assert data[0].author.images[0].coverType == ImageType.POSTER.value
    assert data[0].author.images[0].extension == "string"
    assert data[0].author.remotePoster == "string"
    assert data[0].author.path == "string"
    assert isinstance(data[0].author.qualityProfileId, int)
    assert isinstance(data[0].author.metadataProfileId, int)
    assert data[0].author.monitored is True
    assert data[0].author.monitorNewItems == "string"
    assert data[0].author.genres == ["string"]
    assert data[0].author.cleanName == "string"
    assert data[0].author.sortName == "string"
    assert data[0].author.sortNameLastFirst == "string"
    assert isinstance(data[0].author.tags[0], int)
    assert data[0].author.added == datetime(2021, 10, 6, 23, 38, 49)
    assert isinstance(data[0].author.ratings.votes, int)
    assert isinstance(data[0].author.ratings.value, float)
    assert isinstance(data[0].author.ratings.popularity, float)
    assert isinstance(data[0].author.statistics.bookFileCount, int)
    assert isinstance(data[0].author.statistics.bookCount, int)
    assert isinstance(data[0].author.statistics.availableBookCount, int)
    assert isinstance(data[0].author.statistics.totalBookCount, int)
    assert isinstance(data[0].author.statistics.sizeOnDisk, int)
    assert isinstance(data[0].author.statistics.percentOfBooks, float)
    assert isinstance(data[0].author.id, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_series(aresponses, readarr_client: ReadarrClient) -> None:
    """Test search."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/series?authorId=0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/series.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_series(0)
    assert data[0].title == "string"
    assert data[0].description == "string"
    assert data[0].links[0].position == "string"
    assert isinstance(data[0].links[0].seriesPosition, int)
    assert isinstance(data[0].links[0].seriesId, int)
    assert isinstance(data[0].links[0].bookId, int)
    assert isinstance(data[0].links[0].id, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_get_tag_details(aresponses, readarr_client: ReadarrClient) -> None:
    """Test getting tag details."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/tag/detail/0",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/tag-detail.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_tags_details(tagid=0)

    assert isinstance(data.id, int)
    assert data.label == "string"
    assert isinstance(data.delayProfileIds[0], int)
    assert isinstance(data.notificationIds[0], int)
    assert isinstance(data.restrictionIds[0], int)
    assert isinstance(data.importListIds[0], int)
    assert isinstance(data.authorIds[0], int)


@pytest.mark.asyncio
async def test_readarr_bookshelf() -> None:
    """Test readarr bookshelf model."""
    item = BaseModel(
        data={ATTR_DATA: json.loads(load_fixture("readarr/bookshelf.json"))},
        datatype=ReadarrBookshelf,
    )
    assert isinstance(item.basedata, ReadarrBookshelf)
    assert isinstance(item.basedata.authors[0].id, int)
    assert item.basedata.authors[0].monitored is True
    _value = item.basedata.authors[0].books[0]
    assert isinstance(_value.id, int)
    assert _value.title == "string"
    assert _value.authorTitle == "string"
    assert _value.seriesTitle == "string"
    assert _value.overview == "string"
    assert isinstance(_value.authorId, int)
    assert _value.foreignBookId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.monitored is True
    assert _value.anyEditionOk is True
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    assert _value.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert isinstance(_value.pageCount, int)
    assert _value.genres[0] == "string"
    _value = item.basedata.authors[0].books[0].author
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.status == "string"
    assert _value.authorName == "string"
    assert _value.authorNameLastFirst == "string"
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.overview == "string"
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.nextBook.id, int)
    assert isinstance(_value.nextBook.authorMetadataId, int)
    assert _value.nextBook.foreignBookId == "string"
    assert isinstance(_value.nextBook.titleSlug, int)
    assert _value.nextBook.title == "string"
    assert _value.nextBook.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.links[0].url == "string"
    assert _value.nextBook.links[0].name == "string"
    assert _value.nextBook.genres[0] == "string"
    assert isinstance(_value.nextBook.ratings.votes, int)
    assert isinstance(_value.nextBook.ratings.value, float)
    assert _value.nextBook.cleanTitle == "string"
    assert _value.nextBook.monitored is True
    assert _value.nextBook.anyEditionOk is True
    assert _value.nextBook.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.nextBook.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.nextBook.addOptions.searchForNewBook is True
    _value = item.basedata.authors[0].books[0].author.nextBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    _value = item.basedata.authors[0].books[0].author.nextBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert isinstance(_value.books, _ReadarrAuthorValueBooks)
    assert isinstance(_value.series, _ReadarrAuthorValueSeries)
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = item.basedata.authors[0].books[0].author.nextBook
    assert isinstance(_book.editions, _ReadarrEditions)
    assert isinstance(_book.bookFiles, _ReadarrEditionsValueBookFiles)
    assert isinstance(_book.seriesLinks, _ReadarrSeriesLinks)
    assert isinstance(_book.id, int)
    assert isinstance(_book.authorMetadataId, int)
    assert _book.foreignBookId == "string"
    assert isinstance(_book.titleSlug, int)
    assert _book.title == "string"
    assert _book.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.links[0].url == "string"
    assert _book.links[0].name == "string"
    assert _book.genres[0] == "string"
    assert isinstance(_book.ratings.votes, int)
    assert isinstance(_book.ratings.value, float)
    assert _book.cleanTitle == "string"
    assert _book.monitored is True
    assert _book.anyEditionOk is True
    assert _book.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _book.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _book.addOptions.searchForNewBook is True
    _value = item.basedata.authors[0].books[0].author.lastBook.authorMetadata.value
    assert isinstance(_value.id, int)
    assert _value.foreignAuthorId == "string"
    assert isinstance(_value.titleSlug, int)
    assert _value.name == "string"
    assert _value.sortName == "string"
    assert _value.sortNameLastFirst == "string"
    assert _value.aliases[0] == "string"
    assert _value.overview == "string"
    assert _value.gender == "string"
    assert _value.hometown == "string"
    assert _value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.status == "string"
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert _value.genres[0] == "string"
    assert isinstance(_value.ratings.votes, int)
    assert isinstance(_value.ratings.value, float)
    _value = item.basedata.authors[0].books[0].author.lastBook.author.value
    assert isinstance(_value.id, int)
    assert isinstance(_value.authorMetadataId, int)
    assert _value.cleanName == "string"
    assert _value.monitored is True
    assert _value.lastInfoSync == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.path == "string"
    assert _value.rootFolderPath == "string"
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert isinstance(_value.qualityProfileId, int)
    assert isinstance(_value.metadataProfileId, int)
    assert isinstance(_value.tags[0], int)
    assert _value.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.addOptions.booksToMonitor[0] == "string"
    assert _value.addOptions.monitored is True
    assert _value.addOptions.searchForMissingBooks is True
    assert isinstance(_value.metadata.value.id, int)
    assert _value.metadata.value.foreignAuthorId == "string"
    assert isinstance(_value.metadata.value.titleSlug, int)
    assert _value.metadata.value.name == "string"
    assert _value.metadata.value.sortName == "string"
    assert _value.metadata.value.nameLastFirst == "string"
    assert _value.metadata.value.sortNameLastFirst == "string"
    assert _value.metadata.value.aliases[0] == "string"
    assert _value.metadata.value.overview == "string"
    assert _value.metadata.value.gender == "string"
    assert _value.metadata.value.hometown == "string"
    assert _value.metadata.value.born == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.died == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.metadata.value.status == "string"
    assert _value.metadata.value.images[0].url == "string"
    assert _value.metadata.value.images[0].coverType == ImageType.POSTER.value
    assert _value.metadata.value.links[0].url == "string"
    assert _value.metadata.value.links[0].name == "string"
    assert _value.metadata.value.genres[0] == "string"
    assert isinstance(_value.metadata.value.ratings.votes, int)
    assert isinstance(_value.metadata.value.ratings.value, float)
    assert isinstance(_value.qualityProfile.value.id, int)
    assert _value.qualityProfile.value.name == "string"
    assert _value.qualityProfile.value.upgradeAllowed is True
    assert isinstance(_value.qualityProfile.value.cutoff, int)
    assert isinstance(_value.qualityProfile.value.items[0].id, int)
    assert _value.qualityProfile.value.items[0].name == "string"
    assert isinstance(_value.qualityProfile.value.items[0].quality.id, int)
    assert _value.qualityProfile.value.items[0].quality.name == "string"
    assert _value.qualityProfile.value.items[0].items == [None]
    assert _value.qualityProfile.value.items[0].allowed is True
    assert isinstance(_value.metadataProfile.value.id, int)
    assert _value.metadataProfile.value.name == "string"
    assert isinstance(_value.metadataProfile.value.minPopularity, int)
    assert _value.metadataProfile.value.skipMissingDate is True
    assert _value.metadataProfile.value.skipMissingIsbn is True
    assert _value.metadataProfile.value.skipPartsAndSets is True
    assert _value.metadataProfile.value.skipSeriesSecondary is True
    assert _value.metadataProfile.value.allowedLanguages == "string"
    assert isinstance(_value.metadataProfile.value.minPages, int)
    assert _value.metadataProfile.value.ignored == "string"
    assert isinstance(_value.books, _ReadarrAuthorValueBooks)
    assert isinstance(_value.series, _ReadarrAuthorValueSeries)
    assert _value.name == "string"
    assert _value.foreignAuthorId == "string"
    _book = item.basedata.authors[0].books[0].author.lastBook
    assert isinstance(_book.editions, _ReadarrEditions)
    assert isinstance(_book.bookFiles, _ReadarrEditionsValueBookFiles)
    assert isinstance(_book.seriesLinks, _ReadarrSeriesLinks)
    _value = item.basedata.authors[0].books[0]
    assert _value.author.images[0].url == "string"
    assert _value.author.images[0].coverType == ImageType.POSTER.value
    assert _value.author.remotePoster == "string"
    assert _value.author.path == "string"
    assert isinstance(_value.author.qualityProfileId, int)
    assert isinstance(_value.author.metadataProfileId, int)
    assert _value.author.monitored is True
    assert _value.author.rootFolderPath == "string"
    assert _value.author.genres[0] == "string"
    assert _value.author.cleanName == "string"
    assert _value.author.sortName == "string"
    assert _value.author.sortNameLastFirst == "string"
    assert isinstance(_value.author.tags[0], int)
    assert _value.author.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.author.addOptions.monitor == MonitoringOptionsType.ALL.value
    assert _value.author.addOptions.booksToMonitor[0] == "string"
    assert _value.author.addOptions.monitored is True
    assert _value.author.addOptions.searchForMissingBooks is True
    assert isinstance(_value.author.ratings.votes, int)
    assert isinstance(_value.author.ratings.value, float)
    assert isinstance(_value.author.statistics.bookFileCount, int)
    assert isinstance(_value.author.statistics.bookCount, int)
    assert isinstance(_value.author.statistics.availableBookCount, int)
    assert isinstance(_value.author.statistics.totalBookCount, int)
    assert isinstance(_value.author.statistics.sizeOnDisk, int)
    assert _value.images[0].url == "string"
    assert _value.images[0].coverType == ImageType.POSTER.value
    assert _value.links[0].url == "string"
    assert _value.links[0].name == "string"
    assert isinstance(_value.statistics.bookFileCount, int)
    assert isinstance(_value.statistics.bookCount, int)
    assert isinstance(_value.statistics.totalBookCount, int)
    assert isinstance(_value.statistics.sizeOnDisk, int)
    assert _value.added == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _value.addOptions.addType == AddTypes.AUTOMATIC.value
    assert _value.addOptions.searchForNewBook is True
    assert _value.remoteCover == "string"
    _editions = item.basedata.authors[0].books[0].editions[0]
    assert isinstance(_editions.id, int)
    assert isinstance(_editions.bookId, int)
    assert _editions.foreignEditionId == "string"
    assert isinstance(_editions.titleSlug, int)
    assert _editions.isbn13 == "string"
    assert _editions.asin == "string"
    assert _editions.title == "string"
    assert _editions.language == "string"
    assert _editions.overview == "string"
    assert _editions.format == "string"
    assert _editions.isEbook is True
    assert _editions.publisher == "string"
    assert isinstance(_editions.pageCount, int)
    assert _editions.releaseDate == datetime(2021, 12, 10, 10, 0, 6, 987000)
    assert _editions.images[0].url == "string"
    assert _editions.images[0].coverType == ImageType.POSTER.value
    assert _editions.links[0].url == "string"
    assert _editions.links[0].name == "string"
    assert isinstance(_editions.ratings.votes, int)
    assert isinstance(_editions.ratings.value, float)
    assert _editions.monitored is True
    assert _editions.manualAdd is True
    assert _editions.remoteCover == "string"
    assert _editions.grabbed is True
    assert item.basedata.authors[0].books[0].grabbed is True
    assert item.basedata.monitoringOptions.monitor == MonitoringOptionsType.ALL.value
    assert item.basedata.monitoringOptions.booksToMonitor[0] == "string"
    assert item.basedata.monitoringOptions.monitored is True


@pytest.mark.asyncio
async def test_async_add_author(aresponses, readarr_client: ReadarrClient) -> None:
    """Test adding author."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_add_author(ReadarrAuthor("test"))
    assert isinstance(data, ReadarrAuthor)


@pytest.mark.asyncio
async def test_async_edit_authors(aresponses, readarr_client: ReadarrClient) -> None:
    """Test editing authors."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/author.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_authors(ReadarrAuthor("test"))
    assert isinstance(data, ReadarrAuthor)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/editor",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )

    await readarr_client.async_edit_authors(ReadarrAuthorEditor("test"))


@pytest.mark.asyncio
async def test_async_delete_authors(aresponses, readarr_client: ReadarrClient) -> None:
    """Test editing authors."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_delete_authors(0)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/author/editor",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_delete_authors([0, 1])


@pytest.mark.asyncio
async def test_async_readarr_commands(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test Readarr commands."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.APP_UPDATE_CHECK)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.REFRESH_AUTHOR)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.RESCAN_FOLDERS)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.AUTHOR_SEARCH)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.BOOK_SEARCH)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.REFRESH_BOOK)
    assert isinstance(data, Command)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/command",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_readarr_command(ReadarrCommands.RENAME_AUTHOR)
    assert isinstance(data, Command)


@pytest.mark.asyncio
async def test_async_add_book(aresponses, readarr_client: ReadarrClient) -> None:
    """Test adding book."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_add_book(ReadarrBook("test"))
    assert isinstance(data, ReadarrBook)


@pytest.mark.asyncio
async def test_async_edit_book(aresponses, readarr_client: ReadarrClient) -> None:
    """Test editing book."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_book(ReadarrBook("test"))
    assert isinstance(data, ReadarrBook)


@pytest.mark.asyncio
async def test_async_delete_book(aresponses, readarr_client: ReadarrClient) -> None:
    """Test deleting book."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/book/0?deleteFiles=False&addImportListExclusion=True",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_delete_book(0)


@pytest.mark.asyncio
async def test_async_edit_book_files(aresponses, readarr_client: ReadarrClient) -> None:
    """Test editing book files."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_book_files(ReadarrBookFile("test"))
    assert isinstance(data, ReadarrBookFile)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile/editor",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = ReadarrBookFileEditor(
        {"bookFileIds": 0, "quality": {"quality": "test", "revision": "test"}}
    )
    await readarr_client.async_edit_book_files(data)


@pytest.mark.asyncio
async def test_async_delete_book_files(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test deleting book files."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile/0",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_delete_book_files(0)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookfile/bulk",
        "DELETE",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_delete_book_files([0])


@pytest.mark.asyncio
async def test_async_add_bookshelf(aresponses, readarr_client: ReadarrClient) -> None:
    """Test adding bookshelf."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/bookshelf",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    await readarr_client.async_add_bookshelf(ReadarrBookshelf("test"))


@pytest.mark.asyncio
async def test_async_get_development_config(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting development config."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/development",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/config-development.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_development_config()
    assert data.metadataSource == "string"
    assert data.consoleLogLevel == "string"
    assert data.logSql is False
    assert isinstance(data.logRotate, int)
    assert data.filterSentryEvents is True
    assert isinstance(data.id, int)


@pytest.mark.asyncio
async def test_async_edit_development_config(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing development config."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/development",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_development_config(
        ReadarrDevelopmentConfig("test")
    )
    assert isinstance(data, ReadarrDevelopmentConfig)


@pytest.mark.asyncio
async def test_async_edit_import_list(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing import list."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_import_list(ReadarrImportList("test"))
    assert isinstance(data, ReadarrImportList)


@pytest.mark.asyncio
async def test_async_add_import_list(aresponses, readarr_client: ReadarrClient) -> None:
    """Test adding import list."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_add_import_list(ReadarrImportList("test"))
    assert isinstance(data, ReadarrImportList)


@pytest.mark.asyncio
async def test_async_test_import_lists(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test import list testing."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist/test",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_test_import_lists(ReadarrImportList("test"))
    assert data is True

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    assert await readarr_client.async_test_import_lists() is True

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    assert await readarr_client.async_test_import_lists() is False


@pytest.mark.asyncio
async def test_async_importlist_action(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test performing import list action."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlist/action/newznabCategories",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/importlistoptions.json"),
        ),
        match_querystring=True,
    )
    data = ReadarrImportList({"name": "test"})
    data = await readarr_client.async_importlist_action(data)
    assert isinstance(data.options[0].value, int)
    assert data.options[0].name == "Audio/Video"
    assert isinstance(data.options[0].value, int)
    assert data.options[0].hint == "(3020)"
    assert isinstance(data.options[0].value, int)


@pytest.mark.asyncio
async def test_async_edit_metadata_profile(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing metadata profile."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/metadataprofile",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = ReadarrMetadataProfile("test")
    data = await readarr_client.async_edit_metadata_profile(data)
    assert isinstance(data, ReadarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_add_metadata_profile(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test adding metadata profile."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/metadataprofile",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = ReadarrMetadataProfile("test")
    data = await readarr_client.async_add_metadata_profile(data)
    assert isinstance(data, ReadarrMetadataProfile)


@pytest.mark.asyncio
async def test_async_edit_metadata_provider(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing metadata profile."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/metadataprovider",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = ReadarrMetadataProvider("test")
    data = await readarr_client.async_edit_metadata_provider(data)
    assert isinstance(data, ReadarrMetadataProvider)


@pytest.mark.asyncio
async def test_async_edit_naming_config(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing naming config."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/config/naming",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_naming_config(ReadarrNamingConfig("test"))
    assert isinstance(data, ReadarrNamingConfig)


@pytest.mark.asyncio
async def test_async_edit_notification(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing notification."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_notification(ReadarrNotification("test"))
    assert isinstance(data, ReadarrNotification)


@pytest.mark.asyncio
async def test_async_add_notification(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test adding notification."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_add_notification(ReadarrNotification("test"))
    assert isinstance(data, ReadarrNotification)


@pytest.mark.asyncio
async def test_async_test_notifications(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test notification testing."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification/test",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    data = ReadarrNotification("test")
    assert await readarr_client.async_test_notifications(data) is True

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation.json"),
        ),
        match_querystring=True,
    )
    assert await readarr_client.async_test_notifications() is True

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/notification/testall",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/validation-failed.json"),
        ),
        match_querystring=True,
    )
    assert await readarr_client.async_test_notifications() is False


@pytest.mark.asyncio
async def test_async_download_release(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test download release."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/release",
        "POST",
        aresponses.Response(
            status=201,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_download_release("test", 0)
    assert isinstance(data, ReadarrRelease)


@pytest.mark.asyncio
async def test_async_get_root_folders(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test getting root folders."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/rootfolder",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/rootfolder.json"),
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_get_root_folders()

    assert data[0].name == "books"
    assert data[0].path == "/books/"
    assert isinstance(data[0].defaultMetadataProfileId, int)
    assert isinstance(data[0].defaultQualityProfileId, int)
    assert data[0].defaultMonitorOption == "all"
    assert data[0].defaultNewItemMonitorOption == "all"
    assert data[0].defaultTags == []
    assert data[0].isCalibreLibrary is False
    assert isinstance(data[0].port, int)
    assert data[0].outputProfile == "default"
    assert data[0].useSsl is False
    assert data[0].accessible is True
    assert isinstance(data[0].freeSpace, int)
    assert isinstance(data[0].totalSpace, int)
    assert isinstance(data[0].id, int)


@pytest.mark.asyncio
async def test_async_edit_root_folder(
    aresponses, readarr_client: ReadarrClient
) -> None:
    """Test editing root folder."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/rootfolder",
        "PUT",
        aresponses.Response(
            status=202,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    data = await readarr_client.async_edit_root_folder(ReadarrRootFolder("test"))
    assert isinstance(data, ReadarrRootFolder)
