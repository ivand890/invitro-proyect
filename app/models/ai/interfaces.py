from abc import ABC, abstractmethod


class ReviewAnalyzerInterface(ABC):

    @abstractmethod
    def get_suggestions(self, review: str) -> list[str]:
        pass

    @abstractmethod
    def get_sentiment(self, review: str) -> str:
        pass

    @abstractmethod
    def get_score(self, review: str) -> float:
        pass
