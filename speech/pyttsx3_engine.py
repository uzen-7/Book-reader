from __future__ import annotations

import pyttsx3

from speech.base_tts import BaseTTSEngine


class Pyttsx3Engine(BaseTTSEngine):
    """Offline TTS engine using pyttsx3 and system speech backends."""

    def __init__(self, voice_id: str | None = None, rate: int = 180, volume: float = 1.0) -> None:
        self.engine = pyttsx3.init()
        self.voice_id = voice_id
        self.rate = rate
        self.volume = volume

    def initialize(self) -> None:
        self.engine.setProperty("rate", self.rate)
        self.engine.setProperty("volume", self.volume)

        if self.voice_id:
            voices = self.engine.getProperty("voices")
            for voice in voices:
                if voice.id == self.voice_id:
                    self.engine.setProperty("voice", voice.id)
                    break

    def get_voices(self) -> list[str]:
        voices = self.engine.getProperty("voices")
        return [voice.name for voice in voices]

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self) -> None:
        self.engine.stop()

    def pause(self) -> None:
        try:
            self.engine.stop()
        except Exception:
            pass

    def resume(self) -> None:
        pass
