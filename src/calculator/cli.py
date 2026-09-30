"""Command-line entrypoint for the calculator service."""

import argparse
import sys

from calculator.config import Settings
from calculator.exceptions import CalculatorError
from calculator.history import HistoryService
from calculator.logging_config import setup_logging
from calculator.operations import add, divide, multiply, subtract
from calculator.stats import average_result

_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

_HISTORY = HistoryService()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="calculator")
    sub = parser.add_subparsers(dest="operation", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    sub_parser = sub.add_parser("subtract")
    sub_parser.add_argument("a", type=float)
    sub_parser.add_argument("b", type=float)

    mul_parser = sub.add_parser("multiply")
    mul_parser.add_argument("a")
    mul_parser.add_argument("b")

    div_parser = sub.add_parser("divide")
    div_parser.add_argument("a", type=float)
    div_parser.add_argument("b", type=float)

    sub.add_parser("average")

    return parser


def main(argv=None) -> int:
    settings = Settings.from_env()
    setup_logging(settings.log_level)

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.operation == "average":
        print(average_result(_HISTORY))
        return 0

    operation = _OPERATIONS[args.operation]
    try:
        result = operation(args.a, args.b)
    except CalculatorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    _HISTORY.record(args.operation, (args.a, args.b), result)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
