from dataclasses import dataclass
from math import hypot

from angular_momentum import AngularMomentumSystem
from center_of_mass import CenterOfMassSystem
from energy import EnergySystem
from momentum import MomentumSystem


@dataclass(frozen=True)
class PhysicalStateSnapshot:
    """Scientific snapshot of a body system at one instant."""

    total_energy: float
    total_momentum: tuple
    angular_momentum: float
    center_of_mass: tuple

    @classmethod
    def capture(cls, bodies, gravitational_constant=1):
        energy = EnergySystem(gravitational_constant)
        momentum = MomentumSystem()
        angular_momentum = AngularMomentumSystem()
        center_of_mass = CenterOfMassSystem()

        return cls(
            total_energy=energy.total_energy(bodies),
            total_momentum=momentum.total_momentum(bodies),
            angular_momentum=angular_momentum.total_angular_momentum(bodies),
            center_of_mass=center_of_mass.center_of_mass(bodies),
        )

    def as_dict(self):
        return {
            "total_energy": self.total_energy,
            "total_momentum": self.total_momentum,
            "angular_momentum": self.angular_momentum,
            "center_of_mass": self.center_of_mass,
        }


class ConservationValidator:
    """Compare two physical snapshots without modifying simulation state."""

    def compare(self, initial, final):
        if not isinstance(initial, PhysicalStateSnapshot):
            raise TypeError("initial must be a PhysicalStateSnapshot instance.")
        if not isinstance(final, PhysicalStateSnapshot):
            raise TypeError("final must be a PhysicalStateSnapshot instance.")

        energy_error = abs(final.total_energy - initial.total_energy)
        momentum_delta = (
            final.total_momentum[0] - initial.total_momentum[0],
            final.total_momentum[1] - initial.total_momentum[1],
        )
        momentum_error = hypot(*momentum_delta)
        angular_momentum_error = abs(
            final.angular_momentum - initial.angular_momentum
        )
        center_of_mass_delta = (
            final.center_of_mass[0] - initial.center_of_mass[0],
            final.center_of_mass[1] - initial.center_of_mass[1],
        )
        center_of_mass_error = hypot(*center_of_mass_delta)

        return {
            "energy_change": final.total_energy - initial.total_energy,
            "energy_error": energy_error,
            "momentum_change": momentum_delta,
            "momentum_error": momentum_error,
            "angular_momentum_change": (
                final.angular_momentum - initial.angular_momentum
            ),
            "angular_momentum_error": angular_momentum_error,
            "center_of_mass_change": center_of_mass_delta,
            "center_of_mass_error": center_of_mass_error,
        }
