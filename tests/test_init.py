# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_flask.__init__."""
# import packaging.version

# def test_version():
#     from libranet_flask import __version__

#     assert isinstance(__version__, str)
#     assert packaging.version.parse(__version__) > packaging.version.parse("0.0")


def test_copyright():
    from libranet_flask import __copyright__

    assert isinstance(__copyright__, str)
    assert "Libranet" in __copyright__
