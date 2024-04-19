import requests

url = 'https://dummyjson.com/products/1'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print(json_data)
else:
    print(f"Failed to fetch JSON data. Status code: {response.status_code}")    
