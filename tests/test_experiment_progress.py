import pytest

from experiment_progress import (
    DEFAULT_HINT_COST,
    DEFAULT_STAGE_REWARD,
    add_coins,
    complete_stage,
    default_experiment_progress,
    ensure_experiment_progress,
    is_stage_completed,
    is_stage_unlocked,
    spend_hint,
)


def test_new_progress_starts_empty():
    profile = {}
    progress = ensure_experiment_progress(profile)

    assert progress == default_experiment_progress()


def test_first_stage_is_unlocked_and_completion_rewards_coins_once():
    profile = {}

    assert is_stage_unlocked(profile, "experiment-1", 1) is True

    result = complete_stage(profile, "experiment-1", 1)

    assert result == {
        "completed_now": True,
        "coins_awarded": DEFAULT_STAGE_REWARD,
    }
    assert is_stage_completed(profile, "experiment-1", 1) is True
    assert profile["experiment_progress"]["coins"] == DEFAULT_STAGE_REWARD

    result = complete_stage(profile, "experiment-1", 1)
    assert result == {"completed_now": False, "coins_awarded": 0}
    assert profile["experiment_progress"]["coins"] == DEFAULT_STAGE_REWARD


def test_next_stage_stays_locked_until_previous_stage_is_completed():
    profile = {}

    assert is_stage_unlocked(profile, "experiment-1", 2) is False

    with pytest.raises(ValueError, match="Stage is locked"):
        complete_stage(profile, "experiment-1", 2)

    complete_stage(profile, "experiment-1", 1)

    assert is_stage_unlocked(profile, "experiment-1", 2) is True
    complete_stage(profile, "experiment-1", 2)
    assert is_stage_completed(profile, "experiment-1", 2) is True


def test_different_experiments_have_independent_progress():
    profile = {}

    complete_stage(profile, "experiment-1", 1)

    assert is_stage_unlocked(profile, "experiment-1", 2) is True
    assert is_stage_unlocked(profile, "experiment-2", 2) is False


def test_hint_spending_requires_enough_coins():
    profile = {}
    add_coins(profile, DEFAULT_HINT_COST)

    assert spend_hint(profile) is True
    assert profile["experiment_progress"]["coins"] == 0
    assert spend_hint(profile) is False


def test_add_coins_from_external_reward_source():
    profile = {}

    assert add_coins(profile, 25) == 25
    assert add_coins(profile, 5) == 30


def test_invalid_progress_values_are_repaired():
    profile = {
        "experiment_progress": {
            "coins": -5,
            "completed_stages": {"experiment-1": [1, "bad", -2, True]},
        }
    }

    progress = ensure_experiment_progress(profile)

    assert progress["coins"] == 0
    assert progress["completed_stages"] == {"experiment-1": [1]}


def test_invalid_stage_identifiers_are_rejected():
    with pytest.raises(ValueError):
        is_stage_unlocked({}, "", 1)

    with pytest.raises(ValueError):
        is_stage_unlocked({}, "experiment-1", 0)
