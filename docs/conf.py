"""Sphinx configuration."""

project = "libranet-flask"
author = "Wouter Vanden Hove"
copyright = ", Wouter Vanden Hove"  # noqa: A001 # pylint: disable=redefined-builtin
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
