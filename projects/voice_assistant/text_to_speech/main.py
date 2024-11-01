import pyttsx3

def speak_response(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    response = "Hello! I am your assistant."
    speak_response(response)
