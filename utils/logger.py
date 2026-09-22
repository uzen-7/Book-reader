from __future__ import annotations

import logging
from pathlib import Path


def get_logger(name: str, log_dir: str | Path | None = None) -> logging.Logger:
    """Return a configured logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        stream = logging.StreamHandler()
        stream.setFormatter(formatter)
        logger.addHandler(stream)

        if log_dir is not None:
            logs_path = Path(log_dir)
            logs_path.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(logs_path / "application.log", encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
