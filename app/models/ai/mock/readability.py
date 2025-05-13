import re


def calculate_readability(review: str) -> float:
    """
    Calculate a simple readability score for the review
    using a Flesch Reading Ease approximation.
    Returns a float score (higher is easier to read).
    """
    words = review.split()
    num_words = len(words)
    num_sentences = max(1, review.count('.')
                        + review.count('!')
                        + review.count('?'))
    num_syllables = sum(len(
        re.findall(r'[aeiouy]+', word.lower())
        ) for word in words)
    score = 206.835 - 1.015 * (num_words / num_sentences) \
        - 84.6 * (num_syllables / num_words)
    return round(score, 2)
