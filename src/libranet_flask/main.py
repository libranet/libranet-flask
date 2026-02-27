"""libranet_flask.main."""

import flask
import flask_cors
import libranet_logging


def before_first_request() -> None:
    """Perform setup-actions before serving the first request.

    Use instantiated app via
        >>> app = flask.current_app
    """


def before_request() -> None:
    """Perform setup-actions before serving the any request.

    Use instantiated app via
    >>> app = flask.current_app

    """


def register_blueprints(app: flask.Flask) -> None:
    """Register all blueprints for application."""
    import libranet_flask.cli.flask  # noqa: PLC0415
    import libranet_flask.endpoints  # noqa: PLC0415

    # mount api-endpoints under /
    app.register_blueprint(libranet_flask.endpoints.api, url_prefix="/")

    # register cli-commands
    app.register_blueprint(libranet_flask.cli.flask.demo)


def register_cors(app: flask.Flask) -> None:
    """Register cors-extension."""
    cors = flask_cors.CORS()
    resources = {"*": {"origins": "*"}}
    cors.init_app(app, resources=resources)


def create_app() -> flask.Flask:
    """Factory-method to instantiate a new ``Flask``-app."""
    libranet_logging.initialize()

    app = flask.Flask(__name__)
    # see https://github.com/flask-dashboard/Flask-MonitoringDashboard/commit/40530882d2298b4601e4e95e4b6a9a760be32b96
    # app.before_first_request(before_first_request)  # deprecated
    app.before_request(before_request)

    register_cors(app)
    register_blueprints(app)

    app.logger.debug("debug from flask")
    app.logger.info("info from flask")
    app.logger.warning("warn from flask")

    return app
