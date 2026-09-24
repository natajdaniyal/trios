"""Runtime layer for the experiment-facing TRIOS Bot.

This module turns a BotConfiguration into a small, deterministic runtime
contract. It does not know about Streamlit, accounts, physics, simulation,
reports, or UI widgets.
"""

from dataclasses import dataclass

from bot_configuration import BotConfiguration, KeywordMatcher


@dataclass(frozen=True)
class BotEvaluationResult:
    """Immutable result of evaluating one learner prediction."""

    language: str
    answer: str
    matched_keywords: tuple[str, ...]
    missing_keywords: tuple[str, ...]
    match_count: int
    required_matches: int
    status: str
    is_correct: bool


class BotRuntime:
    """Execute the experiment-facing Bot contract for one configuration."""

    def __init__(self, configuration):
        if not isinstance(configuration, BotConfiguration):
            raise TypeError(
                "BotRuntime expects a BotConfiguration instance."
            )

        self.configuration = configuration
        self._matcher = KeywordMatcher(configuration)

    def question(self, language):
        """Return the configured question for the selected language."""
        return self.configuration.question(language)

    def evaluate(self, answer, language):
        """Evaluate one learner answer against the configured Bot rules."""
        # KeywordMatcher performs the answer type and language validation.
        matched_keywords = tuple(
            self._matcher.matched_keywords(answer, language)
        )
        configured_keywords = self.configuration.keywords(language)
        missing_keywords = tuple(
            keyword
            for keyword in configured_keywords
            if keyword not in matched_keywords
        )

        match_count = len(matched_keywords)
        required_matches = self.configuration.minimum_matches

        if match_count >= required_matches:
            status = "correct"
        elif match_count > 0:
            status = "partial"
        else:
            status = "incorrect"

        return BotEvaluationResult(
            language=language,
            answer=answer,
            matched_keywords=matched_keywords,
            missing_keywords=missing_keywords,
            match_count=match_count,
            required_matches=required_matches,
            status=status,
            is_correct=status == "correct",
        )
