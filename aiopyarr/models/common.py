"""Common Models."""
# pylint: disable=invalid-name, too-many-instance-attributes
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel


@dataclass(init=False)
class Diskspace(BaseModel):
    """Radarr diskspace attributes."""

    freeSpace: int | None = None
    label: str | None = None
    path: str | None = None
    totalSpace: int | None = None


@dataclass(init=False)
class _CommonAttrs(BaseModel):
    """Common attributes."""

    audioBitrate: str | None = None
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


@dataclass(init=False)
class _LogRecord(BaseModel):
    """Sonarr log record attributes."""

    id: int | None = None
    level: str | None = None
    logger: str | None = None
    message: str | None = None
    time: str | None = None


@dataclass(init=False)
class _RecordCommon(BaseModel):
    """Sonarr common attributes."""

    page: int | None = None
    pageSize: int | None = None
    sortDirection: str | None = None
    sortKey: str | None = None
    totalRecords: int | None = None


@dataclass(init=False)
class Logs(_RecordCommon):
    """Log attributes."""

    records: list[_LogRecord] | None = None

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.records = [_LogRecord(record) for record in self.records or []]


@dataclass(init=False)
class LogFiles(BaseModel):
    """Log file attributes"""

    filename: str | None = None
    lastWriteTime: str | None = None
    contentsUrl: str | None = None
    downloadUrl: str | None = None
    id: int | None = None


@dataclass(init=False)
class Tag(BaseModel):
    """Radarr tag attributes."""

    id: int | None = None
    label: str | None = None


@dataclass(init=False)
class SystemBackup(BaseModel):
    """System backup attributes."""

    id: int | None = None
    name: str | None = None
    path: str | None = None
    time: str | None = None
    type: str | None = None
