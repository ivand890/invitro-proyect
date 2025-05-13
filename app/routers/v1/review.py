from fastapi import APIRouter
from pydantic import BaseModel
from app.services.feedback_service import generate_feedback


class ReviewRequest(BaseModel):
    """Request model for submitting a product review."""

    review: str


class FeedbackResponse(BaseModel):
    """Response model for structured feedback."""

    sentiment: str
    readability_score: float
    suggestions: list[str]


review_router = APIRouter(prefix="/review")


@review_router.post("/feedback", response_model=FeedbackResponse)
def review_feedback(request: ReviewRequest) -> FeedbackResponse:
    """Endpoint to receive a review and return AI-generated feedback."""
    return FeedbackResponse(**generate_feedback(request.review))
