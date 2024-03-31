from app.database.db import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    postalCode = db.Column(db.String(20))
    streetAddress = db.Column(db.String(200))
    addressLocality = db.Column(db.String(100))
    addressRegion = db.Column(db.String(100))
    addressCountry = db.Column(db.String(100))