"""Tests for calculator.validators."""

import pytest

from calculator.exceptions import InvalidOperandError
from calculator.validators import validate_operand


def test_accepts_int_and_float():
    validate_operand(1)
    validate_operand(1.5)


def test_rejects_bool():
    with pytest.raises(InvalidOperandError):
        validate_operand(True)


def test_rejects_string():
    with pytest.raises(InvalidOperandError):
        validate_operand("1")


def test_error_message_includes_name():
    with pytest.raises(InvalidOperandError, match="b must be a number"):
        validate_operand("x", name="b")
