"""libranet_flask.cli."""

import cyclopts

from libranet_flask.about import version
from libranet_flask.cli.subcmd1 import app_subcmd1

app: cyclopts.App = cyclopts.App(version=version)

# register subcommands
app.command(obj=app_subcmd1)


@app.default
def main() -> None:
    """Run the main command."""
