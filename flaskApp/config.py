import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

class Config:
    # SQLAlchemy 中用于指定数据库连接字符串的配置项。在这个例子中，'sqlite:///steel.db' 表示使用 SQLite 数据库，并且数据库文件名为 steel.db
    SQLALCHEMY_DATABASE_URI ='sqlite:///steel.db'

    # 当设置为 False 时，可以避免 SQLAlchemy 发出有关对象修改的信号，减少性能开销和不必要的警告信息。
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