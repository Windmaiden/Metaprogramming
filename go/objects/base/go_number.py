import string

from go.objects.base.go_base_object import GoBaseObject


class GoNumber(GoBaseObject):
    """ Class for process any numbers int float etc. """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check is number """
        if text[0] not in string.digits + '.':
            return ""

        number = ""
        for char in text:
            if char == '_':
                if number[-1] != '_':
                    number += char
                else:
                    raise ValueError("Invalid number")
            elif char.lower() in string.ascii_lowercase + string.digits + '.':
                number += char
            else:
                break
        for digit in string.digits:
            if digit in number:
                break
        else:
            return ""
        if number.endswith('_'):
            raise ValueError("Invalid number")
        return number

    def is_float(self) -> bool:
        """ Check string is like float """
        if '.' in self._string and not self._string.endswith('i'):
            return True
        return False

    def is_integer(self) -> bool:
        """ Check string is like integer """
        if '.' not in self._string:
            return True
        return False

    def is_imaginary(self) -> bool:
        """ Check string is like imaginary """
        if '.' in self._string and self._string.endswith('i'):
            return True
        return False
