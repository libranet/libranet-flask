"""demo_flask.endpoints."""
import logging
import typing as tp

import flask

log = logging.getLogger(__name__)
api = flask.Blueprint("api", __name__)


@api.route("/")
def index() -> str:
    log.info("Hello homepage")
    return "Hello Libranet."


@api.route("/message", methods=["GET", "POST"])
def message() -> tp.Dict[str, str]:
    return {"message": "Hello World."}


@api.route("/health-check", methods=["GET"])
def health() -> str:
    return "OK"


@api.route("/favicon.ico")
def favicon():
    # return flask.send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/png")
    return flask.send_from_directory("static", "favicon.png", mimetype="image/png")


# @app.route('/css/<path:filename>')
# def css(filename):
#     return send_from_directory('css', filename)
