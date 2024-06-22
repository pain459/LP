import redis

# Connect to the Redis master
client = redis.StrictRedis(
    host='localhost',  # Replace with the appropriate host if needed
    port=6379,         # Redis master port
    password='your_password',
    decode_responses=True
)

# Create
client.set('mykey', 'myvalue')
print("Set key to value")

# Read
value = client.get('mykey')
print(f"Got value: {value}")

# Update
client.set('mykey', 'newvalue')
print("Updated key to newvalue")

# Read updated value
new_value = client.get('mykey')
print(f"Got new value: {new_value}")

# Delete
client.delete('mykey')
print("Deleted key")

# Try reading deleted key
deleted_value = client.get('mykey')
print(f"Got deleted value: {deleted_value}")
