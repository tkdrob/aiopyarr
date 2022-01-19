import json
import os

TEST_RESPONSE_HEADERS = {"Content-Type": "application/json"}


def fixture(filename, asjson=True):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", f"{filename}.json")
    with open(path, encoding="utf-8") as fptr:
        if asjson:
            return json.loads(fptr.read())
        return fptr.read()


class MockResponse:
    url = ""
    mock_status = 200
    mock_message = None
    mock_data = None
    mock_raises = None

    @property
    def status(self):
        return self.mock_status

    async def json(self):
        if self.mock_raises is not None:
            raise self.mock_raises  # pylint: disable=raising-bad-type
        if self.mock_data or self.mock_message:
            return {
                "response": {
                    "data": self.mock_data,
                    "message": self.mock_message,
                    "result": "success" if self.mock_status == 200 else "failure",
                }
            }
        cmd = self.url.split("&cmd=")[1].split("&")[0]
        try:
            return fixture(cmd)
        except OSError:
            return {}


class MockedRequests:
    _calls = []

    def add(self, url: str):
        self._calls.append(url)

    def clear(self):
        self._calls.clear()

    def __repr__(self) -> str:
        return f"<MockedRequests: {self._calls}>"

    @property
    def count(self) -> int:
        return len(self._calls)

    def has(self, string: str) -> bool:
        return bool([entry for entry in self._calls if string in entry])
