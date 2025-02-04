from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 导入 flaskApp 模块中的 config 子模块，其中可能包含应用的配置信息
from flaskApp import config

# 创建一个 Flask 应用实例，使用当前模块的名称作为应用的名称
app = Flask(__name__)
# 创建一个 SQLAlchemy 实例，用于后续的数据库操作，如创建表、查询、插入、更新和删除等操作
db = SQLAlchemy()


def create_app():
    # 从 config 子模块的 Config 类中加载配置信息到 app 中，例如数据库 URI、调试模式等
    app.config.from_object(config.Config)
    # 将 SQLAlchemy 实例 db 与 Flask 应用 app 进行初始化，以便使用数据库操作功能
    db.init_app(app)
    # 导入 flaskApp 模块中的 routes 子模块，其中可能包含应用的路由定义
    from flaskApp import routes
    # 返回创建和配置好的 Flask 应用实例
    return app

# 创建并配置应用
app = create_app()

