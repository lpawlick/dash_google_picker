from typing import Union, List, Dict

class ViewGroup():
    """
    A ViewGroup is a collection of one or many Views. It can be used to group Views into a separate tab in the :class:`~GooglePicker`.

    :param args: One or many :class:`~ViewId` or :class:`~ViewGroup`. The first argument needs to be a :class:`~ViewId` which is the root view for this group.
    :param label: The label shown only on the root view of this group.
    """
    def __init__(self, *args : List[str], label : Union[str, None] = None):
        if not args or not isinstance(args[0], str):
            raise ValueError("A ViewGroup needs one ViewID as root item")
        
        self.views = list(args)
        self.label = label

    def add(self, view : Union[str, "ViewGroup"]):
        """
        Adds a new View to the ViewGroup.

        :param view: A :class:`~ViewId` or :class:`~ViewGroup` to add to this ViewGroup.
        """
        self.views.append(view)

    def remove(self, view : Union[str, "ViewGroup"]):
        """
        Remove a view from the ViewGroup.

        :param view: A :class:`~ViewId` or :class:`~ViewGroup` to remove from this ViewGroup.
        """

        self.views.remove(view)

    def to_plotly_json(self) -> Dict[str, Union[str, List[Union[str, "ViewGroup"]]]]:
        """
        Converts the ViewGroup to a dictionary for plotly. This is used internally by dash to pass the ViewGroup to the react frontend.

        :return: A dictionary representing the ViewGroup.
        """
        return {"type": "ViewGroup", "views": self.views, "label": self.label}
