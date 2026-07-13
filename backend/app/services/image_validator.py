from PIL import Image
from pathlib import Path


ALLOWED_FORMATS = ["JPEG", "PNG", "JPG", "WEBP"]


def validate_image(file_path: str):

    path = Path(file_path)

    # Check if file exists
    if not path.exists():
        return {
            "valid": False,
            "message": "Image file does not exist"
        }

    try:
        image = Image.open(path)

        width, height = image.size

        # Check format
        if image.format not in ALLOWED_FORMATS:
            return {
                "valid": False,
                "message": "Unsupported image format"
            }

        # Check resolution
        if width < 200 or height < 200:
            return {
                "valid": False,
                "message": "Image resolution is too small"
            }

        return {
            "valid": True,
            "message": "Image is valid",
            "width": width,
            "height": height,
            "format": image.format
        }

    except Exception:
        return {
            "valid": False,
            "message": "Invalid image file"
        }