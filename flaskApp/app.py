from flaskApp import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskApp.config import Config
from flaskApp.models import db
from flaskApp.routes import index

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def main_index():
    return index()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
