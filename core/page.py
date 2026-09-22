from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SpeechChunk:
    """One spoken unit. The queue will process these sequentially."""

    page_number: int
    text: str
    sentence_index: int = 0
    chunk_index: int = 0
    source: str = "text"


@dataclass
class ReadingPosition:
    """Current reading position used for asking to resume later."""

    document_id: Optional[str] = None
    page_index: int = 0
    paragraph_index: int = 0
    sentence_index: int = 0
    chunk_index: int = 0
    position_label: str = ""
    updated_at: Optional[str] = None
