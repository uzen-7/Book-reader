from __future__ import annotations

from PySide6.QtWidgets import QTextEdit


class DocumentViewer(QTextEdit):
    """Simple text viewer for extracted page text."""

    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)
        self.setPlaceholderText("Open a book to begin reading.")

    def set_document_text(self, text: str) -> None:
        self.setPlainText(text)
