from go.objects.base.go_base_object import GoBaseObject


class GoString(GoBaseObject):
    """ Class for process string in file """

    @staticmethod
    def match(text: str) -> str:
        """ Simple check for string """
        if text[0] not in {'"', "'", "`"}:
            return ""

        start = 1
        while True:
            next_quotes_pos = text.find(text[0], start)
            if next_quotes_pos == -1:
                raise ValueError("Unclosed string")

            escaped = text[next_quotes_pos - 1] == "\\"
            if escaped:
                escaped = text[next_quotes_pos - 2:next_quotes_pos] != "\\\\"
            if not escaped:
                break

            start = next_quotes_pos + 1

        return text[:next_quotes_pos + 1]
