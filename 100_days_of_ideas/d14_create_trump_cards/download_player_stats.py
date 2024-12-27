import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for player stats
# base_url = "https://stats.espncricinfo.com/ci/engine/stats/index.html"
base_url = "https://www.espncricinfo.com/cricketers/sachin-tendulkar-35320"

# Query parameters for batting statistics (can be modified for other stats)
params = {
    "class": "1",  # Test matches (1), ODI (2), T20I (3)
    "template": "results",
    "type": "batting",  # Batting stats
    "view": "innings"
}

# Send HTTP request
response = requests.get(base_url, params=params)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find table rows containing player stats
    rows = soup.select("table.engineTable > tbody > tr.data1")
    players = []

    for row in rows:
        cols = row.find_all("td")
        player_name = cols[0].text.strip()
        matches = cols[1].text.strip()
        runs = cols[5].text.strip()
        avg = cols[8].text.strip()
        players.append({"Player Name": player_name, "Matches": matches, "Runs": runs, "Average": avg})

    # Convert to DataFrame
    df = pd.DataFrame(players)

    # Save to CSV
    df.to_csv("espncricinfo_batting_stats.csv", index=False)
    print("Data saved to espncricinfo_batting_stats.csv")
else:
    print(f"Failed to fetch data: HTTP {response.status_code}")
