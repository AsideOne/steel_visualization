
# 从自定义的 flaskApp 模块中导入 create_app 函数，可能用于创建 Flask 应用程序
# 但是在当前代码中并未使用到 create_app 函数，也许后续可以考虑使用它来创建应用程序
from flaskApp import create_app
# 从 Flask 库中导入 Flask 类，用于创建 Flask 应用程序
from flask import Flask
# 从 flask_sqlalchemy 库中导入 SQLAlchemy 类，用于数据库操作，如创建表、执行查询等
from flask_sqlalchemy import SQLAlchemy
# 从 flaskApp 模块的 config 子模块中导入 Config 类，该类包含应用程序的配置信息
from flaskApp.config import Config
# 从 flaskApp 模块的 models 子模块中导入 db 对象，可能是 SQLAlchemy 的实例，用于数据库操作
from flaskApp.models import db
# 从 flaskApp 模块的 routes 子模块中导入 index 函数，可能是一个路由处理函数
from flaskApp.routes import index


# 创建一个 Flask 应用程序实例，__name__ 表示当前模块的名称
app = Flask(__name__)
# 从 Config 类中加载应用程序的配置信息到 app 中，如数据库 URI、调试模式等
app.config.from_object(Config)
# 使用 db 对象的 init_app 方法将数据库操作和 Flask 应用程序关联起来
db.init_app(app)


# 使用 @app.route 装饰器将 main_index 函数绑定到根路径 '/'，当用户访问根路径时将调用该函数
@app.route('/')
def main_index():
    # 调用 index 函数，并将其返回的结果作为响应内容返回给用户
    return index()


# 确保代码仅在作为主程序运行时执行，而不是作为模块被导入时执行
if __name__ == '__main__':
    # 创建一个应用程序上下文，某些操作（如创建数据库表）需要在应用程序的上下文中进行
    with app.app_context():
        # 使用 db 的 create_all 方法根据定义的模型创建数据库表
        db.create_all()
    # 运行 Flask 应用程序，并开启调试模式，在调试模式下，服务器会自动重新加载代码，并且会显示详细的错误信息
    app.run(debug=True)