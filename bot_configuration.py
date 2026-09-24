"""TRIOS Bot configuration and multilingual keyword matching.

This layer defines the educational/demo interaction data for one experiment:
- a localized question for each supported language;
- localized keywords for each supported language;
- the minimum number of keywords required for a match.

It does not know about Streamlit, accounts, reports, physics, or simulation.
"""

from collections.abc import Mapping
from unicodedata import combining, normalize as unicode_normalize


SUPPORTED_LANGUAGES = ("fa", "en", "ar", "zh", "es", "fr", "de", "ja")


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
    """Localized configuration for the TRIOS Bot attached to one experiment."""

    def __init__(self, translations, minimum_matches=1):
        if not isinstance(translations, Mapping):
            raise TypeError("translations must be a mapping of language codes.")

        provided_languages = set(translations)
        supported_languages = set(SUPPORTED_LANGUAGES)

        missing_languages = supported_languages - provided_languages
        if missing_languages:
            missing = ", ".join(
                language for language in SUPPORTED_LANGUAGES if language in missing_languages
            )
            raise ValueError(
                f"BotConfiguration is missing translations for: {missing}."
            )

        unsupported_languages = provided_languages - supported_languages
        if unsupported_languages:
            unsupported = ", ".join(sorted(unsupported_languages))
            raise ValueError(
                f"Unsupported BotConfiguration languages: {unsupported}."
            )

        if (
            not isinstance(minimum_matches, int)
            or isinstance(minimum_matches, bool)
        ):
            raise TypeError("minimum_matches must be an integer.")
        if minimum_matches < 1:
            raise ValueError("minimum_matches must be at least 1.")

        localized_data = {}
        for language in SUPPORTED_LANGUAGES:
            localized = translations[language]
            if not isinstance(localized, Mapping):
                raise TypeError(
                    f"Translation for language '{language}' must be a mapping."
                )

            if "question" not in localized:
                raise ValueError(
                    f"Translation for language '{language}' requires a question."
                )
            if "keywords" not in localized:
                raise ValueError(
                    f"Translation for language '{language}' requires keywords."
                )

            question = localized["question"]
            if not isinstance(question, str) or not question.strip():
                raise ValueError(
                    f"Translation for language '{language}' requires a non-empty question."
                )

            keywords = localized["keywords"]
            if isinstance(keywords, (str, bytes)):
                raise TypeError(
                    f"Keywords for language '{language}' must be an iterable of strings."
                )

            try:
                keywords = list(keywords)
            except TypeError as exc:
                raise TypeError(
                    f"Keywords for language '{language}' must be an iterable of strings."
                ) from exc

            normalized_keywords = []
            seen = set()
            for keyword in keywords:
                if not isinstance(keyword, str):
                    raise TypeError(
                        f"Every keyword for language '{language}' must be a string."
                    )
                if not keyword.strip():
                    raise ValueError(
                        f"Keywords for language '{language}' cannot be empty."
                    )

                normalized = normalize_text(keyword)
                if normalized not in seen:
                    normalized_keywords.append(keyword.strip())
                    seen.add(normalized)

            if not normalized_keywords:
                raise ValueError(
                    f"Translation for language '{language}' requires at least one keyword."
                )

            if minimum_matches > len(normalized_keywords):
                raise ValueError(
                    "minimum_matches cannot exceed the number of keywords in "
                    f"language '{language}'."
                )

            localized_data[language] = {
                "question": question.strip(),
                "keywords": tuple(normalized_keywords),
                "answer": str(localized.get("answer", "")).strip(),
                "explanation": str(localized.get("explanation", "")).strip(),
                "hint": str(localized.get("hint", "")).strip(),
            }

        self._translations = localized_data
        self.minimum_matches = minimum_matches

    @property
    def translations(self):
        """Return the configured localized Bot data."""
        return {
            language: {
                "question": data["question"],
                "keywords": data["keywords"],
                "answer": data["answer"],
                "explanation": data["explanation"],
                "hint": data["hint"],
            }
            for language, data in self._translations.items()
        }

    def languages(self):
        """Return the supported languages available for this configuration."""
        return SUPPORTED_LANGUAGES

    def question(self, language):
        """Return the experiment-specific Bot question for a language."""
        language = self._validate_language(language)
        return self._translations[language]["question"]

    def keywords(self, language):
        """Return the experiment-specific Bot keywords for a language."""
        language = self._validate_language(language)
        return self._translations[language]["keywords"]

    @staticmethod
    def answer(self, language):
        """Return the configured final answer for a language."""
        language = self._validate_language(language)
        return self._translations[language]["answer"]

    def explanation(self, language):
        """Return the configured explanation for a language."""
        language = self._validate_language(language)
        return self._translations[language]["explanation"]

    def hint(self, language):
        """Return the configured hint for a language."""
        language = self._validate_language(language)
        return self._translations[language]["hint"]

    @staticmethod
    def _validate_language(language):
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported Bot language: {language!r}. "
                f"Supported languages: {', '.join(SUPPORTED_LANGUAGES)}."
            )
        return language

    def __repr__(self):
        return (
            f"BotConfiguration(languages={SUPPORTED_LANGUAGES!r}, "
            f"minimum_matches={self.minimum_matches!r})"
        )


class KeywordMatcher:
    """Evaluate an answer against the Bot keywords for the selected language."""

    def __init__(self, configuration):
        if not isinstance(configuration, BotConfiguration):
            raise TypeError(
                "KeywordMatcher expects a BotConfiguration instance."
            )
        self.configuration = configuration

    def matched_keywords(self, answer, language):
        """Return configured keywords found in the answer for a language."""
        self._validate_language(language)

        if not isinstance(answer, str):
            raise TypeError("Answer must be a string.")

        normalized_answer = normalize_text(answer)
        if not normalized_answer:
            return []

        return [
            keyword
            for keyword in self.configuration.keywords(language)
            if normalize_text(keyword) in normalized_answer
        ]

    def match_count(self, answer, language):
        return len(self.matched_keywords(answer, language))

    def matches(self, answer, language):
        return (
            self.match_count(answer, language)
            >= self.configuration.minimum_matches
        )

    def _validate_language(self, language):
        return self.configuration._validate_language(language)
