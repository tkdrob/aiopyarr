"""PyArr base model."""
from __future__ import annotations

import json
from datetime import datetime
from enum import Enum
from re import search, sub
from typing import Any

from ..const import LOGGER

from .const import (  # isort:skip
    CONVERT_TO_BOOL,
    CONVERT_TO_DATETIME,
    CONVERT_TO_FLOAT,
    CONVERT_TO_INTEGER,
)


def get_datetime_from_string(string: str) -> datetime | None:
    """Convert string to datetime object."""
    if string is not None:
        if search(r"^\d{4}-\d{2}-\d{2}$", string):
            return datetime.strptime(string, "%Y-%m-%d")
        if search(r".\d{7}Z$", string):
            string = sub(r"\dZ", "Z", string)
        elif not search(r"\.\d+Z$", string):
            string = sub("Z", ".000000Z", string)
        return datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return None


class ApiJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder."""

    def default(self, o: Any):
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


class BaseModel:
    """BaseModel."""

    _datatype: Any = None

    def __init__(
        self,
        data: dict[str, Any] | list[dict[str, Any]],
        datatype: Any = None,
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

    def __post_init__(self):  # pylint: disable=too-many-branches
        """Post init."""
        if hasattr(self, "completionMessage") and (
            not hasattr(self, "clientUserAgent") or not hasattr(self, "lastStartTime")
        ):
            if self.__getattribute__("isNewMovie") is None:
                self.__setattr__("isNewMovie", False)
            else:
                LOGGER.debug("isNewMovie is now always included by API")
        for key in CONVERT_TO_BOOL:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                if self.__getattribute__(key) == "False":
                    self.__setattr__(key, False)
                else:
                    self.__setattr__(key, bool(self.__getattribute__(key)))
        for key in CONVERT_TO_FLOAT:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                self.__setattr__(key, float(self.__getattribute__(key)))
        for key in CONVERT_TO_INTEGER:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                try:
                    self.__setattr__(key, int(self.__getattribute__(key)))
                except ValueError:
                    pass
        for key in CONVERT_TO_DATETIME:
            if hasattr(self, key) and self.__getattribute__(key) is not None:
                self.__setattr__(
                    key, get_datetime_from_string(self.__getattribute__(key))
                )

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
