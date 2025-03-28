from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import jsonify

app = Flask(__name__)
# Update the MySQL connection URL to match the service name specified in docker-compose.yml
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_username:your_password@mysql/your_database'
db = SQLAlchemy(app)


class UrlMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(50), unique=True, nullable=False)
    original_url = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['originalUrl']
    # Implement logic to shorten URL and store in the database

    # Fetch all shortened URLs from the database
    all_shortened_urls = UrlMapping.query.all()

    # Return a list of shortened URLs
    return jsonify(shortened_urls=[url.short_url for url in all_shortened_urls])


@app.route('/<short_url>')
def redirect_url(short_url):
    # Implement logic to retrieve the original URL and redirect.
    return redirect("Original URL", code=302)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
