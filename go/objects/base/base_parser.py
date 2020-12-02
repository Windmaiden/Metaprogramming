from typing import List

from go.objects.base.go_base_object import GoBaseObject
from go.objects.base.go_block_comment import GoBlockComment
from go.objects.base.go_identifier import GoIdentifier
from go.objects.base.go_line_comments import GoLineComment
from go.objects.base.go_new_line import GoNewLine
from go.objects.base.go_number import GoNumber
from go.objects.base.go_operator import GoOperator
from go.objects.base.go_space import GoSpace
from go.objects.base.go_string import GoString

OBJECTS = [
    GoSpace,
    GoNewLine,
    GoBlockComment,
    GoLineComment,
    GoIdentifier,
    GoString,
    GoNumber,
    GoOperator,
]


def parse_go_base_objects(text: str) -> List[GoBaseObject]:
    """ Parse text into list GoBaseObjects """
    go_base_objects: List[GoBaseObject] = []
    while text:
        for go_base_object in OBJECTS:
            temp = go_base_object.match(text)
            if temp:
                go_base_objects.append(go_base_object(temp))
                text = text[len(temp):]
                break
        else:
            raise ValueError("Parsing ERROR")
    return go_base_objects


if __name__ == "__main__":
    # Fast Simple Test
    with open("main.go", 'r', encoding='utf-8') as file:
        text = file.read()
    assert text == ''.join([str(o) for o in parse_go_base_objects(text)])
