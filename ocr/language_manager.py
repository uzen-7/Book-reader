from __future__ import annotations

import shutil
from typing import List


class LanguageManager:
    """Tracks OCR language data availability and configuration."""

    SUPPORTED_LANGUAGES = {
        "English": "eng",
        "Hindi": "hin",
        "Nepali": "nep",
    }

    @staticmethod
    def available_languages() -> list[str]:
        """Return installed Tesseract language codes."""
        try:
            result = shutil.which("tesseract")
            if not result:
                return []
        except Exception:
            return []

        import subprocess

        try:
            completed = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True, check=False)
        except FileNotFoundError:
            return []

        languages: list[str] = []
        for line in completed.stdout.splitlines()[1:]:
            if line.strip():
                languages.append(line.strip().split()[0])
        return languages

    @staticmethod
    def validate_language(config: str) -> bool:
        """Return True when the configured tesseract language is installed."""
        installed = LanguageManager.available_languages()
        return config in installed

    @staticmethod
    def language_code(label: str) -> str:
        """Translate human-readable label into a Tesseract code."""
        return LanguageManager.SUPPORTED_LANGUAGES.get(label, "eng")
