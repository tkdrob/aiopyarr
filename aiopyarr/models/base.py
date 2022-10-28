"""PyArr base model."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Any

import ciso8601

from ..const import ATTR_DATA
from .const import (
    CONVERT_TO_BOOL,
    CONVERT_TO_DATE,
    CONVERT_TO_DATETIME,
    CONVERT_TO_ENUM,
    CONVERT_TO_FLOAT,
    CONVERT_TO_INTEGER,
    ProtocolType,
)


def get_datetime(
    _input: datetime | str | None, utc: bool = False
) -> datetime | str | int | None:
    """Convert input to datetime object."""
    if isinstance(_input, str):
        if _input.isnumeric():
            return int(_input)
        if utc:
            return ciso8601.parse_datetime(_input)
        return ciso8601.parse_datetime_as_naive(_input)
    return _input


def get_date(_input: datetime | str | None) -> date | None:
    """Convert input to date object."""
    if (result := get_datetime(_input)) and isinstance(result, datetime):
        return result.date()
    return None


def get_enum_value(val: str) -> str | Enum:
    """Convert input to the correct enum."""
    for protocol in ProtocolType:
        if (
            val.isnumeric()
            and protocol.value == int(val)
            or protocol.name.lower() == val
        ):
            return protocol
    return val


def toraw(obj):
    """Convert object to dict."""
    if isinstance(obj, dict):
        return {k: toraw(v) for k, v in obj.items()}
    if hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [toraw(v) for v in obj]
    if hasattr(obj, "attributes"):
        return obj.attributes
    if isinstance(obj, datetime):
        return f"{obj.isoformat()}Z"
    return obj


def generate_data(
    data: dict[str, Any] | list[dict[str, Any]], datatype: Any = None
) -> Any:
    """Generate data."""
    if datatype is None:
        return data

    if isinstance(data, list):
        return [datatype(item) for item in data]

    return datatype(data)


@dataclass(init=False)
class BaseModel:
    """BaseModel."""

    def __init__(
        self,
        data: dict[str, Any] | list[dict[str, Any]],
        datatype: Any = None,
    ) -> None:
        """Init."""
        self.basedata = None
        if isinstance(data, dict):
            for key, value in data.items():
                if key == ATTR_DATA:
                    value = generate_data(value, datatype)
                elif key in CONVERT_TO_DATETIME:
                    if key == "airDateUtc":
                        value = get_datetime(value, utc=True)
                    else:
                        value = get_datetime(value)
                elif key in CONVERT_TO_DATE:
                    value = get_date(value)
                elif key in CONVERT_TO_ENUM:
                    value = get_enum_value(value)
                elif key in CONVERT_TO_FLOAT and value is not None:
                    value = float(value)
                elif key in CONVERT_TO_INTEGER and value is not None:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                elif key in CONVERT_TO_BOOL:
                    value = False if value == "False" else bool(value)
                self.__setattr__(key, value)

        self.__post_init__()

    def __post_init__(self):
        """Post init."""

    @property
    def attributes(self):
        """Return attributes of the object."""
        return {
            k: v
            if isinstance(v, bool)
            else str(v)
            if k in CONVERT_TO_INTEGER
            else toraw(v)
            for k, v in self.__dict__.items()
            if k != "basedata"
        }
