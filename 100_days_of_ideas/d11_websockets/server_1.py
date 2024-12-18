import asyncio
import websockets
import os
import subprocess
import shlex
import sys

# SCRIPTS_DIR = "./scripts"100_days_of_ideas\d11_websockets\scripts
# SCRIPTS_DIR = "D:\\src_git\\LP\\LP\\100_days_of_ideas\\d11_websockets\\scripts\\"
SCRIPTS_DIR = "\\scripts\\"
async def run_local_script(script_name):
    """
    Runs a local script from SCRIPTS_DIR with the given args.
    Returns (success, output) where:
      success = True if script ran successfully, False otherwise
      output = stdout or error message
    """
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.isfile(script_path):
        return False, f"Error: Script '{script_name}' does not exist."

    cmd = [sys.executable, script_path]
    print(f"Running command: {cmd}")

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            print(f"Script '{script_name}' executed successfully. Output: {output}")
            return True, output
        else:
            error_msg = f"Script '{script_name}' failed with error:\n{result.stderr.strip()}"
            print(error_msg)
            return False, error_msg
    except Exception as e:
        error_msg = f"Error running script '{script_name}': {e}"
        print(error_msg)
        return False, error_msg

async def message_handler(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")

            parts = shlex.split(message)
            if len(parts) == 0:
                await websocket.send("Invalid command.")
                continue

            command = parts[0].upper()
            if command == "RUN" and len(parts) >= 2:
                script_name = parts[1]
                args = parts[2:]

                success, output = await run_local_script(script_name, args)
                if success:
                    # Even if output is empty, we will send 'Success:\n' to confirm something was sent.
                    await websocket.send(f"Success:\n{output}")
                else:
                    await websocket.send(output)
            else:
                await websocket.send("Unknown command. Use 'RUN <script_name> [args]'")

    except websockets.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Unexpected error in message_handler: {e}")

async def main():
    server = await websockets.serve(message_handler, "localhost", 6789)
    print("Server running on ws://localhost:6789")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
