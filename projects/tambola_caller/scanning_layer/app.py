from flask import Flask, request, jsonify
import os
import logging
from utils import extract_numbers_from_image

app = Flask(__name__)
data_storage_path = './scanning_layer/data/numbers.txt'

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Ensure the data storage directory exists
os.makedirs(os.path.dirname(data_storage_path), exist_ok=True)

# Load existing numbers if they exist
if os.path.exists(data_storage_path):
    with open(data_storage_path, 'r') as file:
        numbers = set(file.read().splitlines())
else:
    numbers = set()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join('./scanning_layer/data', file.filename)
    file.save(file_path)
    logging.debug(f"File saved to {file_path}")

    # Read numbers from the image
    new_numbers = extract_numbers_from_image(file_path)
    logging.debug(f"Extracted numbers: {new_numbers}")

    # Update the set of unique numbers
    numbers.update(new_numbers)

    # Save the updated numbers back to the file
    with open(data_storage_path, 'w') as file:
        file.write('\n'.join(numbers))

    return jsonify({"numbers": list(numbers)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
