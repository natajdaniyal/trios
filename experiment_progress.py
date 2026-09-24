"""Learner progression and coin mechanics for TRIOS experiments.

This module contains no Streamlit/UI code and no physics or simulation logic.
It only defines persistent progression rules that higher layers can use.
"""

DEFAULT_STAGE_REWARD = 10
DEFAULT_HINT_COST = 5


def default_experiment_progress():
    """Return a fresh persistent progression structure."""
    return {
        "coins": 0,
        "completed_stages": {},
    }


def ensure_experiment_progress(profile):
    """Add missing progression fields without changing existing progress."""
    if not isinstance(profile, dict):
        raise TypeError("profile must be a dictionary.")

    progress = profile.get("experiment_progress")
    if not isinstance(progress, dict):
        progress = default_experiment_progress()
        profile["experiment_progress"] = progress

    coins = progress.get("coins", 0)
    if not isinstance(coins, int) or isinstance(coins, bool) or coins < 0:
        progress["coins"] = 0

    completed_stages = progress.get("completed_stages")
    if not isinstance(completed_stages, dict):
        progress["completed_stages"] = {}

    normalized = {}
    for experiment_id, stages in progress["completed_stages"].items():
        if isinstance(stages, (list, tuple, set)):
            normalized[str(experiment_id)] = sorted(
                {
                    int(stage)
                    for stage in stages
                    if isinstance(stage, int) and not isinstance(stage, bool) and stage > 0
                }
            )
    progress["completed_stages"] = normalized
    return progress


def _validate_ids(experiment_id, stage_number):
    if not isinstance(experiment_id, str) or not experiment_id.strip():
        raise ValueError("experiment_id must be a non-empty string.")
    if (
        not isinstance(stage_number, int)
        or isinstance(stage_number, bool)
        or stage_number < 1
    ):
        raise ValueError("stage_number must be a positive integer.")


def is_stage_completed(profile, experiment_id, stage_number):
    """Return whether a stage has been completed at least once."""
    _validate_ids(experiment_id, stage_number)
    progress = ensure_experiment_progress(profile)
    return stage_number in progress["completed_stages"].get(experiment_id, [])


def is_stage_unlocked(profile, experiment_id, stage_number):
    """Stage 1 is open; later stages require the immediately previous stage."""
    _validate_ids(experiment_id, stage_number)
    if stage_number == 1:
        return True
    return is_stage_completed(profile, experiment_id, stage_number - 1)


def complete_stage(profile, experiment_id, stage_number, reward=DEFAULT_STAGE_REWARD):
    """Mark a stage complete and award coins once for its first completion.

    Returns a dict containing whether the stage was newly completed and the
    number of coins awarded.
    """
    _validate_ids(experiment_id, stage_number)

    if (
        not isinstance(reward, int)
        or isinstance(reward, bool)
        or reward < 0
    ):
        raise ValueError("reward must be a non-negative integer.")

    progress = ensure_experiment_progress(profile)
    stages = progress["completed_stages"].setdefault(experiment_id, [])

    if stage_number in stages:
        return {"completed_now": False, "coins_awarded": 0}

    if not is_stage_unlocked(profile, experiment_id, stage_number):
        raise ValueError("Stage is locked.")

    stages.append(stage_number)
    stages.sort()
    progress["coins"] += reward

    return {"completed_now": True, "coins_awarded": reward}


def spend_hint(profile, cost=DEFAULT_HINT_COST):
    """Spend coins for one hint.

    The caller owns the one-hint-per-attempt rule. This function only handles
    the persistent wallet transaction.
    """
    if (
        not isinstance(cost, int)
        or isinstance(cost, bool)
        or cost <= 0
    ):
        raise ValueError("cost must be a positive integer.")

    progress = ensure_experiment_progress(profile)
    if progress["coins"] < cost:
        return False

    progress["coins"] -= cost
    return True


def add_coins(profile, amount):
    """Add coins from any approved reward source, such as a daily reward."""
    if (
        not isinstance(amount, int)
        or isinstance(amount, bool)
        or amount <= 0
    ):
        raise ValueError("amount must be a positive integer.")

    progress = ensure_experiment_progress(profile)
    progress["coins"] += amount
    return progress["coins"]
