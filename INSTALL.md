# Installation guide

## Linux / Ubuntu

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv python3-full tesseract-ocr tesseract-ocr-eng tesseract-ocr-hin tesseract-ocr-nep espeak-ng
```

## Python environment

```bash
cd "Book reader"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Verification

```bash
python3 --version
tesseract --version
tesseract --list-langs
espeak --version
```

## Notes

- Tesseract language data must match the OCR language selected in the app.
- If using a language pack missing from the system, install it explicitly.
- The app relies on offline TTS via `pyttsx3` and system engines such as `espeak-ng`.
