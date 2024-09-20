import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(5, 3) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(-4, 2) == -6
    assert calc.subtract(0, 0) == 0
