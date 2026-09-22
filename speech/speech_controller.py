from __future__ import annotations

from enum import Enum, auto

from speech.base_tts import BaseTTSEngine


class SpeechState(Enum):
    STOPPED = auto()
    PLAYING = auto()
    PAUSED = auto()
    LOADING = auto()
    ERROR = auto()


class SpeechController:
    """Stateful controller that keeps TTS logic separate from the UI."""

    def __init__(self, engine: BaseTTSEngine) -> None:
        self.engine = engine
        self.state = SpeechState.STOPPED

    def play(self, text: str) -> None:
        self.state = SpeechState.PLAYING
        self.engine.speak(text)
        self.state = SpeechState.STOPPED

    def pause(self) -> None:
        self.state = SpeechState.PAUSED
        self.engine.pause()

    def resume(self) -> None:
        self.state = SpeechState.PLAYING
        self.engine.resume()

    def stop(self) -> None:
        self.state = SpeechState.STOPPED
        self.engine.stop()
