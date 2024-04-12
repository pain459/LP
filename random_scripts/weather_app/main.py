import requests
import argparse
import json

def api_call(lat, lon, appid):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def main():
    parser = argparse.ArgumentParser(description='Make an API call to OpenWeatherMap and download JSON.')
    parser.add_argument('--latitude', type=str, help='Latitude of the location')
    parser.add_argument('--longitude', type=str, help='Longitude of the location')
    parser.add_argument('--appid', type=str, help='API Key for OpenWeatherMap')
    
    args = parser.parse_args()

    # Make API call
    data = api_call(args.latitude, args.longitude, args.appid)

    # Print or do something with the downloaded data
    if data:
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()


# Sample call python api_caller.py --latitude 17.3934959 --longitude 78.3661469 --appid <your_api_key>
# filtering with jq
# python main.py --latitude 17.3934959 --longitude 78.3661469 --appid <your_api_key> | jq '.main.temp, .weather[0].description'
# 307.2
# "scattered clouds"