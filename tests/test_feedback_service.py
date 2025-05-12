import pytest
from app.services.feedback_service import generate_feedback

def test_generate_feedback_positive():
    review = "I love this product! It is excellent."
    feedback = generate_feedback(review)
    assert feedback["sentiment"] == "positive"
    assert isinstance(feedback["readability_score"], float)
    assert isinstance(feedback["suggestions"], list)

def test_generate_feedback_negative():
    review = "This is a terrible product. I hate it."
    feedback = generate_feedback(review)
    assert feedback["sentiment"] == "negative"

def test_generate_feedback_neutral():
    review = "This product is okay."
    feedback = generate_feedback(review)
    assert feedback["sentiment"] == "neutral"
