"""TRIOS Bot configuration and keyword matching.

This layer defines the educational/demo interaction data for one experiment:
- the question shown by TRIOS Bot;
- the keywords that count as a matching answer;
- the minimum number of keywords required for a match.

It does not know about Streamlit, accounts, reports, physics, or simulation.
"""

from unicodedata import combining, normalize as unicode_normalize


def normalize_text(value):
    """Normalize human-entered text for stable keyword matching."""
    if not isinstance(value, str):
        raise TypeError("Text must be a string.")

    value = unicode_normalize("NFKC", value)
    value = "".join(char for char in value if not combining(char))
    value = value.replace("ي", "ی").replace("ى", "ی").replace("ك", "ک")
    value = value.replace("\u200c", " ")
    return " ".join(value.casefold().split())


class BotConfiguration:
    """Configuration for the TRIOS Bot attached to one experiment."""

    def __init__(self, question, keywords, minimum_matches=1):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("BotConfiguration requires a non-empty question.")

        if isinstance(keywords, (str, bytes)):
            raise TypeError("keywords must be an iterable of strings.")

        try:
            keywords = list(keywords)
        except TypeError as exc:
            raise TypeError("keywords must be an iterable of strings.") from exc

        normalized_keywords = []
        seen = set()
        for keyword in keywords:
            if not isinstance(keyword, str):
                raise TypeError("Every keyword must be a string.")
            if not keyword.strip():
                raise ValueError("Keywords cannot be empty.")

            normalized = normalize_text(keyword)
            if normalized not in seen:
                normalized_keywords.append(keyword.strip())
                seen.add(normalized)

        if not normalized_keywords:
            raise ValueError("BotConfiguration requires at least one keyword.")

        if (
            not isinstance(minimum_matches, int)
            or isinstance(minimum_matches, bool)
        ):
            raise TypeError("minimum_matches must be an integer.")
        if not 1 <= minimum_matches <= len(normalized_keywords):
            raise ValueError(
                "minimum_matches must be between 1 and the number of keywords."
            )

        self.question = question.strip()
        self.keywords = tuple(normalized_keywords)
        self.minimum_matches = minimum_matches

    def __repr__(self):
        return (
            f"BotConfiguration(question={self.question!r}, "
            f"keywords={self.keywords!r}, "
            f"minimum_matches={self.minimum_matches!r})"
        )


class KeywordMatcher:
    """Evaluate an answer against a BotConfiguration's keywords."""

    def __init__(self, configuration):
        if not isinstance(configuration, BotConfiguration):
            raise TypeError(
                "KeywordMatcher expects a BotConfiguration instance."
            )
        self.configuration = configuration

    def matched_keywords(self, answer):
        """Return the configured keywords found in the supplied answer."""
        if not isinstance(answer, str):
            raise TypeError("Answer must be a string.")

        normalized_answer = normalize_text(answer)
        if not normalized_answer:
            return []

        return [
            keyword
            for keyword in self.configuration.keywords
            if normalize_text(keyword) in normalized_answer
        ]

    def match_count(self, answer):
        return len(self.matched_keywords(answer))

    def matches(self, answer):
        return self.match_count(answer) >= self.configuration.minimum_matches
