from flaskApp.models import SteelPrice, db
from datetime import datetime

def save_steel_price(name, price, timestamp):
    existing_data = {f"{item.name}-{item.price}": item for item in SteelPrice.query.all()}
    key = f"{name}-{price}"
    if key not in existing_data:
        steel_price = SteelPrice(name=name, price=price, timestamp=timestamp)
        db.session.add(steel_price)
        db.session.commit()

def get_all_steel_prices():
    """
    获取所有钢铁价格数据
    """
    return SteelPrice.query.all()

def get_steel_price_by_name(name):
    """
    根据名称获取钢铁价格数据
    """
    return SteelPrice.query.filter_by(name=name).first()

def update_steel_price(name, new_price):
    """
    更新指定名称的钢铁价格
    """
    steel_price = SteelPrice.query.filter_by(name=name).first()
    if steel_price:
        steel_price.price = new_price
        steel_price.timestamp = datetime.now()
        db.session.commit()

def delete_steel_price(name):
    """
    删除指定名称的钢铁价格数据
    """
    steel_price = SteelPrice.query.filter_by(name=name).first()
    if steel_price:
        db.session.delete(steel_price)
        db.session.commit()