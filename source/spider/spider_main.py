#_*_coding:utf-8_*_

import sys  
import time
import threading
import thread
import wx

import html_downloader
import html_parser
import html_outputer

from spider_url import SpiderUrl
from url_queue import UrlQueue
			
class SpiderThread(threading.Thread):
	"""
	爬虫的线程类
	"""

	def __init__(self, frame, crawl_depth, url_queue, con):

		threading.Thread.__init__(self)
		# 初始化参数
		self.frame = frame

		#初始化爬虫
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		self.crawl_depth = crawl_depth
		self.url_queue = url_queue
		self.con = con
		self.timeout = 3
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

	def run(self):
		while 1:
			if SpiderMain.stoped :
				break			
			# 当队列为空时，默认当做还有其他线程正在工作，等待3秒，如果3秒过后还为空则超时退出
			if self.url_queue.is_empty() and (SpiderMain.thread_num == SpiderMain.wait_thread_num):
				break
			else:
				if self.url_queue.is_empty() :
					self.wait()
				elif SpiderMain.wait_thread_num == 0:
					self.wait()
				else:
					SpiderMain.wait_thread_num -= 1
					try:
						spider_url = self.url_queue.get()
						url_str = spider_url.get_url()
						url_depth = spider_url.get_depth()
						html_cont = self.downloader.download(url_str,headers=self.headers,timeout=self.timeout)	
						# 将解析得的url放入带爬取链接队列中深度+1
						new_urls_str = self.parser.parse(url_str,html_cont)
						# 如果深度如果连接的深度超过了就不加入队列
						if url_depth + 1 <= self.crawl_depth: 
							self.url_queue.put(new_urls_str, url_depth+1)
							self.notifyAll()
						if self.frame != None:
							wx.CallAfter(self.frame.print_on_spider_grid, [self.getName(), url_str, spider_url.get_method(), url_depth] )
						#else:
						print self.getName() +" url:" + url_str + " depth:" + str(url_depth)
						self.outputer.collect_urls(new_urls_str)
					except Exception:
						print "爬虫错误！"
					finally:
						if SpiderMain.wait_thread_num < SpiderMain.thread_num:
							SpiderMain.wait_thread_num += 1
							if SpiderMain.wait_thread_num > 0:
								self.notifyAll()

	def wait(self):
		self.con.acquire()
		self.con.wait()
		self.con.release()

	def notifyAll(self):
		self.con.acquire()
		self.con.notifyAll()
		self.con.release()


class SpiderMain:
	"""
	爬虫的控制主类
	"""

	def __init__(self, frame, root_url, thread_num, crawl_depth):
		self.frame = frame
		self.root_url = root_url
		self.crawl_depth = crawl_depth

		SpiderMain.thread_num = thread_num
		SpiderMain.wait_thread_num = thread_num
		SpiderMain.stoped = False
		self.con = threading.Condition()

		self.url_queue = UrlQueue(root_url)
		self.threads = []
		
	def crawling(self):
		"""
		初始化线程爬取
		"""
		for x in range(SpiderMain.thread_num):
			t = SpiderThread(self.frame, self.crawl_depth, self.url_queue, self.con)
			self.threads.append(t)
			t.start()

		# 启动一个线程检测所有线程，当所有完成工作后提示
		thread.start_new_thread(self.check_done,())


	def stop(self):
		"""
		停止
		"""
		SpiderMain.stoped = True

	def all_is_done(self):
		"""
		所有线程是否都完成工作
		"""
		# 如果有线程还活着那么返回False
		for t in self.threads:
			if t.is_alive():
				return False
		return True

	def check_done(self):
		"""
		检查是否所有线程都完成工作
		"""
		while 1:
			if self.all_is_done():
				break
		self.frame.confirm_dialog(u"爬取完成！")

if __name__ == '__main__':
	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
	crawl_depth = 2
	thread_num = 5
	con = threading.Condition()
	spider_main = SpiderMain(None, root_url, thread_num, crawl_depth)
	spider_main.crawling()