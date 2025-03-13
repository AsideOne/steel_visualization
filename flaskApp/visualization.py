from flask import Flask, render_template
import sqlite3
import json
from flaskApp.config import Config
from flaskApp.models import db
from data import DatabaseManager
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
from flaskApp.routes import api_data, index, data_table  # 导入路由函数

visualization = Flask(__name__, static_folder='templates')
# 从 Config 类中加载应用程序的配置信息到 app 中，如数据库 URI、调试模式等
visualization.config.from_object(Config)
# 使用 db 对象的 init_app 方法将数据库操作和 Flask 应用程序关联起来
db.init_app(visualization)

# 初始化 DatabaseManager 类
database_manager = DatabaseManager(visualization)

# 注册路由
visualization.add_url_rule('/api/data', 'api_data', api_data)
visualization.add_url_rule('/index', 'index', index)
visualization.add_url_rule('/data_table', 'data_table', data_table)

@visualization.route('/')
def main_index():
    print('featch_data_for_visualization')
    data = fetch_data_for_visualization()
    print('visuallyzation返回数据')
    all_steel_prices = database_manager.fetch_all_data()
    steel_names = [steel.name for steel in all_steel_prices]
    steel_prices = [steel.price for steel in all_steel_prices]
    # 获取日期数据
    steel_dates = [str(steel.date) for steel in all_steel_prices]
    return render_template('index2.html', steel_names=steel_names, steel_prices=steel_prices, steel_dates=steel_dates)

from flaskApp.models import SteelPrice

def fetch_data_for_visualization():
    data = SteelPrice.query.with_entities(SteelPrice.date, SteelPrice.price).all()
    result = [{'date': str(item.date), 'price': item.price} for item in data]
    return result

def run_scrapy_spider():
    subprocess.run(['scrapy', 'crawl', 'steel_price_spider'])

scheduler = BackgroundScheduler()
scheduler.add_job(run_scrapy_spider, 'interval', hours=1)  # 每小时执行一次
scheduler.start()

# 确保代码仅在作为主程序运行时执行，而不是作为模块被导入时执行
if __name__ == '__main__':
    # 创建数据库
    with visualization.app_context():
        database_manager.create_database()  # 使用 DatabaseManager 类创建数据库
    # 运行 Flask 应用程序，并开启调试模式，在调试模式下，服务器会自动重新加载代码，并且会显示详细的错误信息
    visualization.run(debug=True)