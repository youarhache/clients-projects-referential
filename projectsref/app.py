from flask import Flask

from projectsref.rest import projectsref_api
from projectsref.flask_settings import DevConfig

def create_app(config_object = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(projectsref_api.blueprint)
    return app