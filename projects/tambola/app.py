import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt
import random
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tambola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app, async_mode='gevent')
bcrypt = Bcrypt(app)

# Ensure the log directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging to write to a file
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    numbers = db.Column(db.PickleType, nullable=False)
    marked_numbers = db.Column(MutableList.as_mutable(PickleType), nullable=False, default=[])
    ticket_number = db.Column(db.Integer, nullable=False)

used_numbers = set()

def reset_used_numbers():
    global used_numbers
    used_numbers = set()
    logger.info("Used numbers reset")

def generate_ticket_numbers():
    global used_numbers
    columns = {
        0: sorted(list(range(1, 10))),
        1: sorted(list(range(10, 20))),
        2: sorted(list(range(20, 30))),
        3: sorted(list(range(30, 40))),
        4: sorted(list(range(40, 50))),
        5: sorted(list(range(50, 60))),
        6: sorted(list(range(60, 70))),
        7: sorted(list(range(70, 80))),
        8: sorted(list(range(80, 91))),
    }

    ticket = [[None for _ in range(9)] for _ in range(3)]
    numbers_added = 0

    # Ensure each column is covered at least once
    for col in range(9):
        row = random.choice(ticket)
        num = random.choice(columns[col])
        while num in used_numbers:
            num = random.choice(columns[col])
        row[col] = num
        used_numbers.add(num)
        numbers_added += 1

    # Ensure each row has exactly 5 numbers
    for row in ticket:
        while row.count(None) > 4:
            col = random.choice(range(9))
            if row[col] is None:
                num = random.choice(columns[col])
                while num in used_numbers:
                    num = random.choice(columns[col])
                row[col] = num
                used_numbers.add(num)
                numbers_added += 1

    # Fill remaining slots to make exactly 15 numbers in total
    while numbers_added < 15:
        row = random.choice(ticket)
        col = random.choice(range(9))
        if row[col] is None:
            num = random.choice(columns[col])
            while num in used_numbers:
                num = random.choice(columns[col])
            row[col] = num
            used_numbers.add(num)
            numbers_added += 1

    # Sort each column to ensure ascending order within each column
    for col in range(9):
        col_nums = sorted([row[col] for row in ticket if row[col] is not None])
        idx = 0
        for row in ticket:
            if row[col] is not None:
                row[col] = col_nums[idx]
                idx += 1

    return ticket


@app.route('/')
def home():
    logger.info("Home page accessed")
    return render_template('home.html')

@app.route('/select_role', methods=['POST'])
def select_role():
    role = request.form['role']
    logger.info(f"Role selected: {role}")
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
            logger.info(f"Admin logged in: {username}")
            return redirect(url_for('admin'))
        else:
            logger.warning(f"Invalid admin login attempt: {username}")
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
            logger.info(f"Player logged in: {username}")
            return redirect(url_for('game'))
        else:
            logger.warning(f"Invalid player login attempt: {username}")
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
            logger.warning(f"Attempt to create existing user: {username}")
            return 'User already exists!'
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        logger.info(f"New user created: {username}")
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
        logger.info(f"User deleted: {user.username}")
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
        reset_used_numbers()
        logger.info("Game ended by admin")
        return redirect(url_for('admin_login'))
    else:
        logger.warning("Invalid end game password attempt")
        return 'Invalid password'

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    logger.info(f"Game page accessed by user: {user.username}")
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
    
    logger.info(f"Ticket generated for user ID: {user_id}, Ticket Number: {ticket_number}")
    return redirect(url_for('admin'))

@app.route('/mark_number', methods=['POST'])
def mark_number():
    if 'username' not in session:
        return redirect(url_for('home'))
    user = User.query.filter_by(username=session['username']).first()
    ticket_id = request.form['ticket_id']
    ticket = Ticket.query.filter_by(user_id=user.id, id=ticket_id).first()
    number = int(request.form['number'])
    logger.debug(f"Initial marked numbers: {ticket.marked_numbers}")
    if number in ticket.marked_numbers:
        ticket.marked_numbers.remove(number)
        action = "unmarked"
    else:
        ticket.marked_numbers.append(number)
        action = "marked"
    logger.debug(f"Marked numbers before commit: {ticket.marked_numbers}")
    db.session.commit()
    # Fetch the updated ticket again to confirm the changes were saved
    updated_ticket = Ticket.query.filter_by(id=ticket_id).first()
    logger.info(f"Number {number} {action} on ticket {ticket_id} by user {user.username}")
    logger.debug(f"Ticket {ticket_id} marked numbers after update: {updated_ticket.marked_numbers}")
    return jsonify({'success': True})

@app.route('/save_state', methods=['POST'])
def save_state():
    if 'username' not in session:
        return jsonify({'success': False, 'error': 'User not logged in'}), 401
    user = User.query.filter_by(username=session['username']).first()
    tickets = Ticket.query.filter_by(user_id=user.id).all()
    db.session.commit()
    logger.info(f"State saved for user: {user.username}")
    return jsonify({'success': True})

@app.route('/get_marked_numbers', methods=['POST'])
def get_marked_numbers():
    if 'username' not in session:
        return jsonify({'success': False, 'error': 'User not logged in'}), 401
    user = User.query.filter_by(username=session['username']).first()
    ticket_id = request.form['ticket_id']
    ticket = Ticket.query.filter_by(user_id=user.id, id=ticket_id).first()
    if not ticket:
        logger.error(f"Ticket not found for ticket_id {ticket_id} and user {user.username}")
        return jsonify({'success': False, 'error': 'Ticket not found'}), 404
    logger.info(f"Retrieved marked numbers for ticket {ticket_id} by user {user.username}: {ticket.marked_numbers}")
    logger.debug(f"Ticket {ticket_id} data: {ticket}")
    return jsonify({'success': True, 'marked_numbers': ticket.marked_numbers})

@app.route('/logout')
def logout():
    username = session.get('username', 'Unknown')
    session.clear()
    logger.info(f"User logged out: {username}")
    return redirect(url_for('home'))

def create_admin_user():
    admin_username = "admin"
    admin_password = "admin123"
    existing_admin = User.query.filter_by(username=admin_username).first()
    if not existing_admin:
        hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
        new_admin = User(username=admin_username, password=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        logger.info(f"Admin user created with username: {admin_username} and password: {admin_password}")
    else:
        logger.info('Admin user already exists.')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin_user()
    socketio.run(app, host='0.0.0.0', port=5000)
