from flask import Flask, request, jsonify

app = Flask(__name__)
response_text = ""

@app.route('/set_response', methods=['POST'])
def set_response():
    global response_text
    response_text = request.json.get("response", "")
    return jsonify({"status": "success"})

@app.route('/get_response', methods=['GET'])
def get_response():
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
