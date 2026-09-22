from __future__ import annotations

from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QMessageBox,
                               QPushButton, QTextEdit, QVBoxLayout, QWidget)

from gui.document_viewer import DocumentViewer
from gui.player_controls import PlayerControls
from gui.settings_dialog import SettingsDialog
from gui.styles import DARK_THEME


class MainWindow(QMainWindow):
    """Main desktop window for the application."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Universal Book Reader")
        self.resize(1200, 800)
        self.setStyleSheet(DARK_THEME)

        central = QWidget()
        main_layout = QVBoxLayout(central)

        top_bar = QHBoxLayout()
        self.open_button = QPushButton("Open Book")
        self.settings_button = QPushButton("Settings")
        self.about_button = QPushButton("About")
        top_bar.addWidget(self.open_button)
        top_bar.addWidget(self.settings_button)
        top_bar.addWidget(self.about_button)
        top_bar.addStretch()

        main_layout.addLayout(top_bar)

        self.page_label = QLabel("Page 1 / 1")
        self.viewer = DocumentViewer()
        self.controls = PlayerControls()

        main_layout.addWidget(self.page_label)
        main_layout.addWidget(self.viewer)
        main_layout.addWidget(self.controls)

        self.setCentralWidget(central)

        self.settings_dialog = SettingsDialog()
        self.connect_actions()

    def connect_actions(self) -> None:
        self.settings_button.clicked.connect(self.open_settings)
        self.about_button.clicked.connect(self.show_about)

    def open_settings(self) -> None:
        self.settings_dialog.exec()

    def show_about(self) -> None:
        QMessageBox.about(
            self,
            "About Universal Book Reader",
            "A Python-based document-to-speech reader supporting PDF, OCR, DOCX, and image documents.",
        )

    def set_page_text(self, text: str, page_number: int, total_pages: int) -> None:
        self.viewer.set_document_text(text)
        self.page_label.setText(f"Page {page_number} / {total_pages}")
