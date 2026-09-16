"""Compatibility entry point for the existing demo experiment.

The public run_test(profile) function is preserved for the current menu,
while its execution now travels through the Experiment -> Stage ->
Physical Configuration -> Simulation path.
"""

from experiment_execution import run_experiment
from experiment_infrastructure import Experiment, ExperimentStage
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration


EXPERIMENT_NAME = "آزمایش آزمایشی نیرو"


def _build_demo_experiment():
    configuration = StagePhysicalConfiguration(stage_name="demo-stage")
    configuration.add_body(BodyPhysicalConfiguration("A", 1.0, 0.0, 0.0, 0.0, 0.0))
    configuration.add_body(BodyPhysicalConfiguration("B", 1.0, 1.0, 0.0, 0.0, 0.0))

    experiment = Experiment(EXPERIMENT_NAME)
    experiment.add_stage(ExperimentStage("demo-stage", configuration))
    return experiment


def run_test(profile):
    print("\n==============================")
    print("🧪 آزمایش آزمایشی Trios")
    print("==============================")

    prediction = input("\n✍️ فرضیه تو چیست؟ ")
    print("\n🔬 آزمایش انجام شد...")

    execution_result = run_experiment(
        _build_demo_experiment(),
        steps_per_stage=1,
        time_step=0.01,
    )

    stage_result = execution_result.data["stages"][0]
    moved = any(
        abs(body["velocity_x"]) > 0 or abs(body["velocity_y"]) > 0
        for body in stage_result["bodies"]
    )

    result = "نیروی گرانشی باعث حرکت جسم شد." if moved else "حرکت قابل مشاهده‌ای ثبت نشد."
    correct = True

    print("\n🧪 نتیجه:")
    print(result)

    profile.add_experiment(EXPERIMENT_NAME, prediction, result, correct)

    print("\n🤖 Trios-Bot:")
    print("گزارش آزمایش ذخیره شد. 🌌")
