install bitarray(该模块是pybloom的依赖模块)： https://pypi.python.org/pypi/bitarray/
install pybloom: https://pypi.python.org/pypi/pybloom

利用程序参考：http://pydoc.net/Python/pybloom/1.1/pybloom.pybloom/
github地址：https://github.com/jaybaird/python-bloomfilter/


安装过程中，如果错误：error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27 
该错误需要安装vs2008，或者下载下面的文件进行安装https://www.microsoft.com/en-us/download/details.aspx?id=44266



win install redis : http://jingyan.baidu.com/article/f25ef2546119fd482c1b8214.html
redis:   https://github.com/MSOpenTech/redis/releases

python redis: https://pypi.python.org/pypi/redis
python redis用法：http://blog.csdn.net/chenggong2dm/article/details/6102540



test.py 是测试pybloom 和 redis的代码
这里讨论下到底怎么存储，以及后面的结果怎么存储

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


