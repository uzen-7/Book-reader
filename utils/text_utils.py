from __future__ import annotations

import re


def clean_text(raw_text: str) -> str:
    """Normalize text while preserving paragraph boundaries and punctuation."""
    if not raw_text:
        return ""

    text = raw_text.replace("\x00", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\n +", "\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r" ?\n ?", " ", text)
    text = text.strip()
    return text
