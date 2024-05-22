from flask import Flask, request, jsonify
import os
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, filename='/app/logs/c3.log', format='%(asctime)s - %(levelname)s - %(message)s')

output_directory = '/app/output/'
os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists

@app.route('/execute', methods=['POST'])
def execute_task():
    task_data = request.json
    priority = task_data['priority']
    data = task_data['data']
    file_path = os.path.join(output_directory, f"result_{priority}.json")

    # Simulate execution and write results
    try:
        result = f"Executed task with data: {data} and priority: {priority}"
        with open(file_path, 'w') as file:
            json.dump({"status": "Completed", "result": result}, file)
        logging.info(f"Task executed and result stored: {file_path}")
        return jsonify({"status": "Completed", "file": file_path})
    except Exception as e:
        logging.error(f"Failed to execute task or write result: {str(e)}")
        return jsonify({"status": "Error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
