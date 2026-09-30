"""Core arithmetic operations for the calculator package."""

from calculator.exceptions import DivisionByZeroError
from calculator.validators import validate_operand


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    validate_operand(a, name="a")
    validate_operand(b, name="b")
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    validate_operand(a, name="a")
    validate_operand(b, name="b")
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    validate_operand(a, name="a")
    validate_operand(b, name="b")
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a and b.

    Raises:
        DivisionByZeroError: if b is zero.
    """
    validate_operand(a, name="a")
    validate_operand(b, name="b")
    if b == 0:
        raise DivisionByZeroError("cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to exponent."""
    validate_operand(base, name="base")
    validate_operand(exponent, name="exponent")
    return base**exponent
