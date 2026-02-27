"""libranet_flask.logging."""

import importlib.resources

import libranet_logging


def initialize() -> None:
    """Configure logging using the logging.yaml file from the package resources."""
    logging_yaml_file = importlib.resources.files("libranet_flask").joinpath("logging.yaml")  # Python3.9+
    libranet_logging.initialize(path=logging_yaml_file)
