from app.database.db import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200))
    menu = db.Column(db.String(200))
    telephone = db.Column(db.String(20))
    priceRange = db.Column(db.String(10))
    address = db.relationship('Address', backref='restaurant', uselist=False)