import pytest

from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(1, 1) == 2

def test_subtract():
    c = Calculator()
    assert c.subtract(5, 1) == 4