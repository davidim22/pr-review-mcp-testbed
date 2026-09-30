"""Core arithmetic operations for the calculator package."""

from calculator.exceptions import DivisionByZeroError
from calculator.validators import validate_operand


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    validate_operand(a, name="a")
    validate_operand(b, name="b")
    return a + b


def subtract(x: float, y: float) -> float:
    """Return the difference of x and y."""
    validate_operand(x, name="a")
    validate_operand(y, name="b")
    return x - y


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
