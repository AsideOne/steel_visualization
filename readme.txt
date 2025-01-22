flask  Flask 是一个轻量级的 Python Web 开发框架，它简单易用，适合快速开发小型到中型的 Web 应用程序
scrapy 是一个强大的 Python 爬虫框架，用于从网站上提取结构化数据。它具有高效、快速和可扩展的特点，适用于大规模的数据抓取任务。
BeautifulSoup 是 Python 中一个用于解析 HTML 和 XML 文档的库，它提供了一种简单而强大的方式来遍历、搜索和修改解析树，帮助你从网页中提取所需的数据
flask_sqlalchemy 是一个 Flask 扩展，它简化了在 Flask 应用中使用 SQLAlchemy 的过程，使得在 Python 中操作关系型数据库变得更加方便和高效。
APScheduler 可以避免阻塞主线程，更适合在生产环境中使用。

SQLite 项目中使用的数据库为SQLliteSQLite 不需要像 MySQL、Oracle 等传统数据库那样启动一个单独的数据库服务器进程。
它直接读写磁盘上的数据库文件，这使得它的使用非常方便，尤其是在一些小型应用或者嵌入式设备中。例如，在一个 Python 脚本中使用 SQLite，
只需要导入sqlite3模块就可以直接操作数据库，无需额外的配置和管理数据库服务器。




from flask import Flask：从 Flask 库中导入 Flask 类。
app = Flask(__name__)：创建一个 Flask 应用实例，__name__ 表示当前模块的名称。
@app.route('/')：一个装饰器，将下面的函数绑定到根 URL（/）。
def hello_world():：定义一个处理函数，当用户访问根 URL 时会调用这个函数。
return 'Hello, World!'：函数返回的内容，会作为 HTTP 响应的主体。
app.run()：运行 Flask 应用程序，默认监听 127.0.0.1:5000 端口。