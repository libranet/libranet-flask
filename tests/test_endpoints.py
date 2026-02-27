# pylint: disable=import-outside-toplevel
"""Tests for libranet_flask.endpoints."""


def test_endpoint_index(client):
    resp = client.get("/")
    assert b"Hello." in resp.data

    acl_allow_origin = resp.headers.get("Access-Control-Allow-Origin")
    assert acl_allow_origin == "*"
