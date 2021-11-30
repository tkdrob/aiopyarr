# aiopyarr

![python version](https://img.shields.io/badge/Python-3.8=><=3.10-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/aiopyarr)](https://pypi.org/project/aiopyarr)
![Actions](https://github.com/tkdrob/aiopyarr/workflows/Actions/badge.svg?branch=master)

_Python API client for Radarr/Sonarr._

## Installation

```bash
python3 -m pip install aiopyarr
```

## Example usage

More examples can be found in the `tests` directory.

```python
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
```

## Contribute

**All** contributions are welcome!

1. Fork the repository
2. Clone the repository locally and open the devcontainer or use GitHub codespaces
3. Do your changes
4. Lint the files with `make lint`
5. Ensure all tests passes with `make test`
6. Ensure 100% coverage with `make coverage`
7. Commit your work, and push it to GitHub
8. Create a PR against the `master` branch