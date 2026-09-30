"""Input validation helpers for the calculator package."""

from numbers import Number

from calculator.exceptions import InvalidOperandError


def validate_operand(value: object, *, name: str = "value") -> None:
    """Raise InvalidOperandError if value is not a real number."""
    if isinstance(value, bool) or not isinstance(value, Number):
        raise InvalidOperandError(
            f"{name} must be a number, got {type(value).__name__}"
        )
