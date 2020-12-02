from os.path import (
    basename,
    isdir,
)

from go.objects.base import (
    GoBaseObjectType,
    GoNewLine,
)
from go.objects.base.base_parser import parse_go_base_objects
from go.objects.go_object import GoObject


class GoFile(GoObject):
    """ Class for process Go code in file level
    Attributes
        path: path to file
        file_name: basename of file

    Methods
        is_go_file(path) Check is go lang file
        get_line(GoObject) Return line at object located
        get_line_pos(GoObject) Return line position object
    """

    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self._parse_file()

    @property
    def file_name(self) -> str:
        """ File name """
        return basename(self.path)

    def _parse_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            text = file.read()
        self._objects = parse_go_base_objects(text)

    @staticmethod
    def is_go_file(path: str) -> bool:
        """ Check path is go file """
        if isdir(path):
            return False
        return path.endswith('.go')

    def get_line(self, go_object: GoBaseObjectType):
        """ Get line location go_object """
        line = 1
        for object_ in self.objects:
            if isinstance(object_, GoNewLine):
                line += 1
            if object_ is go_object:
                return line
        else:
            raise RuntimeError("Object not found")

    def get_line_pos(self, go_object: GoBaseObjectType):
        """ Get object location at line """
        end_index = self.objects.index(go_object)
        start_index = end_index - 1
        while not isinstance(self.objects[start_index], GoNewLine):
            start_index -= 1

        return sum([len(o) for o in self.objects[start_index:end_index]])
