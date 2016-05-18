#_*_coding:utf-8_*_

import sys  
import re
import time
import threading
import Queue
import wx

import html_downloader
import html_parser
import html_outputer


from spider_url import SpiderUrl
			
class SpiderThread(threading.Thread):
	"""
	爬虫的多线程（由于需要给界面反馈信息，所以需要定制）
	"""

	def __init__(self, frame, crawl_depth, url_manager, con):

		threading.Thread.__init__(self)
		# 初始化参数
		self.frame = frame

		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()

		#初始化爬虫

		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		self.crawl_depth = crawl_depth
		self.url_manager = url_manager
		self.con = con

		self.stoped = False
		self.timeout = 3
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

	def stop(self):
		self.stoped = True
		self.timeToQuit.set()


	def run(self):
		while 1:
			print "等待线程数",UrlManager.wait_thread_num;
			print "是否为空",self.url_manager.new_url_empty()
			if self.stoped :
				break			
			# 当队列为空时，默认当做还有其他线程正在工作，等待3秒，如果3秒过后还为空则超时退出
			if self.url_manager.new_url_empty() and (UrlManager.thread_num == UrlManager.wait_thread_num):
				print "退出"
				break
			else:
				#print "空闲线程：",UrlManager.wait_thread_num
				#print "队列是否为空：",self.url_manager.new_url_empty()
				if self.url_manager.new_url_empty() :
					#print "空等"
					self.con.acquire()
					self.con.wait()
					self.con.release()
				elif UrlManager.wait_thread_num == 0:
					#print "无线程等"
					self.con.acquire()
					self.con.wait()
					self.con.release()
				else:
					UrlManager.wait_thread_num -= 1
					try:
						spider_url = self.url_manager.get_new_url()
						url_str = spider_url.get_url_str()
						url_depth = spider_url.get_url_depth()

						# 如果url的深度超过或等于爬取的深度那么跳过爬下一个
						if url_depth > self.crawl_depth:
							continue
						html_cont = self.downloader.download(url_str,headers=self.headers,timeout=self.timeout)
				
						# 将解析得的url放入带爬取链接队列中深度+1
						new_urls_str = self.parser.parse(url_str,html_cont)
						if url_depth + 1 <= self.crawl_depth: 
							self.url_manager.add_new_urls(new_urls_str, url_depth+1)
						print self.getName() +" url:" + url_str + " depth:" + str(url_depth)
						wx.CallAfter(self.frame.print_on_spider_grid, [self.getName(), url_str, "get", url_depth] )
						self.outputer.collect_urls(new_urls_str)
						
					except Exception:
						print "爬虫错误！"
					finally:
						if UrlManager.wait_thread_num < UrlManager.thread_num:
							UrlManager.wait_thread_num += 1
							if UrlManager.wait_thread_num > 0:
								self.con.acquire()
								self.con.notifyAll()
								self.con.release()

class UrlManager(object):
	"""
	url统一管理
	"""

	def __init__(self, thread_num, con):
		# 待爬取的数据不限长度
		self.new_url_queue = Queue.Queue(maxsize = -1)
		# url过滤器
		self.url_filter = set()
		# 已爬取过的url
		self.old_urls = set()
		self.domain = None

		UrlManager.thread_num = thread_num
		UrlManager.wait_thread_num = thread_num
		self.con = con
	
	def init_spider(self, root_url):
		self.new_url_queue.put(SpiderUrl(root_url, 0))
		self.domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",root_url,re.M|re.I).group()	

	def add_new_url(self, spider_url):
		"""
		将连接添加到带爬取队列中并设置过滤器
		"""
		if (self.domain is None) or (spider_url is None):
			return

		url_str = spider_url.get_url_str()
		new_domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",url_str,re.M|re.I)
		if url_str not in self.url_filter and new_domain and (new_domain.group()==self.domain):
			# 将url添加到带待爬取的url队列
			self.new_url_queue.put(spider_url)
			# 同时将url添加到过滤器
			self.url_filter.add(url_str)


	def add_new_urls(self, urls_str, depth):
		"""
		批量添加新链接
		"""
		if urls_str is None or len(urls_str) == 0:
			return

		self.con.acquire()
		for url_str in urls_str:
			self.add_new_url(SpiderUrl(url_str, depth))
		self.con.notifyAll()
		self.con.release()

	def new_url_empty(self):
		"""
		判断是否还有待爬取的链接
		"""
		return self.new_url_queue.empty()


	def get_new_url(self):
		# 获取带爬取的链接
		new_url = self.new_url_queue.get()
		# 将连接添加到已爬取的连接
		self.old_urls.add(new_url)
		return new_url


	def reset_spider(self):
		"""
		重置爬虫设置
		"""
		# 清空待爬取链接列表
		while not(self.new_url_queue.empty()):
			self.new_url_queue.get()

		# 重置过滤器
		self.url_filter.clear()
		# 清空已爬取的url队列
		self.old_urls.clear()


if __name__ == '__main__':
	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
	crawl_depth = 2
	thread_num = 5
	con = threading.Condition()
	url_manager = UrlManager(thread_num, con)
	url_manager.init_spider(root_url)
	for x in range(thread_num):
		t = SpiderThread(None,crawl_depth, url_manager, con)
		t.start()