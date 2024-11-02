import speech_recognition as sr
import requests

def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        # Send command to orchestration service in Docker
        response = requests.post("http://localhost:8000/process_command", json={"command": command})
        print("Response from orchestration:", response.json())
    except Exception as e:
        print("Error recognizing audio:", e)

if __name__ == "__main__":
    capture_audio()
