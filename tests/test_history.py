"""Tests for calculator.history."""

from calculator.history import HistoryService


def test_record_appends_entry():
    history = HistoryService()
    history.clear()
    history.record("add", (1, 2), 3)
    assert history.last() == [history.entries[-1]]
    assert history.entries[-1].operation == "add"


def test_clear_empties_history():
    history = HistoryService()
    history.record("add", (1, 2), 3)
    history.clear()
    assert history.entries == []


def test_last_returns_most_recent_n():
    history = HistoryService()
    history.clear()
    history.record("add", (1, 2), 3)
    history.record("subtract", (5, 2), 3)
    recent = history.last(2)
    assert [e.operation for e in recent] == ["add", "subtract"]
