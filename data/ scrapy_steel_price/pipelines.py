from scrapy.exceptions import DropItem
from flaskApp.models import db, SteelPrice


class SteelPricePipeline:
    def open_spider(self, spider):
        # 在爬虫开始时初始化数据库连接
        db.create_all()

    def close_spider(self, spider):
        # 在爬虫结束时关闭数据库连接
        pass

    def process_item(self, item, spider):
        # 检查所需的数据是否完整
        if not all(item.values()):
            raise DropItem("Missing data in %s" % item)
        try:
            steel_price = SteelPrice(
                price=float(item['price']),
                date=item['date'],
                region=item['region']
            )
            db.session.add(steel_price)
            db.session.commit()
        except Exception as e:
            print(f"Error inserting item into database: {e}")
            db.session.rollback()
            raise DropItem(f"Failed to insert item into database: {e}")
        return item