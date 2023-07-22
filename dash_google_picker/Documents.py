from typing import List, Dict, Union
from dataclasses import dataclass

@dataclass
class GoogleDocument:
    """
    A dataclass representing a Google Document.

    The class takes a dictionary as an argument and sets the key-value pairs as attributes
    on the object. The dictionary should represent the properties of a Google Document
    as per the `Google Picker API <https://developers.google.com/drive/picker/reference#document>`_.

    .. note::
        This class is not intended to be manually instantiated. Instances of this class are
        created by the :class:`~GoogleDocuments` class.

    :ivar attributes: A dictionary representing the attributes of the Google Document.

    Attributes are dynamically set based on the key-value pairs in the dictionary provided.
    """

    __module__ = "dash_google_picker.GoogleDocument"

    def __init__(self, dict_data: Dict[str, Union[str, int, bool]]):
        """
        Initialize a GoogleDocument object with a dictionary.

        :param dict_data: A dictionary where the keys represent attribute names and the values
                            represent attribute values. Should represent a Google Document as 
                            per the Google Picker API.
        """

class GoogleDocuments:
    """
    A class to represent a list of GoogleDocument objects.

    The class takes a list of dictionaries as an argument and creates a :class:`~GoogleDocument` object
    for each dictionary in the list.

    Usage:
    ::

        documents = GoogleDocuments([{'id': '1', 'title': 'Title', 'url': 'http://...'}, {...}, ...])

    :ivar documents: A list of :class:`~GoogleDocument` objects.

    .. note::
        Only data from the Google Picker API returned by the :class:`~GooglePicker` should be passed into this class.
    """

    def __new__(cls, documents_data: List[Dict[str, Union[str, int, bool]]]) -> List['GoogleDocument']:
        """
        Create a list of GoogleDocument objects from a list of dictionaries.

        :param documents_data: A list of dictionaries where each dictionary should represent
                                the properties of a Google Document as per the Google Picker API.
        :return: A list of :class:`~GoogleDocument` objects.
        """
