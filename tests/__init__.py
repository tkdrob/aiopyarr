"""Tests for PyArr."""
import pathlib

from aiohttp.client import ClientSession

from aiopyarr.models.host_configuration import PyArrHostConfiguration

API_TOKEN = "ur1234567-0abc12de3f456gh7ij89k012"
TEST_HOST_CONFIGURATION = PyArrHostConfiguration(
    api_token=API_TOKEN, ipaddress="127.0.0.1"
)
RADARR_API = "v3"
READARR_API = "v1"
SONARR_API = "v3"


def load_fixture(filename):
    """Load a fixture."""
    return pathlib.Path(__file__).parent.joinpath("fixtures", filename).read_text()
