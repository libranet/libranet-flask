"""Tests for module libranet_flask.cli."""

import pytest


def test_cli(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that the main command runs without error."""
    from libranet_flask.cli import app

    # Invoke the app with no arguments (runs default command)
    # Must pass empty list explicitly to prevent cyclopts from using sys.argv
    with pytest.raises(SystemExit) as exc_info:
        app([])

    assert exc_info.value.code == 0

    captured = capsys.readouterr()
    # main() currently does nothing (pass), so no output expected
    assert captured.out == ""


def test_app_version(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that --version flag works."""
    from libranet_flask.about import version
    from libranet_flask.cli import app

    # Invoke the app with --version flag
    with pytest.raises(SystemExit) as exc_info:
        app(["--version"])

    # --version typically exits with code 0
    assert exc_info.value.code == 0

    captured = capsys.readouterr()
    assert str(version) in captured.out
