from app import create_app, db
from sqlalchemy import inspect
from app.models import Patient, Analysis, LabReport, Bill

app = create_app()
app.app_context().push()

# Check and create tables if they don't exist
inspector = inspect(db.engine)

# List of all tables to check and create
tables = {
    "patient": Patient,
    "analysis": Analysis,
    "lab_report": LabReport,
    "bill": Bill
}

for table_name, model in tables.items():
    if not inspector.has_table(table_name):
        print(f"Table '{table_name}' not found, creating...")
        model.__table__.create(db.engine)
    else:
        print(f"Table '{table_name}' already exists, skipping creation.")

print("Database tables checked and created if needed.")
