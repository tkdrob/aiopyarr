"""Tests for host configuration."""
# pylint:disable=protected-access
from aiohttp.client import ClientSession
import pytest

from aiopyarr.const import HEADERS
from aiopyarr.exceptions import ArrException
from aiopyarr.models.host_configuration import PyArrHostConfiguration
from aiopyarr.radarr_client import RadarrClient

from . import API_TOKEN, RADARR_API, load_fixture


@pytest.mark.asyncio
async def test_host_configuration(aresponses) -> None:
    """Test host configuration."""
    aresponses.add(
        "127.0.0.1:7000",
        "/api/v4/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    host_config = PyArrHostConfiguration(
        api_token=API_TOKEN, ipaddress="127.0.0.1", port=7000
    )
    async with ClientSession():
        client = RadarrClient(
            host_configuration=host_config,
            raw_response=True,
            api_ver="v4",
        )
        data = await client.async_get_system_status()
    assert client._host.api_token == API_TOKEN
    assert client._host.hostname is None
    assert client._host.ipaddress == "127.0.0.1"
    assert client._host.port == 7000
    assert client._host.ssl is False
    assert client._host.verify_ssl is True
    assert client._host.base_api_path is None
    assert client._host.url is None
    assert client._host.base_url == "http://127.0.0.1:7000"
    assert client._host.api_ver == "v4"
    url = client._host.api_url("test")
    assert url == "http://127.0.0.1:7000/api/v4/test"
    assert HEADERS["X-Api-Key"] == API_TOKEN

    assert data[0]["freeSpace"]
    assert data[0]["label"]
    assert data[0]["path"]
    assert data[0]["totalSpace"]


@pytest.mark.asyncio
async def test_host_configuration_with_hostname(aresponses) -> None:
    """Test host configuration with hostname."""
    aresponses.add(
        "localhost:7000",
        f"/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    host_config = PyArrHostConfiguration(
        api_token=API_TOKEN, hostname="localhost", ipaddress="127.0.0.1", port=7000
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=host_config)
        await client.async_get_system_status()
    assert client._host.api_token == API_TOKEN
    assert client._host.hostname == "localhost"
    assert client._host.ipaddress == "127.0.0.1"
    assert client._host.port == 7000
    assert client._host.ssl is False
    assert client._host.verify_ssl is True
    assert client._host.base_api_path is None
    assert client._host.url is None
    assert client._host.base_url == "http://localhost:7000"
    assert client._host.api_ver == RADARR_API
    url = client._host.api_url("test")
    assert url == "http://localhost:7000/api/v3/test"
    assert HEADERS["X-Api-Key"] == API_TOKEN


@pytest.mark.asyncio
async def test_host_configuration_with_url(aresponses) -> None:
    """Test host configuration with url."""
    aresponses.add(
        "localhost:7878",
        f"/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    host_config = PyArrHostConfiguration(
        api_token=API_TOKEN,
        ipaddress="127.0.0.1",
        port=7000,
        ssl=True,
        verify_ssl=False,
        url="http://localhost:7878",
    )
    async with ClientSession():
        client = RadarrClient(host_configuration=host_config)
        await client.async_get_system_status()
    assert client._host.api_token == API_TOKEN
    assert client._host.hostname is None
    assert client._host.ipaddress == "127.0.0.1"
    assert client._host.port == 7000
    assert client._host.ssl is True
    assert client._host.verify_ssl is False
    assert client._host.base_api_path is None
    assert client._host.url == "http://localhost:7878"
    assert client._host.base_url == "http://localhost:7878"
    assert client._host.api_ver == RADARR_API
    url = client._host.api_url("test")
    assert url == "http://localhost:7878/api/v3/test"
    assert HEADERS["X-Api-Key"] == API_TOKEN


@pytest.mark.asyncio
async def test_no_host_configuration_given(aresponses) -> None:
    """Test host configuration not given."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/radarr/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(
            api_token=API_TOKEN,
            ipaddress="127.0.0.1",
            ssl=True,
            verify_ssl=False,
            base_api_path="/radarr",
        )
        await client.async_get_system_status()
    assert client._host.api_token == API_TOKEN
    assert client._host.hostname is None
    assert client._host.ipaddress == "127.0.0.1"
    assert client._host.port == 7878
    assert client._host.ssl is True
    assert client._host.verify_ssl is False
    assert client._host.base_api_path == "/radarr"
    assert client._host.base_url == "https://127.0.0.1:7878/radarr"
    assert client._host.url is None
    assert client._host.api_ver == RADARR_API
    assert HEADERS["X-Api-Key"] == API_TOKEN


@pytest.mark.asyncio
async def test_host_configuration_exceptions() -> None:
    """Test host configuration exceptions."""

    with pytest.raises(ArrException):
        PyArrHostConfiguration(ipaddress="127.0.0.1")

    with pytest.raises(ArrException):
        PyArrHostConfiguration(api_token=API_TOKEN)


@pytest.mark.asyncio
async def test_host_configuration_url_no_port(aresponses) -> None:
    """Test host configuration url with no port included."""
    aresponses.add(
        "127.0.0.1:7878",
        f"/radarr/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(
            api_token=API_TOKEN,
            url="http://127.0.0.1/radarr",
            verify_ssl=True,
        )
        await client.async_get_system_status()
    assert client._host.api_token == API_TOKEN
    assert client._host.hostname is None
    assert client._host.ipaddress is None
    assert client._host.port == 7878
    assert client._host.ssl is False
    assert client._host.verify_ssl is True
    assert client._host.base_api_path is None
    assert client._host.url == "http://127.0.0.1:7878/radarr"
    assert client._host.base_url == "http://127.0.0.1:7878/radarr"
    assert client._host.api_ver == RADARR_API
    assert HEADERS["X-Api-Key"] == API_TOKEN

    aresponses.add(
        "localhost:7878",
        f"/radarr/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(
            api_token=API_TOKEN,
            url="http://localhost/radarr",
            verify_ssl=True,
        )
        await client.async_get_system_status()
    assert client._host.url == "http://localhost:7878/radarr"
    assert client._host.base_url == "http://localhost:7878/radarr"

    aresponses.add(
        "127.0.0.1:7878",
        f"/radarr/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(
            api_token=API_TOKEN,
            url="http://127.0.0.1/radarr/",
            verify_ssl=True,
        )
        await client.async_get_system_status()
    assert client._host.url == "http://127.0.0.1:7878/radarr"
    assert client._host.base_url == "http://127.0.0.1:7878/radarr"

    aresponses.add(
        "localhost:7878",
        f"/radarr/api/{RADARR_API}/system/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    async with ClientSession():
        client = RadarrClient(
            api_token=API_TOKEN,
            url="http://localhost/radarr/",
            verify_ssl=True,
        )
        await client.async_get_system_status()
    assert client._host.url == "http://localhost:7878/radarr"
    assert client._host.base_url == "http://localhost:7878/radarr"
