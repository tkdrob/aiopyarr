"""Tests for object models."""
from datetime import datetime
from aiopyarr.models.base import BaseModel
from aiopyarr.models.common import Diskspace

from aiopyarr.readarr_client import ReadarrClient
import pytest
from aiohttp.client import ClientSession

from aiopyarr.sonarr_client import SonarrClient
from aiopyarr.models.readarr import _ReadarrBookValueSeriesLinks, _ReadarrEditionsValue, ReadarrBookshelf


from . import TEST_HOST_CONFIGURATION, load_fixture



@pytest.mark.asyncio
async def test_readarr_bookshelf():
    """Test readarr bookshelf model."""
    item = ReadarrBookshelf()
    item.__post_init__()
    assert item.authors[0].id == 0