import json
import ijson
import requests
import memory_profiler
from memory_profiler import profile

# STEP 1: Fetch JSON Data from API
@profile
def fetch_json(api_url, json_filename):
    response = requests.get(api_url)
    data = response.json()

    # Create a deeply nested JSON structure
    nested_data = {"level1": {"level2": {"level3": {"level4": {"level5": {"level6": {}}}}}}}

    # Add 2000 keys at 6th level deep
    for i in range(2000):
        nested_data["level1"]["level2"]["level3"]["level4"]["level5"]["level6"][f"key_{i}"] = f"value_{i}"

    # Merge API data at the 1st level for realism
    nested_data["api_data"] = data

    # Save JSON to a file
    with open(json_filename, "w") as json_file:
        json.dump(nested_data, json_file, indent=4)

    print(f"Sample JSON saved as {json_filename}")

# STEP 2: Use ijson to Stream and Search for a Key
@profile
def extract_deep_values(json_file, target_key):
    with open(json_file, 'rb') as f:
        parser = ijson.parse(f)
        key_stack = []
        value_found = None
        
        for prefix, event, value in parser:
            if event == 'map_key':
                key_stack.append(value)
                if len(key_stack) == 6 and key_stack[-1] == target_key:
                    value_found = True
            elif value_found and event in ('string', 'number', 'boolean', 'null'):
                print(f"Found {target_key}: {value}")  # Print the found value
                value_found = False
            elif event in ('end_map', 'end_array'):
                if key_stack:
                    key_stack.pop()

# Measure Memory Usage
if __name__ == "__main__":
    json_filename = "sample.json"
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    fetch_json(api_url, json_filename)
    
    target_key = "key_100"
    extract_deep_values(json_filename, target_key)
