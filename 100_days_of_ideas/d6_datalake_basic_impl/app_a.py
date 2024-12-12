from flask import Flask, jsonify
import random
import time
import os
import json

app = Flask(__name__)

# Configure the location of the datalake directory
DATALAKE_DIR = 'datalake'
if not os.path.exists(DATALAKE_DIR):
    os.makedirs(DATALAKE_DIR)

@app.route('/log_metric', methods=['GET'])
def log_metric():
    # Generate a random metric: "up" or "down"
    metric_status = random.choice(["up", "down"])
    timestamp = int(time.time())

    # Create a metric record
    metric_record = {
        "timestamp": timestamp,
        "status": metric_status
    }

    # Write to datalake: 
    #   For simplicity, one file per metric. In reality, you'd probably batch these.
    file_path = os.path.join(DATALAKE_DIR, f"metric_{timestamp}.json")
    with open(file_path, 'w') as f:
        json.dump(metric_record, f)

    return jsonify({"message": "Metric logged", "metric": metric_record})

if __name__ == '__main__':
    # Run the Flask app
    # After starting the app, you can hit http://localhost:5000/log_metric to generate metrics.
    app.run(host='0.0.0.0', port=5000)
