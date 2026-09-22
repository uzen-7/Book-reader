#!/usr/bin/env bash
set -eu

cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is required but was not found in PATH."
  exit 1
fi

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if ! command -v tesseract >/dev/null 2>&1; then
  echo "Warning: Tesseract is not installed. Install it with: sudo apt install tesseract-ocr"
fi

if ! command -v espeak >/dev/null 2>&1 && ! command -v espeak-ng >/dev/null 2>&1; then
  echo "Warning: Offline TTS backend not found. Install espeak-ng for an offline fallback."
fi

echo "Setup complete. Activate the environment with: source .venv/bin/activate"
