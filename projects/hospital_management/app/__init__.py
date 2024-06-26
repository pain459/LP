import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    db.init_app(app)

    service_name = os.getenv('SERVICE_NAME')

    if service_name == 'patient_registration':
        from app.patient_registration.routes import bp as patient_registration_bp
        app.register_blueprint(patient_registration_bp, url_prefix='/patients')

    elif service_name == 'doc_analysis':
        from app.doc_analysis.routes import bp as doc_analysis_bp
        app.register_blueprint(doc_analysis_bp, url_prefix='/analysis')

    elif service_name == 'lab_reports':
        from app.lab_reports.routes import bp as lab_reports_bp
        app.register_blueprint(lab_reports_bp, url_prefix='/reports')

    elif service_name == 'final_bill_discharge':
        from app.final_bill_discharge.routes import bp as final_bill_discharge_bp
        app.register_blueprint(final_bill_discharge_bp, url_prefix='/bills')

    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.get_table_names():
            print("Database is empty, creating tables and running migrations.")
            db.create_all()
            # Run migrations
            os.system("flask db upgrade")
        else:
            print("Database already initialized, skipping table creation and migrations.")

    return app
