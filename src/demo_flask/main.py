"""demo_flask.main."""
import flask
import flask_cors
import libranet_logging

import demo_flask.cli
import demo_flask.endpoints


def before_first_request() -> None:
    """Perform setup-actions before serving the first request.

    Use instantiated app via
        >>> app = flask.current_app
    """
    pass  # noqa


def before_request() -> None:
    """Perform setup-actions before serving the any request.

    Use instantiated app via
    >>> app = flask.current_app

    """
    pass  # noqa


def register_blueprints(app: flask.Flask) -> None:
    """register all blueprints for application"""

    # mount api-endpoints under /
    app.register_blueprint(demo_flask.endpoints.api, url_prefix="/")

    # register cli-commands
    app.register_blueprint(demo_flask.cli.demo)


def register_cors(app: flask.Flask) -> None:
    """register cors-extension."""
    cors = flask_cors.CORS()
    resources = {"*": {"origins": "*"}}
    cors.init_app(app, resources=resources)


def create_app() -> flask.Flask:
    """Factory-method to instantiate a new ``Flask``-app."""
    libranet_logging.initialize()

    app = flask.Flask(__name__)
    app.before_first_request(before_first_request)
    app.before_request(before_request)

    register_cors(app)
    register_blueprints(app)

    app.logger.debug("debug from flask")
    app.logger.info("info from flask")
    app.logger.warn("warn from flask")

    return app
