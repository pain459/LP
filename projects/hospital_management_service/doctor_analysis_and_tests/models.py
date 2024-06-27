from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DoctorAnalysisAndTests(db.Model):
    __tablename__ = 'doctor_analysis_and_tests'
    id = db.Column(db.Integer, primary_key=True)
    patient_unique_id = db.Column(db.String(64), nullable=False, index=True)
    analysis = db.Column(db.JSON, nullable=False)
    tests = db.Column(db.JSON, nullable=False)
    medicines = db.Column(db.JSON, nullable=False)

class Symptom(db.Model):
    __tablename__ = 'symptoms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Medicine(db.Model):
    __tablename__ = 'medicines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
