"""Tests for PyArr."""
import pathlib

from aiopyarr.models.host_configuration import PyArrHostConfiguration

TEST_HOST_CONFIGURATION = PyArrHostConfiguration(
    ipaddress="127.0.0.1", api_token="ur1234567-0abc12de3f456gh7ij89k012"
)
RADARR_API = "v3"
READARR_API = "v1"
SONARR_API = "v3"


def load_fixture(filename):
    """Load a fixture."""
    return pathlib.Path(__file__).parent.joinpath("fixtures", filename).read_text()
