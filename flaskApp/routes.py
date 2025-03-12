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


@app.route('/index')
def index1():
    # 渲染 index1.html 模板
    return render_template('index.html')


# 其他现有的路由和视图函数保持不变