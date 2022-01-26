"""PyArr model constants."""

from enum import Enum

CONVERT_TO_BOOL = ("downloadForced",)

CONVERT_TO_FLOAT = (
    "ageHours",
    "ageMinutes",
)

CONVERT_TO_INTEGER = (
    "age",
    "fileId",
    "foreignAuthorId",
    "foreignEditionId",
    "isbn",
    "isbn13",
    "preferredWordScore",
    "size",
    "sizeleft",
    "titleSlug",
    "trackNumber",
    "tvdbId",
    "tvRageId",
)

CONVERT_TO_DATETIME = (
    "added",
    "airDate",
    "airDateUtc",
    "born",
    "buildTime",
    "date",
    "dateAdded",
    "died",
    "digitalRelease",
    "ended",
    "estimatedCompletionTime",
    "firstAired",
    "inCinemas",
    "installedOn",
    "lastExecution",
    "lastExecutionTime",
    "lastInfoSync",
    "lastModified",
    "lastStartTime",
    "lastWriteTime",
    "modified",
    "nextExecution",
    "physicalRelease",
    "publishDate",
    "publishedDate",
    "queued",
    "releaseDate",
    "started",
    "startTime",
    "stateChangeTime",
    "time",
)

CONVERT_TO_ENUM = (
    "preferredProtocol",
    "protocol",
)


class ProtocolType(Enum):
    """Protocol type."""

    UNKNOWN = 0
    USENET = 1
    TORRENT = 2
