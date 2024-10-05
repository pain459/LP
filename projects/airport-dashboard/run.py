# run.py
from app import app, db
from app.models import Flight

# Initialize the database if it doesn't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
