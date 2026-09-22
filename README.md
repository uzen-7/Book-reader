# Universal Book Reader

Universal Book Reader is a Python desktop application for reading PDFs, DOCX files, and image-based documents aloud using offline OCR and TTS.

## Features

- Searchable PDF extraction using PyMuPDF
- OCR for scanned PDFs and image pages using Tesseract
- DOCX text extraction through python-docx
- Image OCR for JPG, PNG, WEBP, BMP, TIFF, and related file types
- Text cleaning and segmentation for speech
- Offline TTS via pyttsx3 with system voice support
- SQLite persistence for settings and recent books
- Modular architecture suitable for future GUI and advanced OCR work

## Supported formats

- PDF
- DOCX
- JPEG
- JPG
- PNG
- WEBP
- BMP
- TIFF
- TIF

## Project structure

```text
.
├── app/
│   ├── __init__.py
│   ├── application.py
│   └── config.py
├── core/
│   ├── __init__.py
│   ├── document.py
│   ├── document_manager.py
│   └── page.py
├── database/
│   ├── __init__.py
│   └── database.py
├── extraction/
│   ├── __init__.py
│   ├── base_extractor.py
│   ├── docx_extractor.py
│   ├── document_detector.py
│   └── pdf_extractor.py
├── gui/
├── ocr/
│   ├── __init__.py
│   ├── image_preprocessor.py
│   ├── language_manager.py
│   └── ocr_engine.py
├── speech/
│   ├── __init__.py
│   ├── base_tts.py
│   ├── pyttsx3_engine.py
│   ├── speech_controller.py
│   └── speech_queue.py
├── tests/
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── logger.py
│   └── text_utils.py
├── .venv/
├── INSTALL.md
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── run.sh
├── setup.sh
└── tests/
```

## Installation

```bash
git clone <repo-url>
cd "Book reader"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## System dependencies

Install the system packages for OCR and speech:

```bash
sudo apt update
sudo apt install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-hin tesseract-ocr-nep espeak-ng
```

## Running

```bash
source .venv/bin/activate
python main.py
```

## OCR configuration

The OCR engine uses Tesseract and can be configured through the `ocr.language_manager` and the `OCRProcessor` settings. The default language is English (`eng`).

## TTS configuration

The default implementation is `pyttsx3`, which works with installed system audio engines. A dedicated GUI and settings layer can be added on top of this architecture.

## Troubleshooting

- If Tesseract is missing, install it using the commands above.
- If OCR returns empty text, the page may be low contrast or a non-text image.
- If TTS is not working, verify the system speech backend is installed and operational.

## Development notes

The project is intentionally structured for incremental growth. The current core implementation covers the document detection, extraction, OCR, TTS abstraction, and text processing layers.

## Testing

```bash
source .venv/bin/activate
pytest -q
```

## Future improvements

- Complete PySide6 GUI with document viewer and playback controls
- OCR cache system and resume tracking
- Search, bookmarks, and chapter navigation
- Advanced OCR preprocessing and page classification
- Optional online TTS backend
