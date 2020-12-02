from go.objects.base.go_base_object import GoBaseObject


class GoBlockComment(GoBaseObject):
    """ Class for process block comments """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check block comment
        :raise
            ValueError if block comment unclosed
        """
        if not text.startswith('/*'):
            return ""

        close_comment = text.find('*/')
        if close_comment == -1:
            raise ValueError("Unclosed block comment")
        return text[:close_comment + len('*/')]
