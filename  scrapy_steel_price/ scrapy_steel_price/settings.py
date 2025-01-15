# 设置用户代理，避免被网站反爬虫机制拦截
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# 配置日志级别
LOG_LEVEL = 'INFO'
# 配置管道，用于处理抓取的数据
ITEM_PIPELINES = {
   'scrapy_steel_price.pipelines.SteelPricePipeline': 300,
}