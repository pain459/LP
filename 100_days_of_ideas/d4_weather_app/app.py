import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

# A global list to store recent searches
recent_searches = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            return get_weather(city)

    # Render the home page with recent searches
    return render_template('index.html', recent_searches=recent_searches)


def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: API key not found in environment variables."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]

        # Add to recent searches. If list exceeds 5, remove the oldest
        recent_searches.append(city)
        if len(recent_searches) > 5:
            recent_searches.pop(0)

        return render_template('result.html', city=city, temperature=temperature, recent_searches=recent_searches)
    else:
        error_message = "City not found or API error."
        return render_template('result.html', city=city, temperature=None, error=error_message, recent_searches=recent_searches)


if __name__ == '__main__':
    app.run(debug=True)
