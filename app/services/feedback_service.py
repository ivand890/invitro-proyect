from app.models.ai.mock import ReviewAnalyzer

def generate_feedback(review: str) -> dict:
    """
    Generate structured feedback for a product review.
    Returns a dict with sentiment, readability_score, and suggestions.
    """
    analyzer = ReviewAnalyzer()
    sentiment = analyzer.get_sentiment(review)
    readability_score = analyzer.get_score(review)
    suggestions = analyzer.get_suggestions(review)
    return {
        "sentiment": sentiment,
        "readability_score": readability_score,
        "suggestions": suggestions,
    }
