from flask import Flask, request, jsonify
import os
import json
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, filename='/app/logs/c3.log', format='%(asctime)s - %(levelname)s - %(message)s')

output_directory = '/app/output/'
os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists

@app.route('/execute', methods=['POST'])
def execute_task():
    task_data = request.json
    priority = task_data['priority']
    data = task_data['data']
    # Create a timestamp for unique file naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(output_directory, f"result_{priority}_{timestamp}.json")

    # Process the task and store the result
    try:
        # Example of task processing logic; adjust as necessary
        processed_result = process_task(data)
        result_info = {
            "status": "Completed",
            "result": processed_result,
            "data_received": data,
            "priority": priority
        }
        with open(file_path, 'w') as file:
            json.dump(result_info, file)
        logging.info(f"Task executed and result stored: {file_path}")
        return jsonify({"status": "Completed", "file": file_path})
    except Exception as e:
        logging.error(f"Failed to execute task or write result: {str(e)}")
        return jsonify({"status": "Error", "error": str(e)}), 500

def process_task(data):
    """Simulate processing of the task based on the input data."""
    # This is a placeholder for your task processing logic
    # Return a dictionary with detailed results of processing
    return {"processed_data": f"Processed based on input: {data}"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
