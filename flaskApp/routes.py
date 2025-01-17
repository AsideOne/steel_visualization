from flask import render_template, jsonify
from flaskApp import app, db
from flaskApp.models import SteelPrice


@app.route('/api/data')
def api_data():
    data = SteelPrice.query.all()
    data_list = [{'date': item.date, 'price': item.price, 'region': item.region} for item in data]
    return jsonify(data_list)
def index():
    data = SteelPrice.query.all()
    # 提取废钢名称和价格数据，准备传递给模板
    steel_names = [steel.name for steel in data]
    steel_prices = [steel.price for steel in data]
    return render_template('index.html', steel_names=steel_names, steel_prices=steel_prices)
