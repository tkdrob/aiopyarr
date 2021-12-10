"""Tests for common methods."""
from datetime import datetime
from aiopyarr.models.common import Diskspace, SystemBackup

from aiopyarr.readarr_client import ReadarrClient
import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient
from aiopyarr.radarr_client import RadarrClient
from aiopyarr.models.readarr import _ReadarrBookValueSeriesLinks


from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_system_backup(aresponses):
    """Test getting author info."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/system/backup?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/system-backup.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_system_backup()
    assert isinstance(data, list) and isinstance(data[0], SystemBackup)
    assert data[0].id == 0
    assert data[0].name == "string"
    assert data[0].path == "string"
    assert data[0].type == "scheduled"
    assert data[0].time == "2021-12-09T13:22:49.441Z"


@pytest.mark.asyncio
async def test_async_get_tags(aresponses):
    """Test getting tags."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/tag/1?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/tag.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_tags(tagid=1)

        assert data.label == "amzn"
        assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_logs(aresponses):
    """Test getting history."""
    aresponses.add(
        "127.0.0.1:8989",
        "/api/v3/log?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortKey=time&sortDir=desc&filterKey=None&filterValue=All",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/logs.json"),
        ),
        match_querystring=True,
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
async def test_get_log_file(aresponses):
    """Test getting log file info."""
    aresponses.add(
        "127.0.0.1:8787",
        "/api/v1/log/file?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("readarr/log-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_log_file()
    assert data[0].filename == "string"
    assert data[0].lastWriteTime == "2021-12-09T23:19:21Z"
    assert data[0].contentsUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].id == 0