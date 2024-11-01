from flask import Flask, request, jsonify

app = Flask(__name__)

def interpret_command(command):
    if "weather" in command:
        return {"action": "get_weather"}
    elif "time" in command:
        return {"action": "tell_time"}
    # Add more command interpretations here
    return {"action": "unknown"}

@app.route('/interpret', methods=['POST'])
def interpret():
    data = request.json
    command = data.get("command", "")
    action = interpret_command(command)
    return jsonify(action)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
