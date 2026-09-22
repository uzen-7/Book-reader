from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class BaseExtractor(ABC):
    """Base interface for document extractors."""

    @abstractmethod
    def extract(self, file_path: str | Path) -> list[dict]:
        """Return a list of extracted page dictionaries."""
