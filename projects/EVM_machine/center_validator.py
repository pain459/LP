import pandas as pd
import os
import time
from flask import Flask, request, jsonify
import logging
from threading import Thread

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load voting center IDs from file
voting_centers_file = 'voting_centers.csv'
if os.path.exists(voting_centers_file):
    voting_centers_df = pd.read_csv(voting_centers_file)
else:
    print("Voting centers file not found.")
    exit()

# Create a set of valid center IDs for quick lookup
valid_center_ids = set(voting_centers_df['CenterID'].values)

# Dictionary to track authenticated sessions and their last seen times
authenticated_sessions = {}

# Dictionary to track active center IDs
active_center_ids = set()

# Route to validate center ID
@app.route('/validate_center_id', methods=['GET'])
def validate_center_id():
    center_id = request.args.get('center_id')
    app.logger.debug(f'Received center_id: {center_id}')
    if center_id not in valid_center_ids:
        app.logger.debug(f'Invalid center_id: {center_id}')
        return jsonify({"status": "error", "message": "Invalid center ID."}), 400
    if center_id in active_center_ids:
        app.logger.debug(f'Center_id already in use: {center_id}')
        return jsonify({"status": "error", "message": "Center ID already in use."}), 400
    active_center_ids.add(center_id)
    authenticated_sessions[center_id] = time.time()
    return jsonify({"status": "success"}), 200

# Route to handle heartbeat updates
@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    center_id = data.get('center_id')
    app.logger.debug(f'Heartbeat received for center_id: {center_id}')
    if center_id in authenticated_sessions:
        authenticated_sessions[center_id] = time.time()
        return jsonify({"status": "success"}), 200
    app.logger.debug(f'Invalid center_id for heartbeat: {center_id}')
    return jsonify({"status": "error", "message": "Invalid center ID."}), 400

# Route to get authenticated sessions and last seen times
@app.route('/authenticated_sessions', methods=['GET'])
def get_authenticated_sessions():
    sessions = [
        {"center_id": center_id, "last_seen": time.ctime(last_seen)}
        for center_id, last_seen in authenticated_sessions.items()
    ]
    return jsonify({"status": "success", "sessions": sessions}), 200

# Function to remove inactive sessions
def remove_inactive_sessions():
    while True:
        current_time = time.time()
        inactive_sessions = [
            center_id for center_id, last_seen in authenticated_sessions.items()
            if current_time - last_seen > 60
        ]
        for center_id in inactive_sessions:
            app.logger.debug(f'Removing inactive center_id: {center_id}')
            del authenticated_sessions[center_id]
            active_center_ids.remove(center_id)
        time.sleep(30)  # Check every 30 seconds

if __name__ == '__main__':
    # Start the thread to remove inactive sessions
    cleanup_thread = Thread(target=remove_inactive_sessions)
    cleanup_thread.daemon = True
    cleanup_thread.start()

    app.run(host='0.0.0.0', port=5000)
