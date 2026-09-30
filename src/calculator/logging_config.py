"""Logging setup for the calculator service."""

import logging

_configured = False


def setup_logging(level: str = "INFO") -> None:
    """Configure root logging once, idempotently."""
    global _configured
    resolved_level = getattr(logging, level.upper(), logging.INFO)
    if _configured:
        logging.getLogger().setLevel(resolved_level)
        return
    logging.basicConfig(
        level=resolved_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger().setLevel(resolved_level)
    _configured = True
