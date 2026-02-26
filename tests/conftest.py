# pylint: disable=import-outside-toplevel
"""conftest.py - custom pytest-plugins.

This file contains the configurations that we need for running our tests:
For more information about conftest.py, please see:

 - https://docs.pytest.org/en/latest/writing_plugins.html
 - https://pytest-flask.readthedocs.io/en/latest/tutorial.html
 - https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files

The "_helpers"-directory contains code that can be re-used in various tests.

Note: The tests-directory itself is NOT a python-package (no __init__.py).
Please avoid putting an __init.py-file in this directory.

If you by accident put an __init__.py in this tests-directory,
you will not be able to run pytest, instead it will fail with:

    > ImportError: Error importing plugin "_helpers": No module named '_helpers'

"""

import pytest


pytest_plugins = [
    "_helpers",
]


@pytest.fixture()
def app():
    import libranet_flask.main

    app = libranet_flask.main.create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
