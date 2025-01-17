import scrapy
from bs4 import BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup
from flaskApp.app import app
from flaskApp.models import SteelPrice, db

def scrape_steel_price():
    url = 'https://feigang.mysteel.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    steel_info_divs = soup.find_all('div', class_='index-item-content')

    with app.app_context():
        for div in steel_info_divs:
            name = div.find('a', class_='index-item-title').text.encode('iso-8859-1').decode('utf-8')
            price = div.find('p', class_='index-item-value').text
            steel_price = SteelPrice(name=name, price=price)
            db.session.add(steel_price)
        db.session.commit()

if __name__ == '__main__':
    scrape_steel_price()


# class SteelPriceSpider(scrapy.Spider):
#     name = "steel_price_spider"
#     # start_urls = ['https://feigang.mysteel.com/']  # 我的钢铁网废钢页
#     url = 'https://feigang.mysteel.com/'
#     # 找到所有包含废钢信息的div元素
#     response = requests.get(url)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # 找到所有包含废钢信息的div元素
#     steel_info_divs = soup.find_all('div', class_='index-item-content')
#
#     for div in steel_info_divs:
#         # 获取废钢名称
#         name = div.find('a', class_='index-item-title').text.encode('iso-8859-1').decode('utf-8')
#         # 获取废钢价格
#         price = div.find('p', class_='index-item-value').text
#         print(f'废钢名称：{name}，价格：{price}')

    # def parse(self, response):
    #     # 假设废钢价格信息在 div 元素中，class 为 'price-item'，并且包含 price、date 和 region 信息
    #     for item in response.css('div.price-item'):
    #         yield {
    #             'price': item.css('span.price::text').get(),
    #             'date': item.css('span.date::text').get(),
    #             'region': item.css('span.region::text').get(),
    #         }