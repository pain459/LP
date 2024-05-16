from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send, emit
from flask_bcrypt import Bcrypt
import random
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tambola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
            socketio.emit('number_called', {'number': number}, broadcast=True)
            time.sleep(speed)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('game'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('game'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return 'User already exists!'
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return 'User created successfully!'
    return render_template('admin.html')

@app.route('/game')
def game():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/generate_ticket', methods=['POST'])
def generate_ticket():
    user_id = User.query.filter_by(username=session['username']).first().id
    ticket = generate_ticket_numbers()
    new_ticket = Ticket(numbers=ticket, user_id=user_id)
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'ticket': ticket})

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

def generate_ticket_numbers():
    ticket = []
    for _ in range(3):
        row = random.sample(range(1, 91), 5)
        ticket.append(row)
    return ticket

def create_admin_user():
    admin_username = "admin"
    admin_password = "admin123"
    existing_admin = User.query.filter_by(username=admin_username).first()
    if not existing_admin:
        hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        new_admin = User(username=admin_username, password=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print(f'Admin user created with username: {admin_username} and password: {admin_password}')
    else:
        print('Admin user already exists.')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin_user()
    socketio.run(app)
