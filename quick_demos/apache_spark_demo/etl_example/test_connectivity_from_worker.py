import socket

# Define the Spark master's hostname and port
host = 'spark-master'
port = 7077

# Try to establish a connection
try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout for the connection attempt (optional)
    s.settimeout(5)
    # Attempt to connect to the Spark master
    s.connect((host, port))
    # If the connection is successful, print a success message
    print(f"Connection to {host}:{port} successful!")
    # Close the socket
    s.close()
except Exception as e:
    # If an error occurs, print the error message
    print(f"Error: {e}")
