#_*_coding:utf-8_*_

import sys  
import time
import threading
import thread
import wx
import traceback

import html_downloader
import html_parser
import html_outputer

from spider_url import SpiderUrl
from url_queue import UrlQueue
			
class SpiderThread(threading.Thread):
	"""
	爬虫的线程类
	"""

	def __init__(self, name, frame, url_queue, con, outputer, crawl_depth, login_session):

		threading.Thread.__init__(self)
		# 线程名
		self.name = name
		# 初始化参数
		self.frame = frame

		#初始化爬虫
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = outputer
		self.url_queue = url_queue
		self.con = con
		self.crawl_depth = crawl_depth
		self.login_session = login_session

		self.timeout = 3
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

	def run(self):
		while 1:
			print "空闲",SpiderMain.wait_thread_num
			print "空",self.url_queue.is_empty()
			if SpiderMain.stoped:
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
						# 下载
						html_cont = self.downloader.download(spider_url, headers=self.headers, timeout=self.timeout, login_session=self.login_session)	
						# 将解析得的url放入带爬取链接队列中深度已经+1
						spider_url_set = self.parser.parse(spider_url,html_cont)
						
						# 将已爬取的这个spider_url写入数据库
						self.outputer.write_date(spider_url)

						if(spider_url.get_depth() + 1 <= self.crawl_depth):
							# 加锁
							self.con.acquire()
						
							# 如果深度如果连接的深度超过了就不加入队列
							self.url_queue.put(spider_url_set)
							# 唤醒因为队列为空而等待的线程
							self.con.notifyAll()
							self.con.release()

						if self.frame != None:
							wx.CallAfter(self.frame.print_on_spider_grid, [self.getName(), spider_url.get_url(), spider_url.get_method(), spider_url.get_depth()] )
						else:
							print self.getName() +" url:" + spider_url.get_url() + " depth:" + str(spider_url.get_depth()) + " method:" + spider_url.get_method()
					except Exception, e:
						print traceback.format_exc()
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

	def __init__(self, frame, root_url, thread_num, crawl_depth, login_session):
		self.frame = frame
		self.root_url = root_url
		self.crawl_depth = crawl_depth

		SpiderMain.thread_num = thread_num
		SpiderMain.wait_thread_num = thread_num
		SpiderMain.stoped = False
		self.con = threading.Condition()

		self.url_queue = UrlQueue(root_url)
		self.outputer = html_outputer.HtmlOutputer()
		self.crawl_depth = crawl_depth
		self.login_session = login_session

		self.threads = []
		
	def crawling(self):
		"""
		初始化线程爬取
		"""
		for x in range(SpiderMain.thread_num):
			t = SpiderThread("Thread-"+str(x+1), self.frame, self.url_queue, self.con, self.outputer, self.crawl_depth, self.login_session)
			self.threads.append(t)
			t.start()

		# 启动一个线程检测所有线程，当所有完成工作后提示
		thread.start_new_thread(self.check_done,())

	def stop(self):
		"""
		停止
		"""
		self.frame.start_crawling_button.SetLabel(u"正在停止")
		self.frame.start_crawling_button.Enable(False)
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
		if self.frame is not None:
			self.frame.start_crawling_button.Enable(True)
			self.frame.start_crawling_button.SetLabel(u"开始爬取")
			self.frame.confirm_dialog(u"爬取完成！")
			
		else:
			print u"所有线程都完成工作。。。"

		# 睡眠三秒再关闭数据库连接，不然有些线程没写完会引发异常
		time.sleep(3)
		self.outputer.close_sql_worker()

if __name__ == '__main__':
	root_url = "http://127.0.0.1/cms/"
	crawl_depth = 43
	thread_num = 1
	con = threading.Condition()
	spider_main = SpiderMain(None, root_url, thread_num, crawl_depth, None)
	spider_main.crawling()