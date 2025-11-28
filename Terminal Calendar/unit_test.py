import importlib.util
from pathlib import Path


def load_script(path):
    """Loads a Python script as a module so it executes like running it normally."""
    spec = importlib.util.spec_from_file_location("calendar_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_calendar_valid(monkeypatch, capsys):
    """Test valid input: 30 days starting on Wednesday (day 3)."""

    # Fake user input sequence (30 days, start weekday = 3)
    inputs = iter(["30", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    script_path = Path("Terminal_Calendar.py")
    assert script_path.exists(), "Terminal_Calendar.py not found!"

    load_script(script_path)

    output = capsys.readouterr().out

    # calendar header
    assert "Mon Tue Wed Thu Fri Sat Sun" in output

    # should include day 1 and day 30
    assert " 1 " in output
    assert "30" in output

    # first week must start with two empty columns (starting day = 3 → two spaces groups)
    first_week_line = output.splitlines()[1]
    assert first_week_line.startswith("        ")  # 8 spaces = two columns


def test_calendar_invalid_days(monkeypatch, capsys):
    """Test invalid number of days triggers error message."""

    inputs = iter(["20"])  # invalid days (<28)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    script_path = Path("Terminal_Calendar.py")
    assert script_path.exists(), "Terminal_Calendar.py not found!"

    load_script(script_path)

    output = capsys.readouterr().out
    assert "Invalid number of days" in output

