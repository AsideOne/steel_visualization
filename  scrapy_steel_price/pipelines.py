from scrapy.exceptions import DropItem
from flaskApp.models import db, SteelPrice
from flaskApp import app
from datetime import datetime

class SteelPricePipeline:
    def open_spider(self, spider):
        # 在爬虫开始时，确保数据库表已经创建
        with app.app_context():
            db.create_all()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if not all(item.values()):
            raise DropItem("Missing data in %s" % item)
        try:
            with app.app_context():
                today = datetime.now().date()  # 获取当前日期
                # 检查数据库中是否已经存在当天的相同数据
                existing_data = SteelPrice.query.filter_by(name=item['name'], date=today).first()
                if not existing_data:
                    # 创建 SteelPrice 实例并添加到数据库会话中
                    steel_price = SteelPrice(name=item['name'], price=item['price'], date=today)
                    db.session.add(steel_price)
                # 提交会话以保存数据到数据库
                db.session.commit()
        except Exception as e:
            print(f"Error inserting item into database: {e}")
            # 发生错误时回滚会话
            db.session.rollback()
            raise DropItem(f"Failed to insert item into database: {e}")
        return item