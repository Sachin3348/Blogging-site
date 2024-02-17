from flask import Flask
from .routes import user_routes

app = Flask(__name__, instance_relative_config=True)


def create_app():
    # Load the default config
    app.config.from_object('config.default')

    # Load the config from instance folder
    app.config.from_pyfile('config.py')

    # Load the file specified on APP_CONFIG_FILE environment variable
    # Variables defined here will override those in default config
    app.config.from_envvar('APP_CONFIG_FILE')

    app.register_blueprint(user_routes.user_route, url_prefix="/user")
    return app
