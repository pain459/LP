from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Initializing the votes dictionary with Greek capital letters Alpha to Upsilon for 20 candidates
candidates = [chr(913 + i) for i in range(20)]  # 913 is the Unicode for capital Alpha
votes = {candidate: 0 for candidate in candidates}


@app.route('/results', methods=['GET'])
def results():
    # Returns the current vote counts in a JSON format
    return jsonify(votes)


@app.route('/download_results', methods=['GET'])
def download_results():
    # Assumes the database is stored at a specific path, update this as necessary
    db_path = 'path_to_your_database.db'  # Ensure this is the correct path to your database
    return send_file(db_path, attachment_filename='results.db', as_attachment=True)


if __name__ == '__main__':
    # SSL configuration: make sure 'cert.pem' and 'key.pem' are in the correct directory or adjust paths accordingly
    app.run(host='0.0.0.0', port=5002, ssl_context=('cert.pem', 'key.pem'))
