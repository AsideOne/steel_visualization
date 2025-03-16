from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import db
from .routes import routes  # 导入 routes 蓝图

def create_app():
    app = Flask(__name__)

    # 调试：打印配置加载状态
    print("Loading config...")
    app.config.from_object(Config)
    print("Config loaded.")

    # 调试：打印 SQLAlchemy 绑定状态
    print("Initializing SQLAlchemy...")
    db.init_app(app)
    print("SQLAlchemy initialized.")

    # 注册 routes 蓝图
    app.register_blueprint(routes)

    return app