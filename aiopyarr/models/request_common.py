"""Request Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, line-too-long, too-many-lines
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .base import BaseModel
from .const import ProtocolType


@dataclass(init=False)
class _SelectOption(BaseModel):
    """Select option attributes."""

    name: str
    order: int
    value: str | list[str] | int


@dataclass(init=False)
class _SelectOptionExtended(_SelectOption):
    """Select options extended attributes."""

    dividerAfter: bool


@dataclass(init=False)
class _Fields(_SelectOption):
    """Fields attributes."""

    advanced: bool
    errors: list
    helpText: str
    hidden: str
    label: str
    pending: bool
    selectOptions: list[_SelectOptionExtended] | None = None
    type: str
    warnings: list

    def __post_init__(self):
        self.selectOptions = [
            _SelectOptionExtended(opt) for opt in self.selectOptions or []
        ]


@dataclass(init=False)
class _Common(BaseModel):
    """Common attributes."""

    fields: list[_Fields] | None = None
    implementation: str
    implementationName: str
    infoLink: str
    name: str

    def __post_init__(self):
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class _Common2(BaseModel):
    """Common attributes."""

    downloadId: str
    eventType: str


@dataclass(init=False)
class _Common3(BaseModel):
    """Common attributes."""

    id: int
    name: str


@dataclass(init=False)
class _Common4(BaseModel):
    """Common attributes."""

    downloadClient: str
    downloadId: str
    estimatedCompletionTime: datetime
    indexer: str
    outputPath: str


@dataclass(init=False)
class _Common5(BaseModel):
    """Common attributes."""

    coverType: str
    url: str


@dataclass(init=False)
class _Common6(BaseModel):
    """Common attributes."""

    monitored: bool
    overview: str


@dataclass(init=False)
class _Common7(BaseModel):
    """Common attributes."""

    id: int
    indexer: str
    protocol: ProtocolType


@dataclass(init=False)
class _QualityInfo(_Common3):
    """Quality info attributes."""

    modifier: str
    resolution: int
    source: str


@dataclass(init=False)
class _Revision(BaseModel):
    """Revision attributes."""

    isRepack: bool
    real: int
    version: int


@dataclass(init=False)
class _Quality(BaseModel):
    """Quality attributes."""

    quality: type[_QualityInfo] = field(default=_QualityInfo)
    revision: type[_Revision] = field(default=_Revision)

    def __post_init__(self):
        """Post init."""
        self.quality = _QualityInfo(self.quality)
        self.revision = _Revision(self.revision)


@dataclass(init=False)
class _Common8(BaseModel):
    """Common attributes."""

    id: int
    protocol: ProtocolType
    quality: type[_Quality] = field(default=_Quality)
    size: int
    sizeleft: int
    status: str
    statusMessages: list[_StatusMessage] | None = None
    timeleft: str
    title: str
    trackedDownloadState: str
    trackedDownloadStatus: str


@dataclass(init=False)
class _Common9(BaseModel):
    """Common attributes."""

    certification: str
    genres: list[str]
    imdbId: str
    runtime: int
    title: str
    year: int


@dataclass(init=False)
class _CommonAttrs(BaseModel):
    """Common attributes."""

    audioBitrate: str
    audioChannels: float
    audioCodec: str
    audioLanguages: str
    audioStreamCount: int
    resolution: str
    runTime: str
    scanType: str
    subtitles: str
    videoBitDepth: int
    videoBitrate: int
    videoCodec: str
    videoDynamicRangeType: str
    videoFps: float


@dataclass(init=False)
class _CommandBody(BaseModel):
    """Command body attributes."""

    completionMessage: str
    isExclusive: bool
    isNewMovie: bool
    isTypeExclusive: bool
    lastExecutionTime: datetime
    lastStartTime: datetime
    name: str
    requiresDiskAccess: bool
    sendUpdatesToClient: bool
    suppressMessages: bool
    trigger: str
    updateScheduledTask: bool


@dataclass(init=False)
class _CustomFilterAttr(BaseModel):
    """Custom filter attributes."""

    key: str
    type: str
    value: list[str]


@dataclass(init=False)
class _MetadataFields(_Fields):
    """Metadata fields attributes."""

    section: str


@dataclass(init=False)
class _FilesystemFolder(BaseModel):
    """Filesystem folder attributes."""

    name: str
    path: str


@dataclass(init=False)
class _FilesystemDirectory(_FilesystemFolder):
    """Filesystem directory attributes."""

    lastModified: datetime
    size: int
    type: str


@dataclass(init=False)
class _ImportListCommon(_FilesystemFolder):
    """Import list common attributes."""

    configContract: str
    listOrder: int
    rootFolderPath: str


@dataclass(init=False)
class _LocalizationStrings(BaseModel):
    """Localization strings attributes."""

    About: str
    Absolute: str
    AcceptConfirmationModal: str
    Actions: str
    Activity: str
    Add: str
    AddCustomFormat: str
    AddDelayProfile: str
    AddDownloadClient: str
    Added: str
    AddedAuthorSettings: str
    AddedToDownloadQueue: str
    AddExclusion: str
    AddImportListExclusionHelpText: str
    AddIndexer: str
    AddingTag: str
    AddList: str
    AddListExclusion: str
    AddMissing: str
    AddMovie: str
    AddMovies: str
    AddMoviesMonitored: str
    AddNew: str
    AddNewItem: str
    AddNewMessage: str
    AddNewMovie: str
    AddNewTmdbIdMessage: str
    AddNotification: str
    AddQualityProfile: str
    AddRemotePathMapping: str
    AddRestriction: str
    AddRootFolder: str
    AddToDownloadQueue: str
    AdvancedSettingsHiddenClickToShow: str
    AdvancedSettingsShownClickToHide: str
    AfterManualRefresh: str
    Age: str
    Agenda: str
    AgeWhenGrabbed: str
    All: str
    AllAuthorBooks: str
    AllBooks: str
    AllExpandedCollapseAll: str
    AllExpandedExpandAll: str
    AllFiles: str
    AllMoviesHiddenDueToFilter: str
    AllMoviesInPathHaveBeenImported: str
    AllowAuthorChangeClickToChangeAuthor: str
    AllowedLanguages: str
    AllowFingerprinting: str
    AllowFingerprintingHelpText: str
    AllowFingerprintingHelpTextWarning: str
    AllowHardcodedSubs: str
    AllowHardcodedSubsHelpText: str
    AllResultsHiddenFilter: str
    AlreadyInYourLibrary: str
    AlternateTitles: str
    AlternateTitleslength1Title: str
    AlternateTitleslength1Titles: str
    AlternativeTitle: str
    Always: str
    AnalyseVideoFiles: str
    Analytics: str
    AnalyticsEnabledHelpText: str
    AnalyticsEnabledHelpTextWarning: str
    Announced: str
    AnnouncedMsg: str
    AnyEditionOkHelpText: str
    ApiKey: str
    APIKey: str
    ApiKeyHelpTextWarning: str
    AppDataDirectory: str
    AppDataLocationHealthCheckMessage: str
    Apply: str
    ApplyTags: str
    ApplyTagsHelpTexts1: str
    ApplyTagsHelpTexts2: str
    ApplyTagsHelpTexts3: str
    ApplyTagsHelpTexts4: str
    AptUpdater: str
    AreYouSureYouWantToDeleteFormat: str
    AreYouSureYouWantToDeleteThisDelayProfile: str
    AreYouSureYouWantToDeleteThisImportListExclusion: str
    AreYouSureYouWantToDeleteThisRemotePathMapping: str
    AreYouSureYouWantToRemoveSelectedItemFromQueue: str
    AreYouSureYouWantToRemoveSelectedItemsFromQueue: str
    AreYouSureYouWantToRemoveTheSelectedItemsFromBlocklist: str
    AreYouSureYouWantToResetYourAPIKey: str
    AsAllDayHelpText: str
    ASIN: str
    AudioFileMetadata: str
    AudioInfo: str
    AuthBasic: str
    Authentication: str
    AuthenticationMethodHelpText: str
    AuthForm: str
    Author: str
    AuthorClickToChangeBook: str
    AuthorEditor: str
    AuthorFolderFormat: str
    AuthorIndex: str
    AuthorNameHelpText: str
    Authors: str
    Automatic: str
    AutomaticallySwitchEdition: str
    AutomaticSearch: str
    AutoRedownloadFailedHelpText: str
    AutoUnmonitorPreviouslyDownloadedBooksHelpText: str
    AutoUnmonitorPreviouslyDownloadedMoviesHelpText: str
    AvailabilityDelay: str
    AvailabilityDelayHelpText: str
    Backup: str
    BackupFolderHelpText: str
    BackupIntervalHelpText: str
    BackupNow: str
    BackupRetentionHelpText: str
    Backups: str
    BeforeUpdate: str
    BindAddress: str
    BindAddressHelpText: str
    BindAddressHelpTextWarning: str
    Blocklist: str
    Blocklisted: str
    BlocklistHelpText: str
    BlocklistRelease: str
    BlocklistReleases: str
    Book: str
    BookAvailableButMissing: str
    BookDownloaded: str
    BookEditor: str
    BookFileCountBookCountTotalTotalBookCountInterp: str
    BookFileCounttotalBookCountBooksDownloadedInterp: str
    BookFilesCountMessage: str
    BookHasNotAired: str
    BookIndex: str
    BookIsDownloading: str
    BookIsDownloadingInterp: str
    BookIsNotMonitored: str
    BookList: str
    BookMissingFromDisk: str
    BookMonitoring: str
    BookNaming: str
    Books: str
    BooksTotal: str
    BookStudio: str
    BookTitle: str
    Branch: str
    BranchUpdate: str
    BranchUpdateMechanism: str
    BuiltIn: str
    BypassDelayIfHighestQuality: str
    BypassDelayIfHighestQualityHelpText: str
    BypassProxyForLocalAddresses: str
    Calendar: str
    CalendarOptions: str
    CalendarWeekColumnHeaderHelpText: str
    CalibreContentServer: str
    CalibreContentServerText: str
    CalibreHost: str
    CalibreLibrary: str
    CalibreMetadata: str
    CalibreNotCalibreWeb: str
    CalibreOutputFormat: str
    CalibreOutputProfile: str
    CalibrePassword: str
    CalibrePort: str
    CalibreSettings: str
    CalibreUrlBase: str
    CalibreUsername: str
    Cancel: str
    CancelMessageText: str
    CancelPendingTask: str
    CancelProcessing: str
    CantFindMovie: str
    Cast: str
    CatalogNumber: str
    CertificateValidation: str
    CertificateValidationHelpText: str
    Certification: str
    CertificationCountry: str
    CertificationCountryHelpText: str
    CertValidationNoLocal: str
    ChangeFileDate: str
    ChangeHasNotBeenSavedYet: str
    CheckDownloadClientForDetails: str
    CheckForFinishedDownloadsInterval: str
    ChmodFolder: str
    ChmodFolderHelpText: str
    ChmodFolderHelpTextWarning: str
    ChmodGroup: str
    ChmodGroupHelpText: str
    ChmodGroupHelpTextWarning: str
    ChooseAnotherFolder: str
    ChownGroup: str
    ChownGroupHelpText: str
    ChownGroupHelpTextWarning: str
    CleanLibraryLevel: str
    Clear: str
    ClickToChangeLanguage: str
    ClickToChangeMovie: str
    ClickToChangeQuality: str
    ClickToChangeReleaseGroup: str
    ClientPriority: str
    CloneCustomFormat: str
    CloneFormatTag: str
    CloneIndexer: str
    CloneProfile: str
    Close: str
    CloseCurrentModal: str
    CollapseMultipleBooks: str
    CollapseMultipleBooksHelpText: str
    Collection: str
    ColonReplacement: str
    ColonReplacementFormatHelpText: str
    Columns: str
    CompletedDownloadHandling: str
    Component: str
    Conditions: str
    Connect: str
    Connection: str
    ConnectionLost: str
    ConnectionLostAutomaticMessage: str
    ConnectionLostMessage: str
    Connections: str
    ConnectSettings: str
    ConnectSettingsSummary: str
    ConsideredAvailable: str
    ConsoleLogLevel: str
    Continuing: str
    ContinuingAllBooksDownloaded: str
    ContinuingMoreBooksAreExpected: str
    ContinuingNoAdditionalBooksAreExpected: str
    CopyToClipboard: str
    CopyUsingHardlinksHelpText: str
    CopyUsingHardlinksHelpTextWarning: str
    CouldNotConnectSignalR: str
    CouldNotFindResults: str
    Country: str
    CreateEmptyAuthorFolders: str
    CreateEmptyAuthorFoldersHelpText: str
    CreateEmptyMovieFolders: str
    CreateEmptyMovieFoldersHelpText: str
    CreateGroup: str
    Crew: str
    CurrentlyInstalled: str
    Custom: str
    CustomFilters: str
    CustomFormat: str
    CustomFormatHelpText: str
    CustomFormatJSON: str
    CustomFormats: str
    CustomFormatScore: str
    CustomFormatsSettings: str
    CustomFormatsSettingsSummary: str
    CustomFormatUnknownCondition: str
    CustomFormatUnknownConditionOption: str
    Cutoff: str
    CutoffFormatScoreHelpText: str
    CutoffHelpText: str
    CutoffUnmet: str
    Date: str
    Dates: str
    Day: str
    Days: str
    DBMigration: str
    Debug: str
    DefaultCase: str
    DefaultDelayProfile: str
    DefaultMetadataProfileIdHelpText: str
    DefaultMonitorOptionHelpText: str
    DefaultQualityProfileIdHelpText: str
    DefaultReadarrTags: str
    DefaultTagsHelpText: str
    DelayingDownloadUntilInterp: str
    DelayProfile: str
    DelayProfiles: str
    Delete: str
    DeleteBackup: str
    DeleteBackupMessageText: str
    DeleteBookFile: str
    DeleteBookFileMessageText: str
    DeleteCustomFormat: str
    Deleted: str
    DeleteDelayProfile: str
    DeleteDelayProfileMessageText: str
    DeletedMsg: str
    DeleteDownloadClient: str
    DeleteDownloadClientMessageText: str
    DeleteEmptyFolders: str
    DeleteEmptyFoldersHelpText: str
    DeleteFile: str
    DeleteFileLabel: str
    DeleteFilesHelpText: str
    DeleteFilesLabel: str
    DeleteHeader: str
    DeleteImportList: str
    DeleteImportListExclusion: str
    DeleteImportListExclusionMessageText: str
    DeleteImportListMessageText: str
    DeleteIndexer: str
    DeleteIndexerMessageText: str
    DeleteList: str
    DeleteListMessageText: str
    DeleteMetadataProfile: str
    DeleteMetadataProfileMessageText: str
    DeleteMovieFolderHelpText: str
    DeleteMovieFolderLabel: str
    DeleteNotification: str
    DeleteNotificationMessageText: str
    DeleteQualityProfile: str
    DeleteQualityProfileMessageText: str
    DeleteReleaseProfile: str
    DeleteReleaseProfileMessageText: str
    DeleteRestriction: str
    DeleteRestrictionHelpText: str
    DeleteRootFolder: str
    DeleteRootFolderMessageText: str
    DeleteSelectedBookFiles: str
    DeleteSelectedBookFilesMessageText: str
    DeleteSelectedMovie: str
    DeleteSelectedMovieFiles: str
    DeleteSelectedMovieFilesMessage: str
    DeleteTag: str
    DeleteTagMessageText: str
    DeleteTheMovieFolder: str
    DestinationPath: str
    DestinationRelativePath: str
    DetailedProgressBar: str
    DetailedProgressBarHelpText: str
    Details: str
    Development: str
    DigitalRelease: str
    Disabled: str
    DiscCount: str
    DiscNumber: str
    Discord: str
    DiscordUrlInSlackNotification: str
    Discover: str
    DiskSpace: str
    Docker: str
    DockerUpdater: str
    Donations: str
    DoneEditingGroups: str
    DoNotPrefer: str
    DoNotUpgradeAutomatically: str
    Download: str
    DownloadClient: str
    DownloadClientCheckDownloadingToRoot: str
    DownloadClientCheckNoneAvailableMessage: str
    DownloadClientCheckUnableToCommunicateMessage: str
    DownloadClients: str
    DownloadClientSettings: str
    DownloadClientsSettingsSummary: str
    DownloadClientStatusCheckAllClientMessage: str
    DownloadClientStatusCheckSingleClientMessage: str
    DownloadClientUnavailable: str
    Downloaded: str
    DownloadedAndMonitored: str
    DownloadedButNotMonitored: str
    DownloadFailed: str
    DownloadFailedCheckDownloadClientForMoreDetails: str
    DownloadFailedInterp: str
    Downloading: str
    DownloadPropersAndRepacks: str
    DownloadPropersAndRepacksHelpText1: str
    DownloadPropersAndRepacksHelpText2: str
    DownloadPropersAndRepacksHelpTexts1: str
    DownloadPropersAndRepacksHelpTexts2: str
    DownloadPropersAndRepacksHelpTextWarning: str
    DownloadWarning: str
    DownloadWarningCheckDownloadClientForMoreDetails: str
    Edit: str
    EditAuthor: str
    EditCustomFormat: str
    EditDelayProfile: str
    EditGroups: str
    EditIndexer: str
    Edition: str
    EditionsHelpText: str
    EditListExclusion: str
    EditMovie: str
    EditMovieFile: str
    EditPerson: str
    EditQualityProfile: str
    EditRemotePathMapping: str
    EditRestriction: str
    EmbedMetadataHelpText: str
    EmbedMetadataInBookFiles: str
    Enable: str
    EnableAutoHelpText: str
    EnableAutomaticAdd: str
    EnableAutomaticAddHelpText: str
    EnableAutomaticSearch: str
    EnableAutomaticSearchHelpText: str
    EnableAutomaticSearchHelpTextWarning: str
    EnableColorImpairedMode: str
    EnableColorImpairedModeHelpText: str
    EnableCompletedDownloadHandlingHelpText: str
    Enabled: str
    EnabledHelpText: str
    EnableHelpText: str
    EnableInteractiveSearch: str
    EnableInteractiveSearchHelpText: str
    EnableInteractiveSearchHelpTextWarning: str
    EnableMediaInfoHelpText: str
    EnableProfile: str
    EnableRSS: str
    EnableSSL: str
    EnableSslHelpText: str
    Ended: str
    EndedAllBooksDownloaded: str
    EntityName: str
    Episode: str
    EpisodeDoesNotHaveAnAbsoluteEpisodeNumber: str
    Error: str
    ErrorLoadingContents: str
    ErrorLoadingPreviews: str
    ErrorRestoringBackup: str
    Events: str
    EventType: str
    Exception: str
    Excluded: str
    ExcludeMovie: str
    ExcludeTitle: str
    Existing: str
    ExistingBooks: str
    ExistingItems: str
    ExistingMovies: str
    ExistingTag: str
    ExistingTagsScrubbed: str
    ExportCustomFormat: str
    Extension: str
    ExternalUpdater: str
    ExtraFileExtensionsHelpTexts1: str
    ExtraFileExtensionsHelpTexts2: str
    Failed: str
    FailedDownloadHandling: str
    FailedLoadingSearchResults: str
    FailedToLoadMovieFromAPI: str
    FailedToLoadQueue: str
    FeatureRequests: str
    FileDateHelpText: str
    FileDetails: str
    FileManagement: str
    Filename: str
    FileNames: str
    FileNameTokens: str
    Files: str
    FilesTotal: str
    FileWasDeletedByUpgrade: str
    FileWasDeletedByViaUI: str
    Filter: str
    FilterAnalyticsEvents: str
    FilterAuthor: str
    FilterPlaceHolder: str
    Filters: str
    FilterSentryEventsHelpText: str
    FirstBook: str
    FirstDayOfWeek: str
    Fixed: str
    FocusSearchBox: str
    Folder: str
    FolderMoveRenameWarning: str
    Folders: str
    FollowPerson: str
    Forecast: str
    ForeignIdHelpText: str
    Formats: str
    ForMoreInformationOnTheIndividualDownloadClients: str
    ForMoreInformationOnTheIndividualDownloadClientsClickOnTheInfoButtons: str
    ForMoreInformationOnTheIndividualImportListsClinkOnTheInfoButtons: str
    ForMoreInformationOnTheIndividualIndexers: str
    ForMoreInformationOnTheIndividualIndexersClickOnTheInfoButtons: str
    ForMoreInformationOnTheIndividualListsClickOnTheInfoButtons: str
    FreeSpace: str
    From: str
    FutureBooks: str
    FutureDays: str
    FutureDaysHelpText: str
    General: str
    GeneralSettings: str
    GeneralSettingsSummary: str
    Genres: str
    Global: str
    GoToAuthorListing: str
    GoToInterp: str
    Grab: str
    Grabbed: str
    GrabID: str
    GrabRelease: str
    GrabReleaseMessageText: str
    GrabSelected: str
    Group: str
    HardlinkCopyFiles: str
    HasMonitoredBooksNoMonitoredBooksForThisAuthor: str
    HasPendingChangesNoChanges: str
    HasPendingChangesSaveChanges: str
    HaveNotAddedMovies: str
    Health: str
    HealthNoIssues: str
    HelpText: str
    HiddenClickToShow: str
    HideAdvanced: str
    HideBooks: str
    History: str
    HomePage: str
    Host: str
    HostHelpText: str
    Hostname: str
    Hours: str
    HttpHttps: str
    ICalFeed: str
    ICalHttpUrlHelpText: str
    iCalLink: str
    ICalLink: str
    IconForCutoffUnmet: str
    IconTooltip: str
    IfYouDontAddAnImportListExclusionAndTheAuthorHasAMetadataProfileOtherThanNoneThenThisBookMayBeReaddedDuringTheNextAuthorRefresh: str
    Ignored: str
    IgnoredAddresses: str
    IgnoreDeletedBooks: str
    IgnoreDeletedMovies: str
    IgnoredHelpText: str
    IgnoredMetaHelpText: str
    IgnoredPlaceHolder: str
    IllRestartLater: str
    Images: str
    IMDb: str
    ImdbRating: str
    ImdbVotes: str
    Import: str
    ImportCustomFormat: str
    Imported: str
    ImportedTo: str
    ImportErrors: str
    ImportExistingMovies: str
    ImportExtraFiles: str
    ImportExtraFilesHelpText: str
    ImportFailed: str
    ImportFailedInterp: str
    ImportFailures: str
    ImportHeader: str
    ImportIncludeQuality: str
    Importing: str
    ImportLibrary: str
    ImportListExclusions: str
    ImportListMissingRoot: str
    ImportListMultipleMissingRoots: str
    ImportLists: str
    ImportListSettings: str
    ImportListSpecificSettings: str
    ImportListStatusCheckAllClientMessage: str
    ImportListStatusCheckSingleClientMessage: str
    ImportListSyncIntervalHelpText: str
    ImportMechanismHealthCheckMessage: str
    ImportMovies: str
    ImportNotForDownloads: str
    ImportRootPath: str
    ImportTipsMessage: str
    InCinemas: str
    InCinemasDate: str
    InCinemasMsg: str
    IncludeCustomFormatWhenRenaming: str
    IncludeCustomFormatWhenRenamingHelpText: str
    IncludeHealthWarningsHelpText: str
    IncludePreferredWhenRenaming: str
    IncludeRadarrRecommendations: str
    IncludeRecommendationsHelpText: str
    IncludeUnknownAuthorItemsHelpText: str
    IncludeUnknownMovieItemsHelpText: str
    IncludeUnmonitored: str
    Indexer: str
    IndexerDownloadClientHelpText: str
    IndexerFlags: str
    IndexerIdHelpText: str
    IndexerIdHelpTextWarning: str
    IndexerIdvalue0IncludeInPreferredWordsRenamingFormat: str
    IndexerIdvalue0OnlySupportedWhenIndexerIsSetToAll: str
    IndexerJackettAll: str
    IndexerLongTermStatusCheckAllClientMessage: str
    IndexerLongTermStatusCheckSingleClientMessage: str
    IndexerPriority: str
    IndexerPriorityHelpText: str
    IndexerRssHealthCheckNoAvailableIndexers: str
    IndexerRssHealthCheckNoIndexers: str
    Indexers: str
    IndexerSearchCheckNoAutomaticMessage: str
    IndexerSearchCheckNoAvailableIndexersMessage: str
    IndexerSearchCheckNoInteractiveMessage: str
    IndexerSettings: str
    IndexersSettingsSummary: str
    IndexerStatusCheckAllClientMessage: str
    IndexerStatusCheckSingleClientMessage: str
    IndexerTagHelpText: str
    Info: str
    InstallLatest: str
    InteractiveImport: str
    InteractiveImportErrLanguage: str
    InteractiveImportErrMovie: str
    InteractiveImportErrQuality: str
    InteractiveSearch: str
    Interval: str
    InvalidFormat: str
    ISBN: str
    IsCalibreLibraryHelpText: str
    IsCutoffCutoff: str
    IsCutoffUpgradeUntilThisQualityIsMetOrExceeded: str
    IsExpandedHideBooks: str
    IsExpandedHideFileInfo: str
    IsExpandedShowBooks: str
    IsExpandedShowFileInfo: str
    IsInUseCantDeleteAMetadataProfileThatIsAttachedToAnAuthorOrImportList: str
    IsInUseCantDeleteAQualityProfileThatIsAttachedToAnAuthorOrImportList: str
    IsShowingMonitoredMonitorSelected: str
    IsShowingMonitoredUnmonitorSelected: str
    IsTagUsedCannotBeDeletedWhileInUse: str
    KeepAndUnmonitorMovie: str
    KeyboardShortcuts: str
    Label: str
    Language: str
    LanguageHelpText: str
    Languages: str
    Large: str
    LastDuration: str
    LastExecution: str
    LastUsed: str
    LastWriteTime: str
    LatestBook: str
    LaunchBrowserHelpText: str
    Letterboxd: str
    Level: str
    LibraryHelpText: str
    LinkHere: str
    Links: str
    ListExclusions: str
    Lists: str
    ListSettings: str
    ListsSettingsSummary: str
    ListSyncLevelHelpText: str
    ListSyncLevelHelpTextWarning: str
    ListTagsHelpText: str
    ListUpdateInterval: str
    LoadingBookFilesFailed: str
    LoadingBooksFailed: str
    LoadingMovieCreditsFailed: str
    LoadingMovieExtraFilesFailed: str
    LoadingMovieFilesFailed: str
    Local: str
    LocalPath: str
    LocalPathHelpText: str
    Location: str
    LogFiles: str
    Logging: str
    LogLevel: str
    LogLevelTraceHelpTextWarning: str
    LogLevelvalueTraceTraceLoggingShouldOnlyBeEnabledTemporarily: str
    LogOnly: str
    LogRotateHelpText: str
    LogRotation: str
    Logs: str
    LogSQL: str
    LogSqlHelpText: str
    LongDateFormat: str
    LookingForReleaseProfiles1: str
    LookingForReleaseProfiles2: str
    LowerCase: str
    MaintenanceRelease: str
    Manual: str
    ManualDownload: str
    ManualImport: str
    ManualImportSelectLanguage: str
    ManualImportSelectMovie: str
    ManualImportSelectQuality: str
    ManualImportSetReleaseGroup: str
    MappedDrivesRunningAsService: str
    MarkAsFailed: str
    MarkAsFailedMessageText: str
    MassBookSearch: str
    MassBookSearchWarning: str
    MassMovieSearch: str
    Max: str
    MaximumLimits: str
    MaximumSize: str
    MaximumSizeHelpText: str
    Mechanism: str
    MediaInfo: str
    MediaManagement: str
    MediaManagementSettings: str
    MediaManagementSettingsSummary: str
    Medium: str
    MediumFormat: str
    MegabytesPerMinute: str
    Message: str
    Metadata: str
    MetadataConsumers: str
    MetadataProfile: str
    MetadataProfileIdHelpText: str
    MetadataProfiles: str
    MetadataProviderSource: str
    MetadataSettings: str
    MetadataSettingsSummary: str
    MetadataSource: str
    MetadataSourceHelpText: str
    MIA: str
    Min: str
    MinAvailability: str
    MinFormatScoreHelpText: str
    MinimumAge: str
    MinimumAgeHelpText: str
    MinimumAvailability: str
    MinimumCustomFormatScore: str
    MinimumFreeSpace: str
    MinimumFreeSpaceWhenImportingHelpText: str
    MinimumLimits: str
    MinimumPages: str
    MinimumPopularity: str
    MinPagesHelpText: str
    MinPopularityHelpText: str
    Minutes: str
    MinutesHundredTwenty: str
    MinutesNinety: str
    MinutesSixty: str
    Missing: str
    MissingBooks: str
    MissingBooksAuthorMonitored: str
    MissingBooksAuthorNotMonitored: str
    MissingFromDisk: str
    MissingMonitoredAndConsideredAvailable: str
    MissingNotMonitored: str
    Mode: str
    Monday: str
    Monitor: str
    MonitorAuthor: str
    MonitorBook: str
    MonitorBookExistingOnlyWarning: str
    Monitored: str
    MonitoredAuthorIsMonitored: str
    MonitoredAuthorIsUnmonitored: str
    MonitoredHelpText: str
    MonitoredOnly: str
    MonitoredStatus: str
    Monitoring: str
    MonitoringOptions: str
    MonitoringOptionsHelpText: str
    MonitorMovie: str
    MonitorNewItems: str
    MonitorNewItemsHelpText: str
    MonoVersion: str
    Month: str
    Months: str
    More: str
    MoreControlCFText: str
    MoreDetails: str
    MoreInfo: str
    MountCheckMessage: str
    MoveFiles: str
    MoveFolders1: str
    MoveFolders2: str
    Movie: str
    MovieAlreadyExcluded: str
    MovieChat: str
    MovieDetailsNextMovie: str
    MovieDetailsPreviousMovie: str
    MovieEditor: str
    MovieExcludedFromAutomaticAdd: str
    MovieFiles: str
    MovieFilesTotaling: str
    MovieFolderFormat: str
    MovieID: str
    MovieIndex: str
    MovieIndexScrollBottom: str
    MovieIndexScrollTop: str
    MovieInfoLanguage: str
    MovieInfoLanguageHelpText: str
    MovieInfoLanguageHelpTextWarning: str
    MovieInvalidFormat: str
    MovieIsDownloading: str
    MovieIsDownloadingInterp: str
    MovieIsMonitored: str
    MovieIsOnImportExclusionList: str
    MovieIsRecommend: str
    MovieIsUnmonitored: str
    MovieNaming: str
    Movies: str
    MoviesSelectedInterp: str
    MovieTitle: str
    MovieTitleHelpText: str
    MovieYear: str
    MovieYearHelpText: str
    MultiLanguage: str
    MusicBrainzAuthorID: str
    MusicBrainzBookID: str
    MusicbrainzId: str
    MusicBrainzRecordingID: str
    MusicBrainzReleaseID: str
    MusicBrainzTrackID: str
    MustContain: str
    MustNotContain: str
    Name: str
    NameFirstLast: str
    NameLastFirst: str
    NameStyle: str
    NamingSettings: str
    Negate: str
    Negated: str
    NegateHelpText: str
    NetCore: str
    NETCore: str
    New: str
    NewBooks: str
    NextExecution: str
    No: str
    NoAltTitle: str
    NoBackupsAreAvailable: str
    NoChange: str
    NoChanges: str
    NoEventsFound: str
    NoHistory: str
    NoHistoryBlocklist: str
    NoLeaveIt: str
    NoLimitForAnyRuntime: str
    NoLinks: str
    NoListRecommendations: str
    NoLogFiles: str
    NoMatchFound: str
    NoMinimumForAnyRuntime: str
    NoMoveFilesSelf: str
    NoMoviesExist: str
    NoName: str
    NoResultsFound: str
    NoTagsHaveBeenAddedYet: str
    NotAvailable: str
    NotificationTriggers: str
    NotificationTriggersHelpText: str
    NotMonitored: str
    NoUpdatesAreAvailable: str
    NoVideoFilesFoundSelectedFolder: str
    OAuthPopupMessage: str
    Ok: str
    OnApplicationUpdate: str
    OnApplicationUpdateHelpText: str
    OnBookRetagHelpText: str
    OnDownloadFailureHelpText: str
    OnDownloadHelpText: str
    OnGrab: str
    OnGrabHelpText: str
    OnHealthIssue: str
    OnHealthIssueHelpText: str
    OnImport: str
    OnImportFailureHelpText: str
    OnLatestVersion: str
    OnlyTorrent: str
    OnlyUsenet: str
    OnMovieDelete: str
    OnMovieDeleteHelpText: str
    OnMovieFileDelete: str
    OnMovieFileDeleteForUpgrade: str
    OnMovieFileDeleteForUpgradeHelpText: str
    OnMovieFileDeleteHelpText: str
    OnReleaseImportHelpText: str
    OnRename: str
    OnRenameHelpText: str
    OnUpgrade: str
    OnUpgradeHelpText: str
    OpenBrowserOnStart: str
    OpenThisModal: str
    Options: str
    Organize: str
    OrganizeAndRename: str
    OrganizeConfirm: str
    OrganizeModalAllPathsRelative: str
    OrganizeModalDisabled: str
    OrganizeModalNamingPattern: str
    OrganizeModalSuccess: str
    OrganizeSelectedMovies: str
    Original: str
    Other: str
    OutputFormatHelpText: str
    OutputPath: str
    Overview: str
    OverviewOptions: str
    PackageVersion: str
    PageSize: str
    PageSizeHelpText: str
    Password: str
    PasswordHelpText: str
    PastDays: str
    PastDaysHelpText: str
    Path: str
    PathHelpText: str
    PathHelpTextWarning: str
    Paused: str
    Peers: str
    Pending: str
    PendingChangesDiscardChanges: str
    PendingChangesMessage: str
    PendingChangesStayReview: str
    Permissions: str
    PhysicalRelease: str
    PhysicalReleaseDate: str
    Port: str
    PortHelpText: str
    PortHelpTextWarning: str
    PortNumber: str
    PosterOptions: str
    Posters: str
    PosterSize: str
    PreferAndUpgrade: str
    PreferIndexerFlags: str
    PreferIndexerFlagsHelpText: str
    Preferred: str
    PreferredHelpTexts1: str
    PreferredHelpTexts2: str
    PreferredHelpTexts3: str
    PreferredSize: str
    PreferTorrent: str
    PreferUsenet: str
    Presets: str
    PreviewRename: str
    PreviewRenameHelpText: str
    PreviewRetag: str
    Priority: str
    PriorityHelpText: str
    PrioritySettings: str
    ProcessingFolders: str
    Profiles: str
    ProfilesSettingsSummary: str
    Progress: str
    Proper: str
    PropersAndRepacks: str
    Protocol: str
    ProtocolHelpText: str
    Proxy: str
    ProxyBypassFilterHelpText: str
    ProxyCheckBadRequestMessage: str
    ProxyCheckFailedToTestMessage: str
    ProxyCheckResolveIpMessage: str
    ProxyPasswordHelpText: str
    ProxyType: str
    ProxyUsernameHelpText: str
    PtpOldSettingsCheckMessage: str
    PublishedDate: str
    Publisher: str
    Qualities: str
    QualitiesHelpText: str
    Quality: str
    QualityCutoffHasNotBeenMet: str
    QualityDefinitions: str
    QualityLimitsHelpText: str
    QualityOrLangCutoffHasNotBeenMet: str
    QualityProfile: str
    QualityProfileDeleteConfirm: str
    QualityProfileIdHelpText: str
    QualityProfileInUse: str
    QualityProfiles: str
    QualitySettings: str
    QualitySettingsSummary: str
    Queue: str
    Queued: str
    QueueIsEmpty: str
    QuickImport: str
    RadarrCalendarFeed: str
    RadarrSupportsAnyDownloadClient: str
    RadarrSupportsAnyIndexer: str
    RadarrSupportsAnyRSSMovieListsAsWellAsTheOneStatedBelow: str
    RadarrSupportsCustomConditionsAgainstTheReleasePropertiesBelow: str
    RadarrTags: str
    RadarrUpdated: str
    Ratings: str
    ReadarrSupportsAnyDownloadClientThatUsesTheNewznabStandardAsWellAsOtherDownloadClientsListedBelow: str
    ReadarrSupportsAnyIndexerThatUsesTheNewznabStandardAsWellAsOtherIndexersListedBelow: str
    ReadarrSupportsMultipleListsForImportingBooksAndAuthorsIntoTheDatabase: str
    ReadarrTags: str
    ReadTheWikiForMoreInformation: str
    Real: str
    Reason: str
    RecentChanges: str
    RecentFolders: str
    RecycleBinCleanupDaysHelpText: str
    RecycleBinCleanupDaysHelpTextWarning: str
    RecycleBinHelpText: str
    RecyclingBin: str
    RecyclingBinCleanup: str
    Reddit: str
    Redownload: str
    Refresh: str
    RefreshAndScan: str
    RefreshAuthor: str
    RefreshInformation: str
    RefreshInformationAndScanDisk: str
    RefreshLists: str
    RefreshMovie: str
    RefreshScan: str
    RegularExpressionsCanBeTested: str
    RejectionCount: str
    RelativePath: str
    ReleaseBranchCheckOfficialBranchMessage: str
    Released: str
    ReleaseDate: str
    ReleaseDates: str
    ReleasedMsg: str
    ReleaseGroup: str
    ReleaseProfiles: str
    ReleaseRejected: str
    ReleaseStatus: str
    ReleaseTitle: str
    ReleaseWillBeProcessedInterp: str
    Reload: str
    RemotePath: str
    RemotePathHelpText: str
    RemotePathMappingCheckBadDockerPath: str
    RemotePathMappingCheckDockerFolderMissing: str
    RemotePathMappingCheckDownloadPermissions: str
    RemotePathMappingCheckFileRemoved: str
    RemotePathMappingCheckFilesBadDockerPath: str
    RemotePathMappingCheckFilesGenericPermissions: str
    RemotePathMappingCheckFilesLocalWrongOSPath: str
    RemotePathMappingCheckFilesWrongOSPath: str
    RemotePathMappingCheckFolderPermissions: str
    RemotePathMappingCheckGenericPermissions: str
    RemotePathMappingCheckImportFailed: str
    RemotePathMappingCheckLocalFolderMissing: str
    RemotePathMappingCheckLocalWrongOSPath: str
    RemotePathMappingCheckRemoteDownloadClient: str
    RemotePathMappingCheckWrongOSPath: str
    RemotePathMappings: str
    Remove: str
    RemoveCompleted: str
    RemoveCompletedDownloadsHelpText: str
    RemovedFromTaskQueue: str
    RemovedMovieCheckMultipleMessage: str
    RemovedMovieCheckSingleMessage: str
    RemoveDownloadsAlert: str
    RemoveFailed: str
    RemoveFailedDownloadsHelpText: str
    RemoveFilter: str
    RemoveFromBlocklist: str
    RemoveFromDownloadClient: str
    RemoveFromQueue: str
    RemoveFromQueueText: str
    RemoveHelpTextWarning: str
    RemoveMovieAndDeleteFiles: str
    RemoveMovieAndKeepFiles: str
    RemoveRootFolder: str
    RemoveSelected: str
    RemoveSelectedItem: str
    RemoveSelectedItems: str
    RemoveSelectedMessageText: str
    RemoveTagExistingTag: str
    RemoveTagRemovingTag: str
    RemovingTag: str
    RenameBooks: str
    RenameBooksHelpText: str
    Renamed: str
    RenameFiles: str
    RenameMovies: str
    RenameMoviesHelpText: str
    Reorder: str
    Replace: str
    ReplaceIllegalCharacters: str
    ReplaceIllegalCharactersHelpText: str
    ReplaceWithDash: str
    ReplaceWithSpaceDash: str
    ReplaceWithSpaceDashSpace: str
    Required: str
    RequiredHelpText: str
    RequiredPlaceHolder: str
    RequiredRestrictionHelpText: str
    RequiredRestrictionPlaceHolder: str
    RescanAfterRefreshHelpText: str
    RescanAfterRefreshHelpTextWarning: str
    RescanAuthorFolderAfterRefresh: str
    RescanMovieFolderAfterRefresh: str
    Reset: str
    ResetAPIKey: str
    ResetAPIKeyMessageText: str
    Restart: str
    RestartNow: str
    RestartRadarr: str
    RestartReadarr: str
    RestartReloadNote: str
    RestartRequiredHelpTextWarning: str
    Restore: str
    RestoreBackup: str
    Restrictions: str
    Result: str
    Retention: str
    RetentionHelpText: str
    RetryingDownloadInterp: str
    RootFolder: str
    RootFolderCheckMultipleMessage: str
    RootFolderCheckSingleMessage: str
    RootFolderPathHelpText: str
    RootFolders: str
    RSS: str
    RSSIsNotSupportedWithThisIndexer: str
    RSSSync: str
    RSSSyncInterval: str
    RssSyncIntervalHelpText: str
    RSSSyncIntervalHelpTextWarning: str
    Runtime: str
    Save: str
    SaveChanges: str
    SaveSettings: str
    SceneInformation: str
    SceneNumberHasntBeenVerifiedYet: str
    Scheduled: str
    Score: str
    Script: str
    ScriptPath: str
    Search: str
    SearchAll: str
    SearchBook: str
    SearchBoxPlaceHolder: str
    SearchCutoffUnmet: str
    SearchFailedPleaseTryAgainLater: str
    SearchFiltered: str
    SearchForAllCutoffUnmetBooks: str
    SearchForAllMissingBooks: str
    SearchForMissing: str
    SearchForMonitoredBooks: str
    SearchForMovie: str
    SearchForNewItems: str
    SearchMissing: str
    SearchMonitored: str
    SearchMovie: str
    SearchOnAdd: str
    SearchOnAddHelpText: str
    SearchSelected: str
    Season: str
    Seconds: str
    Security: str
    Seeders: str
    SelectAll: str
    SelectDotDot: str
    SelectedCountAuthorsSelectedInterp: str
    SelectedCountBooksSelectedInterp: str
    SelectFolder: str
    SelectLanguage: str
    SelectLanguages: str
    SelectMovie: str
    SelectQuality: str
    SelectReleaseGroup: str
    SendAnonymousUsageData: str
    SendMetadataToCalibre: str
    Series: str
    SeriesNumber: str
    SeriesTotal: str
    SetPermissions: str
    SetPermissionsLinuxHelpText: str
    SetPermissionsLinuxHelpTextWarning: str
    SetReleaseGroup: str
    SetTags: str
    Settings: str
    SettingsEnableColorImpairedMode: str
    SettingsEnableColorImpairedModeHelpText: str
    SettingsFirstDayOfWeek: str
    SettingsLongDateFormat: str
    SettingsRemotePathMappingHostHelpText: str
    SettingsRemotePathMappingLocalPath: str
    SettingsRemotePathMappingLocalPathHelpText: str
    SettingsRemotePathMappingRemotePath: str
    SettingsRemotePathMappingRemotePathHelpText: str
    SettingsRuntimeFormat: str
    SettingsShortDateFormat: str
    SettingsShowRelativeDates: str
    SettingsShowRelativeDatesHelpText: str
    SettingsTimeFormat: str
    SettingsWeekColumnHeader: str
    SettingsWeekColumnHeaderHelpText: str
    ShortDateFormat: str
    ShouldMonitorExisting: str
    ShouldMonitorExistingHelpText: str
    ShouldMonitorHelpText: str
    ShouldSearchHelpText: str
    ShowAdvanced: str
    ShowAsAllDayEvents: str
    ShowBanners: str
    ShowBannersHelpText: str
    ShowBookCount: str
    ShowBookTitleHelpText: str
    ShowCertification: str
    ShowCinemaRelease: str
    showCinemaReleaseHelpText: str
    ShowCutoffUnmetIconHelpText: str
    ShowDateAdded: str
    ShowGenres: str
    ShowLastBook: str
    ShowMonitored: str
    ShowMonitoredHelpText: str
    ShowMovieInformation: str
    ShowMovieInformationHelpText: str
    ShownAboveEachColumnWhenWeekIsTheActiveView: str
    ShowName: str
    ShownClickToHide: str
    ShowPath: str
    ShowQualityProfile: str
    ShowQualityProfileHelpText: str
    ShowRatings: str
    ShowRelativeDates: str
    ShowRelativeDatesHelpText: str
    ShowReleaseDate: str
    ShowReleaseDateHelpText: str
    ShowSearch: str
    ShowSearchActionHelpText: str
    ShowSearchHelpText: str
    ShowSizeOnDisk: str
    ShowStudio: str
    ShowTitle: str
    ShowTitleHelpText: str
    ShowUnknownAuthorItems: str
    ShowUnknownMovieItems: str
    ShowYear: str
    Shutdown: str
    Size: str
    SizeLimit: str
    SizeOnDisk: str
    SkipBooksWithMissingReleaseDate: str
    SkipBooksWithNoISBNOrASIN: str
    SkipFreeSpaceCheck: str
    SkipFreeSpaceCheckWhenImportingHelpText: str
    SkipPartBooksAndSets: str
    SkipRedownload: str
    SkipredownloadHelpText: str
    SkipSecondarySeriesBooks: str
    Small: str
    Socks4: str
    Socks5: str
    SomeResultsHiddenFilter: str
    SorryThatAuthorCannotBeFound: str
    SorryThatBookCannotBeFound: str
    SorryThatMovieCannotBeFound: str
    Sort: str
    Source: str
    SourcePath: str
    SourceRelativePath: str
    SourceTitle: str
    SpecificBook: str
    SqliteVersionCheckUpgradeRequiredMessage: str
    SSLCertPassword: str
    SslCertPasswordHelpText: str
    SSLCertPasswordHelpText: str
    SslCertPasswordHelpTextWarning: str
    SSLCertPath: str
    SslCertPathHelpText: str
    SSLCertPathHelpText: str
    SslCertPathHelpTextWarning: str
    SSLPort: str
    SslPortHelpTextWarning: str
    StandardBookFormat: str
    StandardMovieFormat: str
    StartImport: str
    StartProcessing: str
    StartSearchForMissingMovie: str
    StartTypingOrSelectAPathBelow: str
    StartupDirectory: str
    Status: str
    StatusEndedContinuing: str
    StatusEndedDeceased: str
    StatusEndedEnded: str
    Studio: str
    Style: str
    SubfolderWillBeCreatedAutomaticallyInterp: str
    SuccessMyWorkIsDoneNoFilesToRename: str
    SuccessMyWorkIsDoneNoFilesToRetag: str
    SuggestTranslationChange: str
    Sunday: str
    SupportsRssvalueRSSIsNotSupportedWithThisIndexer: str
    SupportsSearchvalueSearchIsNotSupportedWithThisIndexer: str
    SupportsSearchvalueWillBeUsedWhenAutomaticSearchesArePerformedViaTheUIOrByReadarr: str
    SupportsSearchvalueWillBeUsedWhenInteractiveSearchIsUsed: str
    System: str
    SystemTimeCheckMessage: str
    Table: str
    TableOptions: str
    TableOptionsColumnsMessage: str
    TagCannotBeDeletedWhileInUse: str
    TagDetails: str
    TagIsNotUsedAndCanBeDeleted: str
    Tags: str
    TagsHelpText: str
    TagsSettingsSummary: str
    Tasks: str
    TaskUserAgentTooltip: str
    TBA: str
    Term: str
    Test: str
    TestAll: str
    TestAllClients: str
    TestAllIndexers: str
    TestAllLists: str
    TheAuthorFolderAndAllOfItsContentWillBeDeleted: str
    TheBooksFilesWillBeDeleted: str
    TheFollowingFilesWillBeDeleted: str
    TheLogLevelDefault: str
    ThisCannotBeCancelled: str
    ThisConditionMatchesUsingRegularExpressions: str
    ThisWillApplyToAllIndexersPleaseFollowTheRulesSetForthByThem: str
    Time: str
    TimeFormat: str
    Timeleft: str
    Title: str
    Titles: str
    TMDb: str
    TMDBId: str
    TmdbIdHelpText: str
    TmdbRating: str
    TmdbVotes: str
    Today: str
    Tomorrow: str
    TooManyBooks: str
    TorrentDelay: str
    TorrentDelayHelpText: str
    TorrentDelayTime: str
    Torrents: str
    TorrentsDisabled: str
    TotalBookCountBooksTotalBookFileCountBooksWithFilesInterp: str
    TotalFileSize: str
    TotalSpace: str
    Trace: str
    TrackNumber: str
    TrackTitle: str
    Trailer: str
    Trakt: str
    Trigger: str
    Type: str
    UI: str
    UILanguage: str
    UILanguageHelpText: str
    UILanguageHelpTextWarning: str
    UISettings: str
    UISettingsSummary: str
    UnableToAddANewConditionPleaseTryAgain: str
    UnableToAddANewCustomFormatPleaseTryAgain: str
    UnableToAddANewDownloadClientPleaseTryAgain: str
    UnableToAddANewImportListExclusionPleaseTryAgain: str
    UnableToAddANewIndexerPleaseTryAgain: str
    UnableToAddANewListExclusionPleaseTryAgain: str
    UnableToAddANewListPleaseTryAgain: str
    UnableToAddANewMetadataProfilePleaseTryAgain: str
    UnableToAddANewNotificationPleaseTryAgain: str
    UnableToAddANewQualityProfilePleaseTryAgain: str
    UnableToAddANewRemotePathMappingPleaseTryAgain: str
    UnableToAddANewRootFolderPleaseTryAgain: str
    UnableToAddRootFolder: str
    UnableToImportCheckLogs: str
    UnableToLoadAltTitle: str
    UnableToLoadBackups: str
    UnableToLoadBlocklist: str
    UnableToLoadCustomFormats: str
    UnableToLoadDelayProfiles: str
    UnableToLoadDownloadClientOptions: str
    UnableToLoadDownloadClients: str
    UnableToLoadGeneralSettings: str
    UnableToLoadHistory: str
    UnableToLoadImportListExclusions: str
    UnableToLoadIndexerOptions: str
    UnableToLoadIndexers: str
    UnableToLoadLanguages: str
    UnableToLoadListExclusions: str
    UnableToLoadListOptions: str
    UnableToLoadLists: str
    UnableToLoadManualImportItems: str
    UnableToLoadMediaManagementSettings: str
    UnableToLoadMetadata: str
    UnableToLoadMetadataProfiles: str
    UnableToLoadMetadataProviderSettings: str
    UnableToLoadMovies: str
    UnableToLoadNamingSettings: str
    UnableToLoadNotifications: str
    UnableToLoadQualities: str
    UnableToLoadQualityDefinitions: str
    UnableToLoadQualityProfiles: str
    UnableToLoadReleaseProfiles: str
    UnableToLoadRemotePathMappings: str
    UnableToLoadRestrictions: str
    UnableToLoadResultsIntSearch: str
    UnableToLoadRootFolders: str
    UnableToLoadTags: str
    UnableToLoadTheCalendar: str
    UnableToLoadUISettings: str
    UnableToUpdateRadarrDirectly: str
    Unavailable: str
    Ungroup: str
    Unlimited: str
    UnmappedFiles: str
    UnmappedFilesOnly: str
    UnmappedFolders: str
    Unmonitored: str
    UnmonitoredHelpText: str
    Unreleased: str
    UnsavedChanges: str
    UnselectAll: str
    UpdateAll: str
    UpdateAutomaticallyHelpText: str
    UpdateAvailable: str
    UpdateCheckStartupNotWritableMessage: str
    UpdateCheckStartupTranslocationMessage: str
    UpdateCheckUINotWritableMessage: str
    UpdateCovers: str
    UpdateCoversHelpText: str
    UpdateMechanismHelpText: str
    Updates: str
    UpdateScriptPathHelpText: str
    UpdateSelected: str
    UpdatingIsDisabledInsideADockerContainerUpdateTheContainerImageInstead: str
    UpgradeAllowedHelpText: str
    UpgradesAllowed: str
    UpgradeUntilCustomFormatScore: str
    UpgradeUntilQuality: str
    UpgradeUntilThisQualityIsMetOrExceeded: str
    UpperCase: str
    Uptime: str
    URLBase: str
    UrlBaseHelpText: str
    UrlBaseHelpTextWarning: str
    UseCalibreContentServer: str
    UseHardlinksInsteadOfCopy: str
    Usenet: str
    UsenetDelay: str
    UsenetDelayHelpText: str
    UsenetDelayTime: str
    UsenetDisabled: str
    UseProxy: str
    Username: str
    UsernameHelpText: str
    UseSSL: str
    UseSslHelpText: str
    UsingExternalUpdateMechanismBranchToUseToUpdateReadarr: str
    UsingExternalUpdateMechanismBranchUsedByExternalUpdateMechanism: str
    Version: str
    VersionUpdateText: str
    VideoCodec: str
    View: str
    VisitGithubCustomFormatsAphrodite: str
    WaitingToImport: str
    WaitingToProcess: str
    Wanted: str
    Warn: str
    WatchLibraryForChangesHelpText: str
    WatchRootFoldersForFileChanges: str
    Week: str
    WeekColumnHeader: str
    Weeks: str
    WhatsNew: str
    WhitelistedHardcodedSubsHelpText: str
    WhitelistedSubtitleTags: str
    Wiki: str
    WouldYouLikeToRestoreBackup: str
    WriteAudioTags: str
    WriteAudioTagsScrub: str
    WriteAudioTagsScrubHelp: str
    WriteBookTagsHelpTextWarning: str
    WriteTagsAll: str
    WriteTagsNew: str
    WriteTagsNo: str
    WriteTagsSync: str
    Year: str
    Yes: str
    YesCancel: str
    YesMoveFiles: str
    Yesterday: str
    YouCanAlsoSearch: str


@dataclass(init=False)
class _LogRecord(BaseModel):
    """Log record attributes."""

    exception: str
    exceptionType: str
    id: int
    level: str
    logger: str
    message: str
    time: datetime


@dataclass(init=False)
class _QualityProfileItems(_Common3):
    """Quality profile items attributes."""

    allowed: bool
    items: list[_QualityProfileItems] | None = None
    quality: type[_QualityInfo] = field(default=_QualityInfo)

    def __post_init__(self):
        self.items = [_QualityProfileItems(item) for item in self.items or []]
        self.quality = _QualityInfo(self.quality)


@dataclass(init=False)
class _ReleaseCommon(BaseModel):
    """Release common attributes."""

    age: int
    ageHours: float
    ageMinutes: float
    approved: bool
    commentUrl: str
    downloadAllowed: bool
    downloadUrl: str
    guid: str
    indexer: str
    indexerId: int
    infoHash: str
    infoUrl: str
    leechers: int
    magnetUrl: str
    protocol: ProtocolType
    publishDate: datetime
    qualityWeight: int
    rejected: bool
    rejections: list[_Rejection] | None = None
    releaseWeight: int
    sceneSource: bool
    seeders: int
    size: int
    temporarilyRejected: bool
    title: str

    def __post_init__(self):
        """Post init."""
        self.rejections = [_Rejection(x) for x in self.rejections or []]


@dataclass(init=False)
class _RecordCommon(BaseModel):
    """Record common attributes."""

    page: int
    pageSize: int
    sortDirection: str
    sortKey: str
    totalRecords: int


@dataclass(init=False)
class _ReleaseProfilePreferred(BaseModel):
    """Release profile preferred attributes."""

    key: str
    value: int


@dataclass(init=False)
class _Rename(BaseModel):
    """Rename attributes."""

    existingPath: str
    newPath: str


@dataclass(init=False)
class _Tag(BaseModel):
    """Tag attributes."""

    id: int
    label: str


@dataclass(init=False)
class _TagDetails(_Tag):
    """Tag details attributes."""

    delayProfileIds: list[int]
    importListIds: list[int]
    notificationIds: list[int]
    restrictionIds: list[int]


@dataclass(init=False)
class _UpdateChanges(BaseModel):
    """Update changes attributes."""

    fixed: list[str]
    new: list[str]


@dataclass(init=False)
class _TitleInfo(BaseModel):
    """Title info attributes."""

    title: str
    titleWithoutYear: str
    year: int


@dataclass(init=False)
class _Notification(BaseModel):
    """Notification attributes."""

    configContract: str
    implementation: str
    implementationName: str
    includeHealthWarnings: bool
    infoLink: str
    onDownload: bool
    onGrab: bool
    onHealthIssue: bool
    onRename: bool
    onUpgrade: bool
    supportsOnDownload: bool
    supportsOnGrab: bool
    supportsOnHealthIssue: bool
    supportsOnRename: bool
    supportsOnUpgrade: bool
    tags: list[int]


@dataclass(init=False)
class _RetagChange(BaseModel):
    """Retag change attributes."""

    field: str
    oldValue: str
    newValue: str


@dataclass(init=False)
class _HistoryCommon(BaseModel):
    """History common attributes."""

    age: int
    ageHours: float
    ageMinutes: float
    downloadClientName: str
    downloadUrl: str
    droppedPath: str
    fileId: int
    importedPath: str
    indexer: str
    nzbInfoUrl: str
    protocol: ProtocolType
    publishedDate: datetime
    reason: str
    releaseGroup: str
    size: int
    torrentInfoHash: str


@dataclass(init=False)
class _HistoryData(_HistoryCommon):
    """History data attributes."""

    downloadClient: str
    downloadForced: bool
    guid: str


@dataclass(init=False)
class _QualityCommon(BaseModel):
    """Quality common attributes."""

    quality: type[_Quality] = field(default=_Quality)
    qualityCutoffNotMet: bool

    def __post_init__(self):
        """Post init."""
        super().__post_init__()
        self.quality = _Quality(self.quality)


@dataclass(init=False)
class _Ratings(BaseModel):
    """Ratings attributes."""

    value: float
    votes: int


@dataclass(init=False)
class _Link(BaseModel):
    """Link attributes."""

    name: str
    url: str


@dataclass(init=False)
class _StatusMessage(BaseModel):
    """Status message attributes."""

    messages: list[str]
    title: str


@dataclass(init=False)
class _Editor(BaseModel):
    """Editor attributes."""

    applyTags: str
    deleteFiles: bool
    minimumAvailability: str
    monitored: bool
    moveFiles: bool
    qualityProfileId: int
    rootFolderPath: str
    tags: list[int]


@dataclass(init=False)
class _IsLoaded(BaseModel):
    """Is loaded attribute."""

    isLoaded: bool


@dataclass(init=False)
class _Rejection(BaseModel):
    """Rejection attributes."""

    reason: str
    type: str


@dataclass(init=False)
class _ManualImport(BaseModel):
    """Manual import attributes."""

    downloadId: str
    id: int
    name: str
    path: str
    quality: type[_Quality] = field(default=_Quality)
    qualityWeight: int
    rejections: list[_Rejection] | None = None
    size: int

    def __post_init__(self):
        """Post init."""
        self.quality = _Quality(self.quality)
        self.rejections = [_Rejection(x) for x in self.rejections or []]


@dataclass(init=False)
class _Monitor(BaseModel):
    """Sonarr series monitor attributes."""

    id: int
    monitored: bool


@dataclass(init=False)
class _MonitorOption(BaseModel):
    """Sonarr series monitor option attributes."""

    monitor: str | None = None
    monitorNewItems: str | None = None


@dataclass(init=False)
class _RootFolder(BaseModel):
    """Root folder attributes."""

    accessible: bool
    freeSpace: int
    id: int
    path: str
    unmappedFolders: list[_FilesystemFolder] | None = None

    def __post_init__(self):
        """Post init."""
        self.unmappedFolders = [
            _FilesystemFolder(unmap) for unmap in self.unmappedFolders or []
        ]


@dataclass(init=False)
class _RootFolderExended(_RootFolder):
    """Extended root folder attributes."""

    defaultMetadataProfileId: int
    defaultMonitorOption: str
    defaultNewItemMonitorOption: str
    defaultQualityProfileId: int
    defaultTags: list[int]
    name: str
    totalSpace: int
