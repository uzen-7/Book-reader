from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QApplication

from app.config import AppConfig
from gui.main_window import MainWindow
from utils.logger import get_logger


logger = get_logger("app", Path.home() / ".universal_book_reader" / "logs")


def main() -> None:
    """Create the application and show the main window."""
    config = AppConfig()
    config.ensure_dirs()

    app = QApplication([])
    app.setApplicationName("Universal Book Reader")
    window = MainWindow()
    window.show()
    logger.info("Application started")
    app.exec()
