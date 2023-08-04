from enum import Enum

class ViewId(str, Enum):
    """
    Enum for representing Google Picker View IDs.

    Each attribute represents a different view that can be used in the Google Picker. 

    :class:`ViewId.DOCS` : str
        Represents the view for all types of documents.

    :class:`ViewId.DOCS_IMAGES` : str
        Represents the view for documents and images.

    :class:`ViewId.DOCS_IMAGES_AND_VIDEOS` : str
        Represents the view for documents, images, and videos.

    :class:`ViewId.DOCS_VIDEOS` : str
        Represents the view for documents and videos.

    :class:`ViewId.DOCUMENTS` : str
        Represents the view for Google documents.

    :class:`ViewId.DRAWINGS` : str
        Represents the view for Google drawings.

    :class:`ViewId.FOLDERS` : str
        Represents the view for Google Drive folders.

    :class:`ViewId.FORMS` : str
        Represents the view for Google forms.

    :class:`ViewId.IMAGE_SEARCH` : str
        Represents the view for image search.

    :class:`ViewId.MAPS` : str
        Represents the view for Google My Maps.

    :class:`ViewId.PDFS` : str
        Represents the view for PDF documents.

    :class:`ViewId.PHOTOS` : str
        Represents the view for Google Photos.

    :class:`ViewId.PHOTO_ALBUMS` : str
        Represents the view for Google Photo albums.

    :class:`ViewId.PHOTO_UPLOAD` : str
        Represents the view for uploading photos.

    :class:`ViewId.PRESENTATIONS` : str
        Represents the view for Google presentations.

    :class:`ViewId.RECENTLY_PICKED` : str
        Represents the view for recently picked items.

    :class:`ViewId.SPREADSHEETS` : str
        Represents the view for Google spreadsheets.

    :class:`ViewId.VIDEO_SEARCH` : str
        Represents the view for video search.

    :class:`ViewId.WEBCAM` : str
        Represents the view for the webcam.

    :class:`ViewId.YOUTUBE` : str
        Represents the view for YouTube videos.

    For more information about what these views mean, check the `Google Picker API documentation <https://developers.google.com/drive/picker/reference?#view-id>`_.
    """
    DOCS = "all"
    DOCS_IMAGES = "docs-images"
    DOCS_IMAGES_AND_VIDEOS = "docs-images-and-videos"
    DOCS_VIDEOS = "docs-videos"
    DOCUMENTS = "documents"
    DRAWINGS = "drawings"
    FOLDERS = "folders"
    FORMS = "forms"
    IMAGE_SEARCH = "image-search"
    MAPS = "maps"
    PDFS = "pdfs"
    PHOTOS = "photos"
    PHOTO_ALBUMS = "photo-albums"
    PHOTO_UPLOAD = "photo-upload"
    PRESENTATIONS = "presentations"
    RECENTLY_PICKED = "recently-picked"
    SPREADSHEETS = "spreadsheets"
    VIDEO_SEARCH = "video-search"
    WEBCAM = "webcam"
    YOUTUBE = "youtube"

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