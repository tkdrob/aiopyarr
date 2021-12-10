"""Decorator for pyarr."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .const import HTTPMethod

if TYPE_CHECKING:
    from .models.common import Diskspace, Logs, Tag, SystemBackup
    from .request_client import RequestClient

    from .models.radarr import (  # isort:skip
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
        RadarrUIConfig,
        RadarrUpdate,
    )
    from .models.sonarr import (  # isort:skip
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
        SonarrSystemStatus,
        SonarrWantedMissing,
    )


def api_command(
    command: str,
    params: dict | None = None,
    data: dict | None = None,
    datatype: type[Logs]
    | type[Diskspace]
    | type[RadarrBlocklist]
    | type[RadarrBlocklistMovie]
    | type[RadarrCalendar]
    | type[RadarrCommand]
    | type[RadarrCustomFilter]
    | type[RadarrDownloadClient]
    | type[RadarrHealth]
    | type[RadarrHostConfig]
    | type[RadarrImportList]
    | type[RadarrIndexer]
    | type[RadarrMetadataConfig]
    | type[RadarrMovie]
    | type[RadarrMovieEditor]
    | type[RadarrMovieFile]
    | type[RadarrMovieHistory]
    | type[RadarrNamingConfig]
    | type[RadarrNotification]
    | type[RadarrQualityProfile]
    | type[RadarrQueue]
    | type[RadarrQueueDetail]
    | type[RadarrQueueStatus]
    | type[RadarrRemotePathMapping]
    | type[RadarrRootFolder]
    | type[RadarrSystemStatus]
    | type[RadarrUIConfig]
    | type[RadarrUpdate]
    | type[SonarrCalendar]
    | type[SonarrCommand]
    | type[SonarrEpisode]
    | type[SonarrEpisodeFile]
    | type[SonarrHistory]
    | type[SonarrParse]
    | type[SonarrQualityProfile]
    | type[SonarrQueue]
    | type[SonarrRelease]
    | type[SonarrRootFolder]
    | type[SonarrSeries]
    | type[SonarrSeriesLookup]
    | type[SonarrSystemStatus]
    | type[SonarrWantedMissing]
    | type[SystemBackup]
    | type[Tag]
    | None = None,
    method: HTTPMethod = HTTPMethod.GET,
):
    """Initialize decorator for PyArr API request."""

    def decorator(_):
        """Initialize decorator."""

        async def wrapper(*args: Any):
            """Initialize wrapper."""
            client: RequestClient = args[0]
            return await client._async_request(  # pylint: disable=protected-access
                *args,
                command,
                params=params,
                data=data,
                datatype=datatype,
                method=method
            )

        return wrapper

    return decorator
