"""Environment-based configuration for the calculator service."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings, overridable via environment variables."""

    log_level: str = "INFO"
    history_limit: int = 100

    @classmethod
    def from_env(cls) -> "Settings":
        """Build Settings from CALCULATOR_* environment variables."""
        return cls(
            log_level=os.environ.get("CALCULATOR_LOG_LEVEL", cls.log_level),
            history_limit=int(
                os.environ.get("CALCULATOR_HISTORY_LIMIT", cls.history_limit)
            ),
        )
