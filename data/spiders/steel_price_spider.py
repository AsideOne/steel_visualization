import scrapy
from bs4 import BeautifulSoup
from datetime import date
from flaskApp.models import ScrapSteelPrice, ScrapSteelSpec, Region

# 假设这里有一个简单的映射函数，根据废钢名称推测品种和规格
def infer_spec(name):
    if "重废" in name:
        variety = "重废"
        specification = "未详细记录"
    elif "钢板料" in name:
        variety = "钢板料"
        specification = "未详细记录"
    elif "钢筋切粒" in name:
        variety = "钢筋切粒"
        specification = "未详细记录"
    elif "破碎料" in name:
        variety = "破碎料"
        specification = "未详细记录"
    else:
        variety = "其他"
        specification = "未详细记录"
    return variety, specification

# 从名称中提取地区关键词
def extract_region(name):
    region_keywords = {
        "华东": "华东地区",
        "华南": "华南地区",
        "华北": "华北地区",
        "华中": "华中地区",
        "西南": "西南地区",
        "东北": "东北地区",
        "西北": "西北地区",
        "陶庄": "陶庄地区"
    }
    for keyword, region in region_keywords.items():
        if keyword in name:
            return region
    return "默认地区"  # 未匹配到关键词时使用默认

class SteelPriceSpider(scrapy.Spider):
    name = "steel_price_spider"
    start_urls = ['https://feigang.mysteel.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        steel_info_divs = soup.find_all('div', class_='index-item-content')
        for div in steel_info_divs:
            try:
                name = div.find('a', class_='index-item-title').text.strip()
                price = div.find('p', class_='index-item-value').text
                price = float(price.replace(',', ''))
                price_date = date.today()

                # 提取地区
                region_name = extract_region(name)

                # 推断品种和规格
                variety, specification = infer_spec(name)

                item = {
                    'variety': variety,
                    'specification': specification,
                    'price': price,
                    'price_date': price_date,
                    'region_name': region_name
                }
                yield item
            except Exception as e:
                self.logger.error(f"Error parsing item: {e}")