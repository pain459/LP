import json
import random
import datetime

# Function to generate random users
def generate_users(role, count=3):
    return [f"{role}_user_{i}@company.com" for i in range(1, count + 1)]

# Function to generate a deep application structure
def generate_application(app_id):
    return {
        "metadata": {
            "name": f"Business App {app_id}",
            "version": f"v{random.randint(1, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}",
            "owner": f"user_{app_id}@company.com",
            "last_updated": str(datetime.datetime.now())
        },
        "infra": {
            "database": random.choice(["PostgreSQL", "MySQL", "MongoDB"]),
            "load_balancer": f"lb-{app_id}.company.com",
            "cloud_provider": random.choice(["AWS", "GCP", "Azure"])
        },
        "access_control": {
            "admin_users": generate_users("admin"),
            "developer_users": generate_users("dev"),
            "qa_users": generate_users("qa"),
            "read_only_users": generate_users("readonly", 5)
        },
        "security": {
            "encryption": random.choice(["AES-256", "RSA-4096", "TLS-1.3"]),
            "vulnerability_score": round(random.uniform(0, 10), 2),
            "last_audit": str(datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365)))
        },
        "business_metrics": {
            "monthly_cost": round(random.uniform(1000, 10000), 2),
            "uptime": round(random.uniform(95, 99.99), 2),
            "deployments_last_month": random.randint(1, 50)
        },
        "deep_nested_data": {
            "level1": {
                "level2": {
                    "level3": {
                        "level4": {
                            "level5": {
                                "level6": {
                                    "level7": {
                                        "level8": {
                                            "unique_search_key": f"deep_value_{app_id}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# Function to generate a team structure
def generate_team(team_id):
    return {
        "team_info": {
            "team_name": f"Team {team_id}",
            "department": random.choice(["Engineering", "Marketing", "HR", "Finance"]),
            "location": random.choice(["New York", "San Francisco", "London", "Berlin"]),
            "employees": random.randint(10, 100)
        },
        "applications": {
            f"app_{app}": generate_application(app) for app in range(1, random.randint(5, 10) + 1)
        },
        "infra": {
            "databases": random.choices(["PostgreSQL", "MySQL", "MongoDB", "Cassandra"], k=2),
            "load_balancers": random.choices(["AWS ALB", "NGINX", "HAProxy"], k=2),
            "monitoring_tools": random.choices(["Datadog", "Prometheus", "Grafana"], k=2)
        },
        "devops": {
            "ci_cd": random.choice(["Jenkins", "GitHub Actions", "GitLab CI"]),
            "kubernetes_cluster": random.choice(["k8s-prod", "k8s-staging"]),
            "config_management": random.choice(["Ansible", "Terraform", "SaltStack"])
        }
    }

# Generate JSON structure with 2000 teams
num_teams = 2000
teams_data = {f"team_{i}": generate_team(i) for i in range(1, num_teams + 1)}

# Save the JSON file
json_filename = "company_data.json"
with open(json_filename, "w") as json_file:
    json.dump(teams_data, json_file, indent=4)

print(f"Generated JSON saved as {json_filename}")
