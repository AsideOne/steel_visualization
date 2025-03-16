from flaskApp.models import db, ScrapSteelPrice, Region, ScrapSteelSpec
from flask import Flask
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:administrator@localhost/steel_price_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class SteelPricePipeline:
    def process_item(self, item, spider):
        with app.app_context():
            # 处理地区信息
            region_name = item['region_name']
            region = Region.query.filter_by(name=region_name).first()
            if not region:
                region = Region(name=region_name)
                db.session.add(region)
                db.session.commit()

            # 处理品种规格信息
            variety = item['variety']
            specification = item['specification']
            spec = ScrapSteelSpec.query.filter_by(variety=variety, specification=specification).first()
            if not spec:
                spec = ScrapSteelSpec(variety=variety, specification=specification)
                db.session.add(spec)
                db.session.commit()

            # 生成废钢 ID
            scrap_steel_id = f"{region.id}-{spec.id}-{item['price_date']}"

            # 检查数据是否已存在
            existing_data = ScrapSteelPrice.query.filter_by(scrap_steel_id=scrap_steel_id).first()
            if not existing_data:
                scrap_steel_price = ScrapSteelPrice(
                    scrap_steel_id=scrap_steel_id,
                    spec_id=spec.id,
                    region_id=region.id,
                    price=item['price'],
                    price_date=item['price_date']
                )
                db.session.add(scrap_steel_price)
                db.session.commit()
        return item