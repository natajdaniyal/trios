"""Runtime layer for the experiment-facing TRIOS Bot.

This module turns a BotConfiguration into a small, deterministic runtime
contract. It does not know about Streamlit, accounts, physics, simulation,
reports, or UI widgets.
"""

from dataclasses import dataclass

from bot_configuration import BotConfiguration, KeywordMatcher, normalize_text


@dataclass(frozen=True)
class BotEvaluationResult:
    """Immutable result of evaluating one learner prediction."""

    language: str
    answer: str
    matched_keywords: tuple[str, ...]
    match_count: int
    required_matches: int
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
        canonical = "".join(char for char in normalize_text(self.configuration.answer(language)) if char.isalnum())
        submitted = "".join(char for char in normalize_text(answer) if char.isalnum())
        if canonical and canonical in submitted:
            matched_keywords = tuple(self.configuration.keywords(language))
        else:
            matched_keywords = tuple(self._matcher.matched_keywords(answer, language))
        match_count = len(matched_keywords)
        required_matches = self.configuration.minimum_matches

        return BotEvaluationResult(
            language=language,
            answer=answer,
            matched_keywords=matched_keywords,
            match_count=match_count,
            required_matches=required_matches,
            is_correct=match_count >= required_matches,
        )
