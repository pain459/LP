import requests
import argparse
import subprocess
import json

def get_location():
    response = requests.get('https://ipinfo.io/json')
    if response.status_code == 200:
        data = response.json()
        return data.get('loc', None)
    else:
        print("Error:", response.status_code)
        return None

def api_call(lat, lon, appid):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error:", response.status_code)
        return None

def main():
    parser = argparse.ArgumentParser(description='Make an API call to OpenWeatherMap and filter JSON output using jq.')
    parser.add_argument('--appid', type=str, help='API Key for OpenWeatherMap')
    args = parser.parse_args()

    # Get location based on IP address
    location = get_location()
    if location:
        lat, lon = location.split(',')
        # Print if you want lat and longitude captured.
        # print(f"Latitude: {lat}, Longitude: {lon}")

        # Make API call
        data = api_call(lat, lon, args.appid)

        if data:
            subprocess.run(['echo', data])
    else:
        print("Error getting location.")

if __name__ == "__main__":
    main()


# Sample
# python api_caller.py --appid <your key>
