from flask import render_template, jsonify
from flaskApp.models import SteelPrice

# 注意这里不再创建 Flask 应用实例，而是使用从 visualization.py 导入的实例

def api_data():
    # 从数据库中查询所有的 SteelPrice 记录
    data = SteelPrice.query.all()
    # 将查询结果转换为列表，列表中的每个元素是一个字典，包含日期、价格和地区信息
    data_list = [{'date': str(item.date), 'price': item.price, 'region': item.region} for item in data]
    # 将数据列表转换为 JSON 格式并作为 HTTP 响应返回，适用于 API 调用
    print(data_list)
    print("route访问")
    return jsonify(data_list)

def index():
    # 渲染 index2.html 模板
    return render_template('index2.html')

def data_table():
    steel_prices = SteelPrice.query.all()
    return render_template('data_table.html', steel_prices=steel_prices)