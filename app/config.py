from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AppConfig:
    """Main application configuration."""

    data_dir: Path = Path.home() / ".universal_book_reader"
    cache_dir: Path = field(default_factory=lambda: Path.home() / ".universal_book_reader" / "cache")
    log_dir: Path = field(default_factory=lambda: Path.home() / ".universal_book_reader" / "logs")
    db_path: Path = field(default_factory=lambda: Path.home() / ".universal_book_reader" / "app.db")
    ocr_language: str = "eng"
    tts_voice: str = "default"
    tts_speed: float = 1.0
    tts_volume: float = 1.0
    theme: str = "dark"
    skip_empty_pages: bool = True
    auto_page_advance: bool = True

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)
