from app.ai.sentiment import analyze_sentiment
from app.ai.readability import calculate_readability
from app.ai.suggestions import generate_suggestions


def generate_feedback(review: str) -> dict:
    """
    Generate structured feedback for a product review.
    Returns a dict with sentiment, readability_score, and suggestions.
    """
    sentiment = analyze_sentiment(review)
    readability_score = calculate_readability(review)
    suggestions = generate_suggestions(review)
    return {
        "sentiment": sentiment,
        "readability_score": readability_score,
        "suggestions": suggestions,
    }
