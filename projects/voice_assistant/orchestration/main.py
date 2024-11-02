from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get("command", "")

    # Send to NLP service for interpretation
    interpretation = requests.post("http://nlp_service:5000/interpret", json={"command": command}).json()
    action = interpretation.get("action")

    if action == "get_weather":
        weather_info = requests.get("http://task_automation:5001/get_weather").json()
        response_text = f"The weather is {weather_info['description']}."
    elif action == "tell_time":
        time_info = requests.get("http://task_automation:5001/tell_time").json()
        response_text = f"The current time is {time_info['time']}."
    else:
        response_text = "I'm not sure what you want."

    # Send response to text-to-speech
    requests.post("http://text_to_speech:5002/set_response", json={"response": response_text})
    return jsonify({"status": "processed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
