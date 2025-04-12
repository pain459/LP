import sqlite3
import argparse
from datetime import datetime

DB_PATH = "/app/data/chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_input TEXT,
            llm_response TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Initialized DB.")

def save_chat(user_input, llm_response):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO chat (timestamp, user_input, llm_response) VALUES (?, ?, ?)",
              (datetime.now().isoformat(), user_input, llm_response))
    conn.commit()
    conn.close()

def get_chats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM chat ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--init", action="store_true")
    args = parser.parse_args()

    if args.init:
        init_db()
