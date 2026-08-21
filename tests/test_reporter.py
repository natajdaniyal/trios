from dataclasses import dataclass
from typing import Optional


@dataclass
class TestResult:
    name: str
    status: str
    duration: Optional[float] = None
    message: Optional[str] = None


class TriosTestReporter:
    """
    Complete reporting system for the Trios test infrastructure.

    The reporter receives test results from the Trios test system
    and produces a clean, unified report.
    """

    def __init__(self):
        self.results: list[TestResult] = []

    def add_result(
        self,
        name: str,
        status: str,
        duration: Optional[float] = None,
        message: Optional[str] = None,
    ):
        """
        Add a test result to the report.
        """

        self.results.append(
            TestResult(
                name=name,
                status=status,
                duration=duration,
                message=message,
            )
        )

    def add_test_result(
        self,
        test_file,
        return_code: int,
        duration: Optional[float] = None,
        message: Optional[str] = None,
    ):
        """
        Add the result of a real Trios custom test.

        return_code == 0  -> PASSED
        return_code != 0  -> FAILED
        """

        status = "PASSED" if return_code == 0 else "FAILED"

        self.add_result(
            name=str(test_file),
            status=status,
            duration=duration,
            message=message,
        )

    @property
    def total(self) -> int:
        """Return total number of recorded tests."""
        return len(self.results)

    @property
    def passed(self) -> int:
        """Return number of passed tests."""
        return sum(
            result.status == "PASSED"
            for result in self.results
        )

    @property
    def failed(self) -> int:
        """Return number of failed tests."""
        return sum(
            result.status == "FAILED"
            for result in self.results
        )

    @property
    def skipped(self) -> int:
        """Return number of skipped tests."""
        return sum(
            result.status == "SKIPPED"
            for result in self.results
        )

    def print_report(self):
        """
        Print the complete Trios test report.
        """

        print()
        print("=" * 58)
        print("📊 TRIOS COMPLETE TEST REPORT")
        print("=" * 58)

        print()
        print(f"🔎 Total Tests    : {self.total}")
        print(f"🧪 Passed         : {self.passed}")
        print(f"❌ Failed         : {self.failed}")
        print(f"⏭️  Skipped        : {self.skipped}")

        print()
        print("-" * 58)
        print("📋 TEST RESULTS")
        print("-" * 58)

        for index, result in enumerate(self.results, start=1):

            if result.status == "PASSED":
                icon = "🟢"
            elif result.status == "FAILED":
                icon = "🔴"
            elif result.status == "SKIPPED":
                icon = "🟡"
            else:
                icon = "⚪"

            duration = ""

            if result.duration is not None:
                duration = f" ({result.duration:.3f}s)"

            print(
                f"{index:02d}. {icon} "
                f"{result.name:<40}"
                f"{result.status}{duration}"
            )

            if result.message:
                print(f"    └─ {result.message}")

        print()
        print("-" * 58)
        print("🧠 SYSTEM HEALTH")
        print("-" * 58)

        if self.failed == 0 and self.total > 0:
            print("🟢 Custom Test System : HEALTHY")
        else:
            print("🔴 Custom Test System : UNHEALTHY")

        print()
        print("=" * 58)

        if self.failed == 0 and self.total > 0:
            print("🟢 TRIOS TEST SYSTEM HEALTHY")
        else:
            print("🔴 TRIOS TEST SYSTEM UNHEALTHY")

        print("=" * 58)


if __name__ == "__main__":
    reporter = TriosTestReporter()

    reporter.add_result(
        "example_test.py",
        "PASSED",
        0.125,
    )

    reporter.add_result(
        "broken_test.py",
        "FAILED",
        0.087,
        "Example failure",
    )

    reporter.print_report()