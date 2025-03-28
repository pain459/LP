from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def current_time():
    return f"<h1>Current Time: {datetime.now()}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
