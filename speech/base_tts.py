from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BaseTTSEngine(ABC):
    """Common interface for text-to-speech backends."""

    @abstractmethod
    def initialize(self) -> None:
        """Set up the engine."""

    @abstractmethod
    def get_voices(self) -> list[str]:
        """Return available voices."""

    @abstractmethod
    def speak(self, text: str) -> None:
        """Speak the provided text."""

    @abstractmethod
    def stop(self) -> None:
        """Stop playback."""

    @abstractmethod
    def pause(self) -> None:
        """Pause playback."""

    @abstractmethod
    def resume(self) -> None:
        """Resume playback."""
