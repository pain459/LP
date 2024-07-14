import redis
import os

# Connect to Redis
redis_conn = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=os.getenv('REDIS_PORT', 6379),
    db=0
)

# Fetch and display top 20 sorted set data
sorted_set = redis_conn.zrevrange('player_ratings', 0, 19, withscores=True)
print("Top 20 Player Ratings:")
for player_id, rating_points in sorted_set:
    print(f"Player ID: {player_id.decode('utf-8')}, Rating Points: {rating_points}")

# List all keys
keys = redis_conn.keys('*')
print("\nAll keys in Redis:")
for key in keys:
    print(key.decode('utf-8'))
