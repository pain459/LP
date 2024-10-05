# run.py
from app import app, db  # Ensure this points to the 'app' directory and not a module conflict

# Initialize the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
