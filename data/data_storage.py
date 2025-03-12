from flaskApp.models import db, SteelPrice


def store_data(price, date, region):
    try:
        steel_price = SteelPrice(price=price, date=date, region=region)
        db.session.add(steel_price)
        db.session.commit()
        print("Data stored successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Failed to store data: {e}")


def fetch_all_data():
    return SteelPrice.query.all()


def fetch_data_by_region(region):
    return SteelPrice.query.filter_by(region=region).all()


from flaskApp.models import db, SteelPrice

class DatabaseManager:
    def __init__(self, app):
        """
        初始化 DatabaseManager 类，将 Flask 应用实例传入
        :param app: Flask 应用实例
        """
        self.app = app
        self.db = db

    def create_database(self):
        """
        创建数据库表
        """
        with self.app.app_context():
            self.db.create_all()
        print("Database created successfully.")

    def store_data(self, price, date, region):
        """
        存储数据到数据库
        :param price: 钢材价格
        :param date: 日期
        :param region: 地区
        """
        try:
            with self.app.app_context():
                steel_price = SteelPrice(price=price, date=date, region=region)
                self.db.session.add(steel_price)
                self.db.session.commit()
            print("Data stored successfully.")
        except Exception as e:
            self.db.session.rollback()
            print(f"Failed to store data: {e}")

    def fetch_all_data(self):
        """
        查询所有数据
        :return: 所有 SteelPrice 记录
        """
        with self.app.app_context():
            return SteelPrice.query.all()

    def fetch_data_by_region(self, region):
        """
        根据地区查询数据
        :param region: 地区
        :return: 指定地区的 SteelPrice 记录
        """
        with self.app.app_context():
            return SteelPrice.query.filter_by(region=region).all()

    def fetch_data_by_date_range(self, start_date, end_date):
        """
        根据日期范围查询数据
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return: 指定日期范围内的 SteelPrice 记录
        """
        with self.app.app_context():
            return SteelPrice.query.filter(SteelPrice.date.between(start_date, end_date)).all()

def fetch_data_by_date_range(start_date, end_date):
    return SteelPrice.query.filter(SteelPrice.date.between(start_date, end_date)).all()