import os
from app import create_app, db
from sqlalchemy import inspect

app = create_app()

# Define a function to import the correct models
def import_models(service_name):
    if service_name == 'patient_registration':
        from app.patient_registration.models import Patient
        return {'patient': Patient}
    elif service_name == 'doc_analysis':
        from app.doc_analysis.models import Patient, Analysis
        return {'patient': Patient, 'analysis': Analysis}
    elif service_name == 'lab_reports':
        from app.lab_reports.models import Patient, LabReport
        return {'patient': Patient, 'lab_report': LabReport}
    elif service_name == 'final_bill_discharge':
        from app.final_bill_discharge.models import Patient, Bill
        return {'patient': Patient, 'bill': Bill}
    else:
        raise ValueError(f"Unknown service name: {service_name}")

# Import the models based on the service name
service_name = os.getenv('SERVICE_NAME')
models = import_models(service_name)

def create_tables():
    with app.app_context():
        inspector = inspect(db.engine)
        
        for table_name, model in models.items():
            if not inspector.has_table(table_name):
                print(f"Table '{table_name}' not found, creating...")
                model.__table__.create(db.engine)
            else:
                print(f"Table '{table_name}' already exists, skipping creation.")
        print("Database tables checked and created if needed.")

create_tables()
