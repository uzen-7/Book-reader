from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


class ImagePreprocessor:
    """Apply conservative preprocessing to improve OCR quality."""

    def preprocess(self, image_path: str | Path, dpi: int = 300) -> Image.Image:
        path = Path(image_path)
        image = Image.open(path)

        if image.mode not in {"RGB", "L"}:
            image = image.convert("RGB")

        image = ImageOps.grayscale(image)
        image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)
        image = image.filter(ImageFilter.SHARPEN)
        image = ImageOps.autocontrast(image)
        image = image.point(lambda p: 255 if p > 180 else 0)
        return image
