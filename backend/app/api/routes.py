from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.services.review_service import review_ui
from app.schemas.review_schema import ReviewResponse

from app.services.image_validator import validate_image


router = APIRouter()


BASE_DIR = Path(__file__).resolve().parents[3]

UPLOAD_DIR = BASE_DIR / "uploads" / "screenshots"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.get("/health")
def health_check():
    return {
        "status": "Backend is healthy"
    }


@router.post("/analyze", response_model=ReviewResponse)
async def analyze_screenshot(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = review_ui(str(file_path))

    return result