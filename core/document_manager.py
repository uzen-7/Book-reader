from __future__ import annotations

from pathlib import Path
from typing import Optional

from core.document import Document


class DocumentManager:
    """Coordinates loading and processing of documents."""

    def __init__(self) -> None:
        self.current_document: Optional[Document] = None

    def open_document(self, file_path: str | Path) -> Document:
        path = Path(file_path)
        return Document(file_path=path, title=path.stem, document_type=path.suffix.lower().lstrip("."))
