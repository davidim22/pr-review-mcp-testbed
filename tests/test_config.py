"""Tests for calculator.config."""

from calculator.config import Settings


def test_defaults():
    settings = Settings()
    assert settings.log_level == "INFO"
    assert settings.history_limit == 100


def test_from_env_overrides(monkeypatch):
    monkeypatch.setenv("CALCULATOR_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("CALCULATOR_HISTORY_LIMIT", "5")
    settings = Settings.from_env()
    assert settings.log_level == "DEBUG"
    assert settings.history_limit == 5


def test_from_env_defaults_when_unset(monkeypatch):
    monkeypatch.delenv("CALCULATOR_LOG_LEVEL", raising=False)
    monkeypatch.delenv("CALCULATOR_HISTORY_LIMIT", raising=False)
    settings = Settings.from_env()
    assert settings.log_level == "INFO"
    assert settings.history_limit == 100
