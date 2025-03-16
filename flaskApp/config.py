# flaskApp/config.py

class Config:
    # MySQL 数据库连接配置
    DB_USER = 'root'
    DB_PASSWORD = 'administrator'
    DB_HOST = 'localhost'
    DB_NAME = 'steel_price_db'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def create_database(app, db):
        """
        创建数据库的方法
        """
        app.config.from_object(Config)
        db.init_app(app)
        with app.app_context():
            db.create_all()
        print("Database created successfully.")