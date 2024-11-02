import pyttsx3
import requests

def play_audio():
    response = requests.get("http://localhost:8000/get_response")
    response_text = response.json().get("response", "")
    
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

if __name__ == "__main__":
    play_audio()
