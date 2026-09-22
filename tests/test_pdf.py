from pathlib import Path

import fitz

from extraction.pdf_extractor import PDFExtractor


def test_pdf_extractor_extracts_searchable_text(tmp_path: Path):
    pdf_path = tmp_path / "sample.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Hello world from PDF extraction.")
    document.save(pdf_path)
    document.close()

    pages = PDFExtractor().extract(pdf_path)
    assert len(pages) == 1
    assert "Hello world from PDF extraction." in pages[0]["text"]
