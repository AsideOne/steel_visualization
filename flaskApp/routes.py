from flask import Blueprint, render_template

from flaskApp.models import ScrapSteelPrice

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/trend_analysis')
def trend_analysis():
    return render_template('trend_analysis.html')

@routes.route('/comparison_analysis')
def comparison_analysis():
    return render_template('comparison_analysis.html')

@routes.route('/spatial_analysis')
def spatial_analysis():
    return render_template('spatial_analysis.html')

@routes.route('/comprehensive_analysis')
def comprehensive_analysis():
    return render_template('comprehensive_analysis.html')

routes.route('/api/data')
def get_steel_price_data():
    try:
        # 查询废钢价格数据
        data = ScrapSteelPrice.query.with_entities(ScrapSteelPrice.price_date, ScrapSteelPrice.price).all()
        result = [{'date': str(item.price_date), 'price': item.price} for item in data]
        return jsonify(result)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify([])