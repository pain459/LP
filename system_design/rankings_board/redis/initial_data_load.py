import psycopg2
import redis
import os

# Connect to PostgreSQL
pg_conn = psycopg2.connect(
    dbname="rankings_board",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
pg_cursor = pg_conn.cursor()

# Connect to Redis
redis_conn = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=os.getenv('REDIS_PORT', 6379),
    db=0
)

# Fetch data from PostgreSQL
pg_cursor.execute("SELECT unique_id, rating_points FROM rankings_board.player_ratings")
rows = pg_cursor.fetchall()

# Load data into Redis sorted set
for row in rows:
    unique_id, rating_points = row
    redis_conn.zadd('player_ratings', {unique_id: rating_points})

pg_cursor.close()
pg_conn.close()

print("Initial data loaded into Redis successfully")
