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

## 4、数据库设计
　　爬虫的数据库字段如下：
> 1. id，类型Integer，自增id；
> 2. url，类型Text，链接；
> 3. depth，类型Integer，链接深度；
> 4. method，类型Text，请求方法，get或者post；
> 5. param，类型Text，请求的参数，method为post才有，get默认为空。

## 5、多线程爬虫原理
　　线程使用宽度优先的方式，也就是待爬取的队列使用的是先进先出的Queue（它还有先进后出方式，以及优先级方式）。
　　在多个线程同步工作的情况下，就是个线程都同用一个待爬取的url队列，所以只有在“待爬取的队列为空”且“等待的线程的数量等于最大的线程数量”时才会线程才会完成工作退出。当然我们为了暂停设置了一个暂停标志位，如果我们控制退出了也就会结束工作退出。
　　多线程爬虫的工作流程如下：
> 1. 初始化线程，初始化的工作包括把种子链接加入公用的url待爬取队列，且种子链接的深度是0；
> 2. 开始爬取，生成多个线程，并且开始线程，然后每个线程会进入工作（后面会讲解单个线程的内部工作）；
> 3. 同时开启一个线程监控所有的线程是否都已经完成工作，如果完成了那么做些收尾的工作，比如界面提醒“爬取完成”和关闭数据库链接什么的；

　　单个线程的工作流程如下：
> 1. 判断，设置的标志位，是否要退出，如果是就退出，否则继续下一步；
> 2. 判断，待爬取队列是否为空且等待的线程数量为最大线程数，如果条件为真则退出，否则继续下一步；
> 3. 判断，队列是否为空，如果为空了，那么进入等待状态，如果不为空那么继续下一步；
> 4. 判断，等待的线程数是否等于0，如果等于0进入等待状态，否则继续下一步；
> 5. 正式进入工作，那么等待的线程数减一表示自己进入工作状态；
> 6. 从队列中获取一个url，使用下载器下载内容，返回之后将内容给解析器解析，并且将这个url写入数据库；
> 7. 判断新解析的url是否符合爬取的深度，如果符合那么加入队列中，并且唤醒因为队列为空而进入等待的线程；
> 8. 最后判断当前的线程是否小于最大线程数，如果小于那么此线程进入等待状态，并且唤醒因为等待线程等于0而进入等待线程；
> 9. 回到第一步继续循环。
　　


