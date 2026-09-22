#!/usr/bin/env bash
set -eu

cd "$(dirname "$0")"

if [ -f .venv/bin/activate ]; then
  . .venv/bin/activate
fi

python main.py
