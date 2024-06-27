from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=True)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    unique_id = db.Column(db.String(64), unique=True, nullable=False)

    @staticmethod
    def generate_unique_id(name):
        return f"{int(time.time())}_{name.replace(' ', '_')}"
