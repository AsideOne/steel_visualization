from flask import render_template, jsonify
from flaskApp import app, db
from flaskApp.models import SteelPrice


@app.route('/api/data')
def api_data():
    # 从数据库中查询所有的 SteelPrice 记录
    data = SteelPrice.query.all()
    # 将查询结果转换为列表，列表中的每个元素是一个字典，包含日期、价格和地区信息
    data_list = [{'date': item.date, 'price': item.price, 'region': item.region} for item in data]
    # 将数据列表转换为 JSON 格式并作为 HTTP 响应返回，适用于 API 调用
    return jsonify(data_list)


def index():
    # 从数据库中查询所有的 SteelPrice 记录
    data = SteelPrice.query.all()
    # 提取每个 SteelPrice 记录的名称，存储在 steel_names 列表中
    steel_names = [steel.name for steel in data]
    # 提取每个 SteelPrice 记录的价格，存储在 steel_prices 列表中
    steel_prices = [steel.price for steel in data]
    print('index页面查询数据')
    # 使用 render_template 函数渲染 index.html 模板，并将 steel_names 和 steel_prices 作为变量传递给模板
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