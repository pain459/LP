from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, EqualTo, NumberRange
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
app.config['WTF_CSRF_SECRET_KEY'] = 'anothersecretkey'
csrf = CSRFProtect(app)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_transaction(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Initialize the database
def init_db():
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            password TEXT,
            balance REAL,
            address TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank (
            id INTEGER PRIMARY KEY,
            total_balance REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            receiver TEXT,
            amount REAL,
            timestamp TEXT,
            transaction_hash TEXT
        )
    ''')
    cursor.execute('INSERT OR IGNORE INTO bank (id, total_balance) VALUES (1, 1000)')
    conn.commit()
    conn.close()

# Initialize users
def init_users():
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    if count == 0:
        for i in range(1, 1001):
            user_id = f"user{i:04}"
            password = hash_password(f"user{i:04}password")
            address = hashlib.sha256(user_id.encode()).hexdigest()
            cursor.execute('INSERT INTO users (user_id, password, balance, address) VALUES (?, ?, ?, ?)',
                           (user_id, password, 0.0, address))
        conn.commit()
    conn.close()

class LoginForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

class TransactionForm(FlaskForm):
    receiver = StringField('Receiver ID', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.0001)], places=4)
    submit = SubmitField('Send')

class SearchForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    submit = SubmitField('Search')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        hashed_password = hash_password(password)

        if user_id == 'admin' and password == 'admin-0000-password':
            session['user_id'] = user_id
            session.permanent = True
            return redirect(url_for('admin'))
        
        conn = sqlite3.connect('kalki_coin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ? AND password = ?', (user_id, hashed_password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user_id
            session.permanent = True
            return redirect(url_for('user_profile', user_id=user_id))
        else:
            flash("Invalid credentials")
            return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' not in session or session['user_id'] != 'admin':
        return redirect(url_for('index'))

    search_form = SearchForm()
    transaction_form = TransactionForm()

    if search_form.validate_on_submit():
        user_id = search_form.user_id.data
        return redirect(url_for('user_profile', user_id=user_id))
    
    if transaction_form.validate_on_submit():
        sender = 'admin'
        receiver = transaction_form.receiver.data
        amount = float(transaction_form.amount.data)

        conn = sqlite3.connect('kalki_coin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT total_balance FROM bank WHERE id = 1')
        bank_balance = cursor.fetchone()[0]

        cursor.execute('SELECT balance, address FROM users WHERE user_id = ?', (receiver,))
        receiver_data = cursor.fetchone()
        if receiver_data:
            receiver_balance, receiver_address = receiver_data

            if bank_balance >= amount:
                new_bank_balance = bank_balance - amount
                new_receiver_balance = receiver_balance + amount

                cursor.execute('UPDATE bank SET total_balance = ? WHERE id = 1', (new_bank_balance,))
                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (new_receiver_balance, receiver))

                timestamp = datetime.now().isoformat()
                transaction_data = f"{sender}{receiver_address}{amount}{timestamp}"
                transaction_hash = hash_transaction(transaction_data)
                cursor.execute('INSERT INTO transactions (sender, receiver, amount, timestamp, transaction_hash) VALUES (?, ?, ?, ?, ?)',
                               ('bank', receiver_address, amount, timestamp, transaction_hash))
                conn.commit()
                flash("Transaction successful")
            else:
                flash("Insufficient bank balance")
        else:
            flash("Receiver not found")

        conn.close()
        return redirect(url_for('admin'))

    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT total_balance FROM bank WHERE id = 1')
    total_balance = cursor.fetchone()[0]
    cursor.execute('SELECT user_id, balance FROM users ORDER BY balance DESC LIMIT 10')
    top_users = cursor.fetchall()
    cursor.execute('SELECT sender, receiver, amount, timestamp, transaction_hash FROM transactions ORDER BY timestamp DESC LIMIT 10')
    transactions = cursor.fetchall()
    conn.close()
    return render_template('admin.html', total_balance=total_balance, top_users=top_users, transactions=transactions, search_form=search_form, transaction_form=transaction_form)

@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_profile(user_id):
    if 'user_id' not in session or (session['user_id'] != user_id and session['user_id'] != 'admin'):
        return redirect(url_for('index'))

    form = TransactionForm()
    if form.validate_on_submit():
        sender = session['user_id']
        receiver = form.receiver.data
        amount = float(form.amount.data)

        conn = sqlite3.connect('kalki_coin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT balance, address FROM users WHERE user_id = ?', (sender,))
        sender_data = cursor.fetchone()

        if sender_data:
            sender_balance, sender_address = sender_data
            if sender_balance >= amount:
                cursor.execute('SELECT balance, address FROM users WHERE user_id = ?', (receiver,))
                receiver_data = cursor.fetchone()
                if receiver_data:
                    receiver_balance, receiver_address = receiver_data
                    new_sender_balance = sender_balance - amount
                    new_receiver_balance = receiver_balance + amount

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (new_sender_balance, sender))
                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (new_receiver_balance, receiver))

                    timestamp = datetime.now().isoformat()
                    transaction_data = f"{sender_address}{receiver_address}{amount}{timestamp}"
                    transaction_hash = hash_transaction(transaction_data)
                    cursor.execute('INSERT INTO transactions (sender, receiver, amount, timestamp, transaction_hash) VALUES (?, ?, ?, ?, ?)',
                                   (sender_address, receiver_address, amount, timestamp, transaction_hash))
                    conn.commit()
                    flash("Transaction successful")
                else:
                    flash("Receiver not found")
            else:
                flash("Insufficient balance")
        else:
            flash("Sender not found")

        conn.close()
        return redirect(url_for('user_profile', user_id=user_id))

    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, balance, address FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user:
        cursor.execute('SELECT sender, receiver, amount, timestamp, transaction_hash FROM transactions WHERE sender = ? OR receiver = ? ORDER BY timestamp DESC', (user[2], user[2]))
        transactions = cursor.fetchall()
    else:
        transactions = []
    conn.close()

    if user:
        return render_template('user_profile.html', user=user, form=form, transactions=transactions)
    else:
        return "User not found"

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    
    form = ChangePasswordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password.data
        confirm_password = form.confirm_password.data

        user_id = session['user_id']
        hashed_old_password = hash_password(old_password)
        hashed_new_password = hash_password(new_password)
        
        conn = sqlite3.connect('kalki_coin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ? AND password = ?', (user_id, hashed_old_password))
        user = cursor.fetchone()
        
        if user or (user_id == 'admin' and old_password == 'admin-0000-password'):
            cursor.execute('UPDATE users SET password = ? WHERE user_id = ?', (hashed_new_password, user_id))
            conn.commit()
            flash("Password changed successfully")
        else:
            flash("Old password is incorrect")
        
        conn.close()
        return redirect(url_for('change_password'))

    return render_template('change_password.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    init_users()
    app.run(debug=True)
