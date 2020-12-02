import re
import string

from go.objects.base.go_base_object import GoBaseObject


KEYWORDS = {
     "break": "BREAK",
     "case": "CASE",
     "chan": "CHAN",
     "const": "CONST",
     "continue": "CONTINUE",

     "default": "DEFAULT",
     "defer": "DEFER",
     "else": "ELSE",
     "fallthrough": "FALLTHROUGH",
     "for": "FOR",

     "func": "FUNC",
     "go": "GO",
     "goto": "GOTO",
     "if": "IF",
     "import": "IMPORT",

     "interface": "INTERFACE",
     "map": "MAP",
     "package": "PACKAGE",
     "range": "RANGE",
     "return": "RETURN",

     "select": "SELECT",
     "struct": "STRUCT",
     "switch": "SWITCH",
     "type": "TYPE",
     "var": "VAR",
}


class GoIdentifier(GoBaseObject):
    """ Class for process object names or go lang special keywords """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check is start text has identifier """
        if text[0].lower() not in string.ascii_lowercase + '_':
            return ""

        identifier = re.match(r"[a-zA-Z0-9_]+", text).group(0)
        return identifier

    @property
    def is_keyword(self) -> bool:
        """ Check if identifier is special key """
        return self._string in KEYWORDS
