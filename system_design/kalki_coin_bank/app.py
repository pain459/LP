from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            password TEXT,
            balance REAL
        )
    ''')
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
            user_id = f"{i:04}"
            cursor.execute('INSERT INTO users (user_id, password, balance) VALUES (?, ?, ?)',
                           (user_id, 'password', 0.0))
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return "Welcome to Kalki Coin Bank"

@app.route('/admin')
def admin():
    conn = sqlite3.connect('kalki_coin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(balance) FROM users')
    total_balance = cursor.fetchone()[0]
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('admin.html', total_balance=total_balance, users=users)

if __name__ == '__main__':
    init_db()
    init_users()
    app.run(debug=True)
