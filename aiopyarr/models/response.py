"""API response model for AioPyArr Api."""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any

from .base import BaseModel

if TYPE_CHECKING:
    from .common import Diskspace, Logs

    from .radarr import (  # isort:skip
        RadarrBlocklist,
        RadarrBlocklistMovie,
        RadarrCalendar,
        RadarrCommand,
        RadarrCustomFilter,
        RadarrDownloadClient,
        RadarrHealth,
        RadarrHostConfig,
        RadarrImportList,
        RadarrIndexer,
        RadarrMetadataConfig,
        RadarrMovie,
        RadarrMovieEditor,
        RadarrMovieFile,
        RadarrMovieHistory,
        RadarrNamingConfig,
        RadarrNotification,
        RadarrQualityProfile,
        RadarrQueue,
        RadarrQueueDetail,
        RadarrQueueStatus,
        RadarrRemotePathMapping,
        RadarrRootFolder,
        RadarrSystemStatus,
        RadarrTag,
        RadarrUIConfig,
        RadarrUpdate,
    )
    from .sonarr import (  # isort:skip
        SonarrCalendar,
        SonarrCommand,
        SonarrEpisode,
        SonarrEpisodeFile,
        SonarrHistory,
        SonarrParse,
        SonarrQualityProfile,
        SonarrQueue,
        SonarrRelease,
        SonarrRootFolder,
        SonarrSeries,
        SonarrSeriesLookup,
        SonarrSystemBackup,
        SonarrSystemStatus,
        SonarrTag,
        SonarrWantedMissing,
    )


class APIResult(str, Enum):
    """ApiResult."""

    SUCCESS = "success"
    ERROR = "error"


class PyArrResponse(BaseModel):  # pylint: disable=too-few-public-methods
    """API response model for PyArr Api."""

    data: dict[str, Any] | list[dict[str, Any]] | None = None
    message: str | None = None
    result: APIResult | None = None
    # fmt: off

    def _generate_data(
        self, data: dict[str, Any] | list[dict[str, Any]]
    ) -> (
        Logs
        | Diskspace
        | RadarrBlocklist
        | RadarrBlocklistMovie
        | RadarrCalendar
        | RadarrCommand
        | RadarrCustomFilter
        | RadarrDownloadClient
        | RadarrHealth
        | RadarrHostConfig
        | RadarrImportList
        | RadarrIndexer
        | RadarrMetadataConfig
        | RadarrMovie
        | RadarrMovieEditor
        | RadarrMovieFile
        | RadarrMovieHistory
        | RadarrNamingConfig
        | RadarrNotification
        | RadarrQualityProfile
        | RadarrQueue
        | RadarrQueueDetail
        | RadarrQueueStatus
        | RadarrRemotePathMapping
        | RadarrRootFolder
        | RadarrSystemStatus
        | RadarrTag
        | RadarrUIConfig
        | RadarrUpdate
        | SonarrCalendar
        | SonarrCommand
        | SonarrEpisode
        | SonarrEpisodeFile
        | SonarrHistory
        | SonarrParse
        | SonarrQualityProfile
        | SonarrQueue
        | SonarrRelease
        | SonarrRootFolder
        | SonarrSeries
        | SonarrSeriesLookup
        | SonarrSystemBackup
        | SonarrSystemStatus
        | SonarrTag
        | SonarrWantedMissing
        | dict[str, Any] | list[dict[str, Any]] | list
    ):  # fmt: on
        """Generate data."""
        if self._datatype is None:
            return data

        if isinstance(data, list):
            return [self._datatype(item, self._datatype) for item in data]

        return self._datatype(data, self._datatype)
