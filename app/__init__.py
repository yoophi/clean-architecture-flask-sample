from flask import Flask

from app.api import api


def init_bp(app: Flask):
    app.register_blueprint(api, url_prefix='/api/v1')


def create_app():
    app = Flask(__name__)
    init_bp(app)
    return app
