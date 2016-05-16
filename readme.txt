# Xss探测器

---

## 1、项目结构说明
　　系统有如下结构目录：
> * bin/，可执行程序目录
> * document/，相关文档存放目录
> * source/，源码存放目录
　　-check/，Xss检测代码存放目录
　　-comm/，存放公用代码以及工具类
　　-gui/，存放界面相关代码存放目录
　　-spider/，爬虫程序相关代码存放
　　-test/，测试代码存放目录

## 2、项目相关运行环境以及依赖
　　运行环境：win7
　　开发语言：python 2.7.10
　　依赖的库如下：
> 1. requests - 2.10，下载地址：https://codeload.github.com/kennethreitz/requests/legacy.tar.gz/master ，安装；
> 2. wxPython -3.0，下载地址： http://www.wxpython.org/download.php#msw， 选择对应环境版本安装，界面的编辑可以下载wxFormBuilder来编辑；
> 3. SQLite3（数据库），下载地址：http://www.sqlite.org/download.html；
> 4. lxml，解析页面。

　　其中sqlite3的使用：https://github.com/palantir/sqlite3worker ，采用这个库来使用对数据库的操作
```
from sqlite3worker import Sqlite3Worker
sql_worker = Sqlite3Worker("/tmp/test.sqlite")
sql_worker.execute("CREATE TABLE tester (timestamp DATETIME, uuid TEXT)")
sql_worker.execute("INSERT into tester values (?, ?)", ("2010-01-01 13:00:00", "bow"))
sql_worker.execute("INSERT into tester values (?, ?)", ("2011-02-02 14:14:14", "dog"))

results = sql_worker.execute("SELECT * from tester")
for timestamp, uuid in results:
    print(timestamp, uuid)

sql_worker.close()
```

## 3、运行
　　界面的运行直接运行gui目录下的XssDetect.py就可以了（后期后调整）：
```
python XssDetect.py
```



