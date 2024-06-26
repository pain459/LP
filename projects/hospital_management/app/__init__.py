from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.patient_registration.routes import bp as patient_registration_bp
    app.register_blueprint(patient_registration_bp, url_prefix='/patients')

    from app.doc_analysis.routes import bp as doc_analysis_bp
    app.register_blueprint(doc_analysis_bp, url_prefix='/analysis')

    from app.lab_reports.routes import bp as lab_reports_bp
    app.register_blueprint(lab_reports_bp, url_prefix='/reports')

    from app.final_bill_discharge.routes import bp as final_bill_discharge_bp
    app.register_blueprint(final_bill_discharge_bp, url_prefix='/bills')

    return app
