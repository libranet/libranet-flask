# pylint: disable=import-outside-toplevel
"""Tests for demo_flask.endpoints."""


def test_endpoint_index(client):
    resp = client.get("/")
    assert b"Hello." in resp.data

    acL_allow_origin = resp.headers.get("Access-Control-Allow-Origin")
    assert acL_allow_origin == "*"
