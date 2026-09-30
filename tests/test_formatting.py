"""Tests for calculator.formatting."""

from calculator.formatting import apply_service_fee, as_percentage, round_result


def test_round_result():
    assert round_result(3.14159, 2) == 3.14


def test_as_percentage():
    assert as_percentage(0.5) == "50%"


def test_apply_service_fee():
    assert round(apply_service_fee(100), 2) == 102.9
