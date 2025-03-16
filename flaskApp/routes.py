from flask import Blueprint, render_template, jsonify
from flaskApp.db_operations import get_all_steel_prices
from flaskApp.models import ScrapSteelPrice, ScrapSteelSpec

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

@routes.route('/api/data')
def get_steel_price_data():
    steel_prices = ScrapSteelPrice.query.join(ScrapSteelSpec).all()
    data = {}
    for price in steel_prices:
        variety = price.spec.variety
        if variety not in data:
            data[variety] = []
        data[variety].append({
            'date': str(price.price_date),
            'price': price.price
        })
    return jsonify(data)