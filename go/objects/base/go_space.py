import re
from typing import Union

from go.objects.base.go_base_object import GoBaseObject


class GoSpace(GoBaseObject):
    """ Class for process space in go file (Not New Line) """

    def __init__(self, space: Union[str, int]):
        if isinstance(space, int):
            tabs = "\t" * int(space / 4)
            spaces = " " * (space % 4)
            space = tabs + spaces
        super().__init__(space)

    def __len__(self):
        return self.ident

    @staticmethod
    def match(text: str) -> str:
        """ Simple check spaces """
        space = re.match(r"[ \t]+", text)
        if space is not None:
            return space.group(0)
        else:
            return ""

    @property
    def ident(self) -> int:
        """ Return size in line """
        return self._string.count(' ') + self._string.count('\t') * 4
