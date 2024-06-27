from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hospital_admin:admin_password@db:5432/hospital_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import patient_blueprint
    app.register_blueprint(patient_blueprint)

    return app
