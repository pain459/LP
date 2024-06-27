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
    def generate_unique_id(name, contact):
        clean_contact = Patient.clean_contact(contact)
        return f"{int(time.time())}_{name.lower().replace(' ', '_')}_{clean_contact}"
    
    @staticmethod
    def clean_contact(contact):
        return contact.replace(" ", "").replace("-", "")
