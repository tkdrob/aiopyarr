"""Tests configuration."""
import asyncio

from aiohttp import ClientSession
import pytest

from aiopyarr.radarr_client import RadarrClient

from . import TEST_HOST_CONFIGURATION
from .common import MockedRequests, MockResponse


@pytest.fixture(autouse=True)
def loop_factory():
    """Create loop."""
    return asyncio.new_event_loop


@pytest.fixture()
def requests():
    yield MockedRequests()


@pytest.fixture()
def response():
    yield MockResponse()


@pytest.fixture()
async def client_session(response, requests):
    async def _mocked_request(*args, **kwargs):
        response.url = args[1]
        requests.add(args[1])
        return response

    async with ClientSession() as session:
        requests.clear()
        session._request = _mocked_request
        yield session


@pytest.fixture()
async def client(client_session):
    async with RadarrClient(
        session=client_session, host_configuration=TEST_HOST_CONFIGURATION
    ) as obj:
        yield obj
