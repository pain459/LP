# run.py
from app import app, db

# Initialize the database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
