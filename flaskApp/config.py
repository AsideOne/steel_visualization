import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

class Config:
    # 获取 flaskApp 下的 instance 目录的绝对路径
    base_dir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(base_dir, 'instance', 'steel.db')
    print(instance_path)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{instance_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def create_database():
        """
        创建数据库的方法
        """
        app.config.from_object(Config)
        db.init_app(app)
        with app.app_context():
            db.create_all()
        print("Database created successfully.")