# 设置用户代理
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# 设置下载延迟
DOWNLOAD_DELAY = 2

# 配置管道
ITEM_PIPELINES = {
    'data.pipelines.SteelPricePipeline': 300,
}

# 配置日志级别
LOG_LEVEL = 'INFO'

# 配置爬虫模块
SPIDER_MODULES = ['data.spiders']
NEWSPIDER_MODULE = 'data.spiders'