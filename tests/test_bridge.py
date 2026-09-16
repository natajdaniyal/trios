import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

from test_reporter import TriosTestReporter


TEST_FOLDER = Path(__file__).parent


# فایل‌های زیرساختی سیستم تست.
# این فایل‌ها خودِ سیستم تست هستند و نباید
# به عنوان Custom Test اجرا شوند.
EXCLUDED_TESTS = {
    "test_bridge.py",
    "test_runner.py",
    "test_reporter.py",
}


def discover_tests():
    """
    Automatically discover every Trios custom test.

    Any new tests/test_*.py file will automatically
    become part of the Trios test system.
    """

    tests = []

    for path in TEST_FOLDER.glob("test_*.py"):

        if path.name in EXCLUDED_TESTS:
            continue

        tests.append(path)

    return sorted(
        tests,
        key=lambda path: path.name.lower()
    )


def _subprocess_environment():
    """Build the environment used by standalone Trios test subprocesses."""

    env = os.environ.copy()

    # Force UTF-8 for Windows subprocesses.
    env["PYTHONIOENCODING"] = "utf-8"

    # Keep the project's existing flat-import architecture available when
    # custom tests are launched as independent Python processes.
    project_root = TEST_FOLDER.parent
    python_paths = [
        project_root,
        project_root / "core",
        project_root / "simulation",
        project_root / "validation",
        project_root / "tools",
    ]

    existing_pythonpath = env.get("PYTHONPATH")
    paths = [str(path) for path in python_paths]

    if existing_pythonpath:
        paths.append(existing_pythonpath)

    env["PYTHONPATH"] = os.pathsep.join(paths)

    return env


def run_custom_test(test_file):
    """
    Execute one Trios custom test.

    Returns:
        0 -> PASSED
        non-zero -> FAILED
    """

    result = subprocess.run(
        [
            sys.executable,
            str(test_file),
        ],
        cwd=TEST_FOLDER.parent,
        env=_subprocess_environment(),
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )

    # Keep original custom-test output visible.
    if result.stdout:
        print(result.stdout, end="")

    if result.stderr:
        print(
            result.stderr,
            end="",
            file=sys.stderr,
        )

    return result.returncode


def run_custom_test_with_result(test_file, reporter):
    """
    Execute one custom test and send its result
    directly to the Trios reporter.
    """

    start_time = time.perf_counter()

    result = subprocess.run(
        [
            sys.executable,
            str(test_file),
        ],
        cwd=TEST_FOLDER.parent,
        env=_subprocess_environment(),
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )

    duration = time.perf_counter() - start_time

    # Show original test output.
    if result.stdout:
        print(result.stdout, end="")

    if result.stderr:
        print(
            result.stderr,
            end="",
            file=sys.stderr,
        )

    message = None

    if result.returncode != 0:

        if result.stderr.strip():
            message = result.stderr.strip()

        elif result.stdout.strip():
            message = result.stdout.strip()

        else:
            message = (
                f"Process exited with code "
                f"{result.returncode}"
            )

    reporter.add_test_result(
        test_file.name,
        result.returncode,
        duration,
        message,
    )

    return result.returncode


def run_all_tests_with_report():
    """
    Run every discovered Trios custom test
    and produce one complete report.
    """

    tests = discover_tests()

    reporter = TriosTestReporter()

    print()
    print("=" * 58)
    print("🔌 TRIOS TEST BRIDGE")
    print("=" * 58)

    print()
    print(f"🔎 Discovered Tests: {len(tests)}")

    print()
    print("-" * 58)

    for index, test_file in enumerate(
        tests,
        start=1,
    ):
        print(
            f"▶ [{index:02d}/{len(tests):02d}] "
            f"{test_file.name}"
        )

        run_custom_test_with_result(
            test_file,
            reporter,
        )

        print("-" * 58)

    print()
    print("📊 Generating complete report...")

    reporter.print_report()

    return reporter


def show_discovered_tests():
    """
    Display every test discovered by the bridge.
    """

    tests = discover_tests()

    print()
    print("=" * 55)
    print("🔌 TRIOS TEST BRIDGE")
    print("=" * 55)

    print()
    print(
        f"🔎 Discovered Tests: {len(tests)}"
    )

    print()

    for index, test in enumerate(
        tests,
        start=1,
    ):
        print(
            f"{index:02d}. {test.name}"
        )

    print()
    print("=" * 55)
    print("🟢 TEST DISCOVERY COMPLETE")
    print("=" * 55)

    return tests


@pytest.mark.parametrize(
    "test_file",
    discover_tests(),
    ids=lambda path: path.name,
)
def test_trios_custom_test(test_file):
    """
    Automatic Pytest bridge.

    Every discovered Trios custom test becomes
    one Pytest test automatically.
    """

    return_code = run_custom_test(test_file)

    assert return_code == 0, (
        f"Trios custom test failed: "
        f"{test_file.name}"
    )


def run_combined_tests():
    """
    Compatibility function for the Trios test runner.

    Runs all discovered custom tests and returns
    the complete reporter.
    """

    return run_all_tests_with_report()


if __name__ == "__main__":
    run_all_tests_with_report()
