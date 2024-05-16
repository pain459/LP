from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt
import random
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tambola.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numbers = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

called_numbers = []
game_running = False

def call_number(speed):
    global game_running
    while game_running:
        number = random.randint(1, 90)
        if number not in called_numbers:
            called_numbers.append(number)
            socketio.emit('number_called', {'number': number})
            time.sleep(speed)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@app.route('/generate_ticket', methods=['POST'])
def generate_ticket():
    user_id = request.json['user_id']
    ticket = generate_ticket_numbers()
    new_ticket = Ticket(numbers=ticket, user_id=user_id)
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'ticket': ticket})

def generate_ticket_numbers():
    ticket = []
    for _ in range(3):
        row = random.sample(range(1, 91), 5)
        ticket.append(row)
    return ticket

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_running
    speed = request.json['speed']
    game_running = True
    threading.Thread(target=call_number, args=(speed,)).start()
    return jsonify({'message': 'Game started!'})

@app.route('/stop_game', methods=['POST'])
def stop_game():
    global game_running
    game_running = False
    return jsonify({'message': 'Game stopped!'})

if __name__ == '__main__':
    db.create_all()
    socketio.run(app)
