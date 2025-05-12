from abc import ABC, abstractmethod

class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, review: str) -> str:
        pass

class ReadabilityScorer(ABC):
    @abstractmethod
    def score(self, review: str) -> float:
        pass

class SuggestionGenerator(ABC):
    @abstractmethod
    def suggest(self, review: str) -> list[str]:
        pass
