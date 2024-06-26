import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    db.init_app(app)

    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.get_table_names():
            print("Database is empty, creating tables and running migrations.")
            db.create_all()
            os.system("flask db upgrade")
        else:
            print("Database already initialized, skipping table creation and migrations.")

    return app

if __name__ == "__main__":
    app = create_app()
