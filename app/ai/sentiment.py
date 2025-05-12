def analyze_sentiment(review: str) -> str:
    """
    Analyze the sentiment of a review using simple rule-based logic.
    Returns: 'positive', 'negative', or 'neutral'.
    """
    review_lower = review.lower()
    if any(word in review_lower for word in ["love", "great", "excellent", "good", "amazing"]):
        return "positive"
    elif any(word in review_lower for word in ["bad", "terrible", "awful", "poor", "hate"]):
        return "negative"
    else:
        return "neutral"
