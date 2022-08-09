from flask import Flask
from app.config import Config
from app.extensions import db, ma, migrate, jwt

from app.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_bp, url_prefix='/')

    return app