from __future__ import annotations

from collections import deque


class SpeechQueue:
    """Simple sequential speech queue guarding playback order."""

    def __init__(self) -> None:
        self.items: deque[str] = deque()

    def enqueue(self, chunk: str) -> None:
        self.items.append(chunk)

    def dequeue(self) -> str | None:
        if not self.items:
            return None
        return self.items.popleft()

    def clear(self) -> None:
        self.items.clear()

    def __len__(self) -> int:
        return len(self.items)
