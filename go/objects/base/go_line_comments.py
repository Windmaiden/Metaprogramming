from go.objects.base.go_base_object import GoBaseObject


class GoLineComment(GoBaseObject):
    """ Class for process line comments """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check line comments """
        if not text.startswith("//"):
            return ""

        new_line_pos = text.find('\n')
        if new_line_pos == -1:
            return text
        else:
            return text[:new_line_pos]