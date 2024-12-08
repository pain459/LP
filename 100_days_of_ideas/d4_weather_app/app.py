import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            return get_weather(city)
    return render_template('index.html')

def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: API key not found in environment variables."

    # Prepare the OpenWeatherMap API URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # get temperature in Celsius
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        # You could retrieve more data here, e.g., weather description, humidity, etc.
        return render_template('result.html', city=city, temperature=temperature)
    else:
        # Handle errors, e.g., city not found
        error_message = "City not found or API error."
        return render_template('result.html', city=city, temperature=None, error=error_message)

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
