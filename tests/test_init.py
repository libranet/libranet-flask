# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_flask.__init__."""

import packaging.version


def test_version() -> None:
    from libranet_flask import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


def test_license() -> None:
    import libranet_flask
    # from libranet_flask import __license__

    assert isinstance(libranet_flask.__license__, str)
    assert "Copyright" in libranet_flask.__license__
