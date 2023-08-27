from typing import Union, List, Dict

class ViewGroup():

    def __init__(self, *args : List[str], label : Union[str, None] = None):
        if not args or not isinstance(args[0], str):
            raise ValueError("A ViewGroup needs one ViewID as root item")
        
        self.views = list(args)
        self.label = label

    def add(self, view : Union[str, "ViewGroup"]) -> None:
        self.views.append(view)

    def remove(self, view : Union[str, "ViewGroup"]) -> None:
        self.views.remove(view)

    def to_plotly_json(self) -> Dict[str, Union[str, List[Union[str, "ViewGroup"]]]]:
        return {"type": "ViewGroup", "views": self.views, "label": self.label}
