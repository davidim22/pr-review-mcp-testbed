"""A small calculator module used to exercise PR review tooling."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def divide(a, b):
    """Return the quotient of a and b, or 0 if dividing by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return 0
