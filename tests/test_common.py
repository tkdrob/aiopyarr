"""Tests for common methods."""
from aiopyarr.models.common import Command, Diskspace, HostConfig, RootFolder, SystemBackup, UIConfig, SystemStatus

from aiopyarr.readarr_client import ReadarrClient
import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient
from aiopyarr.radarr_client import RadarrClient


from . import TEST_HOST_CONFIGURATION, load_fixture


@pytest.mark.asyncio
async def test_async_get_diskspace(aresponses):
    """Test getting diskspace."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/diskspace?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[Diskspace] = await client.async_get_diskspace()

        assert data[0].freeSpace == 16187217043456
        assert data[0].label == "DrivePool"
        assert data[0].path == "D:\\"
        assert data[0].totalSpace == 56009755148288


@pytest.mark.asyncio
async def test_async_get_root_folders(aresponses):
    """Test getting root folders."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/rootfolder?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/rootfolder.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[RootFolder] = await client.async_get_root_folders()

        assert data[0].path == "C:\\Downloads\\Movies"
        assert data[0].freeSpace == 282500063232
        assert data[0].unmappedFolders[0].name == "string"
        assert data[0].unmappedFolders[0].path == "path"
        assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_host_config(aresponses):
    """Test getting host configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/host?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/config-host.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: HostConfig = await client.async_get_host_config()

        assert data.analyticsEnabled is True
        assert data.apiKey == "string"
        assert data.authenticationMethod == "string"
        assert data.backupFolder == "string"
        assert data.backupInterval == 0
        assert data.backupRetention == 0
        assert data.bindAddress == "string"
        assert data.branch == "string"
        assert data.certificateValidation == "string"
        assert data.consoleLogLevel == "string"
        assert data.enableSsl is True
        assert data.id == 0
        assert data.launchBrowser is True
        assert data.logLevel == "string"
        assert data.password == "string"
        assert data.port == 0
        assert data.proxyBypassFilter == "string"
        assert data.proxyBypassLocalAddresses is True
        assert data.proxyEnabled is True
        assert data.proxyHostname == "string"
        assert data.proxyPassword == "string"
        assert data.proxyPort == 0
        assert data.proxyType == "string"
        assert data.proxyUsername == "string"
        assert data.sslCertHash == "string"
        assert data.sslCertPassword == "string"
        assert data.sslCertPath == "string"
        assert data.sslPort == 0
        assert data.urlBase == "string"
        assert data.updateAutomatically is True
        assert data.updateMechanism == "string"
        assert data.updateScriptPath == "string"
        assert data.username == "string"


@pytest.mark.asyncio
async def test_async_get_ui_config(aresponses):
    """Test getting ui configuration."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/config/ui?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/config-ui.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: UIConfig = await client.async_get_ui_config()

        assert data.calendarWeekColumnHeader == "ddd M/D"
        assert data.enableColorImpairedMode is False
        assert data.firstDayOfWeek == 0
        assert data.id == 1
        assert data.longDateFormat == "dddd, MMMM D YYYY"
        assert data.movieInfoLanguage == 1
        assert data.movieRuntimeFormat == "hoursMinutes"
        assert data.shortDateFormat == "MMM D YYYY"
        assert data.showRelativeDates is True
        assert data.timeFormat == "h(:mm)a"
        assert data.uiLanguage == 1


@pytest.mark.asyncio
async def test_async_get_system_status(aresponses):
    """Test getting system status."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/system/status?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("radarr/system-status.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: SystemStatus = await client.async_get_system_status()

        assert data.appData == "C:\\ProgramData\\Radarr"
        assert data.authentication == "none"
        assert data.branch == "nightly"
        assert data.buildTime == "2020-09-01T23:23:23.9621974Z"
        assert data.isAdmin is False
        assert data.isDebug is True
        assert data.isDocker is False
        assert data.isLinux is False
        assert data.isMono is False
        assert data.isMonoRuntime is False
        assert data.isNetCore is True
        assert data.isOsx is False
        assert data.isProduction is False
        assert data.isUserInteractive is True
        assert data.isWindows is True
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
        "/api/v3/log?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortKey=time&sortDir=descending",
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
        assert data.records[0].exception == "string"
        assert data.records[0].exceptionType == "string"


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


@pytest.mark.asyncio
async def test_async_get_custom_filters(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/customfilter?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/customfilter.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_custom_filters()
        assert data[0].id == 10
        assert data[0].type == "string"
        assert data[0].label == "string"
        assert data[0].filters[0].key == "string"
        assert data[0].filters[0].value == ["string"]
        assert data[0].filters[0].type == "string"


@pytest.mark.asyncio
async def test_async_get_command(aresponses):
    """Test getting commands."""
    aresponses.add(
        "127.0.0.1:7878",
        "/api/v3/command?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/command.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[Command] = await client.async_get_commands()

        assert data[0].name == "MessagingCleanup"
        assert data[0].commandName == "Messaging Cleanup"
        assert data[0].message == "Completed"
        assert data[0].body.sendUpdatesToClient is False
        assert data[0].body.updateScheduledTask is True
        assert data[0].body.completionMessage == "Completed"
        assert data[0].body.requiresDiskAccess is False
        assert data[0].body.isExclusive is False
        assert data[0].body.isNewMovie is False
        assert data[0].body.isTypeExclusive is False
        assert data[0].body.name == "MessagingCleanup"
        assert data[0].body.lastExecutionTime == "2021-11-29T19:57:46Z"
        assert data[0].body.lastStartTime == "2021-11-29T19:57:46Z"
        assert data[0].body.trigger == "scheduled"
        assert data[0].body.suppressMessages is False
        assert data[0].priority == "low"
        assert data[0].status == "completed"
        assert data[0].queued == "2021-11-29T20:03:16Z"
        assert data[0].started == "2021-11-29T20:03:16Z"
        assert data[0].ended == "2021-11-29T20:03:16Z"
        assert data[0].duration == "00:00:00.0102456"
        assert data[0].trigger == "scheduled"
        assert data[0].stateChangeTime == "2021-11-29T20:03:16Z"
        assert data[0].sendUpdatesToClient is False
        assert data[0].updateScheduledTask is True
        assert data[0].lastExecutionTime == "2021-11-29T19:57:46Z"
        assert data[0].id == 1987776
