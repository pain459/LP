# app/models.py
from app import db

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_location = db.Column(db.String(50), nullable=False)
    to_location = db.Column(db.String(50), nullable=False)
    flight_number = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Flight {self.flight_number}>'
