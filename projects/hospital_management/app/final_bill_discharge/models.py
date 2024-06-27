from app import db

class Patient(db.Model):
    __tablename__ = 'patient'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    registration_date = db.Column(db.Date, nullable=False)

class Bill(db.Model):
    __tablename__ = 'bill'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    discharge_date = db.Column(db.Date, nullable=False)
