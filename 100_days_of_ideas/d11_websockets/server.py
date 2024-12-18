import asyncio
import websockets

async def echo_handler(websocket, path):
    print(f"Client connected from {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Echo the message back to the client
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    # Start a server on localhost, port 6789
    server = await websockets.serve(echo_handler, "localhost", 6789)
    print("WebSocket server is running on ws://localhost:6789")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
