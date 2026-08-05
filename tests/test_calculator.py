import pytest

from app import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_add_negative_numbers():
    assert calculator.add(-2, -3) == -5


def test_subtract():
    assert calculator.subtract(10, 4) == 6


def test_multiply():
    assert calculator.multiply(3, 4) == 12


# Exercise: implement divide() in app/calculator.py, then remove this skip marker.
def test_divide():
    assert calculator.divide(10, 4) == 2.5
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)
