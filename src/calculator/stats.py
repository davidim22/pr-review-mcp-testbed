"""Aggregate statistics over recorded calculator history."""

from calculator.history import HistoryService


def average_result(history: HistoryService) -> float:
    """Return the mean of all recorded operation results."""
    results = [entry.result for entry in history.entries]
    return sum(results) / len(results)
