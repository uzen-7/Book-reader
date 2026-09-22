from __future__ import annotations

from pathlib import Path


DOCUMENT_EXTENSIONS = {
    "pdf": "pdf",
    "docx": "docx",
    "jpg": "image",
    "jpeg": "image",
    "png": "image",
    "webp": "image",
    "bmp": "image",
    "tif": "image",
    "tiff": "image",
}


def detect_document_type(file_path: str | Path) -> str:
    """Detect the document family for a file path."""
    suffix = Path(file_path).suffix.lower().lstrip(".")
    return DOCUMENT_EXTENSIONS.get(suffix, "unknown")
