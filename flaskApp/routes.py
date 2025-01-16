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
# @app.route('/')
# def index():
#     data = SteelPrice.query.all()
#     data_list = [{'date': item.date, 'price': item.price, 'region': item.region} for item in data]
#     return render_template('index.html', data=data_list)
#
#
# @app.route('/api/data')
# def api_data():
#     data = SteelPrice.query.all()
#     data_list = [{'date': item.date, 'price': item.price, 'region': item.region} for item in data]
#     return jsonify(data_list)
#
#
# @app.route('/api/data/<region>')
# def api_data_by_region(region):
#     data = SteelPrice.query.filter_by(region=region).all()
#     data_list = [{'date': item.date, 'price': item.price} for item in data]
#     return jsonify(data_list)
#
#
# @app.route('/api/statistics')
# def api_statistics():
#     from data_processing import process_data
#     df = process_data()
#     average_price = df['price'].mean()
#     average_price_by_region = df.groupby('region')['price'].mean().to_dict()
#     return jsonify({
#         'average_price': average_price,
#         'average_price_by_region': average_price_by_region
#     })