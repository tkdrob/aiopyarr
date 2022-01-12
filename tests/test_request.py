"""Tests for common methods."""
from datetime import datetime

import pytest
from aiohttp.client import ClientSession

from aiopyarr.radarr_client import RadarrClient
from aiopyarr.readarr_client import ReadarrClient
from aiopyarr.sonarr_client import SonarrClient

from . import (  # isort:skip
    RADARR_API,
    READARR_API,
    SONARR_API,
    TEST_HOST_CONFIGURATION,
    load_fixture,
)

from aiopyarr.models.request import (  # isort:skip
    Command,
    Diskspace,
    Filesystem,
    Health,
    HostConfig,
    LogFile,
    MetadataConfig,
    QueueStatus,
    SystemBackup,
    UIConfig,
    SystemStatus,
    Update,
)


@pytest.mark.asyncio
async def test_async_get_diskspace(aresponses):
    """Test getting diskspace."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/diskspace?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        f"/api/{RADARR_API}/rootfolder?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        data = await client.async_get_root_folders()

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
        f"/api/{RADARR_API}/config/host?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        f"/api/{RADARR_API}/config/ui?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        f"/api/{RADARR_API}/system/status?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/system-status.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: SystemStatus = await client.async_get_system_status()

    assert data.appData == "C:\\ProgramData\\Radarr"
    assert data.authentication == "string"
    assert data.branch == "nightly"
    assert data.buildTime == datetime(2020, 9, 1, 23, 23, 23, 962197)
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
    assert data.startTime == datetime(2020, 9, 1, 23, 50, 20, 241596)
    assert data.startupPath == "C:\\ProgramData\\Radarr"
    assert data.urlBase == ""
    assert data.version == "10.0.0.34882"


@pytest.mark.asyncio
async def test_async_get_system_backup(aresponses):
    """Test getting author info."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/system/backup?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
    assert data[0].time == datetime(2021, 12, 9, 13, 22, 49, 441000)


@pytest.mark.asyncio
async def test_async_get_tags(aresponses):
    """Test getting tags."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/tag/1?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        f"/api/{SONARR_API}/log?apikey=ur1234567-0abc12de3f456gh7ij89k012&page=1&pageSize=10&sortKey=time&sortDir=descending",
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
    assert data.records[0].time == datetime(2021, 11, 19, 9, 28, 26, 549994)
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
        f"/api/{READARR_API}/log/file?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/log-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[LogFile] = await client.async_get_log_file()
    assert data[0].filename == "string"
    assert data[0].lastWriteTime == datetime(2021, 12, 9, 23, 19, 21)
    assert data[0].contentsUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_get_log_file_content(aresponses):
    """Test getting log file content."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/log/file/file.txt?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/log-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_log_file_content("file.txt")


@pytest.mark.asyncio
async def test_get_log_file_update(aresponses):
    """Test getting log file update info."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/log/file/update?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/log-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[LogFile] = await client.async_get_log_file_updates()
    assert data[0].filename == "string"
    assert data[0].lastWriteTime == datetime(2021, 12, 9, 23, 19, 21)
    assert data[0].contentsUrl == "string"
    assert data[0].downloadUrl == "string"
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_get_log_file_update_content(aresponses):
    """Test getting log file update content."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/log/file/update/file.txt?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/log-file.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_log_file_update_content("file.txt")


@pytest.mark.asyncio
async def test_async_get_custom_filters(aresponses):
    """Test getting blocklisted movie."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/customfilter?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
        f"/api/{RADARR_API}/command?apikey=ur1234567-0abc12de3f456gh7ij89k012",
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
    assert data[0].body.lastExecutionTime == datetime(2021, 11, 29, 19, 57, 46)
    assert data[0].body.lastStartTime == datetime(2021, 11, 29, 19, 57, 46)
    assert data[0].body.trigger == "scheduled"
    assert data[0].body.suppressMessages is False
    assert data[0].priority == "low"
    assert data[0].status == "completed"
    assert data[0].queued == datetime(2021, 11, 29, 20, 3, 16)
    assert data[0].started == datetime(2021, 11, 29, 20, 3, 16)
    assert data[0].ended == datetime(2021, 11, 29, 20, 3, 16)
    assert data[0].duration == "00:00:00.0102456"
    assert data[0].trigger == "scheduled"
    assert data[0].stateChangeTime == datetime(2021, 11, 29, 20, 3, 16)
    assert data[0].sendUpdatesToClient is False
    assert data[0].updateScheduledTask is True
    assert data[0].lastExecutionTime == datetime(2021, 11, 29, 19, 57, 46)
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_download_client(aresponses):
    """Test getting download client."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/downloadclient/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/downloadclient.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_download_clients(clientid=0)
    assert data.configContract == "string"
    assert data.enable is True
    assert data.fields[0].order == 0
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert data.fields[0].selectOptions[0].value == 0
    assert data.fields[0].selectOptions[0].name == "Last"
    assert data.fields[0].selectOptions[0].order == 0
    assert data.fields[0].selectOptions[0].dividerAfter is False
    assert data.id == 0
    assert data.implementation == "string"
    assert data.implementationName == "string"
    assert data.infoLink == "string"
    assert data.name == "string"
    assert data.protocol == "string"
    assert data.priority == 0
    assert data.tags == [0]


@pytest.mark.asyncio
async def test_async_get_download_client_config(aresponses):
    """Test getting download client config."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/downloadclient?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/downloadclientconfig.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_download_client_config()
    assert data.downloadClientWorkingFolders == "_UNPACK_|_FAILED_"
    assert data.checkForFinishedDownloadInterval == 10
    assert data.enableCompletedDownloadHandling is True
    assert data.removeCompletedDownloads is False
    assert data.autoRedownloadFailed is True
    assert data.removeFailedDownloads is True
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_filesystem(aresponses):
    """Test getting filesystem attributes."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/filesystem?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/filesystem.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: Filesystem = await client.async_get_filesystem()
    assert data.directories[0].type == "folder"
    assert data.directories[0].name == "app"
    assert data.directories[0].path == "/app/"
    assert data.directories[0].size == 0
    assert data.directories[0].lastModified == datetime(2020, 1, 4, 3, 2, 20)
    assert data.files == []


@pytest.mark.asyncio
async def test_async_get_failed_health_checks(aresponses):
    """Test getting failed health checks."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/health?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/health.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[Health] = await client.async_get_failed_health_checks()

    assert data[0].message == "Enable Completed Download Handling"
    assert data[0].source == "ImportMechanismCheck"
    assert data[0].type == "warning"
    assert (
        data[0].wikiUrl
        == "https://wiki.servarr.com/radarr/system#completed-failed-download-handling"
    )


@pytest.mark.asyncio
async def test_async_get_import_list_exclusions(aresponses):
    """Test getting import list exclusions."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/importlistexclusion?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/importlistexclusion.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_import_list_exclusions()
    assert data.authorName == "string"
    assert data.foreignId == "string"
    assert data.id == 0
    assert data.title == "string"
    assert data.tvdbId == 0

    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )

    with pytest.raises(NotImplementedError):
        await client.async_get_import_list_exclusions()


@pytest.mark.asyncio
async def test_async_get_indexer(aresponses):
    """Test getting import lists."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/indexer/0?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/indexer.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_indexers(indexerid=0)

    assert data.enableRss is True
    assert data.enableAutomaticSearch is True
    assert data.enableInteractiveSearch is True
    assert data.supportsRss is True
    assert data.supportsSearch is True
    assert data.protocol == "string"
    assert data.priority == 0
    assert data.name == "string"
    assert data.fields[0].order == 0
    assert data.fields[0].name == "string"
    assert data.fields[0].label == "string"
    assert data.fields[0].helpText == "string"
    assert data.fields[0].value == "string"
    assert data.fields[0].type == "string"
    assert data.fields[0].advanced is True
    assert data.implementation == "string"
    assert data.implementationName == "string"
    assert data.configContract == "string"
    assert data.infoLink == "string"
    assert data.tags == [{}]
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_indexer_configs(aresponses):
    """Test getting indexer configs."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/indexer?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/config-indexer.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_indexer_configs()

    assert data.minimumAge == 0
    assert data.maximumSize == 0
    assert data.retention == 0
    assert data.rssSyncInterval == 360
    assert data.preferIndexerFlags is True
    assert data.availabilityDelay == 0
    assert data.allowHardcodedSubs is False
    assert data.whitelistedHardcodedSubs == ""
    assert data.id == 1


@pytest.mark.asyncio
async def test_async_get_import_list_exclusions(aresponses):
    """Test getting import list exclusions."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/language?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/language.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_languages()
    assert data.id == -1
    assert data.name == "Any"
    assert data.nameLower == "any"

    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )

    with pytest.raises(NotImplementedError):
        await client.async_get_languages()


@pytest.mark.asyncio
async def test_async_get_import_list_exclusions(aresponses):
    """Test getting import list exclusions."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/localization?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/localization.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_localization()
    data = data.Strings
    assert data.About == "string"
    assert data.Absolute == "string"
    assert data.AcceptConfirmationModal == "string"
    assert data.Actions == "string"
    assert data.Activity == "string"
    assert data.Add == "string"
    assert data.AddCustomFormat == "string"
    assert data.AddDelayProfile == "string"
    assert data.AddDownloadClient == "string"
    assert data.Added == "string"
    assert data.AddedAuthorSettings == "string"
    assert data.AddedToDownloadQueue == "string"
    assert data.AddExclusion == "string"
    assert data.AddImportListExclusionHelpText == "string"
    assert data.AddIndexer == "string"
    assert data.AddingTag == "string"
    assert data.AddList == "string"
    assert data.AddListExclusion == "string"
    assert data.AddMissing == "string"
    assert data.AddMovie == "string"
    assert data.AddMovies == "string"
    assert data.AddMoviesMonitored == "string"
    assert data.AddNew == "string"
    assert data.AddNewItem == "string"
    assert data.AddNewMessage == "string"
    assert data.AddNewMovie == "string"
    assert data.AddNewTmdbIdMessage == "string"
    assert data.AddNotification == "string"
    assert data.AddQualityProfile == "string"
    assert data.AddRemotePathMapping == "string"
    assert data.AddRestriction == "string"
    assert data.AddRootFolder == "string"
    assert data.AddToDownloadQueue == "string"
    assert data.AdvancedSettingsHiddenClickToShow == "string"
    assert data.AdvancedSettingsShownClickToHide == "string"
    assert data.AfterManualRefresh == "string"
    assert data.Age == "string"
    assert data.Agenda == "string"
    assert data.AgeWhenGrabbed == "string"
    assert data.All == "string"
    assert data.AllAuthorBooks == "string"
    assert data.AllBooks == "string"
    assert data.AllExpandedCollapseAll == "string"
    assert data.AllExpandedExpandAll == "string"
    assert data.AllFiles == "string"
    assert data.AllMoviesHiddenDueToFilter == "string"
    assert data.AllMoviesInPathHaveBeenImported == "string"
    assert data.AllowAuthorChangeClickToChangeAuthor == "string"
    assert data.AllowedLanguages == "string"
    assert data.AllowFingerprinting == "string"
    assert data.AllowFingerprintingHelpText == "string"
    assert data.AllowFingerprintingHelpTextWarning == "string"
    assert data.AllowHardcodedSubs == "string"
    assert data.AllowHardcodedSubsHelpText == "string"
    assert data.AllResultsHiddenFilter == "string"
    assert data.AlreadyInYourLibrary == "string"
    assert data.AlternateTitles == "string"
    assert data.AlternateTitleslength1Title == "string"
    assert data.AlternateTitleslength1Titles == "string"
    assert data.AlternativeTitle == "string"
    assert data.Always == "string"
    assert data.AnalyseVideoFiles == "string"
    assert data.Analytics == "string"
    assert data.AnalyticsEnabledHelpText == "string"
    assert data.AnalyticsEnabledHelpTextWarning == "string"
    assert data.Announced == "string"
    assert data.AnnouncedMsg == "string"
    assert data.AnyEditionOkHelpText == "string"
    assert data.ApiKey == "string"
    assert data.APIKey == "string"
    assert data.ApiKeyHelpTextWarning == "string"
    assert data.AppDataDirectory == "string"
    assert data.AppDataLocationHealthCheckMessage == "string"
    assert data.Apply == "string"
    assert data.ApplyTags == "string"
    assert data.ApplyTagsHelpTexts1 == "string"
    assert data.ApplyTagsHelpTexts2 == "string"
    assert data.ApplyTagsHelpTexts3 == "string"
    assert data.ApplyTagsHelpTexts4 == "string"
    assert data.AptUpdater == "string"
    assert data.AreYouSureYouWantToDeleteFormat == "string"
    assert data.AreYouSureYouWantToDeleteThisDelayProfile == "string"
    assert data.AreYouSureYouWantToDeleteThisImportListExclusion == "string"
    assert data.AreYouSureYouWantToDeleteThisRemotePathMapping == "string"
    assert data.AreYouSureYouWantToRemoveSelectedItemFromQueue == "string"
    assert data.AreYouSureYouWantToRemoveSelectedItemsFromQueue == "string"
    assert data.AreYouSureYouWantToRemoveTheSelectedItemsFromBlocklist == "string"
    assert data.AreYouSureYouWantToResetYourAPIKey == "string"
    assert data.AsAllDayHelpText == "string"
    assert data.ASIN == "string"
    assert data.AudioFileMetadata == "string"
    assert data.AudioInfo == "string"
    assert data.AuthBasic == "string"
    assert data.Authentication == "string"
    assert data.AuthenticationMethodHelpText == "string"
    assert data.AuthForm == "string"
    assert data.Author == "string"
    assert data.AuthorClickToChangeBook == "string"
    assert data.AuthorEditor == "string"
    assert data.AuthorFolderFormat == "string"
    assert data.AuthorIndex == "string"
    assert data.AuthorNameHelpText == "string"
    assert data.Authors == "string"
    assert data.Automatic == "string"
    assert data.AutomaticallySwitchEdition == "string"
    assert data.AutomaticSearch == "string"
    assert data.AutoRedownloadFailedHelpText == "string"
    assert data.AutoUnmonitorPreviouslyDownloadedBooksHelpText == "string"
    assert data.AutoUnmonitorPreviouslyDownloadedMoviesHelpText == "string"
    assert data.AvailabilityDelay == "string"
    assert data.AvailabilityDelayHelpText == "string"
    assert data.Backup == "string"
    assert data.BackupFolderHelpText == "string"
    assert data.BackupIntervalHelpText == "string"
    assert data.BackupNow == "string"
    assert data.BackupRetentionHelpText == "string"
    assert data.Backups == "string"
    assert data.BeforeUpdate == "string"
    assert data.BindAddress == "string"
    assert data.BindAddressHelpText == "string"
    assert data.BindAddressHelpTextWarning == "string"
    assert data.Blocklist == "string"
    assert data.Blocklisted == "string"
    assert data.BlocklistHelpText == "string"
    assert data.BlocklistRelease == "string"
    assert data.BlocklistReleases == "string"
    assert data.Book == "string"
    assert data.BookAvailableButMissing == "string"
    assert data.BookDownloaded == "string"
    assert data.BookEditor == "string"
    assert data.BookFileCountBookCountTotalTotalBookCountInterp == "string"
    assert data.BookFileCounttotalBookCountBooksDownloadedInterp == "string"
    assert data.BookFilesCountMessage == "string"
    assert data.BookHasNotAired == "string"
    assert data.BookIndex == "string"
    assert data.BookIsDownloading == "string"
    assert data.BookIsDownloadingInterp == "string"
    assert data.BookIsNotMonitored == "string"
    assert data.BookList == "string"
    assert data.BookMissingFromDisk == "string"
    assert data.BookMonitoring == "string"
    assert data.BookNaming == "string"
    assert data.Books == "string"
    assert data.BooksTotal == "string"
    assert data.BookStudio == "string"
    assert data.BookTitle == "string"
    assert data.Branch == "string"
    assert data.BranchUpdate == "string"
    assert data.BranchUpdateMechanism == "string"
    assert data.BuiltIn == "string"
    assert data.BypassDelayIfHighestQuality == "string"
    assert data.BypassDelayIfHighestQualityHelpText == "string"
    assert data.BypassProxyForLocalAddresses == "string"
    assert data.Calendar == "string"
    assert data.CalendarOptions == "string"
    assert data.CalendarWeekColumnHeaderHelpText == "string"
    assert data.CalibreContentServer == "string"
    assert data.CalibreContentServerText == "string"
    assert data.CalibreHost == "string"
    assert data.CalibreLibrary == "string"
    assert data.CalibreMetadata == "string"
    assert data.CalibreNotCalibreWeb == "string"
    assert data.CalibreOutputFormat == "string"
    assert data.CalibreOutputProfile == "string"
    assert data.CalibrePassword == "string"
    assert data.CalibrePort == "string"
    assert data.CalibreSettings == "string"
    assert data.CalibreUrlBase == "string"
    assert data.CalibreUsername == "string"
    assert data.Cancel == "string"
    assert data.CancelMessageText == "string"
    assert data.CancelPendingTask == "string"
    assert data.CancelProcessing == "string"
    assert data.CantFindMovie == "string"
    assert data.Cast == "string"
    assert data.CatalogNumber == "string"
    assert data.CertificateValidation == "string"
    assert data.CertificateValidationHelpText == "string"
    assert data.Certification == "string"
    assert data.CertificationCountry == "string"
    assert data.CertificationCountryHelpText == "string"
    assert data.CertValidationNoLocal == "string"
    assert data.ChangeFileDate == "string"
    assert data.ChangeHasNotBeenSavedYet == "string"
    assert data.CheckDownloadClientForDetails == "string"
    assert data.CheckForFinishedDownloadsInterval == "string"
    assert data.ChmodFolder == "string"
    assert data.ChmodFolderHelpText == "string"
    assert data.ChmodFolderHelpTextWarning == "string"
    assert data.ChmodGroup == "string"
    assert data.ChmodGroupHelpText == "string"
    assert data.ChmodGroupHelpTextWarning == "string"
    assert data.ChooseAnotherFolder == "string"
    assert data.ChownGroup == "string"
    assert data.ChownGroupHelpText == "string"
    assert data.ChownGroupHelpTextWarning == "string"
    assert data.CleanLibraryLevel == "string"
    assert data.Clear == "string"
    assert data.ClickToChangeLanguage == "string"
    assert data.ClickToChangeMovie == "string"
    assert data.ClickToChangeQuality == "string"
    assert data.ClickToChangeReleaseGroup == "string"
    assert data.ClientPriority == "string"
    assert data.CloneCustomFormat == "string"
    assert data.CloneFormatTag == "string"
    assert data.CloneIndexer == "string"
    assert data.CloneProfile == "string"
    assert data.Close == "string"
    assert data.CloseCurrentModal == "string"
    assert data.CollapseMultipleBooks == "string"
    assert data.CollapseMultipleBooksHelpText == "string"
    assert data.Collection == "string"
    assert data.ColonReplacement == "string"
    assert data.ColonReplacementFormatHelpText == "string"
    assert data.Columns == "string"
    assert data.CompletedDownloadHandling == "string"
    assert data.Component == "string"
    assert data.Conditions == "string"
    assert data.Connect == "string"
    assert data.Connection == "string"
    assert data.ConnectionLost == "string"
    assert data.ConnectionLostAutomaticMessage == "string"
    assert data.ConnectionLostMessage == "string"
    assert data.Connections == "string"
    assert data.ConnectSettings == "string"
    assert data.ConnectSettingsSummary == "string"
    assert data.ConsideredAvailable == "string"
    assert data.ConsoleLogLevel == "string"
    assert data.Continuing == "string"
    assert data.ContinuingAllBooksDownloaded == "string"
    assert data.ContinuingMoreBooksAreExpected == "string"
    assert data.ContinuingNoAdditionalBooksAreExpected == "string"
    assert data.CopyToClipboard == "string"
    assert data.CopyUsingHardlinksHelpText == "string"
    assert data.CopyUsingHardlinksHelpTextWarning == "string"
    assert data.CouldNotConnectSignalR == "string"
    assert data.CouldNotFindResults == "string"
    assert data.Country == "string"
    assert data.CreateEmptyAuthorFolders == "string"
    assert data.CreateEmptyAuthorFoldersHelpText == "string"
    assert data.CreateEmptyMovieFolders == "string"
    assert data.CreateEmptyMovieFoldersHelpText == "string"
    assert data.CreateGroup == "string"
    assert data.Crew == "string"
    assert data.CurrentlyInstalled == "string"
    assert data.Custom == "string"
    assert data.CustomFilters == "string"
    assert data.CustomFormat == "string"
    assert data.CustomFormatHelpText == "string"
    assert data.CustomFormatJSON == "string"
    assert data.CustomFormats == "string"
    assert data.CustomFormatScore == "string"
    assert data.CustomFormatsSettings == "string"
    assert data.CustomFormatsSettingsSummary == "string"
    assert data.CustomFormatUnknownCondition == "string"
    assert data.CustomFormatUnknownConditionOption == "string"
    assert data.Cutoff == "string"
    assert data.CutoffFormatScoreHelpText == "string"
    assert data.CutoffHelpText == "string"
    assert data.CutoffUnmet == "string"
    assert data.Date == "string"
    assert data.Dates == "string"
    assert data.Day == "string"
    assert data.Days == "string"
    assert data.DBMigration == "string"
    assert data.Debug == "string"
    assert data.DefaultCase == "string"
    assert data.DefaultDelayProfile == "string"
    assert data.DefaultMetadataProfileIdHelpText == "string"
    assert data.DefaultMonitorOptionHelpText == "string"
    assert data.DefaultQualityProfileIdHelpText == "string"
    assert data.DefaultReadarrTags == "string"
    assert data.DefaultTagsHelpText == "string"
    assert data.DelayingDownloadUntilInterp == "string"
    assert data.DelayProfile == "string"
    assert data.DelayProfiles == "string"
    assert data.Delete == "string"
    assert data.DeleteBackup == "string"
    assert data.DeleteBackupMessageText == "string"
    assert data.DeleteBookFile == "string"
    assert data.DeleteBookFileMessageText == "string"
    assert data.DeleteCustomFormat == "string"
    assert data.Deleted == "string"
    assert data.DeleteDelayProfile == "string"
    assert data.DeleteDelayProfileMessageText == "string"
    assert data.DeletedMsg == "string"
    assert data.DeleteDownloadClient == "string"
    assert data.DeleteDownloadClientMessageText == "string"
    assert data.DeleteEmptyFolders == "string"
    assert data.DeleteEmptyFoldersHelpText == "string"
    assert data.DeleteFile == "string"
    assert data.DeleteFileLabel == "string"
    assert data.DeleteFilesHelpText == "string"
    assert data.DeleteFilesLabel == "string"
    assert data.DeleteHeader == "string"
    assert data.DeleteImportList == "string"
    assert data.DeleteImportListExclusion == "string"
    assert data.DeleteImportListExclusionMessageText == "string"
    assert data.DeleteImportListMessageText == "string"
    assert data.DeleteIndexer == "string"
    assert data.DeleteIndexerMessageText == "string"
    assert data.DeleteList == "string"
    assert data.DeleteListMessageText == "string"
    assert data.DeleteMetadataProfile == "string"
    assert data.DeleteMetadataProfileMessageText == "string"
    assert data.DeleteMovieFolderHelpText == "string"
    assert data.DeleteMovieFolderLabel == "string"
    assert data.DeleteNotification == "string"
    assert data.DeleteNotificationMessageText == "string"
    assert data.DeleteQualityProfile == "string"
    assert data.DeleteQualityProfileMessageText == "string"
    assert data.DeleteReleaseProfile == "string"
    assert data.DeleteReleaseProfileMessageText == "string"
    assert data.DeleteRestriction == "string"
    assert data.DeleteRestrictionHelpText == "string"
    assert data.DeleteRootFolder == "string"
    assert data.DeleteRootFolderMessageText == "string"
    assert data.DeleteSelectedBookFiles == "string"
    assert data.DeleteSelectedBookFilesMessageText == "string"
    assert data.DeleteSelectedMovie == "string"
    assert data.DeleteSelectedMovieFiles == "string"
    assert data.DeleteSelectedMovieFilesMessage == "string"
    assert data.DeleteTag == "string"
    assert data.DeleteTagMessageText == "string"
    assert data.DeleteTheMovieFolder == "string"
    assert data.DestinationPath == "string"
    assert data.DestinationRelativePath == "string"
    assert data.DetailedProgressBar == "string"
    assert data.DetailedProgressBarHelpText == "string"
    assert data.Details == "string"
    assert data.Development == "string"
    assert data.DigitalRelease == "string"
    assert data.Disabled == "string"
    assert data.DiscCount == "string"
    assert data.DiscNumber == "string"
    assert data.Discord == "string"
    assert data.DiscordUrlInSlackNotification == "string"
    assert data.Discover == "string"
    assert data.DiskSpace == "string"
    assert data.Docker == "string"
    assert data.DockerUpdater == "string"
    assert data.Donations == "string"
    assert data.DoneEditingGroups == "string"
    assert data.DoNotPrefer == "string"
    assert data.DoNotUpgradeAutomatically == "string"
    assert data.Download == "string"
    assert data.DownloadClient == "string"
    assert data.DownloadClientCheckDownloadingToRoot == "string"
    assert data.DownloadClientCheckNoneAvailableMessage == "string"
    assert data.DownloadClientCheckUnableToCommunicateMessage == "string"
    assert data.DownloadClients == "string"
    assert data.DownloadClientSettings == "string"
    assert data.DownloadClientsSettingsSummary == "string"
    assert data.DownloadClientStatusCheckAllClientMessage == "string"
    assert data.DownloadClientStatusCheckSingleClientMessage == "string"
    assert data.DownloadClientUnavailable == "string"
    assert data.Downloaded == "string"
    assert data.DownloadedAndMonitored == "string"
    assert data.DownloadedButNotMonitored == "string"
    assert data.DownloadFailed == "string"
    assert data.DownloadFailedCheckDownloadClientForMoreDetails == "string"
    assert data.DownloadFailedInterp == "string"
    assert data.Downloading == "string"
    assert data.DownloadPropersAndRepacks == "string"
    assert data.DownloadPropersAndRepacksHelpText1 == "string"
    assert data.DownloadPropersAndRepacksHelpText2 == "string"
    assert data.DownloadPropersAndRepacksHelpTexts1 == "string"
    assert data.DownloadPropersAndRepacksHelpTexts2 == "string"
    assert data.DownloadPropersAndRepacksHelpTextWarning == "string"
    assert data.DownloadWarning == "string"
    assert data.DownloadWarningCheckDownloadClientForMoreDetails == "string"
    assert data.Edit == "string"
    assert data.EditAuthor == "string"
    assert data.EditCustomFormat == "string"
    assert data.EditDelayProfile == "string"
    assert data.EditGroups == "string"
    assert data.EditIndexer == "string"
    assert data.Edition == "string"
    assert data.EditionsHelpText == "string"
    assert data.EditListExclusion == "string"
    assert data.EditMovie == "string"
    assert data.EditMovieFile == "string"
    assert data.EditPerson == "string"
    assert data.EditQualityProfile == "string"
    assert data.EditRemotePathMapping == "string"
    assert data.EditRestriction == "string"
    assert data.EmbedMetadataHelpText == "string"
    assert data.EmbedMetadataInBookFiles == "string"
    assert data.Enable == "string"
    assert data.EnableAutoHelpText == "string"
    assert data.EnableAutomaticAdd == "string"
    assert data.EnableAutomaticAddHelpText == "string"
    assert data.EnableAutomaticSearch == "string"
    assert data.EnableAutomaticSearchHelpText == "string"
    assert data.EnableAutomaticSearchHelpTextWarning == "string"
    assert data.EnableColorImpairedMode == "string"
    assert data.EnableColorImpairedModeHelpText == "string"
    assert data.EnableCompletedDownloadHandlingHelpText == "string"
    assert data.Enabled == "string"
    assert data.EnabledHelpText == "string"
    assert data.EnableHelpText == "string"
    assert data.EnableInteractiveSearch == "string"
    assert data.EnableInteractiveSearchHelpText == "string"
    assert data.EnableInteractiveSearchHelpTextWarning == "string"
    assert data.EnableMediaInfoHelpText == "string"
    assert data.EnableProfile == "string"
    assert data.EnableRSS == "string"
    assert data.EnableSSL == "string"
    assert data.EnableSslHelpText == "string"
    assert data.Ended == "string"
    assert data.EndedAllBooksDownloaded == "string"
    assert data.EntityName == "string"
    assert data.Episode == "string"
    assert data.EpisodeDoesNotHaveAnAbsoluteEpisodeNumber == "string"
    assert data.Error == "string"
    assert data.ErrorLoadingContents == "string"
    assert data.ErrorLoadingPreviews == "string"
    assert data.ErrorRestoringBackup == "string"
    assert data.Events == "string"
    assert data.EventType == "string"
    assert data.Exception == "string"
    assert data.Excluded == "string"
    assert data.ExcludeMovie == "string"
    assert data.ExcludeTitle == "string"
    assert data.Existing == "string"
    assert data.ExistingBooks == "string"
    assert data.ExistingItems == "string"
    assert data.ExistingMovies == "string"
    assert data.ExistingTag == "string"
    assert data.ExistingTagsScrubbed == "string"
    assert data.ExportCustomFormat == "string"
    assert data.Extension == "string"
    assert data.ExternalUpdater == "string"
    assert data.ExtraFileExtensionsHelpTexts1 == "string"
    assert data.ExtraFileExtensionsHelpTexts2 == "string"
    assert data.Failed == "string"
    assert data.FailedDownloadHandling == "string"
    assert data.FailedLoadingSearchResults == "string"
    assert data.FailedToLoadMovieFromAPI == "string"
    assert data.FailedToLoadQueue == "string"
    assert data.FeatureRequests == "string"
    assert data.FileDateHelpText == "string"
    assert data.FileDetails == "string"
    assert data.FileManagement == "string"
    assert data.Filename == "string"
    assert data.FileNames == "string"
    assert data.FileNameTokens == "string"
    assert data.Files == "string"
    assert data.FilesTotal == "string"
    assert data.FileWasDeletedByUpgrade == "string"
    assert data.FileWasDeletedByViaUI == "string"
    assert data.Filter == "string"
    assert data.FilterAnalyticsEvents == "string"
    assert data.FilterAuthor == "string"
    assert data.FilterPlaceHolder == "string"
    assert data.Filters == "string"
    assert data.FilterSentryEventsHelpText == "string"
    assert data.FirstBook == "string"
    assert data.FirstDayOfWeek == "string"
    assert data.Fixed == "string"
    assert data.FocusSearchBox == "string"
    assert data.Folder == "string"
    assert data.FolderMoveRenameWarning == "string"
    assert data.Folders == "string"
    assert data.FollowPerson == "string"
    assert data.Forecast == "string"
    assert data.ForeignIdHelpText == "string"
    assert data.Formats == "string"
    assert data.ForMoreInformationOnTheIndividualDownloadClients == "string"
    assert (
        data.ForMoreInformationOnTheIndividualDownloadClientsClickOnTheInfoButtons
        == "string"
    )
    assert (
        data.ForMoreInformationOnTheIndividualImportListsClinkOnTheInfoButtons
        == "string"
    )
    assert data.ForMoreInformationOnTheIndividualIndexers == "string"
    assert (
        data.ForMoreInformationOnTheIndividualIndexersClickOnTheInfoButtons == "string"
    )
    assert data.ForMoreInformationOnTheIndividualListsClickOnTheInfoButtons == "string"
    assert data.FreeSpace == "string"
    assert data.From == "string"
    assert data.FutureBooks == "string"
    assert data.FutureDays == "string"
    assert data.FutureDaysHelpText == "string"
    assert data.General == "string"
    assert data.GeneralSettings == "string"
    assert data.GeneralSettingsSummary == "string"
    assert data.Genres == "string"
    assert data.Global == "string"
    assert data.GoToAuthorListing == "string"
    assert data.GoToInterp == "string"
    assert data.Grab == "string"
    assert data.Grabbed == "string"
    assert data.GrabID == "string"
    assert data.GrabRelease == "string"
    assert data.GrabReleaseMessageText == "string"
    assert data.GrabSelected == "string"
    assert data.Group == "string"
    assert data.HardlinkCopyFiles == "string"
    assert data.HasMonitoredBooksNoMonitoredBooksForThisAuthor == "string"
    assert data.HasPendingChangesNoChanges == "string"
    assert data.HasPendingChangesSaveChanges == "string"
    assert data.HaveNotAddedMovies == "string"
    assert data.Health == "string"
    assert data.HealthNoIssues == "string"
    assert data.HelpText == "string"
    assert data.HiddenClickToShow == "string"
    assert data.HideAdvanced == "string"
    assert data.HideBooks == "string"
    assert data.History == "string"
    assert data.HomePage == "string"
    assert data.Host == "string"
    assert data.HostHelpText == "string"
    assert data.Hostname == "string"
    assert data.Hours == "string"
    assert data.HttpHttps == "string"
    assert data.ICalFeed == "string"
    assert data.ICalHttpUrlHelpText == "string"
    assert data.iCalLink == "string"
    assert data.ICalLink == "string"
    assert data.IconForCutoffUnmet == "string"
    assert data.IconTooltip == "string"
    assert (
        data.IfYouDontAddAnImportListExclusionAndTheAuthorHasAMetadataProfileOtherThanNoneThenThisBookMayBeReaddedDuringTheNextAuthorRefresh
        == "string"
    )
    assert data.Ignored == "string"
    assert data.IgnoredAddresses == "string"
    assert data.IgnoreDeletedBooks == "string"
    assert data.IgnoreDeletedMovies == "string"
    assert data.IgnoredHelpText == "string"
    assert data.IgnoredMetaHelpText == "string"
    assert data.IgnoredPlaceHolder == "string"
    assert data.IllRestartLater == "string"
    assert data.Images == "string"
    assert data.IMDb == "string"
    assert data.ImdbRating == "string"
    assert data.ImdbVotes == "string"
    assert data.Import == "string"
    assert data.ImportCustomFormat == "string"
    assert data.Imported == "string"
    assert data.ImportedTo == "string"
    assert data.ImportErrors == "string"
    assert data.ImportExistingMovies == "string"
    assert data.ImportExtraFiles == "string"
    assert data.ImportExtraFilesHelpText == "string"
    assert data.ImportFailed == "string"
    assert data.ImportFailedInterp == "string"
    assert data.ImportFailures == "string"
    assert data.ImportHeader == "string"
    assert data.ImportIncludeQuality == "string"
    assert data.Importing == "string"
    assert data.ImportLibrary == "string"
    assert data.ImportListExclusions == "string"
    assert data.ImportListMissingRoot == "string"
    assert data.ImportListMultipleMissingRoots == "string"
    assert data.ImportLists == "string"
    assert data.ImportListSettings == "string"
    assert data.ImportListSpecificSettings == "string"
    assert data.ImportListStatusCheckAllClientMessage == "string"
    assert data.ImportListStatusCheckSingleClientMessage == "string"
    assert data.ImportListSyncIntervalHelpText == "string"
    assert data.ImportMechanismHealthCheckMessage == "string"
    assert data.ImportMovies == "string"
    assert data.ImportNotForDownloads == "string"
    assert data.ImportRootPath == "string"
    assert data.ImportTipsMessage == "string"
    assert data.InCinemas == "string"
    assert data.InCinemasDate == "string"
    assert data.InCinemasMsg == "string"
    assert data.IncludeCustomFormatWhenRenaming == "string"
    assert data.IncludeCustomFormatWhenRenamingHelpText == "string"
    assert data.IncludeHealthWarningsHelpText == "string"
    assert data.IncludePreferredWhenRenaming == "string"
    assert data.IncludeRadarrRecommendations == "string"
    assert data.IncludeRecommendationsHelpText == "string"
    assert data.IncludeUnknownAuthorItemsHelpText == "string"
    assert data.IncludeUnknownMovieItemsHelpText == "string"
    assert data.IncludeUnmonitored == "string"
    assert data.Indexer == "string"
    assert data.IndexerDownloadClientHelpText == "string"
    assert data.IndexerFlags == "string"
    assert data.IndexerIdHelpText == "string"
    assert data.IndexerIdHelpTextWarning == "string"
    assert data.IndexerIdvalue0IncludeInPreferredWordsRenamingFormat == "string"
    assert data.IndexerIdvalue0OnlySupportedWhenIndexerIsSetToAll == "string"
    assert data.IndexerJackettAll == "string"
    assert data.IndexerLongTermStatusCheckAllClientMessage == "string"
    assert data.IndexerLongTermStatusCheckSingleClientMessage == "string"
    assert data.IndexerPriority == "string"
    assert data.IndexerPriorityHelpText == "string"
    assert data.IndexerRssHealthCheckNoAvailableIndexers == "string"
    assert data.IndexerRssHealthCheckNoIndexers == "string"
    assert data.Indexers == "string"
    assert data.IndexerSearchCheckNoAutomaticMessage == "string"
    assert data.IndexerSearchCheckNoAvailableIndexersMessage == "string"
    assert data.IndexerSearchCheckNoInteractiveMessage == "string"
    assert data.IndexerSettings == "string"
    assert data.IndexersSettingsSummary == "string"
    assert data.IndexerStatusCheckAllClientMessage == "string"
    assert data.IndexerStatusCheckSingleClientMessage == "string"
    assert data.IndexerTagHelpText == "string"
    assert data.Info == "string"
    assert data.InstallLatest == "string"
    assert data.InteractiveImport == "string"
    assert data.InteractiveImportErrLanguage == "string"
    assert data.InteractiveImportErrMovie == "string"
    assert data.InteractiveImportErrQuality == "string"
    assert data.InteractiveSearch == "string"
    assert data.Interval == "string"
    assert data.InvalidFormat == "string"
    assert data.ISBN == "string"
    assert data.IsCalibreLibraryHelpText == "string"
    assert data.IsCutoffCutoff == "string"
    assert data.IsCutoffUpgradeUntilThisQualityIsMetOrExceeded == "string"
    assert data.IsExpandedHideBooks == "string"
    assert data.IsExpandedHideFileInfo == "string"
    assert data.IsExpandedShowBooks == "string"
    assert data.IsExpandedShowFileInfo == "string"
    assert (
        data.IsInUseCantDeleteAMetadataProfileThatIsAttachedToAnAuthorOrImportList
        == "string"
    )
    assert (
        data.IsInUseCantDeleteAQualityProfileThatIsAttachedToAnAuthorOrImportList
        == "string"
    )
    assert data.IsShowingMonitoredMonitorSelected == "string"
    assert data.IsShowingMonitoredUnmonitorSelected == "string"
    assert data.IsTagUsedCannotBeDeletedWhileInUse == "string"
    assert data.KeepAndUnmonitorMovie == "string"
    assert data.KeyboardShortcuts == "string"
    assert data.Label == "string"
    assert data.Language == "string"
    assert data.LanguageHelpText == "string"
    assert data.Languages == "string"
    assert data.Large == "string"
    assert data.LastDuration == "string"
    assert data.LastExecution == "string"
    assert data.LastUsed == "string"
    assert data.LastWriteTime == "string"
    assert data.LatestBook == "string"
    assert data.LaunchBrowserHelpText == "string"
    assert data.Letterboxd == "string"
    assert data.Level == "string"
    assert data.LibraryHelpText == "string"
    assert data.LinkHere == "string"
    assert data.Links == "string"
    assert data.ListExclusions == "string"
    assert data.Lists == "string"
    assert data.ListSettings == "string"
    assert data.ListsSettingsSummary == "string"
    assert data.ListSyncLevelHelpText == "string"
    assert data.ListSyncLevelHelpTextWarning == "string"
    assert data.ListTagsHelpText == "string"
    assert data.ListUpdateInterval == "string"
    assert data.LoadingBookFilesFailed == "string"
    assert data.LoadingBooksFailed == "string"
    assert data.LoadingMovieCreditsFailed == "string"
    assert data.LoadingMovieExtraFilesFailed == "string"
    assert data.LoadingMovieFilesFailed == "string"
    assert data.Local == "string"
    assert data.LocalPath == "string"
    assert data.LocalPathHelpText == "string"
    assert data.Location == "string"
    assert data.LogFiles == "string"
    assert data.Logging == "string"
    assert data.LogLevel == "string"
    assert data.LogLevelTraceHelpTextWarning == "string"
    assert data.LogLevelvalueTraceTraceLoggingShouldOnlyBeEnabledTemporarily == "string"
    assert data.LogOnly == "string"
    assert data.LogRotateHelpText == "string"
    assert data.LogRotation == "string"
    assert data.Logs == "string"
    assert data.LogSQL == "string"
    assert data.LogSqlHelpText == "string"
    assert data.LongDateFormat == "string"
    assert data.LookingForReleaseProfiles1 == "string"
    assert data.LookingForReleaseProfiles2 == "string"
    assert data.LowerCase == "string"
    assert data.MaintenanceRelease == "string"
    assert data.Manual == "string"
    assert data.ManualDownload == "string"
    assert data.ManualImport == "string"
    assert data.ManualImportSelectLanguage == "string"
    assert data.ManualImportSelectMovie == "string"
    assert data.ManualImportSelectQuality == "string"
    assert data.ManualImportSetReleaseGroup == "string"
    assert data.MappedDrivesRunningAsService == "string"
    assert data.MarkAsFailed == "string"
    assert data.MarkAsFailedMessageText == "string"
    assert data.MassBookSearch == "string"
    assert data.MassBookSearchWarning == "string"
    assert data.MassMovieSearch == "string"
    assert data.Max == "string"
    assert data.MaximumLimits == "string"
    assert data.MaximumSize == "string"
    assert data.MaximumSizeHelpText == "string"
    assert data.Mechanism == "string"
    assert data.MediaInfo == "string"
    assert data.MediaManagement == "string"
    assert data.MediaManagementSettings == "string"
    assert data.MediaManagementSettingsSummary == "string"
    assert data.Medium == "string"
    assert data.MediumFormat == "string"
    assert data.MegabytesPerMinute == "string"
    assert data.Message == "string"
    assert data.Metadata == "string"
    assert data.MetadataConsumers == "string"
    assert data.MetadataProfile == "string"
    assert data.MetadataProfileIdHelpText == "string"
    assert data.MetadataProfiles == "string"
    assert data.MetadataProviderSource == "string"
    assert data.MetadataSettings == "string"
    assert data.MetadataSettingsSummary == "string"
    assert data.MetadataSource == "string"
    assert data.MetadataSourceHelpText == "string"
    assert data.MIA == "string"
    assert data.Min == "string"
    assert data.MinAvailability == "string"
    assert data.MinFormatScoreHelpText == "string"
    assert data.MinimumAge == "string"
    assert data.MinimumAgeHelpText == "string"
    assert data.MinimumAvailability == "string"
    assert data.MinimumCustomFormatScore == "string"
    assert data.MinimumFreeSpace == "string"
    assert data.MinimumFreeSpaceWhenImportingHelpText == "string"
    assert data.MinimumLimits == "string"
    assert data.MinimumPages == "string"
    assert data.MinimumPopularity == "string"
    assert data.MinPagesHelpText == "string"
    assert data.MinPopularityHelpText == "string"
    assert data.Minutes == "string"
    assert data.MinutesHundredTwenty == "string"
    assert data.MinutesNinety == "string"
    assert data.MinutesSixty == "string"
    assert data.Missing == "string"
    assert data.MissingBooks == "string"
    assert data.MissingBooksAuthorMonitored == "string"
    assert data.MissingBooksAuthorNotMonitored == "string"
    assert data.MissingFromDisk == "string"
    assert data.MissingMonitoredAndConsideredAvailable == "string"
    assert data.MissingNotMonitored == "string"
    assert data.Mode == "string"
    assert data.Monday == "string"
    assert data.Monitor == "string"
    assert data.MonitorAuthor == "string"
    assert data.MonitorBook == "string"
    assert data.MonitorBookExistingOnlyWarning == "string"
    assert data.Monitored == "string"
    assert data.MonitoredAuthorIsMonitored == "string"
    assert data.MonitoredAuthorIsUnmonitored == "string"
    assert data.MonitoredHelpText == "string"
    assert data.MonitoredOnly == "string"
    assert data.MonitoredStatus == "string"
    assert data.Monitoring == "string"
    assert data.MonitoringOptions == "string"
    assert data.MonitoringOptionsHelpText == "string"
    assert data.MonitorMovie == "string"
    assert data.MonitorNewItems == "string"
    assert data.MonitorNewItemsHelpText == "string"
    assert data.MonoVersion == "string"
    assert data.Month == "string"
    assert data.Months == "string"
    assert data.More == "string"
    assert data.MoreControlCFText == "string"
    assert data.MoreDetails == "string"
    assert data.MoreInfo == "string"
    assert data.MountCheckMessage == "string"
    assert data.MoveFiles == "string"
    assert data.MoveFolders1 == "string"
    assert data.MoveFolders2 == "string"
    assert data.Movie == "string"
    assert data.MovieAlreadyExcluded == "string"
    assert data.MovieChat == "string"
    assert data.MovieDetailsNextMovie == "string"
    assert data.MovieDetailsPreviousMovie == "string"
    assert data.MovieEditor == "string"
    assert data.MovieExcludedFromAutomaticAdd == "string"
    assert data.MovieFiles == "string"
    assert data.MovieFilesTotaling == "string"
    assert data.MovieFolderFormat == "string"
    assert data.MovieID == "string"
    assert data.MovieIndex == "string"
    assert data.MovieIndexScrollBottom == "string"
    assert data.MovieIndexScrollTop == "string"
    assert data.MovieInfoLanguage == "string"
    assert data.MovieInfoLanguageHelpText == "string"
    assert data.MovieInfoLanguageHelpTextWarning == "string"
    assert data.MovieInvalidFormat == "string"
    assert data.MovieIsDownloading == "string"
    assert data.MovieIsDownloadingInterp == "string"
    assert data.MovieIsMonitored == "string"
    assert data.MovieIsOnImportExclusionList == "string"
    assert data.MovieIsRecommend == "string"
    assert data.MovieIsUnmonitored == "string"
    assert data.MovieNaming == "string"
    assert data.Movies == "string"
    assert data.MoviesSelectedInterp == "string"
    assert data.MovieTitle == "string"
    assert data.MovieTitleHelpText == "string"
    assert data.MovieYear == "string"
    assert data.MovieYearHelpText == "string"
    assert data.MultiLanguage == "string"
    assert data.MusicBrainzAuthorID == "string"
    assert data.MusicBrainzBookID == "string"
    assert data.MusicbrainzId == "string"
    assert data.MusicBrainzRecordingID == "string"
    assert data.MusicBrainzReleaseID == "string"
    assert data.MusicBrainzTrackID == "string"
    assert data.MustContain == "string"
    assert data.MustNotContain == "string"
    assert data.Name == "string"
    assert data.NameFirstLast == "string"
    assert data.NameLastFirst == "string"
    assert data.NameStyle == "string"
    assert data.NamingSettings == "string"
    assert data.Negate == "string"
    assert data.Negated == "string"
    assert data.NegateHelpText == "string"
    assert data.NetCore == "string"
    assert data.NETCore == "string"
    assert data.New == "string"
    assert data.NewBooks == "string"
    assert data.NextExecution == "string"
    assert data.No == "string"
    assert data.NoAltTitle == "string"
    assert data.NoBackupsAreAvailable == "string"
    assert data.NoChange == "string"
    assert data.NoChanges == "string"
    assert data.NoEventsFound == "string"
    assert data.NoHistory == "string"
    assert data.NoHistoryBlocklist == "string"
    assert data.NoLeaveIt == "string"
    assert data.NoLimitForAnyRuntime == "string"
    assert data.NoLinks == "string"
    assert data.NoListRecommendations == "string"
    assert data.NoLogFiles == "string"
    assert data.NoMatchFound == "string"
    assert data.NoMinimumForAnyRuntime == "string"
    assert data.NoMoveFilesSelf == "string"
    assert data.NoMoviesExist == "string"
    assert data.NoName == "string"
    assert data.NoResultsFound == "string"
    assert data.NoTagsHaveBeenAddedYet == "string"
    assert data.NotAvailable == "string"
    assert data.NotificationTriggers == "string"
    assert data.NotificationTriggersHelpText == "string"
    assert data.NotMonitored == "string"
    assert data.NoUpdatesAreAvailable == "string"
    assert data.NoVideoFilesFoundSelectedFolder == "string"
    assert data.OAuthPopupMessage == "string"
    assert data.Ok == "string"
    assert data.OnApplicationUpdate == "string"
    assert data.OnApplicationUpdateHelpText == "string"
    assert data.OnBookRetagHelpText == "string"
    assert data.OnDownloadFailureHelpText == "string"
    assert data.OnDownloadHelpText == "string"
    assert data.OnGrab == "string"
    assert data.OnGrabHelpText == "string"
    assert data.OnHealthIssue == "string"
    assert data.OnHealthIssueHelpText == "string"
    assert data.OnImport == "string"
    assert data.OnImportFailureHelpText == "string"
    assert data.OnLatestVersion == "string"
    assert data.OnlyTorrent == "string"
    assert data.OnlyUsenet == "string"
    assert data.OnMovieDelete == "string"
    assert data.OnMovieDeleteHelpText == "string"
    assert data.OnMovieFileDelete == "string"
    assert data.OnMovieFileDeleteForUpgrade == "string"
    assert data.OnMovieFileDeleteForUpgradeHelpText == "string"
    assert data.OnMovieFileDeleteHelpText == "string"
    assert data.OnReleaseImportHelpText == "string"
    assert data.OnRename == "string"
    assert data.OnRenameHelpText == "string"
    assert data.OnUpgrade == "string"
    assert data.OnUpgradeHelpText == "string"
    assert data.OpenBrowserOnStart == "string"
    assert data.OpenThisModal == "string"
    assert data.Options == "string"
    assert data.Organize == "string"
    assert data.OrganizeAndRename == "string"
    assert data.OrganizeConfirm == "string"
    assert data.OrganizeModalAllPathsRelative == "string"
    assert data.OrganizeModalDisabled == "string"
    assert data.OrganizeModalNamingPattern == "string"
    assert data.OrganizeModalSuccess == "string"
    assert data.OrganizeSelectedMovies == "string"
    assert data.Original == "string"
    assert data.Other == "string"
    assert data.OutputFormatHelpText == "string"
    assert data.OutputPath == "string"
    assert data.Overview == "string"
    assert data.OverviewOptions == "string"
    assert data.PackageVersion == "string"
    assert data.PageSize == "string"
    assert data.PageSizeHelpText == "string"
    assert data.Password == "string"
    assert data.PasswordHelpText == "string"
    assert data.PastDays == "string"
    assert data.PastDaysHelpText == "string"
    assert data.Path == "string"
    assert data.PathHelpText == "string"
    assert data.PathHelpTextWarning == "string"
    assert data.Paused == "string"
    assert data.Peers == "string"
    assert data.Pending == "string"
    assert data.PendingChangesDiscardChanges == "string"
    assert data.PendingChangesMessage == "string"
    assert data.PendingChangesStayReview == "string"
    assert data.Permissions == "string"
    assert data.PhysicalRelease == "string"
    assert data.PhysicalReleaseDate == "string"
    assert data.Port == "string"
    assert data.PortHelpText == "string"
    assert data.PortHelpTextWarning == "string"
    assert data.PortNumber == "string"
    assert data.PosterOptions == "string"
    assert data.Posters == "string"
    assert data.PosterSize == "string"
    assert data.PreferAndUpgrade == "string"
    assert data.PreferIndexerFlags == "string"
    assert data.PreferIndexerFlagsHelpText == "string"
    assert data.Preferred == "string"
    assert data.PreferredHelpTexts1 == "string"
    assert data.PreferredHelpTexts2 == "string"
    assert data.PreferredHelpTexts3 == "string"
    assert data.PreferredSize == "string"
    assert data.PreferTorrent == "string"
    assert data.PreferUsenet == "string"
    assert data.Presets == "string"
    assert data.PreviewRename == "string"
    assert data.PreviewRenameHelpText == "string"
    assert data.PreviewRetag == "string"
    assert data.Priority == "string"
    assert data.PriorityHelpText == "string"
    assert data.PrioritySettings == "string"
    assert data.ProcessingFolders == "string"
    assert data.Profiles == "string"
    assert data.ProfilesSettingsSummary == "string"
    assert data.Progress == "string"
    assert data.Proper == "string"
    assert data.PropersAndRepacks == "string"
    assert data.Protocol == "string"
    assert data.ProtocolHelpText == "string"
    assert data.Proxy == "string"
    assert data.ProxyBypassFilterHelpText == "string"
    assert data.ProxyCheckBadRequestMessage == "string"
    assert data.ProxyCheckFailedToTestMessage == "string"
    assert data.ProxyCheckResolveIpMessage == "string"
    assert data.ProxyPasswordHelpText == "string"
    assert data.ProxyType == "string"
    assert data.ProxyUsernameHelpText == "string"
    assert data.PtpOldSettingsCheckMessage == "string"
    assert data.PublishedDate == "string"
    assert data.Publisher == "string"
    assert data.Qualities == "string"
    assert data.QualitiesHelpText == "string"
    assert data.Quality == "string"
    assert data.QualityCutoffHasNotBeenMet == "string"
    assert data.QualityDefinitions == "string"
    assert data.QualityLimitsHelpText == "string"
    assert data.QualityOrLangCutoffHasNotBeenMet == "string"
    assert data.QualityProfile == "string"
    assert data.QualityProfileDeleteConfirm == "string"
    assert data.QualityProfileIdHelpText == "string"
    assert data.QualityProfileInUse == "string"
    assert data.QualityProfiles == "string"
    assert data.QualitySettings == "string"
    assert data.QualitySettingsSummary == "string"
    assert data.Queue == "string"
    assert data.Queued == "string"
    assert data.QueueIsEmpty == "string"
    assert data.QuickImport == "string"
    assert data.RadarrCalendarFeed == "string"
    assert data.RadarrSupportsAnyDownloadClient == "string"
    assert data.RadarrSupportsAnyIndexer == "string"
    assert data.RadarrSupportsAnyRSSMovieListsAsWellAsTheOneStatedBelow == "string"
    assert (
        data.RadarrSupportsCustomConditionsAgainstTheReleasePropertiesBelow == "string"
    )
    assert data.RadarrTags == "string"
    assert data.RadarrUpdated == "string"
    assert data.Ratings == "string"
    assert (
        data.ReadarrSupportsAnyDownloadClientThatUsesTheNewznabStandardAsWellAsOtherDownloadClientsListedBelow
        == "string"
    )
    assert (
        data.ReadarrSupportsAnyIndexerThatUsesTheNewznabStandardAsWellAsOtherIndexersListedBelow
        == "string"
    )
    assert (
        data.ReadarrSupportsMultipleListsForImportingBooksAndAuthorsIntoTheDatabase
        == "string"
    )
    assert data.ReadarrTags == "string"
    assert data.ReadTheWikiForMoreInformation == "string"
    assert data.Real == "string"
    assert data.Reason == "string"
    assert data.RecentChanges == "string"
    assert data.RecentFolders == "string"
    assert data.RecycleBinCleanupDaysHelpText == "string"
    assert data.RecycleBinCleanupDaysHelpTextWarning == "string"
    assert data.RecycleBinHelpText == "string"
    assert data.RecyclingBin == "string"
    assert data.RecyclingBinCleanup == "string"
    assert data.Reddit == "string"
    assert data.Redownload == "string"
    assert data.Refresh == "string"
    assert data.RefreshAndScan == "string"
    assert data.RefreshAuthor == "string"
    assert data.RefreshInformation == "string"
    assert data.RefreshInformationAndScanDisk == "string"
    assert data.RefreshLists == "string"
    assert data.RefreshMovie == "string"
    assert data.RefreshScan == "string"
    assert data.RegularExpressionsCanBeTested == "string"
    assert data.RejectionCount == "string"
    assert data.RelativePath == "string"
    assert data.ReleaseBranchCheckOfficialBranchMessage == "string"
    assert data.Released == "string"
    assert data.ReleaseDate == "string"
    assert data.ReleaseDates == "string"
    assert data.ReleasedMsg == "string"
    assert data.ReleaseGroup == "string"
    assert data.ReleaseProfiles == "string"
    assert data.ReleaseRejected == "string"
    assert data.ReleaseStatus == "string"
    assert data.ReleaseTitle == "string"
    assert data.ReleaseWillBeProcessedInterp == "string"
    assert data.Reload == "string"
    assert data.RemotePath == "string"
    assert data.RemotePathHelpText == "string"
    assert data.RemotePathMappingCheckBadDockerPath == "string"
    assert data.RemotePathMappingCheckDockerFolderMissing == "string"
    assert data.RemotePathMappingCheckDownloadPermissions == "string"
    assert data.RemotePathMappingCheckFileRemoved == "string"
    assert data.RemotePathMappingCheckFilesBadDockerPath == "string"
    assert data.RemotePathMappingCheckFilesGenericPermissions == "string"
    assert data.RemotePathMappingCheckFilesLocalWrongOSPath == "string"
    assert data.RemotePathMappingCheckFilesWrongOSPath == "string"
    assert data.RemotePathMappingCheckFolderPermissions == "string"
    assert data.RemotePathMappingCheckGenericPermissions == "string"
    assert data.RemotePathMappingCheckImportFailed == "string"
    assert data.RemotePathMappingCheckLocalFolderMissing == "string"
    assert data.RemotePathMappingCheckLocalWrongOSPath == "string"
    assert data.RemotePathMappingCheckRemoteDownloadClient == "string"
    assert data.RemotePathMappingCheckWrongOSPath == "string"
    assert data.RemotePathMappings == "string"
    assert data.Remove == "string"
    assert data.RemoveCompleted == "string"
    assert data.RemoveCompletedDownloadsHelpText == "string"
    assert data.RemovedFromTaskQueue == "string"
    assert data.RemovedMovieCheckMultipleMessage == "string"
    assert data.RemovedMovieCheckSingleMessage == "string"
    assert data.RemoveDownloadsAlert == "string"
    assert data.RemoveFailed == "string"
    assert data.RemoveFailedDownloadsHelpText == "string"
    assert data.RemoveFilter == "string"
    assert data.RemoveFromBlocklist == "string"
    assert data.RemoveFromDownloadClient == "string"
    assert data.RemoveFromQueue == "string"
    assert data.RemoveFromQueueText == "string"
    assert data.RemoveHelpTextWarning == "string"
    assert data.RemoveMovieAndDeleteFiles == "string"
    assert data.RemoveMovieAndKeepFiles == "string"
    assert data.RemoveRootFolder == "string"
    assert data.RemoveSelected == "string"
    assert data.RemoveSelectedItem == "string"
    assert data.RemoveSelectedItems == "string"
    assert data.RemoveSelectedMessageText == "string"
    assert data.RemoveTagExistingTag == "string"
    assert data.RemoveTagRemovingTag == "string"
    assert data.RemovingTag == "string"
    assert data.RenameBooks == "string"
    assert data.RenameBooksHelpText == "string"
    assert data.Renamed == "string"
    assert data.RenameFiles == "string"
    assert data.RenameMovies == "string"
    assert data.RenameMoviesHelpText == "string"
    assert data.Reorder == "string"
    assert data.Replace == "string"
    assert data.ReplaceIllegalCharacters == "string"
    assert data.ReplaceIllegalCharactersHelpText == "string"
    assert data.ReplaceWithDash == "string"
    assert data.ReplaceWithSpaceDash == "string"
    assert data.ReplaceWithSpaceDashSpace == "string"
    assert data.Required == "string"
    assert data.RequiredHelpText == "string"
    assert data.RequiredPlaceHolder == "string"
    assert data.RequiredRestrictionHelpText == "string"
    assert data.RequiredRestrictionPlaceHolder == "string"
    assert data.RescanAfterRefreshHelpText == "string"
    assert data.RescanAfterRefreshHelpTextWarning == "string"
    assert data.RescanAuthorFolderAfterRefresh == "string"
    assert data.RescanMovieFolderAfterRefresh == "string"
    assert data.Reset == "string"
    assert data.ResetAPIKey == "string"
    assert data.ResetAPIKeyMessageText == "string"
    assert data.Restart == "string"
    assert data.RestartNow == "string"
    assert data.RestartRadarr == "string"
    assert data.RestartReadarr == "string"
    assert data.RestartReloadNote == "string"
    assert data.RestartRequiredHelpTextWarning == "string"
    assert data.Restore == "string"
    assert data.RestoreBackup == "string"
    assert data.Restrictions == "string"
    assert data.Result == "string"
    assert data.Retention == "string"
    assert data.RetentionHelpText == "string"
    assert data.RetryingDownloadInterp == "string"
    assert data.RootFolder == "string"
    assert data.RootFolderCheckMultipleMessage == "string"
    assert data.RootFolderCheckSingleMessage == "string"
    assert data.RootFolderPathHelpText == "string"
    assert data.RootFolders == "string"
    assert data.RSS == "string"
    assert data.RSSIsNotSupportedWithThisIndexer == "string"
    assert data.RSSSync == "string"
    assert data.RSSSyncInterval == "string"
    assert data.RssSyncIntervalHelpText == "string"
    assert data.RSSSyncIntervalHelpTextWarning == "string"
    assert data.Runtime == "string"
    assert data.Save == "string"
    assert data.SaveChanges == "string"
    assert data.SaveSettings == "string"
    assert data.SceneInformation == "string"
    assert data.SceneNumberHasntBeenVerifiedYet == "string"
    assert data.Scheduled == "string"
    assert data.Score == "string"
    assert data.Script == "string"
    assert data.ScriptPath == "string"
    assert data.Search == "string"
    assert data.SearchAll == "string"
    assert data.SearchBook == "string"
    assert data.SearchBoxPlaceHolder == "string"
    assert data.SearchCutoffUnmet == "string"
    assert data.SearchFailedPleaseTryAgainLater == "string"
    assert data.SearchFiltered == "string"
    assert data.SearchForAllCutoffUnmetBooks == "string"
    assert data.SearchForAllMissingBooks == "string"
    assert data.SearchForMissing == "string"
    assert data.SearchForMonitoredBooks == "string"
    assert data.SearchForMovie == "string"
    assert data.SearchForNewItems == "string"
    assert data.SearchMissing == "string"
    assert data.SearchMonitored == "string"
    assert data.SearchMovie == "string"
    assert data.SearchOnAdd == "string"
    assert data.SearchOnAddHelpText == "string"
    assert data.SearchSelected == "string"
    assert data.Season == "string"
    assert data.Seconds == "string"
    assert data.Security == "string"
    assert data.Seeders == "string"
    assert data.SelectAll == "string"
    assert data.SelectDotDot == "string"
    assert data.SelectedCountAuthorsSelectedInterp == "string"
    assert data.SelectedCountBooksSelectedInterp == "string"
    assert data.SelectFolder == "string"
    assert data.SelectLanguage == "string"
    assert data.SelectLanguages == "string"
    assert data.SelectMovie == "string"
    assert data.SelectQuality == "string"
    assert data.SelectReleaseGroup == "string"
    assert data.SendAnonymousUsageData == "string"
    assert data.SendMetadataToCalibre == "string"
    assert data.Series == "string"
    assert data.SeriesNumber == "string"
    assert data.SeriesTotal == "string"
    assert data.SetPermissions == "string"
    assert data.SetPermissionsLinuxHelpText == "string"
    assert data.SetPermissionsLinuxHelpTextWarning == "string"
    assert data.SetReleaseGroup == "string"
    assert data.SetTags == "string"
    assert data.Settings == "string"
    assert data.SettingsEnableColorImpairedMode == "string"
    assert data.SettingsEnableColorImpairedModeHelpText == "string"
    assert data.SettingsFirstDayOfWeek == "string"
    assert data.SettingsLongDateFormat == "string"
    assert data.SettingsRemotePathMappingHostHelpText == "string"
    assert data.SettingsRemotePathMappingLocalPath == "string"
    assert data.SettingsRemotePathMappingLocalPathHelpText == "string"
    assert data.SettingsRemotePathMappingRemotePath == "string"
    assert data.SettingsRemotePathMappingRemotePathHelpText == "string"
    assert data.SettingsRuntimeFormat == "string"
    assert data.SettingsShortDateFormat == "string"
    assert data.SettingsShowRelativeDates == "string"
    assert data.SettingsShowRelativeDatesHelpText == "string"
    assert data.SettingsTimeFormat == "string"
    assert data.SettingsWeekColumnHeader == "string"
    assert data.SettingsWeekColumnHeaderHelpText == "string"
    assert data.ShortDateFormat == "string"
    assert data.ShouldMonitorExisting == "string"
    assert data.ShouldMonitorExistingHelpText == "string"
    assert data.ShouldMonitorHelpText == "string"
    assert data.ShouldSearchHelpText == "string"
    assert data.ShowAdvanced == "string"
    assert data.ShowAsAllDayEvents == "string"
    assert data.ShowBanners == "string"
    assert data.ShowBannersHelpText == "string"
    assert data.ShowBookCount == "string"
    assert data.ShowBookTitleHelpText == "string"
    assert data.ShowCertification == "string"
    assert data.ShowCinemaRelease == "string"
    assert data.showCinemaReleaseHelpText == "string"
    assert data.ShowCutoffUnmetIconHelpText == "string"
    assert data.ShowDateAdded == "string"
    assert data.ShowGenres == "string"
    assert data.ShowLastBook == "string"
    assert data.ShowMonitored == "string"
    assert data.ShowMonitoredHelpText == "string"
    assert data.ShowMovieInformation == "string"
    assert data.ShowMovieInformationHelpText == "string"
    assert data.ShownAboveEachColumnWhenWeekIsTheActiveView == "string"
    assert data.ShowName == "string"
    assert data.ShownClickToHide == "string"
    assert data.ShowPath == "string"
    assert data.ShowQualityProfile == "string"
    assert data.ShowQualityProfileHelpText == "string"
    assert data.ShowRatings == "string"
    assert data.ShowRelativeDates == "string"
    assert data.ShowRelativeDatesHelpText == "string"
    assert data.ShowReleaseDate == "string"
    assert data.ShowReleaseDateHelpText == "string"
    assert data.ShowSearch == "string"
    assert data.ShowSearchActionHelpText == "string"
    assert data.ShowSearchHelpText == "string"
    assert data.ShowSizeOnDisk == "string"
    assert data.ShowStudio == "string"
    assert data.ShowTitle == "string"
    assert data.ShowTitleHelpText == "string"
    assert data.ShowUnknownAuthorItems == "string"
    assert data.ShowUnknownMovieItems == "string"
    assert data.ShowYear == "string"
    assert data.Shutdown == "string"
    assert data.Size == "string"
    assert data.SizeLimit == "string"
    assert data.SizeOnDisk == "string"
    assert data.SkipBooksWithMissingReleaseDate == "string"
    assert data.SkipBooksWithNoISBNOrASIN == "string"
    assert data.SkipFreeSpaceCheck == "string"
    assert data.SkipFreeSpaceCheckWhenImportingHelpText == "string"
    assert data.SkipPartBooksAndSets == "string"
    assert data.SkipRedownload == "string"
    assert data.SkipredownloadHelpText == "string"
    assert data.SkipSecondarySeriesBooks == "string"
    assert data.Small == "string"
    assert data.Socks4 == "string"
    assert data.Socks5 == "string"
    assert data.SomeResultsHiddenFilter == "string"
    assert data.SorryThatAuthorCannotBeFound == "string"
    assert data.SorryThatBookCannotBeFound == "string"
    assert data.SorryThatMovieCannotBeFound == "string"
    assert data.Sort == "string"
    assert data.Source == "string"
    assert data.SourcePath == "string"
    assert data.SourceRelativePath == "string"
    assert data.SourceTitle == "string"
    assert data.SpecificBook == "string"
    assert data.SqliteVersionCheckUpgradeRequiredMessage == "string"
    assert data.SSLCertPassword == "string"
    assert data.SslCertPasswordHelpText == "string"
    assert data.SSLCertPasswordHelpText == "string"
    assert data.SslCertPasswordHelpTextWarning == "string"
    assert data.SSLCertPath == "string"
    assert data.SslCertPathHelpText == "string"
    assert data.SSLCertPathHelpText == "string"
    assert data.SslCertPathHelpTextWarning == "string"
    assert data.SSLPort == "string"
    assert data.SslPortHelpTextWarning == "string"
    assert data.StandardBookFormat == "string"
    assert data.StandardMovieFormat == "string"
    assert data.StartImport == "string"
    assert data.StartProcessing == "string"
    assert data.StartSearchForMissingMovie == "string"
    assert data.StartTypingOrSelectAPathBelow == "string"
    assert data.StartupDirectory == "string"
    assert data.Status == "string"
    assert data.StatusEndedContinuing == "string"
    assert data.StatusEndedDeceased == "string"
    assert data.StatusEndedEnded == "string"
    assert data.Studio == "string"
    assert data.Style == "string"
    assert data.SubfolderWillBeCreatedAutomaticallyInterp == "string"
    assert data.SuccessMyWorkIsDoneNoFilesToRename == "string"
    assert data.SuccessMyWorkIsDoneNoFilesToRetag == "string"
    assert data.SuggestTranslationChange == "string"
    assert data.Sunday == "string"
    assert data.SupportsRssvalueRSSIsNotSupportedWithThisIndexer == "string"
    assert data.SupportsSearchvalueSearchIsNotSupportedWithThisIndexer == "string"
    assert (
        data.SupportsSearchvalueWillBeUsedWhenAutomaticSearchesArePerformedViaTheUIOrByReadarr
        == "string"
    )
    assert data.SupportsSearchvalueWillBeUsedWhenInteractiveSearchIsUsed == "string"
    assert data.System == "string"
    assert data.SystemTimeCheckMessage == "string"
    assert data.Table == "string"
    assert data.TableOptions == "string"
    assert data.TableOptionsColumnsMessage == "string"
    assert data.TagCannotBeDeletedWhileInUse == "string"
    assert data.TagDetails == "string"
    assert data.TagIsNotUsedAndCanBeDeleted == "string"
    assert data.Tags == "string"
    assert data.TagsHelpText == "string"
    assert data.TagsSettingsSummary == "string"
    assert data.Tasks == "string"
    assert data.TaskUserAgentTooltip == "string"
    assert data.TBA == "string"
    assert data.Term == "string"
    assert data.Test == "string"
    assert data.TestAll == "string"
    assert data.TestAllClients == "string"
    assert data.TestAllIndexers == "string"
    assert data.TestAllLists == "string"
    assert data.TheAuthorFolderAndAllOfItsContentWillBeDeleted == "string"
    assert data.TheBooksFilesWillBeDeleted == "string"
    assert data.TheFollowingFilesWillBeDeleted == "string"
    assert data.TheLogLevelDefault == "string"
    assert data.ThisCannotBeCancelled == "string"
    assert data.ThisConditionMatchesUsingRegularExpressions == "string"
    assert data.ThisWillApplyToAllIndexersPleaseFollowTheRulesSetForthByThem == "string"
    assert data.Time == "string"
    assert data.TimeFormat == "string"
    assert data.Timeleft == "string"
    assert data.Title == "string"
    assert data.Titles == "string"
    assert data.TMDb == "string"
    assert data.TMDBId == "string"
    assert data.TmdbIdHelpText == "string"
    assert data.TmdbRating == "string"
    assert data.TmdbVotes == "string"
    assert data.Today == "string"
    assert data.Tomorrow == "string"
    assert data.TooManyBooks == "string"
    assert data.TorrentDelay == "string"
    assert data.TorrentDelayHelpText == "string"
    assert data.TorrentDelayTime == "string"
    assert data.Torrents == "string"
    assert data.TorrentsDisabled == "string"
    assert data.TotalBookCountBooksTotalBookFileCountBooksWithFilesInterp == "string"
    assert data.TotalFileSize == "string"
    assert data.TotalSpace == "string"
    assert data.Trace == "string"
    assert data.TrackNumber == "string"
    assert data.TrackTitle == "string"
    assert data.Trailer == "string"
    assert data.Trakt == "string"
    assert data.Trigger == "string"
    assert data.Type == "string"
    assert data.UI == "string"
    assert data.UILanguage == "string"
    assert data.UILanguageHelpText == "string"
    assert data.UILanguageHelpTextWarning == "string"
    assert data.UISettings == "string"
    assert data.UISettingsSummary == "string"
    assert data.UnableToAddANewConditionPleaseTryAgain == "string"
    assert data.UnableToAddANewCustomFormatPleaseTryAgain == "string"
    assert data.UnableToAddANewDownloadClientPleaseTryAgain == "string"
    assert data.UnableToAddANewImportListExclusionPleaseTryAgain == "string"
    assert data.UnableToAddANewIndexerPleaseTryAgain == "string"
    assert data.UnableToAddANewListExclusionPleaseTryAgain == "string"
    assert data.UnableToAddANewListPleaseTryAgain == "string"
    assert data.UnableToAddANewMetadataProfilePleaseTryAgain == "string"
    assert data.UnableToAddANewNotificationPleaseTryAgain == "string"
    assert data.UnableToAddANewQualityProfilePleaseTryAgain == "string"
    assert data.UnableToAddANewRemotePathMappingPleaseTryAgain == "string"
    assert data.UnableToAddANewRootFolderPleaseTryAgain == "string"
    assert data.UnableToAddRootFolder == "string"
    assert data.UnableToImportCheckLogs == "string"
    assert data.UnableToLoadAltTitle == "string"
    assert data.UnableToLoadBackups == "string"
    assert data.UnableToLoadBlocklist == "string"
    assert data.UnableToLoadCustomFormats == "string"
    assert data.UnableToLoadDelayProfiles == "string"
    assert data.UnableToLoadDownloadClientOptions == "string"
    assert data.UnableToLoadDownloadClients == "string"
    assert data.UnableToLoadGeneralSettings == "string"
    assert data.UnableToLoadHistory == "string"
    assert data.UnableToLoadImportListExclusions == "string"
    assert data.UnableToLoadIndexerOptions == "string"
    assert data.UnableToLoadIndexers == "string"
    assert data.UnableToLoadLanguages == "string"
    assert data.UnableToLoadListExclusions == "string"
    assert data.UnableToLoadListOptions == "string"
    assert data.UnableToLoadLists == "string"
    assert data.UnableToLoadManualImportItems == "string"
    assert data.UnableToLoadMediaManagementSettings == "string"
    assert data.UnableToLoadMetadata == "string"
    assert data.UnableToLoadMetadataProfiles == "string"
    assert data.UnableToLoadMetadataProviderSettings == "string"
    assert data.UnableToLoadMovies == "string"
    assert data.UnableToLoadNamingSettings == "string"
    assert data.UnableToLoadNotifications == "string"
    assert data.UnableToLoadQualities == "string"
    assert data.UnableToLoadQualityDefinitions == "string"
    assert data.UnableToLoadQualityProfiles == "string"
    assert data.UnableToLoadReleaseProfiles == "string"
    assert data.UnableToLoadRemotePathMappings == "string"
    assert data.UnableToLoadRestrictions == "string"
    assert data.UnableToLoadResultsIntSearch == "string"
    assert data.UnableToLoadRootFolders == "string"
    assert data.UnableToLoadTags == "string"
    assert data.UnableToLoadTheCalendar == "string"
    assert data.UnableToLoadUISettings == "string"
    assert data.UnableToUpdateRadarrDirectly == "string"
    assert data.Unavailable == "string"
    assert data.Ungroup == "string"
    assert data.Unlimited == "string"
    assert data.UnmappedFiles == "string"
    assert data.UnmappedFilesOnly == "string"
    assert data.UnmappedFolders == "string"
    assert data.Unmonitored == "string"
    assert data.UnmonitoredHelpText == "string"
    assert data.Unreleased == "string"
    assert data.UnsavedChanges == "string"
    assert data.UnselectAll == "string"
    assert data.UpdateAll == "string"
    assert data.UpdateAutomaticallyHelpText == "string"
    assert data.UpdateAvailable == "string"
    assert data.UpdateCheckStartupNotWritableMessage == "string"
    assert data.UpdateCheckStartupTranslocationMessage == "string"
    assert data.UpdateCheckUINotWritableMessage == "string"
    assert data.UpdateCovers == "string"
    assert data.UpdateCoversHelpText == "string"
    assert data.UpdateMechanismHelpText == "string"
    assert data.Updates == "string"
    assert data.UpdateScriptPathHelpText == "string"
    assert data.UpdateSelected == "string"
    assert (
        data.UpdatingIsDisabledInsideADockerContainerUpdateTheContainerImageInstead
        == "string"
    )
    assert data.UpgradeAllowedHelpText == "string"
    assert data.UpgradesAllowed == "string"
    assert data.UpgradeUntilCustomFormatScore == "string"
    assert data.UpgradeUntilQuality == "string"
    assert data.UpgradeUntilThisQualityIsMetOrExceeded == "string"
    assert data.UpperCase == "string"
    assert data.Uptime == "string"
    assert data.URLBase == "string"
    assert data.UrlBaseHelpText == "string"
    assert data.UrlBaseHelpTextWarning == "string"
    assert data.UseCalibreContentServer == "string"
    assert data.UseHardlinksInsteadOfCopy == "string"
    assert data.Usenet == "string"
    assert data.UsenetDelay == "string"
    assert data.UsenetDelayHelpText == "string"
    assert data.UsenetDelayTime == "string"
    assert data.UsenetDisabled == "string"
    assert data.UseProxy == "string"
    assert data.Username == "string"
    assert data.UsernameHelpText == "string"
    assert data.UseSSL == "string"
    assert data.UseSslHelpText == "string"
    assert data.UsingExternalUpdateMechanismBranchToUseToUpdateReadarr == "string"
    assert (
        data.UsingExternalUpdateMechanismBranchUsedByExternalUpdateMechanism == "string"
    )
    assert data.Version == "string"
    assert data.VersionUpdateText == "string"
    assert data.VideoCodec == "string"
    assert data.View == "string"
    assert data.VisitGithubCustomFormatsAphrodite == "string"
    assert data.WaitingToImport == "string"
    assert data.WaitingToProcess == "string"
    assert data.Wanted == "string"
    assert data.Warn == "string"
    assert data.WatchLibraryForChangesHelpText == "string"
    assert data.WatchRootFoldersForFileChanges == "string"
    assert data.Week == "string"
    assert data.WeekColumnHeader == "string"
    assert data.Weeks == "string"
    assert data.WhatsNew == "string"
    assert data.WhitelistedHardcodedSubsHelpText == "string"
    assert data.WhitelistedSubtitleTags == "string"
    assert data.Wiki == "string"
    assert data.WouldYouLikeToRestoreBackup == "string"
    assert data.WriteAudioTags == "string"
    assert data.WriteAudioTagsScrub == "string"
    assert data.WriteAudioTagsScrubHelp == "string"
    assert data.WriteBookTagsHelpTextWarning == "string"
    assert data.WriteTagsAll == "string"
    assert data.WriteTagsNew == "string"
    assert data.WriteTagsNo == "string"
    assert data.WriteTagsSync == "string"
    assert data.Year == "string"
    assert data.Yes == "string"
    assert data.YesCancel == "string"
    assert data.YesMoveFiles == "string"
    assert data.Yesterday == "string"
    assert data.YouCanAlsoSearch == "string"

    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )

    with pytest.raises(NotImplementedError):
        await client.async_get_localization()


@pytest.mark.asyncio
async def test_async_get_image(aresponses):
    """Test getting image."""
    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/mediacover/0/poster-250.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(imageid=0, size="small")

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/mediacover/0/poster-500.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(imageid=0, size="medium")

    aresponses.add(
        "127.0.0.1:8989",
        f"/api/{SONARR_API}/mediacover/0/poster.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = SonarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(imageid=0)


@pytest.mark.asyncio
async def test_async_get_author_image(aresponses):
    """Test getting author image."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/author/0/poster-250.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0, size="small", author=True)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/author/0/poster-500.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0, size="medium", author=True)

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/author/0/poster.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0, author=True)


@pytest.mark.asyncio
async def test_async_get_book_image(aresponses):
    """Test getting book image."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/book/0/poster-250.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0, size="small")

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/book/0/poster-500.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0, size="medium")

    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/mediacover/book/0/poster.jpg?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        await client.async_get_image(0)


@pytest.mark.asyncio
async def test_async_get_media_management_configs(aresponses):
    """Test getting media management configs."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/config/mediamanagement?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/config-mediamanagement.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_media_management_configs()

    assert data.allowFingerprinting == "newFiles"
    assert data.autoRenameFolders is True
    assert data.autoUnmonitorPreviouslyDownloadedBooks is False
    assert data.autoUnmonitorPreviouslyDownloadedEpisodes is False
    assert data.autoUnmonitorPreviouslyDownloadedMovies is False
    assert data.chmodFolder == "002"
    assert data.chownGroup == ""
    assert data.copyUsingHardlinks is False
    assert data.createEmptyAuthorFolders is False
    assert data.createEmptyMovieFolders is False
    assert data.createEmptySeriesFolders is False
    assert data.deleteEmptyFolders is False
    assert data.downloadPropersAndRepacks == "preferAndUpgrade"
    assert data.enableMediaInfo is True
    assert data.episodeTitleRequired == "always"
    assert data.extraFileExtensions == "srt,mp4,avi,mkv"
    assert data.fileDate == "string"
    assert data.id == 1
    assert data.importExtraFiles is True
    assert data.minimumFreeSpaceWhenImporting == 100
    assert data.pathsDefaultStatic is False
    assert data.recycleBin == "/recycle/"
    assert data.recycleBinCleanupDays == 7
    assert data.rescanAfterRefresh == "afterManual"
    assert data.setPermissionsLinux is False
    assert data.skipFreeSpaceCheckWhenImporting is False
    assert data.watchLibraryForChanges is True


@pytest.mark.asyncio
async def test_async_get_metadata_config(aresponses):
    """Test getting metadata config."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/metadata?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/metadata.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[MetadataConfig] = await client.async_get_metadata_configs()

    assert data[0].enable is True
    assert data[0].name == "string"
    assert data[0].fields[0].order == 0
    assert data[0].fields[0].name == "string"
    assert data[0].fields[0].label == "string"
    assert data[0].fields[0].helpText == "string"
    assert data[0].fields[0].value == "string"
    assert data[0].fields[0].type == "string"
    assert data[0].fields[0].advanced is True
    assert data[0].fields[0].section == "metadata"
    assert data[0].implementationName == "string"
    assert data[0].implementation == "string"
    assert data[0].configContract == "string"
    assert data[0].infoLink == "string"
    assert data[0].tags == [0]
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_quality_definitions(aresponses):
    """Test getting quality definitions."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/qualitydefinition?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/qualitydefinition.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_quality_definitions()
    assert data.quality.id == 0
    assert data.quality.name == "string"
    assert data.quality.source == "string"
    assert data.quality.resolution == 0
    assert data.quality.modifier == "string"
    assert data.title == "string"
    assert data.weight == 0
    assert data.minSize == 0
    assert data.maxSize == 0.0
    assert data.preferredSize == 0
    assert data.id == 0


@pytest.mark.asyncio
async def test_async_get_quality_profiles(aresponses):
    """Test getting quality profiles."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/qualityprofile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/qualityprofile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_quality_profiles()

    assert data[0].name == "string"
    assert data[0].upgradeAllowed is True
    assert data[0].cutoff == 0
    assert data[0].items[0].quality.id == 0
    assert data[0].items[0].quality.name == "string"
    assert data[0].items[0].quality.source == "string"
    assert data[0].items[0].quality.resolution == 0
    assert data[0].items[0].quality.modifier == "string"
    assert data[0].items[0].items == []
    assert data[0].items[0].allowed is False
    assert data[0].items[1].name == "string"
    assert data[0].items[1].items[0].quality.id == 0
    assert data[0].items[1].items[0].quality.name == "string"
    assert data[0].items[1].items[0].quality.source == "string"
    assert data[0].items[1].items[0].quality.resolution == 0
    assert data[0].items[1].items[0].quality.modifier == "string"
    assert data[0].items[1].items[0].items == []
    assert data[0].items[1].items[0].allowed is True
    assert data[0].items[1].allowed is True
    assert data[0].items[1].id == 0
    assert data[0].minFormatScore == 0
    assert data[0].cutoffFormatScore == 0
    assert data[0].formatItems == []
    assert data[0].language.id == 0
    assert data[0].language.name == "string"
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_queue_status(aresponses):
    """Test getting queue status."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/queue/status?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/queue-status.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: QueueStatus = await client.async_get_queue_status()
    assert data.totalCount == 0
    assert data.count == 0
    assert data.unknownCount == 0
    assert data.errors is True
    assert data.warnings is True
    assert data.unknownErrors is True
    assert data.unknownWarnings is True


@pytest.mark.asyncio
async def test_async_get_release_profiles(aresponses):
    """Test getting release profiles."""
    aresponses.add(
        "127.0.0.1:8787",
        f"/api/{READARR_API}/releaseprofile?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/releaseprofile.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = ReadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_release_profiles()
    assert data[0].enabled is True
    assert data[0].required == "string"
    assert data[0].ignored == "string"
    assert data[0].preferred[0].key == "string"
    assert data[0].preferred[0].value == 0
    assert data[0].includePreferredWhenRenaming is False
    assert data[0].indexerId == 0
    assert data[0].tags == [0]
    assert data[0].id == 0

    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )

    with pytest.raises(NotImplementedError):
        await client.async_get_release_profiles()


@pytest.mark.asyncio
async def test_async_get_remote_path_mappings(aresponses):
    """Test getting remote path mappings."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/remotepathmapping?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/remotepathmapping.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_remote_path_mappings()

    assert data[0].host == "localhost"
    assert data[0].remotePath == "C:\\"
    assert data[0].localPath == "A:\\Movies\\"
    assert data[0].id == 1


@pytest.mark.asyncio
async def test_async_get_system_tasks(aresponses):
    """Test getting system tasks."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/system/task?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/system-task.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data = await client.async_get_system_tasks()

    assert data[0].name == "string"
    assert data[0].taskName == "string"
    assert data[0].interval == 0
    assert data[0].lastExecution == datetime(2020, 2, 8, 14, 24, 40, 993044)
    assert data[0].lastStartTime == datetime(2020, 2, 8, 14, 24, 40, 993044)
    assert data[0].nextExecution == datetime(2020, 2, 8, 20, 24, 40, 993044)
    assert data[0].lastDuration == "00:00:00.1976902"
    assert data[0].id == 0


@pytest.mark.asyncio
async def test_async_get_software_update_info(aresponses):
    """Test getting software update info."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/api/{RADARR_API}/update?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/update.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession() as session:
        client = RadarrClient(
            session=session, host_configuration=TEST_HOST_CONFIGURATION
        )
        data: list[Update] = await client.async_get_software_update_info()

    assert data[0].version == "string"
    assert data[0].branch == "string"
    assert data[0].releaseDate == datetime(2020, 9, 2, 5, 36, 13, 47313)
    assert data[0].fileName == "string"
    assert data[0].url == "string"
    assert data[0].installed is False
    assert data[0].installedOn == datetime(2020, 10, 1, 5, 1, 4, 521117)
    assert data[0].installable is False
    assert data[0].latest is False
    assert data[0].changes.new == ["string"]
    assert data[0].changes.fixed == ["string"]
    assert data[0].hash == "string"
