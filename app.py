from flaskApp import create_app
from flaskApp.visualization import database_manager
import subprocess

app = create_app()

if __name__ == '__main__':
    if __name__ == '__main__':
        with app.app_context():
            print("创建表成功")
            database_manager.create_database()

        try:
            print("开始运行爬虫...")
            subprocess.run(['scrapy', 'crawl', 'steel_price_spider'])
            print("爬虫运行完成。")
        except subprocess.CalledProcessError as e:
            print(f"爬虫运行出错: {e}")
    app.run(debug=True)


