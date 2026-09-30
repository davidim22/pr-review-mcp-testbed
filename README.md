# pr-review-mcp-testbed

A sandbox repo for testing an MCP server that reviews pull requests.

## Layout

```
src/calculator/       # package source
  operations.py        # add / subtract / multiply / divide
  validators.py         # shared input validation
  exceptions.py         # CalculatorError hierarchy
  history.py            # HistoryService (in-memory operation log)
  config.py             # Settings (env-driven configuration)
  logging_config.py     # idempotent root logger setup
  cli.py                # `calculator` console script
tests/                 # pytest suite, one file per module
docs/ARCHITECTURE.md  # module responsibilities and data flow
.github/workflows/ci.yml  # lint (ruff) + tests on every push/PR
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests
pytest
```

## Purpose

This repo exists to provide realistic, varied pull requests (clean, buggy,
and mixed-quality) so PR review tooling can be exercised against them. It
is not meant to be a real calculator library — the "enterprise" structure
(package layout, tests, CI, config, docs) is intentionally over-built for
what the code actually does. See [CONTRIBUTING.md](CONTRIBUTING.md) for
the contribution checklist and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
for how the modules fit together.
