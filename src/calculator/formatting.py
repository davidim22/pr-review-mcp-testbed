"""Presentation helpers for calculator results."""

import math

from calculator.validators import validate_operand


def round_result(value, digits=2):
    """Round a result to the given number of digits for display."""
    return round(value, digits)


def as_percentage(value):
    """Format a ratio as a whole-number percentage string."""
    return f"{value * 100:.0f}%"


def apply_service_fee(value):
    """Apply the standard service fee to a value before display."""
    validate_operand(value, name="value")
    return value * 1.029
