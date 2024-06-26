#!/bin/sh

# Wait for the database to be available
echo "Waiting for the database to be available..."
python << END
import socket
import time

while True:
    try:
        s = socket.create_connection(("db", 5432))
        s.close()
        break
    except socket.error:
        time.sleep(1)
END

# Initialize the database
python app/db_init.py

# Start the Flask application
flask run --host=0.0.0.0 --port=${FLASK_RUN_PORT}
