"""Confirm that the performance profiling functions work as expected."""

from time import sleep

from rich.console import Console

from filesorter.profile import (
    output_performance_data,
    performance_data,
    timer,
)


def test_timer():
    # Clear performance data before test
    performance_data.clear()
    with timer("Test Timer"):
        sleep(0.1)  # Simulate some work
    assert len(performance_data) == 1
    context, duration = performance_data[0]
    assert context == "Test Timer"
    # duration should be at least 100 ms
    assert (
        duration >= 100  # noqa: PLR2004
    )


def test_output_performance_data(capsys):
    # clear performance data before test
    performance_data.clear()
    # add some test data
    performance_data.append(("Test Timer 1", 123.45))
    performance_data.append(("Test Timer 2", 678.90))
    console = Console()
    output_performance_data(console, "Performance")
    captured = capsys.readouterr()
    assert "Performance Test Timer 1: 123.45 ms" in captured.out
    assert "Performance Test Timer 2: 678.90 ms" in captured.out
