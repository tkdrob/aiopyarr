"""Request Common Models. These are only for internal module use."""
# pylint: disable=invalid-name, too-many-instance-attributes, line-too-long, too-many-lines
from __future__ import annotations

from dataclasses import dataclass

from .base import BaseModel


@dataclass(init=False)
class _SelectOption(BaseModel):
    """Select options attributes."""

    name: str | None = None
    order: int | None = None
    value: str | list[str] | int | None = None


@dataclass(init=False)
class _SelectOptionExtended(_SelectOption):
    """Select options extended attributes."""

    dividerAfter: bool | None = None


@dataclass(init=False)
class _Fields(_SelectOption):
    """Fields attributes."""

    advanced: bool | None = None
    helpText: str | None = None
    label: str | None = None
    type: str | None = None
    hidden: str | None = None
    selectOptions: list[_SelectOptionExtended] | None = None

    def __post_init__(self):
        self.selectOptions = [
            _SelectOptionExtended(opt) for opt in self.selectOptions or []
        ]


@dataclass(init=False)
class _Common(BaseModel):
    """Common attributes."""

    fields: list[_Fields] | None = None
    implementation: str | None = None
    implementationName: str | None = None
    infoLink: str | None = None
    name: str | None = None

    def __post_init__(self):
        self.fields = [_Fields(field) for field in self.fields or []]


@dataclass(init=False)
class _Common2(BaseModel):
    """Common attributes."""

    downloadId: str | None = None
    eventType: str | None = None


@dataclass(init=False)
class _Common3(BaseModel):
    """Common attributes."""

    id: int | None = None
    name: str | None = None


@dataclass(init=False)
class _Common4(BaseModel):
    """Common attributes."""

    downloadClient: str | None = None
    downloadId: str | None = None
    estimatedCompletionTime: str | None = None
    indexer: str | None = None
    outputPath: str | None = None


@dataclass(init=False)
class _Common5(BaseModel):
    """Common attributes."""

    coverType: str | None = None
    url: str | None = None


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
    videoDynamicRangeType: str | None = None
    videoFps: float | None = None


@dataclass(init=False)
class _CommandBody(BaseModel):
    """Command body attributes."""

    completionMessage: str | None = None
    isExclusive: bool | None = None
    isNewMovie: bool | None = None
    isTypeExclusive: bool | None = None
    lastExecutionTime: str | None = None
    lastStartTime: str | None = None
    name: str | None = None
    requiresDiskAccess: bool | None = None
    sendUpdatesToClient: bool | None = None
    suppressMessages: bool | None = None
    trigger: str | None = None
    updateScheduledTask: bool | None = None


@dataclass(init=False)
class _CustomFilterAttr(BaseModel):
    """Custom filter attributes."""

    key: str | None = None
    type: str | None = None
    value: list[str] | None = None


@dataclass(init=False)
class _MetadataFields(_Fields):
    """Metadata fields attributes."""

    section: str | None = None


@dataclass(init=False)
class _FilesystemFolder(BaseModel):
    """Unmapped folder attributes."""

    name: str | None = None
    path: str | None = None


@dataclass(init=False)
class _FilesystemDirectory(_FilesystemFolder):
    """Filesystem directory attributes."""

    lastModified: str | None = None
    size: int | None = None
    type: str | None = None


@dataclass(init=False)
class _LocalizationStrings(BaseModel):
    """Localization strings attributes."""

    About: str | None = None
    Absolute: str | None = None
    AcceptConfirmationModal: str | None = None
    Actions: str | None = None
    Activity: str | None = None
    Add: str | None = None
    AddCustomFormat: str | None = None
    AddDelayProfile: str | None = None
    AddDownloadClient: str | None = None
    Added: str | None = None
    AddedAuthorSettings: str | None = None
    AddedToDownloadQueue: str | None = None
    AddExclusion: str | None = None
    AddImportListExclusionHelpText: str | None = None
    AddIndexer: str | None = None
    AddingTag: str | None = None
    AddList: str | None = None
    AddListExclusion: str | None = None
    AddMissing: str | None = None
    AddMovie: str | None = None
    AddMovies: str | None = None
    AddMoviesMonitored: str | None = None
    AddNew: str | None = None
    AddNewItem: str | None = None
    AddNewMessage: str | None = None
    AddNewMovie: str | None = None
    AddNewTmdbIdMessage: str | None = None
    AddNotification: str | None = None
    AddQualityProfile: str | None = None
    AddRemotePathMapping: str | None = None
    AddRestriction: str | None = None
    AddRootFolder: str | None = None
    AddToDownloadQueue: str | None = None
    AdvancedSettingsHiddenClickToShow: str | None = None
    AdvancedSettingsShownClickToHide: str | None = None
    AfterManualRefresh: str | None = None
    Age: str | None = None
    Agenda: str | None = None
    AgeWhenGrabbed: str | None = None
    All: str | None = None
    AllAuthorBooks: str | None = None
    AllBooks: str | None = None
    AllExpandedCollapseAll: str | None = None
    AllExpandedExpandAll: str | None = None
    AllFiles: str | None = None
    AllMoviesHiddenDueToFilter: str | None = None
    AllMoviesInPathHaveBeenImported: str | None = None
    AllowAuthorChangeClickToChangeAuthor: str | None = None
    AllowedLanguages: str | None = None
    AllowFingerprinting: str | None = None
    AllowFingerprintingHelpText: str | None = None
    AllowFingerprintingHelpTextWarning: str | None = None
    AllowHardcodedSubs: str | None = None
    AllowHardcodedSubsHelpText: str | None = None
    AllResultsHiddenFilter: str | None = None
    AlreadyInYourLibrary: str | None = None
    AlternateTitles: str | None = None
    AlternateTitleslength1Title: str | None = None
    AlternateTitleslength1Titles: str | None = None
    AlternativeTitle: str | None = None
    Always: str | None = None
    AnalyseVideoFiles: str | None = None
    Analytics: str | None = None
    AnalyticsEnabledHelpText: str | None = None
    AnalyticsEnabledHelpTextWarning: str | None = None
    Announced: str | None = None
    AnnouncedMsg: str | None = None
    AnyEditionOkHelpText: str | None = None
    ApiKey: str | None = None
    APIKey: str | None = None
    ApiKeyHelpTextWarning: str | None = None
    AppDataDirectory: str | None = None
    AppDataLocationHealthCheckMessage: str | None = None
    Apply: str | None = None
    ApplyTags: str | None = None
    ApplyTagsHelpTexts1: str | None = None
    ApplyTagsHelpTexts2: str | None = None
    ApplyTagsHelpTexts3: str | None = None
    ApplyTagsHelpTexts4: str | None = None
    AptUpdater: str | None = None
    AreYouSureYouWantToDeleteFormat: str | None = None
    AreYouSureYouWantToDeleteThisDelayProfile: str | None = None
    AreYouSureYouWantToDeleteThisImportListExclusion: str | None = None
    AreYouSureYouWantToDeleteThisRemotePathMapping: str | None = None
    AreYouSureYouWantToRemoveSelectedItemFromQueue: str | None = None
    AreYouSureYouWantToRemoveSelectedItemsFromQueue: str | None = None
    AreYouSureYouWantToRemoveTheSelectedItemsFromBlocklist: str | None = None
    AreYouSureYouWantToResetYourAPIKey: str | None = None
    AsAllDayHelpText: str | None = None
    ASIN: str | None = None
    AudioFileMetadata: str | None = None
    AudioInfo: str | None = None
    AuthBasic: str | None = None
    Authentication: str | None = None
    AuthenticationMethodHelpText: str | None = None
    AuthForm: str | None = None
    Author: str | None = None
    AuthorClickToChangeBook: str | None = None
    AuthorEditor: str | None = None
    AuthorFolderFormat: str | None = None
    AuthorIndex: str | None = None
    AuthorNameHelpText: str | None = None
    Authors: str | None = None
    Automatic: str | None = None
    AutomaticallySwitchEdition: str | None = None
    AutomaticSearch: str | None = None
    AutoRedownloadFailedHelpText: str | None = None
    AutoUnmonitorPreviouslyDownloadedBooksHelpText: str | None = None
    AutoUnmonitorPreviouslyDownloadedMoviesHelpText: str | None = None
    AvailabilityDelay: str | None = None
    AvailabilityDelayHelpText: str | None = None
    Backup: str | None = None
    BackupFolderHelpText: str | None = None
    BackupIntervalHelpText: str | None = None
    BackupNow: str | None = None
    BackupRetentionHelpText: str | None = None
    Backups: str | None = None
    BeforeUpdate: str | None = None
    BindAddress: str | None = None
    BindAddressHelpText: str | None = None
    BindAddressHelpTextWarning: str | None = None
    Blocklist: str | None = None
    Blocklisted: str | None = None
    BlocklistHelpText: str | None = None
    BlocklistRelease: str | None = None
    BlocklistReleases: str | None = None
    Book: str | None = None
    BookAvailableButMissing: str | None = None
    BookDownloaded: str | None = None
    BookEditor: str | None = None
    BookFileCountBookCountTotalTotalBookCountInterp: str | None = None
    BookFileCounttotalBookCountBooksDownloadedInterp: str | None = None
    BookFilesCountMessage: str | None = None
    BookHasNotAired: str | None = None
    BookIndex: str | None = None
    BookIsDownloading: str | None = None
    BookIsDownloadingInterp: str | None = None
    BookIsNotMonitored: str | None = None
    BookList: str | None = None
    BookMissingFromDisk: str | None = None
    BookMonitoring: str | None = None
    BookNaming: str | None = None
    Books: str | None = None
    BooksTotal: str | None = None
    BookStudio: str | None = None
    BookTitle: str | None = None
    Branch: str | None = None
    BranchUpdate: str | None = None
    BranchUpdateMechanism: str | None = None
    BuiltIn: str | None = None
    BypassDelayIfHighestQuality: str | None = None
    BypassDelayIfHighestQualityHelpText: str | None = None
    BypassProxyForLocalAddresses: str | None = None
    Calendar: str | None = None
    CalendarOptions: str | None = None
    CalendarWeekColumnHeaderHelpText: str | None = None
    CalibreContentServer: str | None = None
    CalibreContentServerText: str | None = None
    CalibreHost: str | None = None
    CalibreLibrary: str | None = None
    CalibreMetadata: str | None = None
    CalibreNotCalibreWeb: str | None = None
    CalibreOutputFormat: str | None = None
    CalibreOutputProfile: str | None = None
    CalibrePassword: str | None = None
    CalibrePort: str | None = None
    CalibreSettings: str | None = None
    CalibreUrlBase: str | None = None
    CalibreUsername: str | None = None
    Cancel: str | None = None
    CancelMessageText: str | None = None
    CancelPendingTask: str | None = None
    CancelProcessing: str | None = None
    CantFindMovie: str | None = None
    Cast: str | None = None
    CatalogNumber: str | None = None
    CertificateValidation: str | None = None
    CertificateValidationHelpText: str | None = None
    Certification: str | None = None
    CertificationCountry: str | None = None
    CertificationCountryHelpText: str | None = None
    CertValidationNoLocal: str | None = None
    ChangeFileDate: str | None = None
    ChangeHasNotBeenSavedYet: str | None = None
    CheckDownloadClientForDetails: str | None = None
    CheckForFinishedDownloadsInterval: str | None = None
    ChmodFolder: str | None = None
    ChmodFolderHelpText: str | None = None
    ChmodFolderHelpTextWarning: str | None = None
    ChmodGroup: str | None = None
    ChmodGroupHelpText: str | None = None
    ChmodGroupHelpTextWarning: str | None = None
    ChooseAnotherFolder: str | None = None
    ChownGroup: str | None = None
    ChownGroupHelpText: str | None = None
    ChownGroupHelpTextWarning: str | None = None
    CleanLibraryLevel: str | None = None
    Clear: str | None = None
    ClickToChangeLanguage: str | None = None
    ClickToChangeMovie: str | None = None
    ClickToChangeQuality: str | None = None
    ClickToChangeReleaseGroup: str | None = None
    ClientPriority: str | None = None
    CloneCustomFormat: str | None = None
    CloneFormatTag: str | None = None
    CloneIndexer: str | None = None
    CloneProfile: str | None = None
    Close: str | None = None
    CloseCurrentModal: str | None = None
    CollapseMultipleBooks: str | None = None
    CollapseMultipleBooksHelpText: str | None = None
    Collection: str | None = None
    ColonReplacement: str | None = None
    ColonReplacementFormatHelpText: str | None = None
    Columns: str | None = None
    CompletedDownloadHandling: str | None = None
    Component: str | None = None
    Conditions: str | None = None
    Connect: str | None = None
    Connection: str | None = None
    ConnectionLost: str | None = None
    ConnectionLostAutomaticMessage: str | None = None
    ConnectionLostMessage: str | None = None
    Connections: str | None = None
    ConnectSettings: str | None = None
    ConnectSettingsSummary: str | None = None
    ConsideredAvailable: str | None = None
    ConsoleLogLevel: str | None = None
    Continuing: str | None = None
    ContinuingAllBooksDownloaded: str | None = None
    ContinuingMoreBooksAreExpected: str | None = None
    ContinuingNoAdditionalBooksAreExpected: str | None = None
    CopyToClipboard: str | None = None
    CopyUsingHardlinksHelpText: str | None = None
    CopyUsingHardlinksHelpTextWarning: str | None = None
    CouldNotConnectSignalR: str | None = None
    CouldNotFindResults: str | None = None
    Country: str | None = None
    CreateEmptyAuthorFolders: str | None = None
    CreateEmptyAuthorFoldersHelpText: str | None = None
    CreateEmptyMovieFolders: str | None = None
    CreateEmptyMovieFoldersHelpText: str | None = None
    CreateGroup: str | None = None
    Crew: str | None = None
    CurrentlyInstalled: str | None = None
    Custom: str | None = None
    CustomFilters: str | None = None
    CustomFormat: str | None = None
    CustomFormatHelpText: str | None = None
    CustomFormatJSON: str | None = None
    CustomFormats: str | None = None
    CustomFormatScore: str | None = None
    CustomFormatsSettings: str | None = None
    CustomFormatsSettingsSummary: str | None = None
    CustomFormatUnknownCondition: str | None = None
    CustomFormatUnknownConditionOption: str | None = None
    Cutoff: str | None = None
    CutoffFormatScoreHelpText: str | None = None
    CutoffHelpText: str | None = None
    CutoffUnmet: str | None = None
    Date: str | None = None
    Dates: str | None = None
    Day: str | None = None
    Days: str | None = None
    DBMigration: str | None = None
    Debug: str | None = None
    DefaultCase: str | None = None
    DefaultDelayProfile: str | None = None
    DefaultMetadataProfileIdHelpText: str | None = None
    DefaultMonitorOptionHelpText: str | None = None
    DefaultQualityProfileIdHelpText: str | None = None
    DefaultReadarrTags: str | None = None
    DefaultTagsHelpText: str | None = None
    DelayingDownloadUntilInterp: str | None = None
    DelayProfile: str | None = None
    DelayProfiles: str | None = None
    Delete: str | None = None
    DeleteBackup: str | None = None
    DeleteBackupMessageText: str | None = None
    DeleteBookFile: str | None = None
    DeleteBookFileMessageText: str | None = None
    DeleteCustomFormat: str | None = None
    Deleted: str | None = None
    DeleteDelayProfile: str | None = None
    DeleteDelayProfileMessageText: str | None = None
    DeletedMsg: str | None = None
    DeleteDownloadClient: str | None = None
    DeleteDownloadClientMessageText: str | None = None
    DeleteEmptyFolders: str | None = None
    DeleteEmptyFoldersHelpText: str | None = None
    DeleteFile: str | None = None
    DeleteFileLabel: str | None = None
    DeleteFilesHelpText: str | None = None
    DeleteFilesLabel: str | None = None
    DeleteHeader: str | None = None
    DeleteImportList: str | None = None
    DeleteImportListExclusion: str | None = None
    DeleteImportListExclusionMessageText: str | None = None
    DeleteImportListMessageText: str | None = None
    DeleteIndexer: str | None = None
    DeleteIndexerMessageText: str | None = None
    DeleteList: str | None = None
    DeleteListMessageText: str | None = None
    DeleteMetadataProfile: str | None = None
    DeleteMetadataProfileMessageText: str | None = None
    DeleteMovieFolderHelpText: str | None = None
    DeleteMovieFolderLabel: str | None = None
    DeleteNotification: str | None = None
    DeleteNotificationMessageText: str | None = None
    DeleteQualityProfile: str | None = None
    DeleteQualityProfileMessageText: str | None = None
    DeleteReleaseProfile: str | None = None
    DeleteReleaseProfileMessageText: str | None = None
    DeleteRestriction: str | None = None
    DeleteRestrictionHelpText: str | None = None
    DeleteRootFolder: str | None = None
    DeleteRootFolderMessageText: str | None = None
    DeleteSelectedBookFiles: str | None = None
    DeleteSelectedBookFilesMessageText: str | None = None
    DeleteSelectedMovie: str | None = None
    DeleteSelectedMovieFiles: str | None = None
    DeleteSelectedMovieFilesMessage: str | None = None
    DeleteTag: str | None = None
    DeleteTagMessageText: str | None = None
    DeleteTheMovieFolder: str | None = None
    DestinationPath: str | None = None
    DestinationRelativePath: str | None = None
    DetailedProgressBar: str | None = None
    DetailedProgressBarHelpText: str | None = None
    Details: str | None = None
    Development: str | None = None
    DigitalRelease: str | None = None
    Disabled: str | None = None
    DiscCount: str | None = None
    DiscNumber: str | None = None
    Discord: str | None = None
    DiscordUrlInSlackNotification: str | None = None
    Discover: str | None = None
    DiskSpace: str | None = None
    Docker: str | None = None
    DockerUpdater: str | None = None
    Donations: str | None = None
    DoneEditingGroups: str | None = None
    DoNotPrefer: str | None = None
    DoNotUpgradeAutomatically: str | None = None
    Download: str | None = None
    DownloadClient: str | None = None
    DownloadClientCheckDownloadingToRoot: str | None = None
    DownloadClientCheckNoneAvailableMessage: str | None = None
    DownloadClientCheckUnableToCommunicateMessage: str | None = None
    DownloadClients: str | None = None
    DownloadClientSettings: str | None = None
    DownloadClientsSettingsSummary: str | None = None
    DownloadClientStatusCheckAllClientMessage: str | None = None
    DownloadClientStatusCheckSingleClientMessage: str | None = None
    DownloadClientUnavailable: str | None = None
    Downloaded: str | None = None
    DownloadedAndMonitored: str | None = None
    DownloadedButNotMonitored: str | None = None
    DownloadFailed: str | None = None
    DownloadFailedCheckDownloadClientForMoreDetails: str | None = None
    DownloadFailedInterp: str | None = None
    Downloading: str | None = None
    DownloadPropersAndRepacks: str | None = None
    DownloadPropersAndRepacksHelpText1: str | None = None
    DownloadPropersAndRepacksHelpText2: str | None = None
    DownloadPropersAndRepacksHelpTexts1: str | None = None
    DownloadPropersAndRepacksHelpTexts2: str | None = None
    DownloadPropersAndRepacksHelpTextWarning: str | None = None
    DownloadWarning: str | None = None
    DownloadWarningCheckDownloadClientForMoreDetails: str | None = None
    Edit: str | None = None
    EditAuthor: str | None = None
    EditCustomFormat: str | None = None
    EditDelayProfile: str | None = None
    EditGroups: str | None = None
    EditIndexer: str | None = None
    Edition: str | None = None
    EditionsHelpText: str | None = None
    EditListExclusion: str | None = None
    EditMovie: str | None = None
    EditMovieFile: str | None = None
    EditPerson: str | None = None
    EditQualityProfile: str | None = None
    EditRemotePathMapping: str | None = None
    EditRestriction: str | None = None
    EmbedMetadataHelpText: str | None = None
    EmbedMetadataInBookFiles: str | None = None
    Enable: str | None = None
    EnableAutoHelpText: str | None = None
    EnableAutomaticAdd: str | None = None
    EnableAutomaticAddHelpText: str | None = None
    EnableAutomaticSearch: str | None = None
    EnableAutomaticSearchHelpText: str | None = None
    EnableAutomaticSearchHelpTextWarning: str | None = None
    EnableColorImpairedMode: str | None = None
    EnableColorImpairedModeHelpText: str | None = None
    EnableCompletedDownloadHandlingHelpText: str | None = None
    Enabled: str | None = None
    EnabledHelpText: str | None = None
    EnableHelpText: str | None = None
    EnableInteractiveSearch: str | None = None
    EnableInteractiveSearchHelpText: str | None = None
    EnableInteractiveSearchHelpTextWarning: str | None = None
    EnableMediaInfoHelpText: str | None = None
    EnableProfile: str | None = None
    EnableRSS: str | None = None
    EnableSSL: str | None = None
    EnableSslHelpText: str | None = None
    Ended: str | None = None
    EndedAllBooksDownloaded: str | None = None
    EntityName: str | None = None
    Episode: str | None = None
    EpisodeDoesNotHaveAnAbsoluteEpisodeNumber: str | None = None
    Error: str | None = None
    ErrorLoadingContents: str | None = None
    ErrorLoadingPreviews: str | None = None
    ErrorRestoringBackup: str | None = None
    Events: str | None = None
    EventType: str | None = None
    Exception: str | None = None
    Excluded: str | None = None
    ExcludeMovie: str | None = None
    ExcludeTitle: str | None = None
    Existing: str | None = None
    ExistingBooks: str | None = None
    ExistingItems: str | None = None
    ExistingMovies: str | None = None
    ExistingTag: str | None = None
    ExistingTagsScrubbed: str | None = None
    ExportCustomFormat: str | None = None
    Extension: str | None = None
    ExternalUpdater: str | None = None
    ExtraFileExtensionsHelpTexts1: str | None = None
    ExtraFileExtensionsHelpTexts2: str | None = None
    Failed: str | None = None
    FailedDownloadHandling: str | None = None
    FailedLoadingSearchResults: str | None = None
    FailedToLoadMovieFromAPI: str | None = None
    FailedToLoadQueue: str | None = None
    FeatureRequests: str | None = None
    FileDateHelpText: str | None = None
    FileDetails: str | None = None
    FileManagement: str | None = None
    Filename: str | None = None
    FileNames: str | None = None
    FileNameTokens: str | None = None
    Files: str | None = None
    FilesTotal: str | None = None
    FileWasDeletedByUpgrade: str | None = None
    FileWasDeletedByViaUI: str | None = None
    Filter: str | None = None
    FilterAnalyticsEvents: str | None = None
    FilterAuthor: str | None = None
    FilterPlaceHolder: str | None = None
    Filters: str | None = None
    FilterSentryEventsHelpText: str | None = None
    FirstBook: str | None = None
    FirstDayOfWeek: str | None = None
    Fixed: str | None = None
    FocusSearchBox: str | None = None
    Folder: str | None = None
    FolderMoveRenameWarning: str | None = None
    Folders: str | None = None
    FollowPerson: str | None = None
    Forecast: str | None = None
    ForeignIdHelpText: str | None = None
    Formats: str | None = None
    ForMoreInformationOnTheIndividualDownloadClients: str | None = None
    ForMoreInformationOnTheIndividualDownloadClientsClickOnTheInfoButtons: str | None = (
        None
    )
    ForMoreInformationOnTheIndividualImportListsClinkOnTheInfoButtons: str | None = None
    ForMoreInformationOnTheIndividualIndexers: str | None = None
    ForMoreInformationOnTheIndividualIndexersClickOnTheInfoButtons: str | None = None
    ForMoreInformationOnTheIndividualListsClickOnTheInfoButtons: str | None = None
    FreeSpace: str | None = None
    From: str | None = None
    FutureBooks: str | None = None
    FutureDays: str | None = None
    FutureDaysHelpText: str | None = None
    General: str | None = None
    GeneralSettings: str | None = None
    GeneralSettingsSummary: str | None = None
    Genres: str | None = None
    Global: str | None = None
    GoToAuthorListing: str | None = None
    GoToInterp: str | None = None
    Grab: str | None = None
    Grabbed: str | None = None
    GrabID: str | None = None
    GrabRelease: str | None = None
    GrabReleaseMessageText: str | None = None
    GrabSelected: str | None = None
    Group: str | None = None
    HardlinkCopyFiles: str | None = None
    HasMonitoredBooksNoMonitoredBooksForThisAuthor: str | None = None
    HasPendingChangesNoChanges: str | None = None
    HasPendingChangesSaveChanges: str | None = None
    HaveNotAddedMovies: str | None = None
    Health: str | None = None
    HealthNoIssues: str | None = None
    HelpText: str | None = None
    HiddenClickToShow: str | None = None
    HideAdvanced: str | None = None
    HideBooks: str | None = None
    History: str | None = None
    HomePage: str | None = None
    Host: str | None = None
    HostHelpText: str | None = None
    Hostname: str | None = None
    Hours: str | None = None
    HttpHttps: str | None = None
    ICalFeed: str | None = None
    ICalHttpUrlHelpText: str | None = None
    iCalLink: str | None = None
    ICalLink: str | None = None
    IconForCutoffUnmet: str | None = None
    IconTooltip: str | None = None
    IfYouDontAddAnImportListExclusionAndTheAuthorHasAMetadataProfileOtherThanNoneThenThisBookMayBeReaddedDuringTheNextAuthorRefresh: str | None = (
        None
    )
    Ignored: str | None = None
    IgnoredAddresses: str | None = None
    IgnoreDeletedBooks: str | None = None
    IgnoreDeletedMovies: str | None = None
    IgnoredHelpText: str | None = None
    IgnoredMetaHelpText: str | None = None
    IgnoredPlaceHolder: str | None = None
    IllRestartLater: str | None = None
    Images: str | None = None
    IMDb: str | None = None
    ImdbRating: str | None = None
    ImdbVotes: str | None = None
    Import: str | None = None
    ImportCustomFormat: str | None = None
    Imported: str | None = None
    ImportedTo: str | None = None
    ImportErrors: str | None = None
    ImportExistingMovies: str | None = None
    ImportExtraFiles: str | None = None
    ImportExtraFilesHelpText: str | None = None
    ImportFailed: str | None = None
    ImportFailedInterp: str | None = None
    ImportFailures: str | None = None
    ImportHeader: str | None = None
    ImportIncludeQuality: str | None = None
    Importing: str | None = None
    ImportLibrary: str | None = None
    ImportListExclusions: str | None = None
    ImportListMissingRoot: str | None = None
    ImportListMultipleMissingRoots: str | None = None
    ImportLists: str | None = None
    ImportListSettings: str | None = None
    ImportListSpecificSettings: str | None = None
    ImportListStatusCheckAllClientMessage: str | None = None
    ImportListStatusCheckSingleClientMessage: str | None = None
    ImportListSyncIntervalHelpText: str | None = None
    ImportMechanismHealthCheckMessage: str | None = None
    ImportMovies: str | None = None
    ImportNotForDownloads: str | None = None
    ImportRootPath: str | None = None
    ImportTipsMessage: str | None = None
    InCinemas: str | None = None
    InCinemasDate: str | None = None
    InCinemasMsg: str | None = None
    IncludeCustomFormatWhenRenaming: str | None = None
    IncludeCustomFormatWhenRenamingHelpText: str | None = None
    IncludeHealthWarningsHelpText: str | None = None
    IncludePreferredWhenRenaming: str | None = None
    IncludeRadarrRecommendations: str | None = None
    IncludeRecommendationsHelpText: str | None = None
    IncludeUnknownAuthorItemsHelpText: str | None = None
    IncludeUnknownMovieItemsHelpText: str | None = None
    IncludeUnmonitored: str | None = None
    Indexer: str | None = None
    IndexerDownloadClientHelpText: str | None = None
    IndexerFlags: str | None = None
    IndexerIdHelpText: str | None = None
    IndexerIdHelpTextWarning: str | None = None
    IndexerIdvalue0IncludeInPreferredWordsRenamingFormat: str | None = None
    IndexerIdvalue0OnlySupportedWhenIndexerIsSetToAll: str | None = None
    IndexerJackettAll: str | None = None
    IndexerLongTermStatusCheckAllClientMessage: str | None = None
    IndexerLongTermStatusCheckSingleClientMessage: str | None = None
    IndexerPriority: str | None = None
    IndexerPriorityHelpText: str | None = None
    IndexerRssHealthCheckNoAvailableIndexers: str | None = None
    IndexerRssHealthCheckNoIndexers: str | None = None
    Indexers: str | None = None
    IndexerSearchCheckNoAutomaticMessage: str | None = None
    IndexerSearchCheckNoAvailableIndexersMessage: str | None = None
    IndexerSearchCheckNoInteractiveMessage: str | None = None
    IndexerSettings: str | None = None
    IndexersSettingsSummary: str | None = None
    IndexerStatusCheckAllClientMessage: str | None = None
    IndexerStatusCheckSingleClientMessage: str | None = None
    IndexerTagHelpText: str | None = None
    Info: str | None = None
    InstallLatest: str | None = None
    InteractiveImport: str | None = None
    InteractiveImportErrLanguage: str | None = None
    InteractiveImportErrMovie: str | None = None
    InteractiveImportErrQuality: str | None = None
    InteractiveSearch: str | None = None
    Interval: str | None = None
    InvalidFormat: str | None = None
    ISBN: str | None = None
    IsCalibreLibraryHelpText: str | None = None
    IsCutoffCutoff: str | None = None
    IsCutoffUpgradeUntilThisQualityIsMetOrExceeded: str | None = None
    IsExpandedHideBooks: str | None = None
    IsExpandedHideFileInfo: str | None = None
    IsExpandedShowBooks: str | None = None
    IsExpandedShowFileInfo: str | None = None
    IsInUseCantDeleteAMetadataProfileThatIsAttachedToAnAuthorOrImportList: str | None = (
        None
    )
    IsInUseCantDeleteAQualityProfileThatIsAttachedToAnAuthorOrImportList: str | None = (
        None
    )
    IsShowingMonitoredMonitorSelected: str | None = None
    IsShowingMonitoredUnmonitorSelected: str | None = None
    IsTagUsedCannotBeDeletedWhileInUse: str | None = None
    KeepAndUnmonitorMovie: str | None = None
    KeyboardShortcuts: str | None = None
    Label: str | None = None
    Language: str | None = None
    LanguageHelpText: str | None = None
    Languages: str | None = None
    Large: str | None = None
    LastDuration: str | None = None
    LastExecution: str | None = None
    LastUsed: str | None = None
    LastWriteTime: str | None = None
    LatestBook: str | None = None
    LaunchBrowserHelpText: str | None = None
    Letterboxd: str | None = None
    Level: str | None = None
    LibraryHelpText: str | None = None
    LinkHere: str | None = None
    Links: str | None = None
    ListExclusions: str | None = None
    Lists: str | None = None
    ListSettings: str | None = None
    ListsSettingsSummary: str | None = None
    ListSyncLevelHelpText: str | None = None
    ListSyncLevelHelpTextWarning: str | None = None
    ListTagsHelpText: str | None = None
    ListUpdateInterval: str | None = None
    LoadingBookFilesFailed: str | None = None
    LoadingBooksFailed: str | None = None
    LoadingMovieCreditsFailed: str | None = None
    LoadingMovieExtraFilesFailed: str | None = None
    LoadingMovieFilesFailed: str | None = None
    Local: str | None = None
    LocalPath: str | None = None
    LocalPathHelpText: str | None = None
    Location: str | None = None
    LogFiles: str | None = None
    Logging: str | None = None
    LogLevel: str | None = None
    LogLevelTraceHelpTextWarning: str | None = None
    LogLevelvalueTraceTraceLoggingShouldOnlyBeEnabledTemporarily: str | None = None
    LogOnly: str | None = None
    LogRotateHelpText: str | None = None
    LogRotation: str | None = None
    Logs: str | None = None
    LogSQL: str | None = None
    LogSqlHelpText: str | None = None
    LongDateFormat: str | None = None
    LookingForReleaseProfiles1: str | None = None
    LookingForReleaseProfiles2: str | None = None
    LowerCase: str | None = None
    MaintenanceRelease: str | None = None
    Manual: str | None = None
    ManualDownload: str | None = None
    ManualImport: str | None = None
    ManualImportSelectLanguage: str | None = None
    ManualImportSelectMovie: str | None = None
    ManualImportSelectQuality: str | None = None
    ManualImportSetReleaseGroup: str | None = None
    MappedDrivesRunningAsService: str | None = None
    MarkAsFailed: str | None = None
    MarkAsFailedMessageText: str | None = None
    MassBookSearch: str | None = None
    MassBookSearchWarning: str | None = None
    MassMovieSearch: str | None = None
    Max: str | None = None
    MaximumLimits: str | None = None
    MaximumSize: str | None = None
    MaximumSizeHelpText: str | None = None
    Mechanism: str | None = None
    MediaInfo: str | None = None
    MediaManagement: str | None = None
    MediaManagementSettings: str | None = None
    MediaManagementSettingsSummary: str | None = None
    Medium: str | None = None
    MediumFormat: str | None = None
    MegabytesPerMinute: str | None = None
    Message: str | None = None
    Metadata: str | None = None
    MetadataConsumers: str | None = None
    MetadataProfile: str | None = None
    MetadataProfileIdHelpText: str | None = None
    MetadataProfiles: str | None = None
    MetadataProviderSource: str | None = None
    MetadataSettings: str | None = None
    MetadataSettingsSummary: str | None = None
    MetadataSource: str | None = None
    MetadataSourceHelpText: str | None = None
    MIA: str | None = None
    Min: str | None = None
    MinAvailability: str | None = None
    MinFormatScoreHelpText: str | None = None
    MinimumAge: str | None = None
    MinimumAgeHelpText: str | None = None
    MinimumAvailability: str | None = None
    MinimumCustomFormatScore: str | None = None
    MinimumFreeSpace: str | None = None
    MinimumFreeSpaceWhenImportingHelpText: str | None = None
    MinimumLimits: str | None = None
    MinimumPages: str | None = None
    MinimumPopularity: str | None = None
    MinPagesHelpText: str | None = None
    MinPopularityHelpText: str | None = None
    Minutes: str | None = None
    MinutesHundredTwenty: str | None = None
    MinutesNinety: str | None = None
    MinutesSixty: str | None = None
    Missing: str | None = None
    MissingBooks: str | None = None
    MissingBooksAuthorMonitored: str | None = None
    MissingBooksAuthorNotMonitored: str | None = None
    MissingFromDisk: str | None = None
    MissingMonitoredAndConsideredAvailable: str | None = None
    MissingNotMonitored: str | None = None
    Mode: str | None = None
    Monday: str | None = None
    Monitor: str | None = None
    MonitorAuthor: str | None = None
    MonitorBook: str | None = None
    MonitorBookExistingOnlyWarning: str | None = None
    Monitored: str | None = None
    MonitoredAuthorIsMonitored: str | None = None
    MonitoredAuthorIsUnmonitored: str | None = None
    MonitoredHelpText: str | None = None
    MonitoredOnly: str | None = None
    MonitoredStatus: str | None = None
    Monitoring: str | None = None
    MonitoringOptions: str | None = None
    MonitoringOptionsHelpText: str | None = None
    MonitorMovie: str | None = None
    MonitorNewItems: str | None = None
    MonitorNewItemsHelpText: str | None = None
    MonoVersion: str | None = None
    Month: str | None = None
    Months: str | None = None
    More: str | None = None
    MoreControlCFText: str | None = None
    MoreDetails: str | None = None
    MoreInfo: str | None = None
    MountCheckMessage: str | None = None
    MoveFiles: str | None = None
    MoveFolders1: str | None = None
    MoveFolders2: str | None = None
    Movie: str | None = None
    MovieAlreadyExcluded: str | None = None
    MovieChat: str | None = None
    MovieDetailsNextMovie: str | None = None
    MovieDetailsPreviousMovie: str | None = None
    MovieEditor: str | None = None
    MovieExcludedFromAutomaticAdd: str | None = None
    MovieFiles: str | None = None
    MovieFilesTotaling: str | None = None
    MovieFolderFormat: str | None = None
    MovieID: str | None = None
    MovieIndex: str | None = None
    MovieIndexScrollBottom: str | None = None
    MovieIndexScrollTop: str | None = None
    MovieInfoLanguage: str | None = None
    MovieInfoLanguageHelpText: str | None = None
    MovieInfoLanguageHelpTextWarning: str | None = None
    MovieInvalidFormat: str | None = None
    MovieIsDownloading: str | None = None
    MovieIsDownloadingInterp: str | None = None
    MovieIsMonitored: str | None = None
    MovieIsOnImportExclusionList: str | None = None
    MovieIsRecommend: str | None = None
    MovieIsUnmonitored: str | None = None
    MovieNaming: str | None = None
    Movies: str | None = None
    MoviesSelectedInterp: str | None = None
    MovieTitle: str | None = None
    MovieTitleHelpText: str | None = None
    MovieYear: str | None = None
    MovieYearHelpText: str | None = None
    MultiLanguage: str | None = None
    MusicBrainzAuthorID: str | None = None
    MusicBrainzBookID: str | None = None
    MusicbrainzId: str | None = None
    MusicBrainzRecordingID: str | None = None
    MusicBrainzReleaseID: str | None = None
    MusicBrainzTrackID: str | None = None
    MustContain: str | None = None
    MustNotContain: str | None = None
    Name: str | None = None
    NameFirstLast: str | None = None
    NameLastFirst: str | None = None
    NameStyle: str | None = None
    NamingSettings: str | None = None
    Negate: str | None = None
    Negated: str | None = None
    NegateHelpText: str | None = None
    NetCore: str | None = None
    NETCore: str | None = None
    New: str | None = None
    NewBooks: str | None = None
    NextExecution: str | None = None
    No: str | None = None
    NoAltTitle: str | None = None
    NoBackupsAreAvailable: str | None = None
    NoChange: str | None = None
    NoChanges: str | None = None
    NoEventsFound: str | None = None
    NoHistory: str | None = None
    NoHistoryBlocklist: str | None = None
    NoLeaveIt: str | None = None
    NoLimitForAnyRuntime: str | None = None
    NoLinks: str | None = None
    NoListRecommendations: str | None = None
    NoLogFiles: str | None = None
    NoMatchFound: str | None = None
    NoMinimumForAnyRuntime: str | None = None
    NoMoveFilesSelf: str | None = None
    NoMoviesExist: str | None = None
    NoName: str | None = None
    NoResultsFound: str | None = None
    NoTagsHaveBeenAddedYet: str | None = None
    NotAvailable: str | None = None
    NotificationTriggers: str | None = None
    NotificationTriggersHelpText: str | None = None
    NotMonitored: str | None = None
    NoUpdatesAreAvailable: str | None = None
    NoVideoFilesFoundSelectedFolder: str | None = None
    OAuthPopupMessage: str | None = None
    Ok: str | None = None
    OnApplicationUpdate: str | None = None
    OnApplicationUpdateHelpText: str | None = None
    OnBookRetagHelpText: str | None = None
    OnDownloadFailureHelpText: str | None = None
    OnDownloadHelpText: str | None = None
    OnGrab: str | None = None
    OnGrabHelpText: str | None = None
    OnHealthIssue: str | None = None
    OnHealthIssueHelpText: str | None = None
    OnImport: str | None = None
    OnImportFailureHelpText: str | None = None
    OnLatestVersion: str | None = None
    OnlyTorrent: str | None = None
    OnlyUsenet: str | None = None
    OnMovieDelete: str | None = None
    OnMovieDeleteHelpText: str | None = None
    OnMovieFileDelete: str | None = None
    OnMovieFileDeleteForUpgrade: str | None = None
    OnMovieFileDeleteForUpgradeHelpText: str | None = None
    OnMovieFileDeleteHelpText: str | None = None
    OnReleaseImportHelpText: str | None = None
    OnRename: str | None = None
    OnRenameHelpText: str | None = None
    OnUpgrade: str | None = None
    OnUpgradeHelpText: str | None = None
    OpenBrowserOnStart: str | None = None
    OpenThisModal: str | None = None
    Options: str | None = None
    Organize: str | None = None
    OrganizeAndRename: str | None = None
    OrganizeConfirm: str | None = None
    OrganizeModalAllPathsRelative: str | None = None
    OrganizeModalDisabled: str | None = None
    OrganizeModalNamingPattern: str | None = None
    OrganizeModalSuccess: str | None = None
    OrganizeSelectedMovies: str | None = None
    Original: str | None = None
    Other: str | None = None
    OutputFormatHelpText: str | None = None
    OutputPath: str | None = None
    Overview: str | None = None
    OverviewOptions: str | None = None
    PackageVersion: str | None = None
    PageSize: str | None = None
    PageSizeHelpText: str | None = None
    Password: str | None = None
    PasswordHelpText: str | None = None
    PastDays: str | None = None
    PastDaysHelpText: str | None = None
    Path: str | None = None
    PathHelpText: str | None = None
    PathHelpTextWarning: str | None = None
    Paused: str | None = None
    Peers: str | None = None
    Pending: str | None = None
    PendingChangesDiscardChanges: str | None = None
    PendingChangesMessage: str | None = None
    PendingChangesStayReview: str | None = None
    Permissions: str | None = None
    PhysicalRelease: str | None = None
    PhysicalReleaseDate: str | None = None
    Port: str | None = None
    PortHelpText: str | None = None
    PortHelpTextWarning: str | None = None
    PortNumber: str | None = None
    PosterOptions: str | None = None
    Posters: str | None = None
    PosterSize: str | None = None
    PreferAndUpgrade: str | None = None
    PreferIndexerFlags: str | None = None
    PreferIndexerFlagsHelpText: str | None = None
    Preferred: str | None = None
    PreferredHelpTexts1: str | None = None
    PreferredHelpTexts2: str | None = None
    PreferredHelpTexts3: str | None = None
    PreferredSize: str | None = None
    PreferTorrent: str | None = None
    PreferUsenet: str | None = None
    Presets: str | None = None
    PreviewRename: str | None = None
    PreviewRenameHelpText: str | None = None
    PreviewRetag: str | None = None
    Priority: str | None = None
    PriorityHelpText: str | None = None
    PrioritySettings: str | None = None
    ProcessingFolders: str | None = None
    Profiles: str | None = None
    ProfilesSettingsSummary: str | None = None
    Progress: str | None = None
    Proper: str | None = None
    PropersAndRepacks: str | None = None
    Protocol: str | None = None
    ProtocolHelpText: str | None = None
    Proxy: str | None = None
    ProxyBypassFilterHelpText: str | None = None
    ProxyCheckBadRequestMessage: str | None = None
    ProxyCheckFailedToTestMessage: str | None = None
    ProxyCheckResolveIpMessage: str | None = None
    ProxyPasswordHelpText: str | None = None
    ProxyType: str | None = None
    ProxyUsernameHelpText: str | None = None
    PtpOldSettingsCheckMessage: str | None = None
    PublishedDate: str | None = None
    Publisher: str | None = None
    Qualities: str | None = None
    QualitiesHelpText: str | None = None
    Quality: str | None = None
    QualityCutoffHasNotBeenMet: str | None = None
    QualityDefinitions: str | None = None
    QualityLimitsHelpText: str | None = None
    QualityOrLangCutoffHasNotBeenMet: str | None = None
    QualityProfile: str | None = None
    QualityProfileDeleteConfirm: str | None = None
    QualityProfileIdHelpText: str | None = None
    QualityProfileInUse: str | None = None
    QualityProfiles: str | None = None
    QualitySettings: str | None = None
    QualitySettingsSummary: str | None = None
    Queue: str | None = None
    Queued: str | None = None
    QueueIsEmpty: str | None = None
    QuickImport: str | None = None
    RadarrCalendarFeed: str | None = None
    RadarrSupportsAnyDownloadClient: str | None = None
    RadarrSupportsAnyIndexer: str | None = None
    RadarrSupportsAnyRSSMovieListsAsWellAsTheOneStatedBelow: str | None = None
    RadarrSupportsCustomConditionsAgainstTheReleasePropertiesBelow: str | None = None
    RadarrTags: str | None = None
    RadarrUpdated: str | None = None
    Ratings: str | None = None
    ReadarrSupportsAnyDownloadClientThatUsesTheNewznabStandardAsWellAsOtherDownloadClientsListedBelow: str | None = (
        None
    )
    ReadarrSupportsAnyIndexerThatUsesTheNewznabStandardAsWellAsOtherIndexersListedBelow: str | None = (
        None
    )
    ReadarrSupportsMultipleListsForImportingBooksAndAuthorsIntoTheDatabase: str | None = (
        None
    )
    ReadarrTags: str | None = None
    ReadTheWikiForMoreInformation: str | None = None
    Real: str | None = None
    Reason: str | None = None
    RecentChanges: str | None = None
    RecentFolders: str | None = None
    RecycleBinCleanupDaysHelpText: str | None = None
    RecycleBinCleanupDaysHelpTextWarning: str | None = None
    RecycleBinHelpText: str | None = None
    RecyclingBin: str | None = None
    RecyclingBinCleanup: str | None = None
    Reddit: str | None = None
    Redownload: str | None = None
    Refresh: str | None = None
    RefreshAndScan: str | None = None
    RefreshAuthor: str | None = None
    RefreshInformation: str | None = None
    RefreshInformationAndScanDisk: str | None = None
    RefreshLists: str | None = None
    RefreshMovie: str | None = None
    RefreshScan: str | None = None
    RegularExpressionsCanBeTested: str | None = None
    RejectionCount: str | None = None
    RelativePath: str | None = None
    ReleaseBranchCheckOfficialBranchMessage: str | None = None
    Released: str | None = None
    ReleaseDate: str | None = None
    ReleaseDates: str | None = None
    ReleasedMsg: str | None = None
    ReleaseGroup: str | None = None
    ReleaseProfiles: str | None = None
    ReleaseRejected: str | None = None
    ReleaseStatus: str | None = None
    ReleaseTitle: str | None = None
    ReleaseWillBeProcessedInterp: str | None = None
    Reload: str | None = None
    RemotePath: str | None = None
    RemotePathHelpText: str | None = None
    RemotePathMappingCheckBadDockerPath: str | None = None
    RemotePathMappingCheckDockerFolderMissing: str | None = None
    RemotePathMappingCheckDownloadPermissions: str | None = None
    RemotePathMappingCheckFileRemoved: str | None = None
    RemotePathMappingCheckFilesBadDockerPath: str | None = None
    RemotePathMappingCheckFilesGenericPermissions: str | None = None
    RemotePathMappingCheckFilesLocalWrongOSPath: str | None = None
    RemotePathMappingCheckFilesWrongOSPath: str | None = None
    RemotePathMappingCheckFolderPermissions: str | None = None
    RemotePathMappingCheckGenericPermissions: str | None = None
    RemotePathMappingCheckImportFailed: str | None = None
    RemotePathMappingCheckLocalFolderMissing: str | None = None
    RemotePathMappingCheckLocalWrongOSPath: str | None = None
    RemotePathMappingCheckRemoteDownloadClient: str | None = None
    RemotePathMappingCheckWrongOSPath: str | None = None
    RemotePathMappings: str | None = None
    Remove: str | None = None
    RemoveCompleted: str | None = None
    RemoveCompletedDownloadsHelpText: str | None = None
    RemovedFromTaskQueue: str | None = None
    RemovedMovieCheckMultipleMessage: str | None = None
    RemovedMovieCheckSingleMessage: str | None = None
    RemoveDownloadsAlert: str | None = None
    RemoveFailed: str | None = None
    RemoveFailedDownloadsHelpText: str | None = None
    RemoveFilter: str | None = None
    RemoveFromBlocklist: str | None = None
    RemoveFromDownloadClient: str | None = None
    RemoveFromQueue: str | None = None
    RemoveFromQueueText: str | None = None
    RemoveHelpTextWarning: str | None = None
    RemoveMovieAndDeleteFiles: str | None = None
    RemoveMovieAndKeepFiles: str | None = None
    RemoveRootFolder: str | None = None
    RemoveSelected: str | None = None
    RemoveSelectedItem: str | None = None
    RemoveSelectedItems: str | None = None
    RemoveSelectedMessageText: str | None = None
    RemoveTagExistingTag: str | None = None
    RemoveTagRemovingTag: str | None = None
    RemovingTag: str | None = None
    RenameBooks: str | None = None
    RenameBooksHelpText: str | None = None
    Renamed: str | None = None
    RenameFiles: str | None = None
    RenameMovies: str | None = None
    RenameMoviesHelpText: str | None = None
    Reorder: str | None = None
    Replace: str | None = None
    ReplaceIllegalCharacters: str | None = None
    ReplaceIllegalCharactersHelpText: str | None = None
    ReplaceWithDash: str | None = None
    ReplaceWithSpaceDash: str | None = None
    ReplaceWithSpaceDashSpace: str | None = None
    Required: str | None = None
    RequiredHelpText: str | None = None
    RequiredPlaceHolder: str | None = None
    RequiredRestrictionHelpText: str | None = None
    RequiredRestrictionPlaceHolder: str | None = None
    RescanAfterRefreshHelpText: str | None = None
    RescanAfterRefreshHelpTextWarning: str | None = None
    RescanAuthorFolderAfterRefresh: str | None = None
    RescanMovieFolderAfterRefresh: str | None = None
    Reset: str | None = None
    ResetAPIKey: str | None = None
    ResetAPIKeyMessageText: str | None = None
    Restart: str | None = None
    RestartNow: str | None = None
    RestartRadarr: str | None = None
    RestartReadarr: str | None = None
    RestartReloadNote: str | None = None
    RestartRequiredHelpTextWarning: str | None = None
    Restore: str | None = None
    RestoreBackup: str | None = None
    Restrictions: str | None = None
    Result: str | None = None
    Retention: str | None = None
    RetentionHelpText: str | None = None
    RetryingDownloadInterp: str | None = None
    RootFolder: str | None = None
    RootFolderCheckMultipleMessage: str | None = None
    RootFolderCheckSingleMessage: str | None = None
    RootFolderPathHelpText: str | None = None
    RootFolders: str | None = None
    RSS: str | None = None
    RSSIsNotSupportedWithThisIndexer: str | None = None
    RSSSync: str | None = None
    RSSSyncInterval: str | None = None
    RssSyncIntervalHelpText: str | None = None
    RSSSyncIntervalHelpTextWarning: str | None = None
    Runtime: str | None = None
    Save: str | None = None
    SaveChanges: str | None = None
    SaveSettings: str | None = None
    SceneInformation: str | None = None
    SceneNumberHasntBeenVerifiedYet: str | None = None
    Scheduled: str | None = None
    Score: str | None = None
    Script: str | None = None
    ScriptPath: str | None = None
    Search: str | None = None
    SearchAll: str | None = None
    SearchBook: str | None = None
    SearchBoxPlaceHolder: str | None = None
    SearchCutoffUnmet: str | None = None
    SearchFailedPleaseTryAgainLater: str | None = None
    SearchFiltered: str | None = None
    SearchForAllCutoffUnmetBooks: str | None = None
    SearchForAllMissingBooks: str | None = None
    SearchForMissing: str | None = None
    SearchForMonitoredBooks: str | None = None
    SearchForMovie: str | None = None
    SearchForNewItems: str | None = None
    SearchMissing: str | None = None
    SearchMonitored: str | None = None
    SearchMovie: str | None = None
    SearchOnAdd: str | None = None
    SearchOnAddHelpText: str | None = None
    SearchSelected: str | None = None
    Season: str | None = None
    Seconds: str | None = None
    Security: str | None = None
    Seeders: str | None = None
    SelectAll: str | None = None
    SelectDotDot: str | None = None
    SelectedCountAuthorsSelectedInterp: str | None = None
    SelectedCountBooksSelectedInterp: str | None = None
    SelectFolder: str | None = None
    SelectLanguage: str | None = None
    SelectLanguages: str | None = None
    SelectMovie: str | None = None
    SelectQuality: str | None = None
    SelectReleaseGroup: str | None = None
    SendAnonymousUsageData: str | None = None
    SendMetadataToCalibre: str | None = None
    Series: str | None = None
    SeriesNumber: str | None = None
    SeriesTotal: str | None = None
    SetPermissions: str | None = None
    SetPermissionsLinuxHelpText: str | None = None
    SetPermissionsLinuxHelpTextWarning: str | None = None
    SetReleaseGroup: str | None = None
    SetTags: str | None = None
    Settings: str | None = None
    SettingsEnableColorImpairedMode: str | None = None
    SettingsEnableColorImpairedModeHelpText: str | None = None
    SettingsFirstDayOfWeek: str | None = None
    SettingsLongDateFormat: str | None = None
    SettingsRemotePathMappingHostHelpText: str | None = None
    SettingsRemotePathMappingLocalPath: str | None = None
    SettingsRemotePathMappingLocalPathHelpText: str | None = None
    SettingsRemotePathMappingRemotePath: str | None = None
    SettingsRemotePathMappingRemotePathHelpText: str | None = None
    SettingsRuntimeFormat: str | None = None
    SettingsShortDateFormat: str | None = None
    SettingsShowRelativeDates: str | None = None
    SettingsShowRelativeDatesHelpText: str | None = None
    SettingsTimeFormat: str | None = None
    SettingsWeekColumnHeader: str | None = None
    SettingsWeekColumnHeaderHelpText: str | None = None
    ShortDateFormat: str | None = None
    ShouldMonitorExisting: str | None = None
    ShouldMonitorExistingHelpText: str | None = None
    ShouldMonitorHelpText: str | None = None
    ShouldSearchHelpText: str | None = None
    ShowAdvanced: str | None = None
    ShowAsAllDayEvents: str | None = None
    ShowBanners: str | None = None
    ShowBannersHelpText: str | None = None
    ShowBookCount: str | None = None
    ShowBookTitleHelpText: str | None = None
    ShowCertification: str | None = None
    ShowCinemaRelease: str | None = None
    showCinemaReleaseHelpText: str | None = None
    ShowCutoffUnmetIconHelpText: str | None = None
    ShowDateAdded: str | None = None
    ShowGenres: str | None = None
    ShowLastBook: str | None = None
    ShowMonitored: str | None = None
    ShowMonitoredHelpText: str | None = None
    ShowMovieInformation: str | None = None
    ShowMovieInformationHelpText: str | None = None
    ShownAboveEachColumnWhenWeekIsTheActiveView: str | None = None
    ShowName: str | None = None
    ShownClickToHide: str | None = None
    ShowPath: str | None = None
    ShowQualityProfile: str | None = None
    ShowQualityProfileHelpText: str | None = None
    ShowRatings: str | None = None
    ShowRelativeDates: str | None = None
    ShowRelativeDatesHelpText: str | None = None
    ShowReleaseDate: str | None = None
    ShowReleaseDateHelpText: str | None = None
    ShowSearch: str | None = None
    ShowSearchActionHelpText: str | None = None
    ShowSearchHelpText: str | None = None
    ShowSizeOnDisk: str | None = None
    ShowStudio: str | None = None
    ShowTitle: str | None = None
    ShowTitleHelpText: str | None = None
    ShowUnknownAuthorItems: str | None = None
    ShowUnknownMovieItems: str | None = None
    ShowYear: str | None = None
    Shutdown: str | None = None
    Size: str | None = None
    SizeLimit: str | None = None
    SizeOnDisk: str | None = None
    SkipBooksWithMissingReleaseDate: str | None = None
    SkipBooksWithNoISBNOrASIN: str | None = None
    SkipFreeSpaceCheck: str | None = None
    SkipFreeSpaceCheckWhenImportingHelpText: str | None = None
    SkipPartBooksAndSets: str | None = None
    SkipRedownload: str | None = None
    SkipredownloadHelpText: str | None = None
    SkipSecondarySeriesBooks: str | None = None
    Small: str | None = None
    Socks4: str | None = None
    Socks5: str | None = None
    SomeResultsHiddenFilter: str | None = None
    SorryThatAuthorCannotBeFound: str | None = None
    SorryThatBookCannotBeFound: str | None = None
    SorryThatMovieCannotBeFound: str | None = None
    Sort: str | None = None
    Source: str | None = None
    SourcePath: str | None = None
    SourceRelativePath: str | None = None
    SourceTitle: str | None = None
    SpecificBook: str | None = None
    SqliteVersionCheckUpgradeRequiredMessage: str | None = None
    SSLCertPassword: str | None = None
    SslCertPasswordHelpText: str | None = None
    SSLCertPasswordHelpText: str | None = None
    SslCertPasswordHelpTextWarning: str | None = None
    SSLCertPath: str | None = None
    SslCertPathHelpText: str | None = None
    SSLCertPathHelpText: str | None = None
    SslCertPathHelpTextWarning: str | None = None
    SSLPort: str | None = None
    SslPortHelpTextWarning: str | None = None
    StandardBookFormat: str | None = None
    StandardMovieFormat: str | None = None
    StartImport: str | None = None
    StartProcessing: str | None = None
    StartSearchForMissingMovie: str | None = None
    StartTypingOrSelectAPathBelow: str | None = None
    StartupDirectory: str | None = None
    Status: str | None = None
    StatusEndedContinuing: str | None = None
    StatusEndedDeceased: str | None = None
    StatusEndedEnded: str | None = None
    Studio: str | None = None
    Style: str | None = None
    SubfolderWillBeCreatedAutomaticallyInterp: str | None = None
    SuccessMyWorkIsDoneNoFilesToRename: str | None = None
    SuccessMyWorkIsDoneNoFilesToRetag: str | None = None
    SuggestTranslationChange: str | None = None
    Sunday: str | None = None
    SupportsRssvalueRSSIsNotSupportedWithThisIndexer: str | None = None
    SupportsSearchvalueSearchIsNotSupportedWithThisIndexer: str | None = None
    SupportsSearchvalueWillBeUsedWhenAutomaticSearchesArePerformedViaTheUIOrByReadarr: str | None = (
        None
    )
    SupportsSearchvalueWillBeUsedWhenInteractiveSearchIsUsed: str | None = None
    System: str | None = None
    SystemTimeCheckMessage: str | None = None
    Table: str | None = None
    TableOptions: str | None = None
    TableOptionsColumnsMessage: str | None = None
    TagCannotBeDeletedWhileInUse: str | None = None
    TagDetails: str | None = None
    TagIsNotUsedAndCanBeDeleted: str | None = None
    Tags: str | None = None
    TagsHelpText: str | None = None
    TagsSettingsSummary: str | None = None
    Tasks: str | None = None
    TaskUserAgentTooltip: str | None = None
    TBA: str | None = None
    Term: str | None = None
    Test: str | None = None
    TestAll: str | None = None
    TestAllClients: str | None = None
    TestAllIndexers: str | None = None
    TestAllLists: str | None = None
    TheAuthorFolderAndAllOfItsContentWillBeDeleted: str | None = None
    TheBooksFilesWillBeDeleted: str | None = None
    TheFollowingFilesWillBeDeleted: str | None = None
    TheLogLevelDefault: str | None = None
    ThisCannotBeCancelled: str | None = None
    ThisConditionMatchesUsingRegularExpressions: str | None = None
    ThisWillApplyToAllIndexersPleaseFollowTheRulesSetForthByThem: str | None = None
    Time: str | None = None
    TimeFormat: str | None = None
    Timeleft: str | None = None
    Title: str | None = None
    Titles: str | None = None
    TMDb: str | None = None
    TMDBId: str | None = None
    TmdbIdHelpText: str | None = None
    TmdbRating: str | None = None
    TmdbVotes: str | None = None
    Today: str | None = None
    Tomorrow: str | None = None
    TooManyBooks: str | None = None
    TorrentDelay: str | None = None
    TorrentDelayHelpText: str | None = None
    TorrentDelayTime: str | None = None
    Torrents: str | None = None
    TorrentsDisabled: str | None = None
    TotalBookCountBooksTotalBookFileCountBooksWithFilesInterp: str | None = None
    TotalFileSize: str | None = None
    TotalSpace: str | None = None
    Trace: str | None = None
    TrackNumber: str | None = None
    TrackTitle: str | None = None
    Trailer: str | None = None
    Trakt: str | None = None
    Trigger: str | None = None
    Type: str | None = None
    UI: str | None = None
    UILanguage: str | None = None
    UILanguageHelpText: str | None = None
    UILanguageHelpTextWarning: str | None = None
    UISettings: str | None = None
    UISettingsSummary: str | None = None
    UnableToAddANewConditionPleaseTryAgain: str | None = None
    UnableToAddANewCustomFormatPleaseTryAgain: str | None = None
    UnableToAddANewDownloadClientPleaseTryAgain: str | None = None
    UnableToAddANewImportListExclusionPleaseTryAgain: str | None = None
    UnableToAddANewIndexerPleaseTryAgain: str | None = None
    UnableToAddANewListExclusionPleaseTryAgain: str | None = None
    UnableToAddANewListPleaseTryAgain: str | None = None
    UnableToAddANewMetadataProfilePleaseTryAgain: str | None = None
    UnableToAddANewNotificationPleaseTryAgain: str | None = None
    UnableToAddANewQualityProfilePleaseTryAgain: str | None = None
    UnableToAddANewRemotePathMappingPleaseTryAgain: str | None = None
    UnableToAddANewRootFolderPleaseTryAgain: str | None = None
    UnableToAddRootFolder: str | None = None
    UnableToImportCheckLogs: str | None = None
    UnableToLoadAltTitle: str | None = None
    UnableToLoadBackups: str | None = None
    UnableToLoadBlocklist: str | None = None
    UnableToLoadCustomFormats: str | None = None
    UnableToLoadDelayProfiles: str | None = None
    UnableToLoadDownloadClientOptions: str | None = None
    UnableToLoadDownloadClients: str | None = None
    UnableToLoadGeneralSettings: str | None = None
    UnableToLoadHistory: str | None = None
    UnableToLoadImportListExclusions: str | None = None
    UnableToLoadIndexerOptions: str | None = None
    UnableToLoadIndexers: str | None = None
    UnableToLoadLanguages: str | None = None
    UnableToLoadListExclusions: str | None = None
    UnableToLoadListOptions: str | None = None
    UnableToLoadLists: str | None = None
    UnableToLoadManualImportItems: str | None = None
    UnableToLoadMediaManagementSettings: str | None = None
    UnableToLoadMetadata: str | None = None
    UnableToLoadMetadataProfiles: str | None = None
    UnableToLoadMetadataProviderSettings: str | None = None
    UnableToLoadMovies: str | None = None
    UnableToLoadNamingSettings: str | None = None
    UnableToLoadNotifications: str | None = None
    UnableToLoadQualities: str | None = None
    UnableToLoadQualityDefinitions: str | None = None
    UnableToLoadQualityProfiles: str | None = None
    UnableToLoadReleaseProfiles: str | None = None
    UnableToLoadRemotePathMappings: str | None = None
    UnableToLoadRestrictions: str | None = None
    UnableToLoadResultsIntSearch: str | None = None
    UnableToLoadRootFolders: str | None = None
    UnableToLoadTags: str | None = None
    UnableToLoadTheCalendar: str | None = None
    UnableToLoadUISettings: str | None = None
    UnableToUpdateRadarrDirectly: str | None = None
    Unavailable: str | None = None
    Ungroup: str | None = None
    Unlimited: str | None = None
    UnmappedFiles: str | None = None
    UnmappedFilesOnly: str | None = None
    UnmappedFolders: str | None = None
    Unmonitored: str | None = None
    UnmonitoredHelpText: str | None = None
    Unreleased: str | None = None
    UnsavedChanges: str | None = None
    UnselectAll: str | None = None
    UpdateAll: str | None = None
    UpdateAutomaticallyHelpText: str | None = None
    UpdateAvailable: str | None = None
    UpdateCheckStartupNotWritableMessage: str | None = None
    UpdateCheckStartupTranslocationMessage: str | None = None
    UpdateCheckUINotWritableMessage: str | None = None
    UpdateCovers: str | None = None
    UpdateCoversHelpText: str | None = None
    UpdateMechanismHelpText: str | None = None
    Updates: str | None = None
    UpdateScriptPathHelpText: str | None = None
    UpdateSelected: str | None = None
    UpdatingIsDisabledInsideADockerContainerUpdateTheContainerImageInstead: str | None = (
        None
    )
    UpgradeAllowedHelpText: str | None = None
    UpgradesAllowed: str | None = None
    UpgradeUntilCustomFormatScore: str | None = None
    UpgradeUntilQuality: str | None = None
    UpgradeUntilThisQualityIsMetOrExceeded: str | None = None
    UpperCase: str | None = None
    Uptime: str | None = None
    URLBase: str | None = None
    UrlBaseHelpText: str | None = None
    UrlBaseHelpTextWarning: str | None = None
    UseCalibreContentServer: str | None = None
    UseHardlinksInsteadOfCopy: str | None = None
    Usenet: str | None = None
    UsenetDelay: str | None = None
    UsenetDelayHelpText: str | None = None
    UsenetDelayTime: str | None = None
    UsenetDisabled: str | None = None
    UseProxy: str | None = None
    Username: str | None = None
    UsernameHelpText: str | None = None
    UseSSL: str | None = None
    UseSslHelpText: str | None = None
    UsingExternalUpdateMechanismBranchToUseToUpdateReadarr: str | None = None
    UsingExternalUpdateMechanismBranchUsedByExternalUpdateMechanism: str | None = None
    Version: str | None = None
    VersionUpdateText: str | None = None
    VideoCodec: str | None = None
    View: str | None = None
    VisitGithubCustomFormatsAphrodite: str | None = None
    WaitingToImport: str | None = None
    WaitingToProcess: str | None = None
    Wanted: str | None = None
    Warn: str | None = None
    WatchLibraryForChangesHelpText: str | None = None
    WatchRootFoldersForFileChanges: str | None = None
    Week: str | None = None
    WeekColumnHeader: str | None = None
    Weeks: str | None = None
    WhatsNew: str | None = None
    WhitelistedHardcodedSubsHelpText: str | None = None
    WhitelistedSubtitleTags: str | None = None
    Wiki: str | None = None
    WouldYouLikeToRestoreBackup: str | None = None
    WriteAudioTags: str | None = None
    WriteAudioTagsScrub: str | None = None
    WriteAudioTagsScrubHelp: str | None = None
    WriteBookTagsHelpTextWarning: str | None = None
    WriteTagsAll: str | None = None
    WriteTagsNew: str | None = None
    WriteTagsNo: str | None = None
    WriteTagsSync: str | None = None
    Year: str | None = None
    Yes: str | None = None
    YesCancel: str | None = None
    YesMoveFiles: str | None = None
    Yesterday: str | None = None
    YouCanAlsoSearch: str | None = None


@dataclass(init=False)
class _LogRecord(BaseModel):
    """Sonarr log record attributes."""

    exception: str | None = None
    exceptionType: str | None = None
    id: int | None = None
    level: str | None = None
    logger: str | None = None
    message: str | None = None
    time: str | None = None


@dataclass(init=False)
class _QualityInfo(_Common3):
    """Quality attributes."""

    modifier: str | None = None
    resolution: int | None = None
    source: str | None = None


@dataclass(init=False)
class _QualityProfileItems(_Common3):
    """Quality profile items attributes."""

    allowed: bool | None = None
    items: list[_QualityProfileItems] | None = None
    quality: _QualityInfo | None = None

    def __post_init__(self):
        self.items = [_QualityProfileItems(item) for item in self.items or []]
        self.quality = _QualityInfo(self.quality) or {}


@dataclass(init=False)
class _ReleaseCommon(BaseModel):
    """Release common attributes."""

    age: int | None = None
    ageHours: float | None = None
    ageMinutes: float | None = None
    approved: bool | None = None
    commentUrl: str | None = None
    downloadAllowed: bool | None = None
    downloadUrl: str | None = None
    guid: str | None = None
    indexer: str | None = None
    indexerId: int | None = None
    infoHash: str | None = None
    infoUrl: str | None = None
    leechers: int | None = None
    magnetUrl: str | None = None
    protocol: str | None = None
    publishDate: str | None = None
    qualityWeight: int | None = None
    rejected: bool | None = None
    rejections: list[str] | None = None
    releaseWeight: int | None = None
    sceneSource: bool | None = None
    seeders: int | None = None
    size: int | None = None
    temporarilyRejected: bool | None = None
    title: str | None = None


@dataclass(init=False)
class _Revision(BaseModel):
    """Revision attributes attributes."""

    isRepack: bool | None = None
    real: int | None = None
    version: int | None = None


@dataclass(init=False)
class _Quality(BaseModel):
    """Quality attributes."""

    quality: _QualityInfo | None = None
    revision: _Revision | None = None

    def __post_init__(self):
        """Post init."""
        self.quality = _QualityInfo(self.quality) or {}
        self.revision = _Revision(self.revision) or {}


@dataclass(init=False)
class _RecordCommon(BaseModel):
    """Sonarr common attributes."""

    page: int | None = None
    pageSize: int | None = None
    sortDirection: str | None = None
    sortKey: str | None = None
    totalRecords: int | None = None


@dataclass(init=False)
class _ReleaseProfilePreferred(BaseModel):
    """Release profile preferred attributes."""

    key: str | None = None
    value: int | None = None


@dataclass(init=False)
class _Rename(BaseModel):
    """Rename common attributes."""

    existingPath: str | None = None
    newPath: str | None = None


@dataclass(init=False)
class _Tag(BaseModel):
    """Radarr tag attributes."""

    id: int | None = None
    label: str | None = None


@dataclass(init=False)
class _TagDetails(_Tag):
    """Readarr tag details attributes."""

    delayProfileIds: list[int] | None = None
    importListIds: list[int] | None = None
    notificationIds: list[int] | None = None
    restrictionIds: list[int] | None = None


@dataclass(init=False)
class _UpdateChanges(BaseModel):
    """Update changes attributes."""

    fixed: list[str] | None = None
    new: list[str] | None = None


@dataclass(init=False)
class _TitleInfo(BaseModel):
    """Title info attributes."""

    title: str | None = None
    titleWithoutYear: str | None = None
    year: int | None = None


@dataclass(init=False)
class _Notification(BaseModel):
    """Notification attributes."""

    configContract: str | None = None
    implementation: str | None = None
    implementationName: str | None = None
    includeHealthWarnings: bool | None = None
    infoLink: str | None = None
    onDownload: bool | None = None
    onGrab: bool | None = None
    onHealthIssue: bool | None = None
    onRename: bool | None = None
    onUpgrade: bool | None = None
    supportsOnDownload: bool | None = None
    supportsOnGrab: bool | None = None
    supportsOnHealthIssue: bool | None = None
    supportsOnRename: bool | None = None
    supportsOnUpgrade: bool | None = None
    tags: list[int | None] | None = None


@dataclass(init=False)
class _RetagChange(BaseModel):
    """Tag change attributes."""

    field: str | None = None
    oldValue: str | None = None
    newValue: str | None = None
