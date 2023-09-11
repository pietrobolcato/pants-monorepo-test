"""Example module of the fancy library, consuming the base library"""

from kittl.libs.base.adder2 import add2


def add3(x: int, y: int, z: int) -> int:
    """
    Adds three integers

    Args:
        x: the left operand
        y: the middle operand
        z: the right operand
    Returns:
        The sum of x, y, and z
    """
    return add2(add2(x, y), z)
