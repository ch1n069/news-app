from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_map

bootstrap = Bootstrap()###activate the boostrap extensions


def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config_map[config_name])
    config_map[config_name].init_app(app)

    bootstrap.init_app(app)



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app


