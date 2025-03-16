from flask import Flask, render_template
from flaskApp.config import Config
from flaskApp.models import db
from data import DatabaseManager
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
from .routes import routes  # 导入 routes 蓝图

visualization = Flask(__name__, static_folder='templates')
visualization.config.from_object(Config)
db.init_app(visualization)

# 注册 routes 蓝图
visualization.register_blueprint(routes)

database_manager = DatabaseManager(visualization)

@visualization.route('/')
def main_index():
    print('featch_data_for_visualization')
    data = fetch_data_for_visualization()
    print('visuallyzation返回数据')
    all_steel_prices = database_manager.fetch_all_data()
    steel_names = []
    steel_prices = []
    steel_dates = []
    for steel_price in all_steel_prices:
        steel_names.append(steel_price.spec.variety)
        steel_prices.append(steel_price.price)
        steel_dates.append(str(steel_price.price_date))
    return render_template('index.html', steel_names=steel_names, steel_prices=steel_prices, steel_dates=steel_dates)

def fetch_data_for_visualization():
    from flaskApp.models import ScrapSteelPrice
    data = ScrapSteelPrice.query.with_entities(ScrapSteelPrice.price_date, ScrapSteelPrice.price).all()
    result = [{'date': str(item.price_date), 'price': item.price} for item in data]
    return result

def run_scrapy_spider():
    subprocess.run(['scrapy', 'crawl', 'steel_price_spider'])

scheduler = BackgroundScheduler()
scheduler.add_job(run_scrapy_spider, 'interval', hours=1)
scheduler.start()

if __name__ == '__main__':
    with visualization.app_context():
        print("创建表成功")
        database_manager.create_database()

    try:
        print("开始运行爬虫...")
        subprocess.run(['scrapy', 'crawl', 'steel_price_spider'])
        print("爬虫运行完成。")
    except subprocess.CalledProcessError as e:
        print(f"爬虫运行出错: {e}")

    visualization.run(debug=True)