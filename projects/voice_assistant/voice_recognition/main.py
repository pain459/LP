import speech_recognition as sr
import requests

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        # Send command to NLP service
        response = requests.post("http://nlp_service:5000/interpret", json={"command": command})
        print("NLP Service Response:", response.json())
    except Exception as e:
        print("Could not recognize voice:", e)

if __name__ == "__main__":
    listen_command()
