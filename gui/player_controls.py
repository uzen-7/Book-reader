from __future__ import annotations

from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


class PlayerControls(QWidget):
    """Playback buttons used by the main window."""

    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout(self)

        self.previous_button = QPushButton("Previous")
        self.play_button = QPushButton("Play")
        self.stop_button = QPushButton("Stop")
        self.next_button = QPushButton("Next")

        layout.addWidget(self.previous_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.next_button)
