"""Execution helpers for the first TRIOS educational experiment.

This layer orchestrates learner-facing challenge content with the existing
simulation/scenario infrastructure. It does not put learner logic into the
physics or simulation core.
"""

from dataclasses import dataclass

from bot_runtime import BotEvaluationResult, BotRuntime
from experiment_challenge import ExperimentChallenge
from experiment_scenarios import build_experiment_one_scenario
from first_experiment import first_stage_challenges


FIRST_EXPERIMENT_STAGE_NUMBER = 1
DEFAULT_CHALLENGE_STEPS = 100
DEFAULT_CHALLENGE_TIME_STEP = 0.01


@dataclass(frozen=True)
class ChallengeExecutionResult:
    """Physics result plus the actual body states produced by each step."""

    challenge_id: str
    scenario_id: str
    time: float
    bodies: tuple[dict, ...]
    trajectory: tuple[tuple[dict, ...], ...]


def evaluate_challenge_prediction(challenge, answer, language):
    """Evaluate a learner prediction without exposing the result itself."""
    if not isinstance(challenge, ExperimentChallenge):
        raise TypeError(
            "challenge must be an ExperimentChallenge instance."
        )
    return BotRuntime(challenge.bot_configuration).evaluate(answer, language)


def run_challenge(
    challenge,
    steps=DEFAULT_CHALLENGE_STEPS,
    time_step=DEFAULT_CHALLENGE_TIME_STEP,
    force_engine=None,
    initial_positions=None,
):
    """Run one challenge's real physical scenario and return its final state."""
    if not isinstance(challenge, ExperimentChallenge):
        raise TypeError(
            "challenge must be an ExperimentChallenge instance."
        )
    if not isinstance(steps, int) or isinstance(steps, bool):
        raise TypeError("steps must be an integer.")
    if steps < 0:
        raise ValueError("steps must be >= 0.")
    if not isinstance(time_step, (int, float)) or isinstance(time_step, bool):
        raise TypeError("time_step must be a number.")
    if time_step <= 0:
        raise ValueError("time_step must be > 0.")

    simulation = build_experiment_one_scenario(
        challenge.scenario_id,
        time_step=time_step,
        positions=initial_positions,
    )
    if force_engine is not None:
        simulation.force_engine = force_engine

    def snapshot():
        return tuple(
            {
                "name": body.name,
                "mass": body.mass,
                "position_x": body.position.x,
                "position_y": body.position.y,
                "velocity_x": body.velocity.x,
                "velocity_y": body.velocity.y,
            }
            for body in simulation.bodies
        )

    trajectory = [snapshot()]
    for _ in range(steps):
        simulation.step()
        trajectory.append(snapshot())

    bodies = trajectory[-1]
    return ChallengeExecutionResult(
        challenge_id=challenge.challenge_id,
        scenario_id=challenge.scenario_id,
        time=simulation.time,
        bodies=bodies,
        trajectory=tuple(trajectory),
    )


def first_stage_challenge(index):
    """Return one ordered stage-1 challenge by zero-based index."""
    challenges = first_stage_challenges()
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError("index must be an integer.")
    if index < 0 or index >= len(challenges):
        raise IndexError("stage-1 challenge index is out of range.")
    return challenges[index]


def first_stage_challenge_count():
    """Return the number of sequential challenges in stage 1."""
    return len(first_stage_challenges())
