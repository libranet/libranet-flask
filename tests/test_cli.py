# pylint: disable=import-outside-toplevel
"""Tests for libranet_flask.cli."""


def test_hello_command(runner):
    result = runner.invoke(args="demo hello")
    assert "World" in result.output

    result = runner.invoke(args=["demo", "hello", "--name", "Flask"])
    assert "Flask" in result.output
