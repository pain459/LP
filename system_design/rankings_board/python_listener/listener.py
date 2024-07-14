import psycopg2
import select
import time
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

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
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT')
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
        print(f"Player {player_id} updated successfully")
        logger.info(f"Player {player_id} updated successfully")
    except Exception as e:
        print(f"Error updating player {player_id}: {e}")

def listen_for_notifications():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT')
            )
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Listen for notifications
        cursor.execute("LISTEN player_update;")
        # print("Waiting for notifications on channel 'player_update'...")
        logger.info("Waiting for notifications on channel 'player_update'...")
        
        while True:
            if select.select([conn], [], [], 5) == ([], [], []):
                continue
            conn.poll()
            while conn.notifies:
                notify = conn.notifies.pop(0)
                logger.info(f"Notification received: {notify.payload}")
                player_id = str(notify.payload)
                update_player_rating(player_id)
    except Exception as e:
        # print(f"Error listening for notifications: {e}")
        logger.error(f"Error listening for notifications: {e}")

if __name__ == "__main__":
    listen_for_notifications()
