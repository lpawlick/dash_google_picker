from typing import List, Dict, Union
from dataclasses import dataclass

@dataclass
class GoogleDocument:
    """
    A class to represent a Google Document.

    Attributes
    ----------
    id : str
        The ID of the document.
    serviceId : str
        The service ID of the document.
    mimeType : str
        The MIME type of the document.
    name : str
        The name of the document.
    description : str
        A description of the document.
    type : str
        The type of the document.
    lastEditedUtc : int
        The last edit time of the document in UTC.
    iconUrl : str
        The URL of the document's icon.
    url : str
        The URL of the document.
    embedUrl : str
        The URL to embed the document.
    sizeBytes : int
        The size of the document in bytes.
    isShared : bool
        A boolean indicating whether the document is shared.
    """
    id: str 
    serviceId: str
    mimeType: str
    name: str
    description: str
    type: str
    lastEditedUtc: int
    iconUrl: str
    url: str
    embedUrl: str
    sizeBytes: int
    isShared: bool

class GoogleDocuments:
    def __new__(cls, documents_data : Union[str, List[Dict[str, Union[str, int, bool]]]]):
        if documents_data is None:
            return []
        else:
            return [GoogleDocument(**doc) for doc in documents_data]

