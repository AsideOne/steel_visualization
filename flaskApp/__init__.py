from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()


def create_app():
    from flaskApp import config

    app.config.from_object(config.Config)
    db.init_app(app)
    from flaskApp import routes
    return app