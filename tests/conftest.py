"""Tests configuration."""

# pylint:disable=redefined-outer-name
import asyncio

from aiohttp import ClientSession
import pytest_asyncio

from aiopyarr.lidarr_client import LidarrClient
from aiopyarr.radarr_client import RadarrClient
from aiopyarr.readarr_client import ReadarrClient
from aiopyarr.sonarr_client import SonarrClient

from tests import TEST_HOST_CONFIGURATION


@pytest_asyncio.fixture(autouse=True)
def loop_factory():
    """Create loop."""
    return asyncio.new_event_loop


@pytest_asyncio.fixture()
async def apisession():
    """Create client session."""
    async with ClientSession() as sess:
        yield sess


@pytest_asyncio.fixture()
async def lidarr_client(apisession):
    """Create Lidarr Client."""
    async with LidarrClient(
        session=apisession, host_configuration=TEST_HOST_CONFIGURATION
    ) as obj:
        yield obj


@pytest_asyncio.fixture()
async def radarr_client(apisession):
    """Create Radarr Client."""
    async with RadarrClient(
        session=apisession, host_configuration=TEST_HOST_CONFIGURATION
    ) as obj:
        yield obj


@pytest_asyncio.fixture()
async def readarr_client(apisession):
    """Create Readarr Client."""
    async with ReadarrClient(
        session=apisession, host_configuration=TEST_HOST_CONFIGURATION
    ) as obj:
        yield obj


@pytest_asyncio.fixture()
async def sonarr_client(apisession):
    """Create Sonarr Client."""
    async with SonarrClient(
        session=apisession, host_configuration=TEST_HOST_CONFIGURATION
    ) as obj:
        yield obj
