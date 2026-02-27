"""libranet_flask.endpoints."""

import logging

import flask

log = logging.getLogger(__name__)
api = flask.Blueprint("api", __name__)


@api.route("/")
def index() -> str:
    """Serve the homepage."""
    log.info("Hello homepage")
    return "Hello."


@api.route("/message", methods=["GET", "POST"])
def message() -> dict[str, str]:
    """Return a greeting message."""
    return {"message": "Hello World."}


@api.route("/health-check", methods=["GET"])
def health() -> str:
    """Return health check status."""
    return "OK"


@api.route("/favicon.ico")
def favicon() -> flask.Response:
    """Serve the favicon."""
    return flask.send_from_directory("static", "favicon.png", mimetype="image/png")


# @app.route('/css/<path:filename>')
# def css(filename):
#     return send_from_directory('css', filename)
