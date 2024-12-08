import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

# Store recent searches as a list of dicts: [{city, temperature, url}, ...]
recent_searches = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', recent_searches=recent_searches)

@app.route('/', methods=['POST'])
def home_post():
    city = request.form.get('city', '').strip()
    lat = request.form.get('lat', '').strip()
    lon = request.form.get('lon', '').strip()

    if city:
        # Search by city name
        return handle_search_by_city(city)
    elif lat and lon:
        # Search by coordinates
        return handle_search_by_coords(lat, lon)
    else:
        # No valid input provided
        error = "Please enter a city OR latitude and longitude."
        return render_template('index.html', recent_searches=recent_searches, error=error)

@app.route('/search')
def search():
    city = request.args.get('city', '').strip()
    # This direct search route currently only supports city re-searches
    # If you want to support lat/lon from recent searches, you'd need to store them and handle here as well.
    if city:
        return handle_search_by_city(city)
    error = "No city provided."
    return render_template('index.html', recent_searches=recent_searches, error=error)

def handle_search_by_city(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: API key not found in environment variables."
    
    # Geocode the city to get coords
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

    return fetch_weather_and_render(api_key, lat, lon, city_name, state, country)


def handle_search_by_coords(lat, lon):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: API key not found in environment variables."

    # Validate lat/lon
    try:
        lat_f = float(lat)
        lon_f = float(lon)
    except ValueError:
        error_message = "Invalid latitude or longitude."
        return render_template('result.html', recent_searches=recent_searches, error=error_message)

    # Reverse geocode to get city/state/country from coords
    rev_geo_url = "http://api.openweathermap.org/geo/1.0/reverse"
    rev_geo_params = {
        'lat': lat_f,
        'lon': lon_f,
        'limit': 1,
        'appid': api_key
    }

    rev_geo_response = requests.get(rev_geo_url, params=rev_geo_params)
    if rev_geo_response.status_code != 200:
        # If reverse geocoding fails, we can still proceed with just coords
        city_name = f"({lat}, {lon})"
        state = ""
        country = ""
    else:
        rev_geo_data = rev_geo_response.json()
        if rev_geo_data:
            city_name = rev_geo_data[0].get('name', f"({lat}, {lon})")
            state = rev_geo_data[0].get('state', '')
            country = rev_geo_data[0].get('country', '')
        else:
            # No reverse geocode data found
            city_name = f"({lat}, {lon})"
            state = ""
            country = ""

    return fetch_weather_and_render(api_key, lat_f, lon_f, city_name, state, country)


def fetch_weather_and_render(api_key, lat, lon, city_name, state, country):
    # Fetch weather for given coords
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

    # Convert timezone offset (in seconds) to a readable string
    offset_hours = timezone_offset / 3600
    if offset_hours >= 0:
        timezone_str = f"UTC+{offset_hours:.1f}"
    else:
        timezone_str = f"UTC{offset_hours:.1f}"

    # Create a direct search URL for city re-search
    # If city_name comes from coords and is something like (lat, lon), that might not geocode back.
    # But we will provide the link anyway.
    direct_search_url = f"/search?city={city_name}"

    # Add to recent searches
    recent_searches.append({
        'city': city_name,
        'temperature': temperature,
        'url': direct_search_url
    })
    if len(recent_searches) > 5:
        recent_searches.pop(0)

    # Render result
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
