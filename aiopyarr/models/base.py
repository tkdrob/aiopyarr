"""PyArr base model."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from re import search, sub
from typing import Any

from ..const import LOGGER
from .const import (
    CONVERT_TO_BOOL,
    CONVERT_TO_DATETIME,
    CONVERT_TO_FLOAT,
    CONVERT_TO_INTEGER,
)


def get_datetime(_input: datetime | str | None) -> datetime | str | int | None:
    """Convert input to datetime object."""
    if isinstance(_input, str):
        if _input.isnumeric():
            return int(_input)
        if search(r"^\d{4}-\d{2}-\d{2}$", _input):
            return datetime.strptime(_input, "%Y-%m-%d")
        if search(r".\d{7}Z$", _input):
            _input = sub(r"\dZ", "Z", _input)
        elif not search(r"\.\d+Z$", _input):
            _input = sub("Z", ".000000Z", _input)
        return datetime.strptime(_input, "%Y-%m-%dT%H:%M:%S.%fZ")
    return _input


@dataclass(init=False)
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

    def __post_init__(self):  # pylint: disable=too-many-branches
        """Post init."""
        if hasattr(self, "completionMessage") and (
            not hasattr(self, "clientUserAgent") or not hasattr(self, "lastStartTime")
        ):
            if self.__getattribute__("isNewMovie") is None:
                self.__setattr__("isNewMovie", False)
                LOGGER.debug("isNewMovie not included by API")
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
                self.__setattr__(key, get_datetime(self.__getattribute__(key)))
