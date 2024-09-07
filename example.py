"""Example usage of aiopyarr."""

import asyncio

from aiopyarr.models.host_configuration import PyArrHostConfiguration
from aiopyarr.radarr_client import RadarrClient

IP = "192.168.100.3"
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


async def async_example():
    """Example usage of aiopyarr."""
    host_configuration = PyArrHostConfiguration(ipaddress=IP, api_token=TOKEN)
    async with RadarrClient(host_configuration=host_configuration) as client:
        print(await client.async_get_system_status())


asyncio.get_event_loop().run_until_complete(async_example())
