from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(128), nullable=False)
    diagnosis = db.Column(db.String(128), nullable=False)
    tests_prescribed = db.Column(db.String(128), nullable=False)
    analysis_date = db.Column(db.DateTime, nullable=False)

class LabReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    test_name = db.Column(db.String(64), nullable=False)
    test_result = db.Column(db.String(128), nullable=False)
    test_date = db.Column(db.DateTime, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), nullable=False)
    discharge_date = db.Column(db.DateTime, nullable=False)
