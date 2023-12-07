from xdsl.dialects.builtin import IntegerType, IntegerAttr, StringAttr
from xdsl.ir import Dialect
from xdsl.irdl import (
    IRDLOperation,
    irdl_op_definition,
)

@irdl_op_definition
class GameOp(IRDLOperation):
    """
        you just lost the game if you see this :)
    """
    name = 'aoc.game'
    def __init__(self, value: IntegerAttr):
        super().__init__(result_types=[value.type], attributes={"value": value})


@irdl_op_definition
class ColorOp(IRDLOperation):
    name = 'aoc.color'
    lhs = str
    rhs = IntegerType
    def __init__(self, value: IntegerAttr):
        super().__init__(result_types=[value.type], attributes={"value": value})

Aoc = Dialect([GameOp,ColorOp],[])
