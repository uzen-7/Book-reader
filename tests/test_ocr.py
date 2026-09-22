from ocr.language_manager import LanguageManager
from ocr.ocr_engine import OCRProcessor


def test_language_manager_reports_configured_languages():
    labels = LanguageManager.SUPPORTED_LANGUAGES
    assert "English" in labels
    assert "Hindi" in labels
    assert "Nepali" in labels


def test_ocr_processor_handles_missing_file_gracefully():
    processor = OCRProcessor(language="eng")
    result = processor.process_image("missing.png")
    assert result.status in {"OCR_FAILED", "OCR_EMPTY"}
