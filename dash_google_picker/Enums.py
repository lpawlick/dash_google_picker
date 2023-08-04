from enum import Enum

class ViewId(str, Enum):
    """
    Enum for all Google Picker Views.

    Each attribute represents a different view that can be used in the Google Picker. Some views are deprecated and will return a 403 error.
    More information about these views can be found in the `Google Picker API documentation <https://developers.google.com/drive/picker/reference?#view-id>`_.
    """

    DOCS = "all"
    """
    Shows all Elements from the Google drive. This is the default view.
    """

    DOCS_IMAGES = "docs-images"
    """
    Shows only Images from the Google drive.
    """

    DOCS_IMAGES_AND_VIDEOS = "docs-images-and-videos"
    """
    Shows only images and videos from the Google drive.
    """

    DOCS_VIDEOS = "docs-videos"
    """
    Shows only videos from the Google drive.
    """

    DOCUMENTS = "documents"
    """
    Shows only Google documents from the Google drive.
    """

    DRAWINGS = "drawings"
    """
    Shows only Google Drive Drawings.
    """

    FOLDERS = "folders"
    """
    Shows only Folders from the Google drive. Making this the only view will make it impossible to select a file.
    """

    FORMS = "forms"
    """
    Shows only Google Forms from the Google drive.
    """

    IMAGE_SEARCH = "image-search"
    """
    This view is deprecated and will return a 403 error.
    """

    MAPS = "maps"
    """
    This view is deprecated and will return a 403 error.
    """

    PDFS = "pdfs"
    """
    Shows only PDFs from the Google drive.
    """

    PHOTOS = "photos"
    """
    This view is deprecated and will return a 403 error.
    """

    PHOTO_ALBUMS = "photo-albums"
    """
    This view is deprecated and will return a 403 error.
    """

    PHOTO_UPLOAD = "photo-upload"
    """
    This view is deprecated and will return a 403 error.
    """

    PRESENTATIONS = "presentations"
    """
    Shows only Google slides from the Google drive.
    """

    RECENTLY_PICKED = "recently-picked"
    """
    Shows only recently picked files from the Google drive. If no files have been picked yet, this view will be empty.
    """

    SPREADSHEETS = "spreadsheets"
    """
    Shows only Google Sheets from the Google drive.
    """

    VIDEO_SEARCH = "video-search"
    """
    This view is deprecated and will return a 403 error.
    """

    WEBCAM = "webcam"
    """
    This view is deprecated and will return a 403 error.
    """

    YOUTUBE = "youtube"
    """
    This view is deprecated and will return a 403 error.
    """

class Feature(str, Enum):
    """
    Enum for representing Google Picker Features.

    Each attribute represents a different feature that can be used in the Google Picker. 

    :class:`Feature.Cba` : str
        Represents the "shadeDialog" feature.

    :class:`Feature.E9` : str
        Represents the "ftd" feature.

    :class:`Feature.Hba` : str
        Represents the "simpleUploadEnabled" feature.

    :class:`Feature.I8` : str
        Represents the "cropA11y" feature.

    :class:`Feature.Jca` : str
        Represents the "urlInputVisible" feature.

    :class:`Feature.K9` : str
        Represents the "formsEnabled" feature.

    :class:`Feature.MINE_ONLY` : str
        Represents the "mineOnly" feature.

    :class:`Feature.MULTISELECT_ENABLED` : str
        Represents the "multiselectEnabled" feature.

    :class:`Feature.NAV_HIDDEN` : str
        Represents the "navHidden" feature.

    :class:`Feature.SIMPLE_UPLOAD_ENABLED` : str
        Represents the "simpleUploadEnabled" feature.

    :class:`Feature.SUPPORT_DRIVES` : str
        Represents the "sdr" feature.

    :class:`Feature.SUPPORT_TEAM_DRIVES` : str
        Represents the "std" feature.

    :class:`Feature.T_DOLLAR` : str
        Represents the "mineOnly" feature.

    :class:`Feature.U_DOLLAR` : str
        Represents the "minimal" feature.

    :class:`Feature.Uaa` : str
        Represents the "profilePhoto" feature.

    :class:`Feature.V_DOLLAR` : str
        Represents the "minew" feature.

    :class:`Feature.A_DOLLAR` : str
        Represents the "horizNav" feature.

    :class:`Feature.bca` : str
        Represents the "sawffmi" feature.

    :class:`Feature.daa` : str
        Represents the "multiselectEnabled" feature.

    :class:`Feature.G_DOLLAR` : str
        Represents the "ignoreLimits" feature.

    :class:`Feature.iaa` : str
        Represents the "navHidden" feature.

    :class:`Feature.kaa` : str
        Represents the "newDriveView" feature.

    :class:`Feature.laa` : str
        Represents the "newHorizNav" feature.

    :class:`Feature.m9` : str
        Represents the "showAttach" feature.

    :class:`Feature.maa` : str
        Represents the "newPhotoGridView" feature.

    :class:`Feature.n9` : str
        Represents the "edbe" feature.

    :class:`Feature.oca` : str
        Represents the "sdr" feature.

    :class:`Feature.qca` : str
        Represents the "std" feature.

    :class:`Feature.waa` : str
        Represents the "odv" feature.

    For more information about what these features mean, check the `Google Picker API documentation <https://developers.google.com/drive/picker/reference?#feature>`_.
    """
    Cba = "shadeDialog"
    E9 = "ftd"
    Hba = "simpleUploadEnabled"
    I8 = "cropA11y"
    Jca = "urlInputVisible"
    K9 = "formsEnabled"
    MINE_ONLY = "mineOnly"
    MULTISELECT_ENABLED = "multiselectEnabled"
    NAV_HIDDEN = "navHidden"
    SIMPLE_UPLOAD_ENABLED = "simpleUploadEnabled"
    SUPPORT_DRIVES = "sdr"
    SUPPORT_TEAM_DRIVES = "std"
    T_DOLLAR = "mineOnly"
    U_DOLLAR = "minimal"
    Uaa = "profilePhoto"
    V_DOLLAR = "minew"
    A_DOLLAR = "horizNav"
    bca = "sawffmi"
    daa = "multiselectEnabled"
    G_DOLLAR = "ignoreLimits"
    iaa = "navHidden"
    kaa = "newDriveView"
    laa = "newHorizNav"
    m9 = "showAttach"
    maa = "newPhotoGridView"
    n9 = "edbe"
    oca = "sdr"
    qca = "std"
    waa = "odv"