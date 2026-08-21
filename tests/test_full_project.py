import os
import sys
import subprocess


TEST_FOLDER = os.path.dirname(__file__)


TESTS = [
    "test_vector.py",
    "test_body.py",
    "test_force.py",
    "test_multiple_forces.py",
    "test_gravitational_force.py",
    "test_physics_engine.py",
    "test_engine_stability.py",
    "test_events.py",
    "test_command.py",
    "test_input_engine.py",
    "test_magnetic_force.py",
    "test_force_system.py",
    "test_force_engine_integration.py",
    "test_full_physics_chain.py",
    "test_simulation_engine.py",
    "test_magnet.py",
    "test_magnetic_behavior.py",
    "test_magnet_physics_integration.py",
]


def run_full_project_test():
    """
    Runs the existing Trios test system.

    Returns:
        passed: number of passed tests
        failed: number of failed tests
    """

    print("\n🌌 TRIOS FULL PROJECT TEST")
    print("===========================")

    passed = 0
    failed = 0

    for test in TESTS:

        print("\n▶ Running:", test)

        result = subprocess.run(
            [
                sys.executable,
                os.path.join(TEST_FOLDER, test)
            ],
            env={
                **os.environ,
                "PYTHONIOENCODING": "utf-8"
            },
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode == 0:
            print("✅", test, "PASSED")
            passed += 1

        else:
            print("❌", test, "FAILED")
            failed += 1

    print("\n===========================")
    print("TOTAL TESTS:", len(TESTS))
    print("PASSED:", passed)
    print("FAILED:", failed)

    if failed == 0:
        print("\n🟢 TRIOS PROJECT HEALTHY")
    else:
        print("\n🔴 TRIOS PROJECT HAS PROBLEMS")

    return passed, failed


def test_full_project():
    """
    Pytest entry point.

    Connects the existing Trios Full Test System
    to pytest.
    """

    passed, failed = run_full_project_test()

    assert failed == 0, (
        f"Trios Full Project Test failed: "
        f"{failed} test(s) failed, "
        f"{passed} test(s) passed."
    )