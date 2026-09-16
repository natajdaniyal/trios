import pytest
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from simulation.physical_configuration_adapter import simulation_from_configuration
from simulation_engine import SimulationEngine


def make_config():
    configuration = StagePhysicalConfiguration()
    configuration.add_body(BodyPhysicalConfiguration("A", 10, 1.0, 2.0, 0.5, -0.5))
    configuration.add_body(BodyPhysicalConfiguration("B", 20, -3.0, 4.0, -1.0, 1.5))
    return configuration


def test_creates_simulation_engine_from_configuration():
    simulation = simulation_from_configuration(make_config(), time_step=0.25)
    assert isinstance(simulation, SimulationEngine)
    assert simulation.time == 0
    assert simulation.physics_engine.time_step == 0.25
    assert [body.name for body in simulation.bodies] == ["A", "B"]


def test_simulation_contains_copied_initial_state():
    simulation = simulation_from_configuration(make_config())
    assert simulation.bodies[0].mass == 10
    assert simulation.bodies[0].position.x == 1.0
    assert simulation.bodies[0].position.y == 2.0
    assert simulation.bodies[0].velocity.x == 0.5
    assert simulation.bodies[0].velocity.y == -0.5


def test_simulation_owns_independent_body_objects():
    configuration = make_config()
    simulation = simulation_from_configuration(configuration)
    configuration.get_body("A").mass = 999
    configuration.get_body("A").position_x = 100
    assert simulation.bodies[0].mass == 10
    assert simulation.bodies[0].position.x == 1.0


def test_empty_configuration_creates_empty_simulation():
    simulation = simulation_from_configuration(StagePhysicalConfiguration())
    assert isinstance(simulation, SimulationEngine)
    assert simulation.bodies == []


def test_rejects_invalid_configuration_type():
    with pytest.raises(TypeError):
        simulation_from_configuration("not a configuration")
