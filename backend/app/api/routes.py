from fastapi import APIRouter, UploadFile, File
from fastapi import HTTPException
from pathlib import Path
import logging
import random
import shutil

from app.services.review_service import review_ui
from app.schemas.review_schema import ReviewResponse

from app.services.image_validator import validate_image
from huggingface_hub.errors import HfHubHTTPError


router = APIRouter()
logger = logging.getLogger(__name__)

DEMO_ISSUES = [
    {
        "category": "Visual Hierarchy",
        "severity": "Minor",
        "component": "Page heading",
        "description": "The primary heading does not stand out clearly from surrounding content.",
        "recommendation": "Increase the heading's visual prominence and keep a clear type scale.",
    },
    {
        "category": "Color & Contrast",
        "severity": "Major",
        "component": "Secondary text",
        "description": "Some supporting text may be difficult to distinguish from its background.",
        "recommendation": "Check text and background color combinations against WCAG contrast guidance.",
    },
    {
        "category": "Layout & Structure",
        "severity": "Minor",
        "component": "Content spacing",
        "description": "Spacing between a few content groups appears inconsistent.",
        "recommendation": "Apply a consistent spacing scale to related sections and controls.",
    },
    {
        "category": "Accessibility",
        "severity": "Major",
        "component": "Form controls",
        "description": "Some controls may benefit from more descriptive visible labels.",
        "recommendation": "Use persistent labels that clearly explain the purpose of each control.",
    },
]


import tempfile

try:
    BASE_DIR = Path(__file__).resolve().parents[2]
    UPLOAD_DIR = BASE_DIR / "uploads" / "screenshots"
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
except Exception:
    UPLOAD_DIR = Path(tempfile.gettempdir()) / "screenshots"
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

    try:
        result = review_ui(str(file_path))
    except HfHubHTTPError as exc:
        logger.warning("Hugging Face inference request failed with HTTP %s", exc.response.status_code)
        if exc.response.status_code == 402:
            issue_count = random.randint(2, len(DEMO_ISSUES))
            result = {
                "overall_score": random.randint(6, 9),
                "total_issues": issue_count,
                "issues": random.sample(DEMO_ISSUES, issue_count),
                "is_demo": True,
            }
        else:
            raise HTTPException(
                status_code=502,
                detail=(
                    "The screenshot analysis service is temporarily unavailable. "
                    "Please try again later."
                ),
            ) from exc

    return result