"""Custom exception types for the calculator package."""


class CalculatorError(Exception):
    """Base class for all calculator errors."""


class InvalidOperandError(CalculatorError):
    """Raised when an operand is not a supported numeric type."""


class DivisionByZeroError(CalculatorError):
    """Raised when a division operation would divide by zero."""
