from . import db

class DoctorAnalysisAndTests(db.Model):
    __tablename__ = 'doctor_analysis_and_tests'
    id = db.Column(db.Integer, primary_key=True)
    patient_unique_id = db.Column(db.String(64), nullable=False, index=True)
    analysis = db.Column(db.JSON, nullable=False)
    tests = db.Column(db.JSON, nullable=False)
    medicines = db.Column(db.JSON, nullable=False)

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class Medicine(db.Model):
    __tablename__ = 'medicines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class DoctorAnalysisAndTestsArchive(db.Model):
    __tablename__ = 'doctor_analysis_and_tests_archive'
    id = db.Column(db.Integer, primary_key=True)
    patient_unique_id = db.Column(db.String(64), nullable=False, index=True)
    analysis = db.Column(db.JSON, nullable=False)
    tests = db.Column(db.JSON, nullable=False)
    medicines = db.Column(db.JSON, nullable=False)
    paid_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
