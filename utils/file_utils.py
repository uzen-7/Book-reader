from __future__ import annotations

from pathlib import Path


def ensure_path(path: str | Path) -> Path:
    """Normalize a file path and return a Path object."""
    return Path(path).expanduser().resolve()


def safe_extension(path: str | Path) -> str:
    """Return a lowercase file extension without a dot."""
    return Path(path).suffix.lower().lstrip(".")
