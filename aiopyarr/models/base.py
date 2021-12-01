"""PyArr base model."""
from __future__ import annotations

import json
from enum import Enum
from typing import Any

from ..const import LOGGER
from .const import CONVERT_TO_BOOL, CONVERT_TO_FLOAT, CONVERT_TO_INTEGER


class ApiJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder."""

    def default(self, o):
        """Encode default JSON."""
        if isinstance(o, BaseModel):

            return {
                key: value
                for key, value in o.__dict__.items()
                if not key.startswith("_")
            }
        if isinstance(o, Enum):
            return o.name
        return json.JSONEncoder.default(self, o)


class APIResponseType(str, Enum):
    """ApiResponseType."""

    DICT = "dict"
    LIST = "list"


class BaseModel:
    """BaseModel."""

    _datatype: BaseModel | None = None
    _responsetype: APIResponseType = APIResponseType.DICT

    def __init__(
        self, data: dict[str, Any] | list[dict[str, Any]], datatype: BaseModel = None
    ) -> None:
        """Init."""
        self._datatype = datatype
        if isinstance(data, dict):
            for key, value in data.items():
                if hasattr(self, key):
                    if hasattr(self, f"_generate_{key}"):
                        value = self.__getattribute__(f"_generate_{key}")(value)
                    self.__setattr__(key, value)

            self.__post_init__()

    def __repr__(self) -> str:
        """Representation."""
        attrs = [
            f"{key}={value}"
            for key, value in self.attributes.items()
            if value is not None and "token" not in key
        ]
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __post_init__(self):
        """Post init."""
        for key in CONVERT_TO_BOOL:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                self.__setattr__(key, bool(self.__getattribute__(key)))
            if hasattr(self, "completionMessage"):
                if self.__getattribute__("isNewMovie") is None:
                    self.__setattr__("isNewMovie", False)
                else:
                    LOGGER.debug("isNewMovie is now always included by API")
        for key in CONVERT_TO_FLOAT:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                self.__setattr__(key, float(self.__getattribute__(key)))
        for key in CONVERT_TO_INTEGER:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                try:
                    self.__setattr__(key, int(self.__getattribute__(key)))
                except ValueError:
                    pass

    @property
    def attributes(self) -> dict[str, Any]:
        """Return the class attributes."""
        return {
            key: json.dumps(
                self.__dict__[key],  # pylint: disable=unnecessary-dict-index-lookup
                cls=ApiJSONEncoder,
            )
            for key, _ in self.__dict__.items()
            if not key.startswith("_")
        }
