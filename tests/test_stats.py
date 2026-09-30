"""Tests for calculator.stats."""

from calculator.history import HistoryService
from calculator.stats import average_result


def test_average_result():
    history = HistoryService()
    history.clear()
    history.record("add", (1, 2), 3)
    history.record("add", (2, 2), 4)
    assert average_result(history) == 3.5
