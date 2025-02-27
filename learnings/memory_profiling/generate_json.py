import json
import random
import ijson

# Function to generate random approvers
def generate_approvers():
    return {
        "dev": [f"dev_approver_{i}" for i in range(1, 4)],
        "qa": [f"qa_approver_{i}" for i in range(1, 4)],
        "uat": [f"uat_approver_{i}" for i in range(1, 4)],
        "prod": [f"prod_approver_{i}" for i in range(1, 4)]
    }

# Function to generate nested software_users structure (6 levels deep)
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

# Generate JSON structure with 200 teams
num_teams = 200
teams_data = {f"team_{i}": generate_team(i) for i in range(1, num_teams + 1)}

# Save the JSON file
json_filename = "teams.json"
with open(json_filename, "w") as json_file:
    json.dump(teams_data, json_file, indent=4)

print(f"Generated JSON saved as {json_filename}")
