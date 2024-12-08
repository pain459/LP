import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

# Store recent searches as a list of dicts: [{city, temp, url}, ...]
recent_searches = []

@app.route('/', methods=['GET'])
def home():
    # Render the home page with recent searches
    return render_template('index.html', recent_searches=recent_searches)

@app.route('/', methods=['POST'])
def home_post():
    city = request.form.get('city')
    if city:
        return handle_search(city)
    return render_template('index.html', recent_searches=recent_searches, error="No city provided.")

@app.route('/search')
def search():
    # This route is used for direct link searches from recent searches
    city = request.args.get('city')
    if city:
        return handle_search(city)
    return render_template('index.html', recent_searches=recent_searches, error="No city provided.")

def handle_search(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: API key not found in environment variables."
    
    # Step 1: Use Geocoding API to get state, country, coordinates
    # e.g. http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API key}
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {
        'q': city,
        'limit': 1,
        'appid': api_key
    }

    geo_response = requests.get(geo_url, params=geo_params)
    if geo_response.status_code != 200 or not geo_response.json():
        error_message = "City not found or geocoding API error."
        return render_template('result.html', recent_searches=recent_searches, error=error_message)
    
    geo_data = geo_response.json()[0]
    city_name = geo_data.get('name', city)
    state = geo_data.get('state', '')  
    country = geo_data.get('country', '')
    lat = geo_data.get('lat')
    lon = geo_data.get('lon')

    if lat is None or lon is None:
        error_message = "Couldn't retrieve coordinates for the given city."
        return render_template('result.html', recent_searches=recent_searches, error=error_message)

    # Step 2: Use Weather API to get temperature, timezone, etc.
    # e.g. https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=metric
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }

    weather_response = requests.get(weather_url, params=weather_params)
    if weather_response.status_code != 200:
        error_message = "Weather API error."
        return render_template('result.html', recent_searches=recent_searches, error=error_message)
    
    weather_data = weather_response.json()
    temperature = weather_data["main"]["temp"]
    timezone_offset = weather_data.get("timezone", 0)

    # Convert timezone offset (in seconds) to a more readable format (e.g., UTC±X)
    # For simplicity, just convert offset in hours:
    offset_hours = timezone_offset / 3600
    if offset_hours >= 0:
        timezone_str = f"UTC+{offset_hours:.1f}"
    else:
        timezone_str = f"UTC{offset_hours:.1f}"

    # Create a direct search link for the same city
    # e.g. /search?city=CityName
    direct_search_url = f"/search?city={city_name}"

    # Add to recent searches
    # If the city already exists in recent searches, we can update it or let duplicates occur.
    # For simplicity, we’ll just add it again.
    recent_searches.append({
        'city': city_name,
        'temperature': temperature,
        'url': direct_search_url
    })
    # Limit recent searches to last 5
    if len(recent_searches) > 5:
        recent_searches.pop(0)

    # Render the result page with enriched information
    return render_template(
        'result.html',
        recent_searches=recent_searches,
        city=city_name,
        state=state,
        country=country,
        timezone=timezone_str,
        latitude=lat,
        longitude=lon,
        temperature=temperature
    )

if __name__ == '__main__':
    app.run(debug=True)
