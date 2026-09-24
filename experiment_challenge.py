"""Content model for one learner-facing experiment challenge."""

from bot_configuration import BotConfiguration


class ExperimentChallenge:
    """One sequential challenge inside an experiment stage."""

    def __init__(self, challenge_id, bot_configuration, scenario_id):
        if not isinstance(challenge_id, str) or not challenge_id.strip():
            raise ValueError("challenge_id must be a non-empty string.")
        if not isinstance(scenario_id, str) or not scenario_id.strip():
            raise ValueError("scenario_id must be a non-empty string.")
        if not isinstance(bot_configuration, BotConfiguration):
            raise TypeError(
                "bot_configuration must be a BotConfiguration instance."
            )

        self.challenge_id = challenge_id.strip()
        self.scenario_id = scenario_id.strip()
        self.bot_configuration = bot_configuration

    def question(self, language):
        return self.bot_configuration.question(language)

    def answer(self, language):
        return self.bot_configuration.answer(language)

    def explanation(self, language):
        return self.bot_configuration.explanation(language)

    def hint(self, language):
        return self.bot_configuration.hint(language)

    def keywords(self, language):
        return self.bot_configuration.keywords(language)

    def __repr__(self):
        return (
            f"ExperimentChallenge(challenge_id={self.challenge_id!r}, "
            f"scenario_id={self.scenario_id!r})"
        )
