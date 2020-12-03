class GoBaseObject:
    """ Parent class for all objects """

    def __init__(self, string: str = ''):
        self._string = string

    def __str__(self):
        return self._string

    def __len__(self):
        return len(self._string)

    @staticmethod
    def match(text: str) -> str:
        """ Check if start string matches this object
        Override if you want

        Return empty string if not matched
        """
        return ""
