# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module demo_flask.__init__."""
# import packaging.version

# def test_version():
#     from demo_flask import __version__

#     assert isinstance(__version__, str)
#     assert packaging.version.parse(__version__) > packaging.version.parse("0.0")


def test_copyright():
    from demo_flask import __copyright__

    assert isinstance(__copyright__, str)
    assert "EK Global" in __copyright__
