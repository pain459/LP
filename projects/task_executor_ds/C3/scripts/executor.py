from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/app/logs/component3.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/execute_task', methods=['POST'])
def execute_task():
    task_data = request.json['data']
    logging.info(f"Received task for execution: {task_data}")
    # Here, implement the actual task execution logic
    logging.info(f"Executing task: {task_data}")
    # Assume task execution is successful
    logging.info(f"Task executed successfully: {task_data}")
    return jsonify({'status': 'Task executed successfully'})

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True, port=5002)
