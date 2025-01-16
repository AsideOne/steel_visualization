import os


class Config:
    # SQLAlchemy 中用于指定数据库连接字符串的配置项。在这个例子中，'sqlite:///steel.db' 表示使用 SQLite 数据库，并且数据库文件名为 steel.db

    SQLALCHEMY_DATABASE_URI ='sqlite:///steel.db'

    # 当设置为 False 时，可以避免 SQLAlchemy 发出有关对象修改的信号，减少性能开销和不必要的警告信息。
    SQLALCHEMY_TRACK_MODIFICATIONS = False