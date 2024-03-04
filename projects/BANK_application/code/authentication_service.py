import sqlite3
import hashlib
import secrets


class AuthenticationService:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password_hash TEXT
            )
        """)
        self.connection.commit()

    def register_user(self, username, password):
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        # Check if username already exists
        self.cursor.execute("""
            SELECT * FROM users WHERE username = ?
        """, (username,))
        existing_user = self.cursor.fetchone()
        if existing_user:
            return "Username already exists. Please choose a different username."
        # Insert new user into the database
        self.cursor.execute("""
            INSERT INTO users (username, password_hash) VALUES (?, ?)
        """, (username, password_hash))
        self.connection.commit()
        return "User registered successfully."

    def login_user(self, username, password):
        # Hash the provided password for comparison
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        # Fetch user from database
        self.cursor.execute("""
            SELECT * FROM users WHERE username = ? AND password_hash = ?
        """, (username, password_hash))
        user = self.cursor.fetchone()
        if user:
            # Generate a session token
            session_token = secrets.token_hex(16)
            return session_token
        else:
            return None
