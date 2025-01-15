from flaskApp import db


class SteelPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    region = db.Column(db.String(50))

