import pytest

from bot_configuration import BotConfiguration
from experiment_infrastructure import Experiment, ExperimentResult, ExperimentStage
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from experiment_execution import run_experiment
from validation.system_validation import ConservationValidator


def make_configuration(*bodies):
    configuration = StagePhysicalConfiguration()
    for body in bodies:
        configuration.add_body(body)
    return configuration


def make_body(name, mass=1, position_x=0, position_y=0, velocity_x=0, velocity_y=0):
    return BodyPhysicalConfiguration(name, mass, position_x, position_y, velocity_x, velocity_y)


def test_run_experiment_returns_experiment_result():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))
    result = run_experiment(experiment, steps_per_stage=0)
    assert isinstance(result, ExperimentResult)
    assert result.data["experiment_name"] == "test-experiment"


def test_run_experiment_preserves_stage_order():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("first", make_configuration(make_body("A"))))
    experiment.add_stage(ExperimentStage("second", make_configuration(make_body("B"))))
    result = run_experiment(experiment, steps_per_stage=0)
    assert [stage["stage_name"] for stage in result.data["stages"]] == ["first", "second"]


def test_run_experiment_runs_requested_steps_with_requested_time_step():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))
    result = run_experiment(experiment, steps_per_stage=3, time_step=0.5)
    assert result.data["stages"][0]["time"] == pytest.approx(1.5)


def test_run_experiment_records_final_body_state():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(
        make_body("A", position_x=2, position_y=3, velocity_x=1, velocity_y=-2)
    )))
    result = run_experiment(experiment, steps_per_stage=2, time_step=1)
    body = result.data["stages"][0]["bodies"][0]
    assert body["name"] == "A"
    assert body["mass"] == 1
    assert body["position_x"] == pytest.approx(4)
    assert body["position_y"] == pytest.approx(-1)
    assert body["velocity_x"] == pytest.approx(1)
    assert body["velocity_y"] == pytest.approx(-2)


def test_run_experiment_collects_measurements():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))

    result = run_experiment(
        experiment,
        steps_per_stage=0,
        measurements=[lambda simulation: ("body_count", len(simulation.bodies))],
    )

    assert result.get_measurement("body_count") == 1


def test_run_experiment_collects_validation_results():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))

    result = run_experiment(
        experiment,
        steps_per_stage=0,
        validators=[
            lambda initial, final: (
                "conservation",
                ConservationValidator().compare(initial, final),
            )
        ],
    )

    validation = result.get_validation("conservation")
    assert validation["energy_error"] == pytest.approx(0)
    assert validation["momentum_error"] == pytest.approx(0)
    assert validation["angular_momentum_error"] == pytest.approx(0)
    assert validation["center_of_mass_error"] == pytest.approx(0)


def test_run_experiment_rejects_invalid_measurements():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))

    with pytest.raises(TypeError):
        run_experiment(experiment, measurements="energy")
    with pytest.raises(TypeError):
        run_experiment(experiment, measurements=["energy"])


def test_run_experiment_rejects_invalid_validators():
    experiment = Experiment("test-experiment")
    experiment.add_stage(ExperimentStage("stage-1", make_configuration(make_body("A"))))

    with pytest.raises(TypeError):
        run_experiment(experiment, validators="energy")
    with pytest.raises(TypeError):
        run_experiment(experiment, validators=["energy"])


def test_run_experiment_rejects_invalid_step_count():
    experiment = Experiment("test-experiment")
    with pytest.raises(TypeError):
        run_experiment(experiment, steps_per_stage=1.5)
    with pytest.raises(TypeError):
        run_experiment(experiment, steps_per_stage=True)
    with pytest.raises(ValueError):
        run_experiment(experiment, steps_per_stage=-1)


def make_bot_configuration():
    return BotConfiguration({
        "fa": {"question": "چه اتفاقی می‌افتد؟", "keywords": ["جذب", "نزدیک"]},
        "en": {"question": "What will happen?", "keywords": ["gravity", "closer"]},
        "ar": {"question": "ماذا سيحدث؟", "keywords": ["جاذبية", "أقرب"]},
        "zh": {"question": "会发生什么？", "keywords": ["引力", "靠近"]},
        "es": {"question": "¿Qué pasará?", "keywords": ["gravedad", "cerca"]},
        "fr": {"question": "Que se passera-t-il ?", "keywords": ["gravité", "proche"]},
        "de": {"question": "Was wird passieren?", "keywords": ["gravitation", "näher"]},
        "ja": {"question": "何が起こりますか？", "keywords": ["重力", "近づく"]},
    })


def test_run_experiment_evaluates_configured_bot():
    experiment = Experiment(
        "bot-experiment",
        bot_configuration=make_bot_configuration(),
    )
    experiment.add_stage(
        ExperimentStage("stage-1", make_configuration(make_body("A")))
    )

    result = run_experiment(
        experiment,
        steps_per_stage=0,
        bot_answer="گرانش باعث می‌شود اجسام به هم نزدیک شوند.",
        bot_language="fa",
    )

    assert result.has_bot_evaluation()
    assert result.get_bot_evaluation().is_correct is True
    assert result.get_bot_evaluation().language == "fa"


def test_run_experiment_requires_bot_answer_when_bot_is_configured():
    experiment = Experiment(
        "bot-experiment",
        bot_configuration=make_bot_configuration(),
    )
    experiment.add_stage(
        ExperimentStage("stage-1", make_configuration(make_body("A")))
    )

    with pytest.raises(ValueError):
        run_experiment(experiment, steps_per_stage=0)


def test_run_experiment_requires_bot_inputs_together():
    experiment = Experiment("bot-experiment")

    with pytest.raises(ValueError):
        run_experiment(
            experiment,
            steps_per_stage=0,
            bot_answer="gravity",
        )
