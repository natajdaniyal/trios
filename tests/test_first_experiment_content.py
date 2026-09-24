import pytest

from bot_configuration import SUPPORTED_LANGUAGES
from experiment_challenge import ExperimentChallenge
from first_experiment import (
    FIRST_EXPERIMENT_ID,
    first_stage_challenges,
)


def test_first_stage_has_three_ordered_challenges():
    challenges = first_stage_challenges()

    assert len(challenges) == 3
    assert [challenge.challenge_id for challenge in challenges] == [
        "stage-1-challenge-1",
        "stage-1-challenge-2",
        "stage-1-challenge-3",
    ]
    assert [challenge.scenario_id for challenge in challenges] == [
        "opposite-poles",
        "same-poles",
        "three-magnets",
    ]


def test_first_stage_uses_independent_bot_configuration_per_challenge():
    first, second, third = first_stage_challenges()

    assert first.bot_configuration is not second.bot_configuration
    assert second.bot_configuration is not third.bot_configuration
    assert first.question("fa") != third.question("fa")


def test_first_stage_exposes_complete_multilingual_content():
    for challenge in first_stage_challenges():
        assert isinstance(challenge, ExperimentChallenge)
        for language in SUPPORTED_LANGUAGES:
            assert challenge.question(language)
            assert challenge.keywords(language)
            assert challenge.answer(language)
            assert challenge.explanation(language)
            assert challenge.hint(language)


def test_first_stage_third_challenge_requires_multiple_concepts():
    third = first_stage_challenges()[2]

    assert third.bot_configuration.minimum_matches == 2
    assert third.bot_configuration.question("fa")
    assert "همزمان" in third.bot_configuration.keywords("fa")


def test_first_experiment_id_is_stable():
    assert FIRST_EXPERIMENT_ID == "three-body-is-hard"


def test_first_stage_rejects_invalid_challenge_content_contract():
    with pytest.raises(TypeError):
        ExperimentChallenge("challenge", object(), "scenario")
