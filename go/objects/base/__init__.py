from typing import Union

from go.objects.base.go_base_object import GoBaseObject
from go.objects.base.go_block_comment import GoBlockComment
from go.objects.base.go_identifier import GoIdentifier
from go.objects.base.go_line_comments import GoLineComment
from go.objects.base.go_new_line import GoNewLine
from go.objects.base.go_number import GoNumber
from go.objects.base.go_operator import GoOperator
from go.objects.base.go_space import GoSpace
from go.objects.base.go_string import GoString

GoBaseObjectType = Union[
    GoBaseObject,
    GoBlockComment,
    GoLineComment,
    GoIdentifier,
    GoNewLine,
    GoNumber,
    GoOperator,
    GoString,
    GoSpace,
]