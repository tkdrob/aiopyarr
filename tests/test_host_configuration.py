"""Tests for host configuration."""
import pytest
from aiohttp.client import ClientSession

from aiopyarr.models.host_configuration import PyArrHostConfiguration
from aiopyarr.radarr_client import RadarrClient

from . import RADARR_API, load_fixture


@pytest.mark.asyncio
async def test_host_configuration(aresponses):
    """Test host configuration."""
    aresponses.add(
        "127.0.0.1:7000",
        f"/api/{RADARR_API}/system/status?apikey=ur1234567-0abc12de3f456gh7ij89k012",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("common/diskspace.json"),
        ),
        match_querystring=True,
    )
    HOST_CONFIGURATION = PyArrHostConfiguration(
        api_token="ur1234567-0abc12de3f456gh7ij89k012", ipaddress="127.0.0.1", port=7000
    )
    async with ClientSession() as session:
        client = RadarrClient(session=session, host_configuration=HOST_CONFIGURATION)
        await client.async_get_system_status()
    assert client._host.api_token == "ur1234567-0abc12de3f456gh7ij89k012"
    assert client._host.hostname is None
    assert client._host.ipaddress == "127.0.0.1"
    assert client._host.port == 7000
    assert client._host.ssl is False
    assert client._host.verify_ssl is True
    assert client._host.base_api_path is None
    assert client._host.url is None
    assert client._host.api_ver == RADARR_API
    assert client._host.base_api_path is None
    assert (
        client._host.api_url("test")
        == "http://127.0.0.1:7000/api/v3/test?apikey=ur1234567-0abc12de3f456gh7ij89k012"
    )
