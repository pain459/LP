from flask import Flask
from .models import db
from .views import doctor_analysis_and_tests_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hospital_admin:admin_password@db:5432/hospital_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(doctor_analysis_and_tests_blueprint)

    return app
