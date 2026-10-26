from pydantic import BaseModel
from typing import List


class UIIssue(BaseModel):
    category: str
    severity: str
    component: str
    description: str
    recommendation: str


class ReviewResponse(BaseModel):
    overall_score: int
    total_issues: int
    issues: List[UIIssue]
    is_demo: bool = False