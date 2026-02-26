"""libranet_flask.cli.flask.

Docs: https://flask.palletsprojects.com/en/2.2.x/cli/
"""
import click
import flask

demo = flask.Blueprint("demo", __name__)


@demo.cli.command("hello")
@click.option("--name", default="World")
def hello(name: str) -> None:
    """

    Usage:
        > bin/flask demo hello --name Foo
    """
    click.echo(f"Hello, {name}!")
