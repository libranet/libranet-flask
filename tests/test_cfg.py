# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_flask.cfg."""

import pathlib as pl

import pytest


def test_get_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    from libranet_flask.cfg import get_settings

    monkeypatch.setenv("PROJECT_NAME", "custom-project")
    monkeypatch.setenv("BASE_DIR", "/tmp/test-base-dir")
    monkeypatch.setenv("TMPDIR", "/custom/tmp")

    settings = get_settings()

    assert settings.project_name == "custom-project"
    assert settings.base_dir == pl.Path("/tmp/test-base-dir")
    assert settings.tmpdir == pl.Path("/custom/tmp")
