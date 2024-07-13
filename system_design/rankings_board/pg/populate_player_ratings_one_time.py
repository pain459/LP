import psycopg2
from concurrent.futures import ThreadPoolExecutor, as_completed

def calculate_rating_points(mp, g, a, f, i):
    # Define weights
    w1, w2, w3, w4, w5 = 1, 5, 3, 2, 3
    # Calculate rating points
    rating_points = w1 * mp + w2 * g + w3 * a - w4 * f - w5 * i
    return rating_points

def update_player_rating(player_id):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname='rankings_board',
            user='admin',
            password='admin',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        
        # Fetch player stats for the given player_id
        cursor.execute("SELECT matches, goals, assists, fouls, injuries FROM rankings_board.player_stats WHERE unique_id = %s", (player_id,))
        player = cursor.fetchone()
        
        if player:
            matches, goals, assists, fouls, injuries = player
            rating_points = calculate_rating_points(matches, goals, assists, fouls, injuries)
            cursor.execute(
                "INSERT INTO rankings_board.player_ratings (unique_id, rating_points) VALUES (%s, %s) "
                "ON CONFLICT (unique_id) DO UPDATE SET rating_points = EXCLUDED.rating_points",
                (player_id, rating_points)
            )
        
        # Commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        return f"Player {player_id} updated successfully"
    except Exception as e:
        return f"Error updating player {player_id}: {e}"

def update_all_players():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname='rankings_board',
            user='admin',
            password='admin',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        
        # Fetch all player IDs
        cursor.execute("SELECT unique_id FROM rankings_board.player_stats")
        player_ids = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()

        # Update ratings using multithreading
        results = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_to_player_id = {executor.submit(update_player_rating, player_id): player_id for player_id in player_ids}
            for future in as_completed(future_to_player_id):
                player_id = future_to_player_id[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    results.append(f"Player {player_id} generated an exception: {exc}")
        return results
    except Exception as e:
        return [f"Error fetching player IDs: {e}"]

if __name__ == "__main__":
    results = update_all_players()
    for result in results:
        print(result)
