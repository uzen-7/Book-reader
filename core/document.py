from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class Page:
    """Represents a single page of extracted document content."""

    page_number: int
    text: str = ""
    source: str = "embedded"
    image_path: Optional[Path] = None
    metadata: dict = field(default_factory=dict)


@dataclass
class Document:
    """Represents a processed book or PDF document."""

    file_path: Path
    title: str
    pages: List[Page] = field(default_factory=list)
    document_type: str = "unknown"
    toc: List[dict] = field(default_factory=list)
    engine: str = "unknown"
