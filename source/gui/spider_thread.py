#_*_coding:utf-8_*_

import sys
import threading

import wx

reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append(r"../spider")

from spider_main import SpiderMain

class SpiderThread(threading.Thread):
	"""
	爬虫的多线程（由于需要给界面反馈信息，所以需要定制）
	"""

	def __init__(self, frame, root_url):

		threading.Thread.__init__(self)
		# 初始化参数
		self.frame = frame
		self.root_url = root_url
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
		self.timeout = 3
		self.crawl_depth = 55

		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()

		self.spider_main = SpiderMain()

	def stop(self):
		self.timeToQuit.set()

	def run(self):
		for url in self.spider_main.craw(self.root_url,self.headers,self.timeout,self.crawl_depth):
			wx.CallAfter(self.frame.print_on_spider_grid, unicode(self.getName() + "--->" + url))
			print self.getName(),"--->",url

# if __name__ == '__main__':
# #	root_url = "https://docs.python.org/3/library/sqlite3.html"
# #	root_url = "http://192.168.204.242/cms/index.php"
# 	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
# 	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
# 	timeout = 3
# 	crawl_depth = 15    # 爬虫深度，最多爬取crawl_depth这么多个链接地址
# 	obj_spider = SpiderMain()
# #	obj_spider.craw(root_url,headers,timeout,crawl_depth)
# 	for x in range(5):
# 		t = SpiderThread(root_url,headers,timeout,crawl_depth)
# 		t.start()	