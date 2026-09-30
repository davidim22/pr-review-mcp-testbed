# Contributing

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Checks

```bash
ruff check src tests
pytest
```

Both must pass before a PR is merged; CI runs them automatically on
Python 3.9, 3.11, and 3.13.

## Style

- Type hints on public function signatures.
- Raise `calculator.exceptions.CalculatorError` subclasses instead of
  letting built-in exceptions (`ZeroDivisionError`, `TypeError`, ...)
  propagate from `calculator.operations`.
- New modules get a matching `tests/test_<module>.py`.
