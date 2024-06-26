from app import db

class LabReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    test_name = db.Column(db.String(256), nullable=False)
    test_result = db.Column(db.String(256), nullable=False)
    test_date = db.Column(db.Date, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
