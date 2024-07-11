from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from config import Config

db = SQLAlchemy()
redis_client = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global redis_client
    redis_client = redis.Redis.from_url(app.config['REDIS_URL'])

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .routes import main
    app.register_blueprint(main)
    return app

def get_redis_client():
    global redis_client
    if not redis_client:
        redis_client = redis.Redis.from_url(Config.REDIS_URL)
    return redis_client
