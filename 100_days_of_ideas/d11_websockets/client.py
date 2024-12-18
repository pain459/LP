from websocket import create_connection

ws = create_connection("ws://localhost:6789")
print("Connected to server")

ws.send("Hello, server!")
print("Sent: Hello, server!")

result = ws.recv()
print("Received:", result)

ws.close()
