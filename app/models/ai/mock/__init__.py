from ..interfaces import ReviewAnalyzerInterface
from .readability import calculate_readability
from .sentiment import analyze_sentiment
from .suggestions import generate_suggestions


class ReviewAnalyzer(ReviewAnalyzerInterface):
    """
    A mock class to analyze product reviews.
    This class simulates the behavior of an AI model for educational purposes.
    """

    def get_suggestions(self, review: str) -> list[str]:
        """Generate suggestions based on the review."""
        return generate_suggestions(review)

    def get_sentiment(self, review: str) -> str:
        """Analyze the sentiment of the review."""
        return analyze_sentiment(review)

    def get_score(self, review: str) -> float:
        """Calculate the readability score of the review."""
        return calculate_readability(review)
