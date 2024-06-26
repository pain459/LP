from app import db

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(256), nullable=False)
    diagnosis = db.Column(db.String(256), nullable=False)
    tests_prescribed = db.Column(db.String(256), nullable=False)
    analysis_date = db.Column(db.Date, nullable=False)
