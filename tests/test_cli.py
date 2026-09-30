"""Tests for calculator.cli."""

from calculator.cli import main


def test_add(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_subtract(capsys):
    assert main(["subtract", "5", "3"]) == 0
    assert capsys.readouterr().out.strip() == "2.0"


def test_divide(capsys):
    assert main(["divide", "10", "2"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_divide_by_zero_returns_nonzero_exit(capsys):
    assert main(["divide", "1", "0"]) == 1
    assert "error" in capsys.readouterr().err
