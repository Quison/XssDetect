目录说明：
bin/   可执行程序目录

document/  相关文档存放目录

source/  存放源代码目录
    check/  XSS检测代码存放目录
    comm/   存放公共函数代码
    config/  配置相关文件存放目录
    gui/  程序界面相关代码存放目录
    spider/  爬虫程序代码存放目录
    test/   测试代码存放目录

README.md && .gitignore git相关默认文件
readme.txt   相关信息记录文件

依赖库：
requests

url处理：
urlparse 

爬虫多线程模块用threading模块吧，参考http://www.jianshu.com/p/86b8e78c418a


sqlite3的使用：https://github.com/palantir/sqlite3worker  采用这个库来使用对数据库的操作
from sqlite3worker import Sqlite3Worker
sql_worker = Sqlite3Worker("/tmp/test.sqlite")
sql_worker.execute("CREATE TABLE tester (timestamp DATETIME, uuid TEXT)")
sql_worker.execute("INSERT into tester values (?, ?)", ("2010-01-01 13:00:00", "bow"))
sql_worker.execute("INSERT into tester values (?, ?)", ("2011-02-02 14:14:14", "dog"))

results = sql_worker.execute("SELECT * from tester")
for timestamp, uuid in results:
    print(timestamp, uuid)

sql_worker.close()
