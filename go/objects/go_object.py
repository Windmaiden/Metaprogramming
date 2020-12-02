from typing import List

from go.objects.base import GoBaseObjectType
from go.objects.base.go_base_object import GoBaseObject


class GoObject(GoBaseObject):
    """ Class as parent go objects with child objects """

    def __init__(self):
        super().__init__()
        self._objects: List[GoBaseObjectType] = []

    @property
    def objects(self) -> List[GoBaseObjectType]:
        """ Careful someone can change this list and objects """
        return self._objects

    def __str__(self):
        string = ''
        for child in self._objects:
            string += str(child)
        return string

    def __len__(self):
        length = 0
        for child in self._objects:
            length += len(child)
        return length
