from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SteelPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(20))
    region = db.Column(db.String(50))
    date = db.Column(db.Date)
