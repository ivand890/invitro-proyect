def generate_suggestions(review: str) -> list[str]:
    """
    Generate suggestions for improving the review content using simple rules.
    Returns a list of suggestion strings.
    """
    suggestions = []
    if len(review.split()) < 10:
        suggestions.append("Add more details to your review.")
    if not review[0].isupper():
        suggestions.append("Start your review with a capital letter.")
    if not review.endswith((".", "!", "?")):
        suggestions.append("End your review with proper punctuation.")
    if len(suggestions) == 0:
        suggestions.append("Your review looks good!")
    return suggestions
