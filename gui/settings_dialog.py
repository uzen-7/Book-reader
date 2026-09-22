from __future__ import annotations

from PySide6.QtWidgets import (QComboBox, QDialog, QFormLayout, QHBoxLayout,
                               QLabel, QPushButton, QVBoxLayout)


class SettingsDialog(QDialog):
    """Minimal settings dialog for language and TTS choices."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(420, 220)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.language_combo = QComboBox()
        self.language_combo.addItems(["English", "Hindi", "Nepali", "English + Hindi", "English + Nepali"])

        self.voice_combo = QComboBox()
        self.voice_combo.addItems(["default", "male", "female"])

        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["0.75x", "1.0x", "1.25x", "1.5x", "2.0x"])

        form.addRow(QLabel("OCR language"), self.language_combo)
        form.addRow(QLabel("Voice"), self.voice_combo)
        form.addRow(QLabel("Speed"), self.speed_combo)

        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        buttons.addStretch()
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)

        layout.addLayout(form)
        layout.addLayout(buttons)
