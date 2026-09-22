from __future__ import annotations

from pathlib import Path

import fitz

from core.document import Document, Page
from extraction.base_extractor import BaseExtractor


class PDFExtractor(BaseExtractor):
    """Extract text from PDF files, preserving page boundaries."""

    def extract(self, file_path: str | Path) -> list[dict]:
        path = Path(file_path)
        document = fitz.open(path)
        pages: list[dict] = []

        for index in range(document.page_count):
            page = document.load_page(index)
            page_text = page.get_text("text")
            clean_text = " ".join(page_text.split())
            source = "embedded" if len(clean_text) > 25 else "ocr_pending"
            pages.append(
                {
                    "page_number": index + 1,
                    "text": clean_text,
                    "source": source,
                    "image_path": None,
                    "metadata": {"page_index": index},
                }
            )

        document.close()
        return pages


def extract_pdf_document(file_path: str | Path) -> Document:
    """Create a Document object from a PDF file."""
    path = Path(file_path)
    pages = PDFExtractor().extract(path)
    document_pages = [Page(page_number=item["page_number"], text=item["text"], source=item["source"], metadata=item["metadata"]) for item in pages]
    return Document(file_path=path, title=path.stem, pages=document_pages, document_type="pdf")
