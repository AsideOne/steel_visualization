import requests
from bs4 import BeautifulSoup

url = 'https://feigang.mysteel.com/'  # 替换为实际的网页地址

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有包含废钢信息的div元素
steel_info_divs = soup.find_all('div', class_='index-item-content')

for div in steel_info_divs:
    # 获取废钢名称
    name = div.find('a', class_='index-item-title').text.encode('iso-8859-1').decode('utf-8')
    # 获取废钢价格
    price = div.find('p', class_='index-item-value').text
    print(f'废钢名称：{name}，价格：{price}')