"""Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from aiopyarr.models.base import APIResponseType, BaseModel


@dataclass(init=False)
class Diskspace(BaseModel):
    """Radarr diskspace attributes."""

    _responsetype = APIResponseType.LIST

    freeSpace: int | None = None
    label: str | None = None
    path: str | None = None
    totalSpace: int | None = None


@dataclass(init=False)
class _CommonAttrs(BaseModel):
    """Common attributes."""

    audioBitrate: int | None = None
    audioChannels: float | None = None
    audioCodec: str | None = None
    audioLanguages: str | None = None
    audioStreamCount: int | None = None
    resolution: str | None = None
    runTime: str | None = None
    scanType: str | None = None
    subtitles: str | None = None
    videoBitDepth: int | None = None
    videoBitrate: int | None = None
    videoCodec: str | None = None
    videoFps: float | None = None
