from __future__ import annotations

from pathlib import Path

import pytesseract
from PIL import Image

from ocr.image_preprocessor import ImagePreprocessor
from utils.text_utils import clean_text


class OCRResult:
    """Single OCR result payload."""

    def __init__(self, text: str, status: str = "OCR_SUCCESS") -> None:
        self.text = text
        self.status = status


class OCRProcessor:
    """Perform OCR for images and scanned PDFs."""

    def __init__(self, language: str = "eng") -> None:
        self.language = language
        self.preprocessor = ImagePreprocessor()

    def _has_meaningful_text(self, candidate: str) -> bool:
        compact = " ".join(candidate.split())
        return len(compact) >= 20

    def process_image(self, image_path: str | Path) -> OCRResult:
        """Run OCR against an image file and return a structured result."""
        path = Path(image_path)
        if not path.exists():
            return OCRResult("", "OCR_FAILED")

        try:
            image = Image.open(path)
            processed = self.preprocessor.preprocess(path)
            processed_path = path.with_suffix(".ocr_temp.png")
            processed.save(processed_path)
            text = pytesseract.image_to_string(processed, lang=self.language)
            cleaned = clean_text(text)
            if not cleaned:
                return OCRResult("", "OCR_EMPTY")
            if not self._has_meaningful_text(cleaned):
                return OCRResult("", "OCR_EMPTY")
            processed_path.unlink(missing_ok=True)
            return OCRResult(cleaned, "OCR_SUCCESS")
        except Exception:
            return OCRResult("", "OCR_FAILED")
