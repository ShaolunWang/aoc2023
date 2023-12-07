
#Our representation is already ssa form:
#
# Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green; 2 red, 13 blue, 8 green; 18 blue, 7 green, 5 red
# Game 2: 3 green, 4 red, 4 blue; 6 red, 4 green, 4 blue; 2 blue, 4 green, 3 red

from enum import Enum, auto

from xdsl.dialects.builtin import IntegerAttr, ModuleOp, StringAttr


class TokenKind(Enum):
    EOF = auto()
    NEWLINE = auto()
    COMMA = auto()
    BLUE = auto()
    GREEN = auto()
    RED = auto()
