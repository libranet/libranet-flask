"""Tests for libranet_flask.logging."""

import logging as std_logging

from libranet_flask import logging


def test_initialize(capsys) -> None:
    """Test that initialize configures logging and log output works."""
    logging.initialize()

    logger = std_logging.getLogger("libranet_flask")
    logger.info("test message")

    captured = capsys.readouterr()
    assert "test message" in captured.out
