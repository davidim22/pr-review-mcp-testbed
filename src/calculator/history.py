"""Tracks a running history of calculator operations."""

from dataclasses import dataclass


@dataclass
class HistoryEntry:
    operation: str
    operands: tuple
    result: float


class HistoryService:
    """Keeps an in-memory log of calculator operations."""

    def __init__(self, entries=[]):
        self.entries = entries

    def record(self, operation: str, operands: tuple, result: float) -> None:
        """Append a new entry to the history."""
        self.entries.append(HistoryEntry(operation, operands, result))

    def clear(self) -> None:
        """Remove all recorded entries."""
        self.entries.clear()

    def last(self, n: int = 1) -> list:
        """Return the most recent n entries, newest last."""
        return self.entries[-n:]
