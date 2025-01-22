import scrapy
from bs4 import BeautifulSoup
import requests
from flaskApp import app, db
from flaskApp.models import SteelPrice

def scrape_steel_price():
    url = 'https://feigang.mysteel.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    steel_info_divs = soup.find_all('div', class_='index-item-content')

    with app.app_context():
        # 确保数据库表已经创建
        db.create_all()
        print("spider数据库创建成功")
        for div in steel_info_divs:
            name = div.find('a', class_='index-item-title').text.encode('iso-8859-1').decode('utf-8')
            price = div.find('p', class_='index-item-value').text
            # 创建 SteelPrice 实例并添加到数据库会话中
            steel_price = SteelPrice(name=name, price=price)
            db.session.add(steel_price)
        # 提交会话以保存数据到数据库
        print("spider插入成功")
        db.session.commit()

        # 查询并展示数据用于测试
        all_steel_prices = SteelPrice.query.all()
        print("查询到的废钢价格数据：")
        for steel_price in all_steel_prices:
            print(f"名称: {steel_price.name}, 价格: {steel_price.price}")

if __name__ == '__main__':
    # 获取创建好的应用
    from flaskApp import app
    with app.app_context():
        scrape_steel_price()

class SteelPriceSpider(scrapy.Spider):
    name = "steel_price_spider"
    start_urls = ['https://feigang.mysteel.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        steel_info_divs = soup.find_all('div', class_='index-item-content')
        for div in steel_info_divs:
            name = div.find('a', class_='index-item-title').text
            price = div.find('p', class_='index-item-value').text
            yield {
                'name': name,
                'price': price
            }