"""
Tests of adder3
"""

from kittl.libs.base.adder2 import add2
from kittl.libs.fancy.adder3 import add3


def test_zero() -> None:
    """Test of add3 with zero"""
    assert add3(0, 0, 0) == 0
    assert add3(0, 1, 0) == 1
    assert add3(0, 1, 2) == 3
    assert add3(1, 2, 0) == 3


def test_add2_add3() -> None:
    """Test relation between add2 and add3"""
    assert add3(1, 2, 3) == (add2(1, 2) + add2(0, 3))
    assert add3(1, 2, 0) == add2(1, 2)


def test_some() -> None:
    """Some unit tests of add3"""
    assert add3(1, 2, 3) == 6
    assert add3(1, 2, 3) == add3(3, 2, 1)
    assert add3(100, 2, 3) == 105