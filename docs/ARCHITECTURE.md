# Architecture

This is intentionally over-built for what it does — the point of the repo
is to give PR review tooling realistic surface area, not to be a real
calculator product.

## Modules

- `calculator.operations` — arithmetic functions (`add`, `subtract`,
  `multiply`, `divide`). Each validates its operands and `divide` raises
  `DivisionByZeroError` on a zero divisor.
- `calculator.validators` — shared input validation (`validate_operand`).
- `calculator.exceptions` — the `CalculatorError` hierarchy.
- `calculator.history` — `HistoryService`, an in-memory log of past
  operations.
- `calculator.config` — `Settings`, environment-driven configuration
  (`CALCULATOR_LOG_LEVEL`, `CALCULATOR_HISTORY_LIMIT`).
- `calculator.logging_config` — idempotent root logger setup.
- `calculator.cli` — the `calculator` console script, wiring the above
  together behind an argparse subcommand interface.

## Data flow

```
cli.main()
  -> Settings.from_env()
  -> setup_logging(settings.log_level)
  -> operations.<op>(a, b)
       -> validators.validate_operand(...)
```

`HistoryService` is not yet wired into the CLI — recording operation
history is left as a natural follow-up extension point.
