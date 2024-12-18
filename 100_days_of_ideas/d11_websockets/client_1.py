from websocket import create_connection

# Connect to the server
ws = create_connection("ws://localhost:6789")
print("Connected to server")

# Run hello.py script
ws.send("RUN hello.py")
response = ws.recv()
print("Response from server:", response)

# Run compute.py with arguments 1,2,3
ws.send("RUN compute.py 1 2 3")
response = ws.recv()
print("Response from server:", response)

ws.close()
print("Closed the connection")
