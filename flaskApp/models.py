from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

# 地区表
class Region(db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # 精确到市级乃至县级区域名称

# 品种规格表
class ScrapSteelSpec(db.Model):
    __tablename__ = 'scrap_steel_spec'
    id = db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String(100), nullable=False)  # 废钢品种，如重型废钢、中型废钢、轻薄料等
    specification = db.Column(db.String(200))  # 规格，涵盖尺寸、厚度、纯度等

# 废钢价格表
class ScrapSteelPrice(db.Model):
    __tablename__ = 'scrap_steel_price'
    id = db.Column(db.Integer, primary_key=True)
    scrap_steel_id = db.Column(db.String(50), unique=True, nullable=False)  # 废钢ID，作为唯一标识符
    spec_id = db.Column(db.Integer, db.ForeignKey('scrap_steel_spec.id'), nullable=False)  # 关联品种规格表
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)  # 关联地区表
    price = db.Column(db.Float, nullable=False)  # 每吨废钢的成交价格
    price_date = db.Column(db.Date, default=date.today)  # 价格日期，精确至年月日

    spec = db.relationship('ScrapSteelSpec', backref=db.backref('prices', lazy=True))
    region = db.relationship('Region', backref=db.backref('prices', lazy=True))

# 库存表
class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    scrap_steel_id = db.Column(db.String(50), db.ForeignKey('scrap_steel_price.scrap_steel_id'), nullable=False)  # 关联废钢价格表
    quantity = db.Column(db.Float, nullable=False)  # 库存数量

    scrap_steel = db.relationship('ScrapSteelPrice', backref=db.backref('inventories', lazy=True))

# 企业信息表
class Enterprise(db.Model):
    __tablename__ = 'enterprise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)  # 企业名称

# 企业交易表
class EnterpriseTransaction(db.Model):
    __tablename__ = 'enterprise_transaction'
    id = db.Column(db.Integer, primary_key=True)
    transaction_number = db.Column(db.String(100), unique=True, nullable=False)  # 交易单号
    supplier_id = db.Column(db.Integer, db.ForeignKey('enterprise.id'), nullable=False)  # 供应商ID
    purchaser_id = db.Column(db.Integer, db.ForeignKey('enterprise.id'), nullable=False)  # 采购商ID
    scrap_steel_id = db.Column(db.String(50), db.ForeignKey('scrap_steel_price.scrap_steel_id'), nullable=False)  # 关联废钢价格表
    transaction_quantity = db.Column(db.Float, nullable=False)  # 交易数量
    transaction_amount = db.Column(db.Float, nullable=False)  # 交易金额
    settlement_method = db.Column(db.String(50), nullable=False)  # 结算方式，如现金、转账、票据等

    supplier = db.relationship('Enterprise', foreign_keys=[supplier_id], backref=db.backref('supplier_transactions', lazy=True))
    purchaser = db.relationship('Enterprise', foreign_keys=[purchaser_id], backref=db.backref('purchaser_transactions', lazy=True))
    scrap_steel = db.relationship('ScrapSteelPrice', backref=db.backref('transactions', lazy=True))

# 市场资讯表
class MarketNews(db.Model):
    __tablename__ = 'market_news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # 资讯标题
    content = db.Column(db.Text)  # 资讯内容
    price_id = db.Column(db.Integer, db.ForeignKey('scrap_steel_price.id'))  # 关联废钢价格表

    price = db.relationship('ScrapSteelPrice', backref=db.backref('news', lazy=True))

# 用户信息表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(200), nullable=False)  # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 关联权限表

    role = db.relationship('Role', backref=db.backref('users', lazy=True))

# 权限表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  # 角色名称