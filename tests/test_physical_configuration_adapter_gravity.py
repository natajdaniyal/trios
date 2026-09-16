from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration
from simulation.physical_configuration_adapter import simulation_from_configuration


def test_default_configuration_simulation_uses_gravity():
    configuration = StagePhysicalConfiguration()
    configuration.add_body(BodyPhysicalConfiguration(name="A", mass=1.0, position_x=0.0))
    configuration.add_body(BodyPhysicalConfiguration(name="B", mass=1.0, position_x=1.0))
    simulation = simulation_from_configuration(configuration, time_step=0.1)
    simulation.step()
    assert simulation.bodies[0].velocity.x > 0
    assert simulation.bodies[1].velocity.x < 0
