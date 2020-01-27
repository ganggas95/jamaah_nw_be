import os
from flask import Flask
from celery import Celery
from flask_injector import FlaskInjector
from jamaah.extensions import db, ma, migrate, jwt, cors, celery_flask
from jamaah.settings import app_config
from jamaah.bind import configure


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv("ENV", "local")])
    FlaskInjector(app, modules=[configure])
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    celery_flask.init_app(app)


app = create_app()
register_extensions(app)
