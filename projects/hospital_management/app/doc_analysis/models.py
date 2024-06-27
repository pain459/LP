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

class Analysis(db.Model):
    __tablename__ = 'analysis'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(256), nullable=False)
    diagnosis = db.Column(db.String(256), nullable=False)
    tests_prescribed = db.Column(db.String(256), nullable=False)
    analysis_date = db.Column(db.Date, nullable=False)
