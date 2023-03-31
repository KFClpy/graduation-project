from flask import Flask

from app_config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
    return app
