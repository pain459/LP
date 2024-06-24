from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)

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
            address = hashlib.sha256(user_id.encode()).hexdigest()
            cursor.execute('INSERT INTO users (user_id, password, balance, address) VALUES (?, ?, ?, ?)',
                           (user_id, 'password', 0.0, address))
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return "Welcome to Kalki Coin Bank"

@app.route('/admin')
def admin():
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT total_balance FROM bank WHERE id = 1')
    total_balance = cursor.fetchone()[0]
    cursor.execute('SELECT * FROM users ORDER BY balance DESC LIMIT 10')
    top_users = cursor.fetchall()
    conn.close()
    return render_template('admin.html', total_balance=total_balance, top_users=top_users)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        user_id = request.form['user_id']
        conn = sqlite3.connect('kalki_coin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect(url_for('user_profile', user_id=user_id))
        else:
            return "User not found"
    return render_template('search.html')

@app.route('/user/<user_id>')
def user_profile(user_id):
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return "User not found"

if __name__ == '__main__':
    init_db()
    init_users()
    app.run(debug=True)
