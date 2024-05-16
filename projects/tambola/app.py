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
socketio = SocketIO(app, async_mode='gevent')
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
    ticket_number = db.Column(db.Integer, nullable=False)

used_numbers = set()

def reset_used_numbers():
    global used_numbers
    used_numbers = set()

def generate_ticket_numbers():
    global used_numbers
    columns = {
        0: list(range(1, 10)),
        1: list(range(10, 20)),
        2: list(range(20, 30)),
        3: list(range(30, 40)),
        4: list(range(40, 50)),
        5: list(range(50, 60)),
        6: list(range(60, 70)),
        7: list(range(70, 80)),
        8: list(range(80, 91)),
    }

    ticket = [[None for _ in range(9)] for _ in range(3)]
    num_count = 0

    # Ensure each column has at least one number
    for i in range(9):
        num = random.choice(columns[i])
        while num in used_numbers:
            num = random.choice(columns[i])
        row = random.choice([0, 1, 2])
        ticket[row][i] = num
        used_numbers.add(num)
        num_count += 1

    # Fill remaining 15 - 9 = 6 numbers
    remaining_slots = [(i, j) for i in range(3) for j in range(9) if ticket[i][j] is None]
    while num_count < 15:
        row, col = random.choice(remaining_slots)
        num = random.choice(columns[col])
        while num in used_numbers:
            num = random.choice(columns[col])
        ticket[row][col] = num
        used_numbers.add(num)
        remaining_slots.remove((row, col))
        num_count += 1

    # Ensure each row has at least 5 numbers
    for row in ticket:
        while row.count(None) > 4:
            col = random.choice([i for i in range(9) if row[i] is None])
            num = random.choice(columns[col])
            while num in used_numbers:
                num = random.choice(columns[col])
            row[col] = num
            used_numbers.add(num)

    return ticket

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

@app.route('/admin/end_game', methods=['POST'])
def end_game():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('home'))
    password = request.form['password']
    if password == 'admin_end_game':  # predefined end game password
        Ticket.query.delete()
        db.session.commit()
        session.clear()
        return redirect(url_for('admin_login'))
    else:
        return 'Invalid password'

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    return render_template('game.html', tickets=tickets, username=session['username'])

@app.route('/generate_ticket', methods=['POST'])
def generate_ticket():
    if 'username' not in session:
        return redirect(url_for('home'))
    user_id = request.form['user_id']
    ticket = generate_ticket_numbers()
    ticket_number = Ticket.query.count() + 1
    new_ticket = Ticket(numbers=ticket, user_id=user_id, ticket_number=ticket_number)
    db.session.add(new_ticket)
    db.session.commit()
    
    # Reset used numbers after every 6 tickets
    if ticket_number % 6 == 0:
        reset_used_numbers()
    
    return redirect(url_for('admin'))

@app.route('/mark_number', methods=['POST'])
def mark_number():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    ticket_id = request.form['ticket_id']
    ticket = Ticket.query.filter_by(user_id=user.id, id=ticket_id).first()
    number = int(request.form['number'])
    if number in ticket.marked_numbers:
        ticket.marked_numbers.remove(number)
    else:
        ticket.marked_numbers.append(number)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/save_state', methods=['POST'])
def save_state():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    db.session.commit()
    return jsonify({'success': True})

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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin_user()
    socketio.run(app, host='0.0.0.0', port=5000)
