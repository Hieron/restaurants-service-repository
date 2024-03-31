from app.database.db import db
from flask import Flask
from app.routes.restaurant_routes import restaurant_routes

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(restaurant_routes, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app