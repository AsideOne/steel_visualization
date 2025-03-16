from flask import Flask, render_template

from data import DatabaseManager
from flaskApp.config import Config
from flaskApp.models import db
from apscheduler.schedulers.background import BackgroundScheduler
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

