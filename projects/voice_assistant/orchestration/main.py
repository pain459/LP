import requests

def orchestrate():
    # Example command
    response = requests.post("http://voice_recognition:5000/listen")
    command_text = response.json().get("command")

    # Send to NLP service for interpretation
    interpretation = requests.post("http://nlp_service:5000/interpret", json={"command": command_text}).json()

    # Execute based on action
    action = interpretation.get("action")
    if action == "get_weather":
        weather_info = requests.get("http://task_automation:5000/get_weather").json()
        response_text = f"The weather is {weather_info['description']}."
    elif action == "tell_time":
        time_info = requests.get("http://task_automation:5000/tell_time").json()
        response_text = f"The current time is {time_info}."
    else:
        response_text = "I'm not sure what you want."

    # Send response to text-to-speech
    requests.post("http://text_to_speech:5000/speak", json={"response": response_text})

if __name__ == "__main__":
    orchestrate()
