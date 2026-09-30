"""Tests for calculator.operations."""

import pytest

from calculator.exceptions import DivisionByZeroError, InvalidOperandError
from calculator.operations import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        divide(1, 0)


@pytest.mark.parametrize("bad_value", ["1", None, [1], True])
def test_operations_reject_invalid_operands(bad_value):
    with pytest.raises(InvalidOperandError):
        add(bad_value, 1)
