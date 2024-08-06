from flask import Flask, render_template
from flask_socketio import SocketIO, send
from pymemcache.client import base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
memcached_client = base.Client(('memcached', 11211))

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    # Save message in Memcached
    messages = memcached_client.get('chat_messages')
    if messages:
        messages = eval(messages)  # Convert byte string to list
    else:
        messages = []

    messages.append(msg)
    memcached_client.set('chat_messages', str(messages))

    send(msg, broadcast=True)

@socketio.on('get_messages')
def handle_get_messages():
    messages = memcached_client.get('chat_messages')
    if messages:
        messages = eval(messages)  # Convert byte string to list
        for message in messages:
            send(message)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
