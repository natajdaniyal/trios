import os
import subprocess
import sys
import time
from pathlib import Path
import pytest
from test_reporter import TriosTestReporter

TEST_FOLDER = Path(__file__).parent
EXCLUDED_TESTS = {"test_bridge.py", "test_runner.py", "test_reporter.py"}


def discover_tests():
    return sorted(
        [path for path in TEST_FOLDER.glob("test_*.py") if path.name not in EXCLUDED_TESTS],
        key=lambda path: path.name.lower(),
    )


def _subprocess_environment():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    project_root = TEST_FOLDER.parent.resolve()
    paths = [
        str(project_root),
        str(project_root / "core"),
        str(project_root / "simulation"),
        str(project_root / "validation"),
        str(project_root / "tools"),
    ]
    existing_pythonpath = env.get("PYTHONPATH")
    if existing_pythonpath:
        paths.append(existing_pythonpath)
    env["PYTHONPATH"] = os.pathsep.join(paths)
    return env


def _subprocess_command(test_file):
    project_root = str(TEST_FOLDER.parent.resolve())
    core_path = str((TEST_FOLDER.parent / "core").resolve())
    simulation_path = str((TEST_FOLDER.parent / "simulation").resolve())
    validation_path = str((TEST_FOLDER.parent / "validation").resolve())
    tools_path = str((TEST_FOLDER.parent / "tools").resolve())
    bootstrap = (
        "import runpy, sys; "
        f"sys.path[:0] = {project_root!r}, {core_path!r}, {simulation_path!r}, {validation_path!r}, {tools_path!r}; "
        "runpy.run_path(sys.argv[1], run_name='__main__')"
    )
    return [sys.executable, "-c", bootstrap, str(test_file)]


def run_custom_test(test_file):
    result = subprocess.run(
        _subprocess_command(test_file),
        cwd=TEST_FOLDER.parent,
        env=_subprocess_environment(),
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode


def run_custom_test_with_result(test_file, reporter):
    start_time = time.perf_counter()
    result = subprocess.run(
        _subprocess_command(test_file),
        cwd=TEST_FOLDER.parent,
        env=_subprocess_environment(),
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    duration = time.perf_counter() - start_time
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    message = None
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or f"Process exited with code {result.returncode}"
    reporter.add_test_result(test_file.name, result.returncode, duration, message)
    return result.returncode


def run_all_tests_with_report():
    tests = discover_tests()
    reporter = TriosTestReporter()
    print("\n" + "=" * 58)
    print("🔌 TRIOS TEST BRIDGE")
    print("=" * 58)
    print(f"\n🔎 Discovered Tests: {len(tests)}\n")
    for index, test_file in enumerate(tests, start=1):
        print(f"▶ [{index:02d}/{len(tests):02d}] {test_file.name}")
        run_custom_test_with_result(test_file, reporter)
        print("-" * 58)
    reporter.print_report()
    return reporter


def show_discovered_tests():
    tests = discover_tests()
    print("\n" + "=" * 55)
    print("🔌 TRIOS TEST BRIDGE")
    print("=" * 55)
    print(f"\n🔎 Discovered Tests: {len(tests)}\n")
    for index, test in enumerate(tests, start=1):
        print(f"{index:02d}. {test.name}")
    print("\n" + "=" * 55)
    print("🟢 TEST DISCOVERY COMPLETE")
    print("=" * 55)
    return tests


@pytest.mark.parametrize("test_file", discover_tests(), ids=lambda path: path.name)
def test_trios_custom_test(test_file):
    return_code = run_custom_test(test_file)
    assert return_code == 0, f"Trios custom test failed: {test_file.name}"


def run_combined_tests():
    return run_all_tests_with_report()


if __name__ == "__main__":
    run_all_tests_with_report()
