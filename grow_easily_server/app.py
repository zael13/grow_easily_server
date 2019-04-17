from flask import Flask

from grow_easily_server.rest import find_recipe, find_item
from grow_easily_server.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(find_recipe.blueprint)
    app.register_blueprint(find_item.blueprint)
    return app
