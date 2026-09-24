import pytest

from bot_runtime import BotEvaluationResult
from first_experiment_runtime import (
    DEFAULT_CHALLENGE_STEPS,
    DEFAULT_CHALLENGE_TIME_STEP,
    first_stage_challenge,
    first_stage_challenge_count,
    evaluate_challenge_prediction,
    run_challenge,
)


def test_first_stage_challenge_order_is_stable():
    assert first_stage_challenge_count() == 3
    assert first_stage_challenge(0).challenge_id == "stage-1-challenge-1"
    assert first_stage_challenge(1).challenge_id == "stage-1-challenge-2"
    assert first_stage_challenge(2).challenge_id == "stage-1-challenge-3"


def test_first_stage_prediction_is_evaluated_without_ui_or_physics_coupling():
    challenge = first_stage_challenge(0)

    result = evaluate_challenge_prediction(
        challenge,
        "این دو آهنربا همدیگر را جذب می‌کنند و نزدیک می‌شوند.",
        "fa",
    )

    assert isinstance(result, BotEvaluationResult)
    assert result.is_correct is True
    assert result.match_count >= result.required_matches


def test_three_magnet_prediction_uses_concept_criteria():
    challenge = first_stage_challenge(2)

    result = evaluate_challenge_prediction(
        challenge,
        "هر آهنربا همزمان از دو آهنربای دیگر اثر می‌گیرد.",
        "fa",
    )

    assert result.is_correct is True


def test_run_challenge_executes_the_real_two_magnet_scenario():
    challenge = first_stage_challenge(0)

    result = run_challenge(challenge, steps=1, time_step=0.01)

    assert result.challenge_id == "stage-1-challenge-1"
    assert result.scenario_id == "opposite-poles"
    assert result.time == pytest.approx(0.01)
    assert len(result.bodies) == 2
    assert result.bodies[0]["velocity_x"] > 0
    assert result.bodies[1]["velocity_x"] < 0


def test_run_challenge_uses_user_selected_initial_positions():
    challenge = first_stage_challenge(0)

    result = run_challenge(
        challenge,
        steps=1,
        time_step=0.01,
        initial_positions={"A": -2.0, "B": 2.0},
    )

    assert result.bodies[0]["position_x"] == pytest.approx(-2.0, abs=1e-3)
    assert result.bodies[1]["position_x"] == pytest.approx(2.0, abs=1e-3)
    assert result.bodies[0]["velocity_x"] > 0
    assert result.bodies[1]["velocity_x"] < 0


def test_run_challenge_executes_the_real_three_magnet_scenario():
    challenge = first_stage_challenge(2)

    result = run_challenge(challenge, steps=1, time_step=0.01)

    assert result.scenario_id == "three-magnets"
    assert len(result.bodies) == 3


@pytest.mark.parametrize("bad_steps", [-1, 1.5, True])
def test_run_challenge_rejects_invalid_steps(bad_steps):
    challenge = first_stage_challenge(0)

    expected = ValueError if bad_steps == -1 else TypeError
    with pytest.raises(expected):
        run_challenge(challenge, steps=bad_steps)


def test_run_challenge_rejects_invalid_time_step():
    challenge = first_stage_challenge(0)

    with pytest.raises(ValueError):
        run_challenge(challenge, time_step=0)

    with pytest.raises(TypeError):
        run_challenge(challenge, time_step="0.01")


def test_run_challenge_defaults_are_explicit():
    assert DEFAULT_CHALLENGE_STEPS == 100
    assert DEFAULT_CHALLENGE_TIME_STEP == 0.01


def test_stage_challenge_helpers_reject_invalid_indices():
    with pytest.raises(TypeError):
        first_stage_challenge("0")

    with pytest.raises(IndexError):
        first_stage_challenge(-1)

    with pytest.raises(IndexError):
        first_stage_challenge(3)
