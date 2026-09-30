"""Tests for calculator.logging_config."""

import logging

from calculator import logging_config


def test_setup_logging_sets_root_level():
    logging_config._configured = False
    logging_config.setup_logging("DEBUG")
    assert logging.getLogger().level == logging.DEBUG


def test_setup_logging_is_idempotent():
    logging_config._configured = False
    logging_config.setup_logging("DEBUG")
    handler_count = len(logging.getLogger().handlers)
    logging_config.setup_logging("DEBUG")
    assert len(logging.getLogger().handlers) == handler_count
