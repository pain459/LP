from flask import Flask, request, jsonify
import logging
from utils import extract_numbers_from_image

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# In-memory storage for numbers
numbers = set()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = f"/tmp/{file.filename}"
    file.save(file_path)
    logging.debug(f"File saved to {file_path}")

    # Read numbers from the image
    new_numbers = extract_numbers_from_image(file_path)
    logging.debug(f"Extracted numbers: {new_numbers}")

    # Update the set of unique numbers
    numbers.update(new_numbers)
    logging.debug(f"Current numbers in memory: {numbers}")

    return jsonify({"numbers": list(numbers)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
