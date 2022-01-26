"""API response model for AioPyArr Api."""
from __future__ import annotations

from enum import Enum
from typing import Any

from .base import BaseModel


class APIResult(str, Enum):
    """ApiResult."""

    SUCCESS = "success"
    ERROR = "error"


class PyArrResponse(BaseModel):  # pylint: disable=too-few-public-methods
    """API response model for PyArr Api."""

    data: dict[str, Any] | list[dict[str, Any]] | None = None
    result: APIResult | None = None

    def _generate_data(self, data: dict[str, Any] | list[dict[str, Any]]) -> Any:
        """Generate data."""
        if self._datatype is None:
            return data

        if isinstance(data, list):
            return [self._datatype(item) for item in data]

        return self._datatype(data)
