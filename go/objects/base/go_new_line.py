import re

from go.objects.base.go_base_object import GoBaseObject


class GoNewLine(GoBaseObject):
    """ Class process \n\r in go file """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check if text start with new line """
        new_line = re.match(r"\n\r?", text)
        if new_line is not None:
            return new_line.group(0)
        else:
            return ""
