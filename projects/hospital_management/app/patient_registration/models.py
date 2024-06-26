from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    registration_date = db.Column(db.Date, nullable=False)
