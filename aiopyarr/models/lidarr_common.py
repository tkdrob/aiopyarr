"""Lidarr Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel, get_datetime

from .request_common import (  # isort:skip
    _Common2,
    _Common3,
    _Common4,
    _Common5,
    _Quality,
    _TitleInfo,
)
