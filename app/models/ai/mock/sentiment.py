def analyze_sentiment(review: str) -> str:
    """
    Analyze the sentiment of a review using simple rule-based logic.
    Returns: 'positive', 'negative', or 'neutral'.
    """
    POSITIVE_WORDS = ["love", "great", "excellent", "good", "amazing"]
    NEGATIVE_WORDS = ["bad", "terrible", "awful", "poor", "hate"]
    review_lower = review.lower()
    if any(word in review_lower for word in POSITIVE_WORDS):
        return "positive"
    elif any(word in review_lower for word in NEGATIVE_WORDS):
        return "negative"
    else:
        return "neutral"
