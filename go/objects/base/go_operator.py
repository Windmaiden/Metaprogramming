import re

from go.objects.base.go_base_object import GoBaseObject


OPERATORS = {
    "ADD": "+",
    "SUB": "-",
    "MUL": "*",
    "QUO": "/",
    "REM": "%",

    "AND": "&",
    "OR": "|",
    "XOR": "^",
    "SHL": "<<",
    "SHR": ">>",
    "AND_NOT": "&^",

    "ADD_ASSIGN": "+=",
    "SUB_ASSIGN": "-=",
    "MUL_ASSIGN": "*=",
    "QUO_ASSIGN": "/=",
    "REM_ASSIGN": "%=",

    "AND_ASSIGN": "&=",
    "OR_ASSIGN": "|=",
    "XOR_ASSIGN": "^=",
    "SHL_ASSIGN": "<<=",
    "SHR_ASSIGN": ">>=",
    "AND_NOT_ASSIGN": "&^=",

    "LAND": "&&",
    "LOR": "||",
    "ARROW": "<-",
    "INC": "++",
    "DEC": "--",

    "EQL": "==",
    "LSS": "<",
    "GTR": ">",
    "ASSIGN": "=",
    "NOT": "!",

    "NEQ": "!=",
    "LEQ": "<=",
    "GEQ": ">=",
    "DEFINE": ":=",
    "ELLIPSIS": "...",

    "LPAREN": "(",
    "LBRACK": "[",
    "LBRACE": "{",
    "COMMA": ",",
    "PERIOD": ".",

    "RPAREN": ")",
    "RBRACK": "]",
    "RBRACE": "}",
    "SEMICOLON": ";",
    "COLON": ":",
}


class GoOperator(GoBaseObject):
    """ Class for process operators """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check for operators """
        for operator in sorted(OPERATORS.values()):
            if text.startswith(operator):
                return operator
        return ""
