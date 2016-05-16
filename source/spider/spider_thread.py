#_*_coding:utf-8_*_

import sys
import threading

import wx
import Queue

reload(sys)
sys.setdefaultencoding( "utf-8" )

from spider_main import SpiderMain
from url_manager import UrlManager

UrlQueue = Queue.Queue()

class SpiderThread(threading.Thread):
	"""
	爬虫的多线程（由于需要给界面反馈信息，所以需要定制）
	"""
	def __init__(self, frame, crawl_depth):

		threading.Thread.__init__(self)
		# 初始化参数
		self.frame = frame

		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()

		#初始化爬虫
		self.spider_main = SpiderMain(crawl_depth)

	def stop(self):
		self.spider_main.stop_crawl()
		self.timeToQuit.set()


	def run(self):
		for url in self.spider_main.craw():
			wx.CallAfter(self.frame.print_on_spider_grid, unicode(self.getName() + "--->" + url))
			print self.getName(),"--->",url

if __name__ == '__main__':
	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
	crawl_depth = 2
	UrlManager.init_spider(root_url)
	UrlManager.init_spider(root_url)
	print UrlManager.has_new_url()
	for x in range(2):
		print x
		t = SpiderThread(None,crawl_depth)
		t.start()	