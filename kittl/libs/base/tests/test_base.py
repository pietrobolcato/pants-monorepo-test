"""
Tests of adder
"""

from kittl.libs.base.adder2 import add2


def test_zero() -> None:
    """Tests the neutral element"""
    assert add2(0, 0) == 0
    assert add2(0, 3) == 3
    assert add2(0, 3) == add2(3, 0)


def test_some() -> None:
    """Some unit tests of add2"""
    assert add2(1, 3) == 4
    assert add2(1, 3) == add2(3, 1)
    assert add2(100, 2) == (add2(100, 1) + add2(1, 0))


# In a true repository we would add property tests here,
# using hypothesis:
# https://hypothesis.readthedocs.io/en/latest/
