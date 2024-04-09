from app.database.db import db
from flask import Flask
from flask_cors import CORS
from app.routes.restaurant_routes import restaurant_routes

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins='*')
    db.init_app(app)
    app.register_blueprint(restaurant_routes, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app