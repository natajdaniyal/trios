import pytest

from body import Body
from experiment_infrastructure import ExperimentStage
from physical_configuration import (
    BodyPhysicalConfiguration,
    StagePhysicalConfiguration,
)
from simulation_engine import SimulationEngine
from simulation.physical_configuration_adapter import simulation_from_stage


def make_stage():
    configuration = StagePhysicalConfiguration()
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="A",
            mass=10,
            position_x=1.0,
            position_y=2.0,
            velocity_x=0.5,
            velocity_y=-0.5,
        )
    )
    configuration.add_body(
        BodyPhysicalConfiguration(
            name="B",
            mass=20,
            position_x=-3.0,
            position_y=4.0,
            velocity_x=-1.0,
            velocity_y=1.5,
        )
    )
    return ExperimentStage("stage-1", configuration)


def test_stage_creates_simulation_engine():
    simulation = simulation_from_stage(make_stage())

    assert isinstance(simulation, SimulationEngine)
    assert len(simulation.bodies) == 2


def test_stage_simulation_contains_fresh_bodies():
    stage = make_stage()
    simulation = simulation_from_stage(stage)

    assert all(isinstance(body, Body) for body in simulation.bodies)
    assert [body.name for body in simulation.bodies] == ["A", "B"]


def test_stage_physical_values_reach_simulation():
    simulation = simulation_from_stage(make_stage(), time_step=0.25)

    assert simulation.physics_engine.time_step == 0.25
    assert simulation.bodies[0].mass == 10
    assert simulation.bodies[0].position.x == 1.0
    assert simulation.bodies[0].position.y == 2.0
    assert simulation.bodies[0].velocity.x == 0.5
    assert simulation.bodies[0].velocity.y == -0.5


def test_stage_simulation_is_independent_from_configuration():
    stage = make_stage()
    simulation = simulation_from_stage(stage)

    stage.physical_configuration.get_body("A").mass = 999
    stage.physical_configuration.get_body("A").position_x = 100

    assert simulation.bodies[0].mass == 10
    assert simulation.bodies[0].position.x == 1.0


def test_rejects_invalid_stage_type():
    with pytest.raises(TypeError):
        simulation_from_stage("not a stage")
