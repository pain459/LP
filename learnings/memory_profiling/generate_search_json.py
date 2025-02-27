import json
import random
import ijson
from memory_profiler import profile, memory_usage

# ==========================
# STEP 1: GENERATE JSON FILE
# ==========================

# Function to generate random approvers
def generate_approvers():
    return {
        "dev": [f"dev_approver_{i}" for i in range(1, 4)],
        "qa": [f"qa_approver_{i}" for i in range(1, 4)],
        "uat": [f"uat_approver_{i}" for i in range(1, 4)],
        "prod": [f"prod_approver_{i}" for i in range(1, 4)]
    }

# Function to generate a nested software_users structure (6 levels deep)
def generate_software_users():
    return {
        "layer1": {
            "layer2": {
                "layer3": {
                    "layer4": {
                        "layer5": {
                            "layer6": {
                                f"software_user_{i}": f"user_{i}@company.com"
                                for i in range(1, 4)
                            }
                        }
                    }
                }
            }
        }
    }

# Function to generate a team entry
def generate_team(team_id):
    return {
        "approvers": generate_approvers(),
        "deployment_type": random.choice(["blue-green", "canary", "rolling"]),
        "lb_address": f"lb-{team_id}.company.com",
        "image_name": f"team_{team_id}/service:v{random.randint(1, 10)}.{random.randint(0, 9)}",
        "software_users": generate_software_users()
    }

@profile
def generate_json_file(json_filename="teams.json", num_teams=200):
    """
    Generates a JSON file with 200 teams, each containing nested structures up to 6 levels deep.
    """
    teams_data = {f"team_{i}": generate_team(i) for i in range(1, num_teams + 1)}

    with open(json_filename, "w") as json_file:
        json.dump(teams_data, json_file, indent=4)

    print(f"Generated JSON saved as {json_filename}")

# ==========================
# STEP 2: STREAMING SEARCH
# ==========================

@profile
def search_deep_key(json_file, target_key):
    """
    Searches for a key at exactly the 6th depth level in a JSON file using streaming.

    :param json_file: Path to the JSON file
    :param target_key: The key to search for
    :return: Found values (if any)
    """
    with open(json_file, 'rb') as f:
        parser = ijson.parse(f)
        key_stack = []
        value_found = None

        for prefix, event, value in parser:
            if event == 'map_key':
                key_stack.append(value)

                # If we reach 6 levels deep and the key matches
                if len(key_stack) == 6 and key_stack[-1] == target_key:
                    value_found = True  # Flag to capture the value

            elif value_found and event in ('string', 'number', 'boolean', 'null'):
                print(f"Found {target_key}: {value}")  # Print the found value
                value_found = False  # Reset flag

            elif event in ('end_map', 'end_array'):
                if key_stack:
                    key_stack.pop()

# ==========================
# STEP 3: MEMORY PROFILING
# ==========================

def measure_memory_usage(func, *args):
    """
    Measures peak memory usage of a function.
    """
    mem_usage = memory_usage((func, args))
    print(f"Peak Memory Usage for {func.__name__}: {max(mem_usage):.2f} MB")

# ==========================
# STEP 4: RUN SCRIPT
# ==========================

if __name__ == "__main__":
    json_filename = "teams.json"
    search_key = "software_user_2"  # Example key to search

    # Generate JSON and measure memory
    measure_memory_usage(generate_json_file, json_filename, 200)

    # Search for key in JSON and measure memory
    measure_memory_usage(search_deep_key, json_filename, search_key)
