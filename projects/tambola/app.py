from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt
import random

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    numbers = db.Column(db.PickleType, nullable=False)
    marked_numbers = db.Column(db.PickleType, nullable=False, default=[])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/select_role', methods=['POST'])
def select_role():
    role = request.form['role']
    if role == 'admin':
        return redirect(url_for('admin_login'))
    else:
        return redirect(url_for('login'))

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = username
            session['role'] = 'admin'
            return redirect(url_for('admin'))
        else:
            return 'Invalid credentials'
    return render_template('admin_login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = username
            session['role'] = 'player'
            return redirect(url_for('game'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('home'))
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
    users = User.query.all()
    tickets = Ticket.query.all()
    return render_template('admin.html', users=users, tickets=tickets)

@app.route('/admin/delete_user', methods=['POST'])
def delete_user():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('home'))
    user_id = request.form['user_id']
    user = User.query.get(user_id)
    if user:
        Ticket.query.filter_by(user_id=user_id).delete()
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('admin'))

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    ticket = Ticket.query.filter_by(user_id=user.id).first()
    return render_template('game.html', ticket=ticket)

@app.route('/generate_ticket', methods=['POST'])
def generate_ticket():
    if 'username' not in session:
        return redirect(url_for('home'))
    user_id = request.form['user_id']
    ticket = generate_ticket_numbers()
    new_ticket = Ticket(numbers=ticket, user_id=user_id)
    db.session.add(new_ticket)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/mark_number', methods=['POST'])
def mark_number():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    ticket = Ticket.query.filter_by(user_id=user.id).first()
    number = int(request.form['number'])
    if number not in ticket.marked_numbers:
        ticket.marked_numbers.append(number)
        db.session.commit()
    return redirect(url_for('game'))

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
