from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from config import Config

db = SQLAlchemy()
redis_client = None
initialized = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global redis_client
    redis_client = redis.Redis.from_url(app.config['REDIS_URL'])

    db.init_app(app)

    with app.app_context():
        from .models import CountryRanking, Player
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    @app.before_request
    def before_request():
        global initialized
        if not initialized:
            sync_redis_with_db()
            initialized = True

    return app

def get_redis_client():
    global redis_client
    if not redis_client:
        redis_client = redis.Redis.from_url(Config.REDIS_URL)
    return redis_client

def sync_redis_with_db():
    from .models import CountryRanking  # Import here to avoid circular import
    rankings = CountryRanking.query.all()
    for ranking in rankings:
        redis_client.zadd('country_rankings', {ranking.country: ranking.points})
