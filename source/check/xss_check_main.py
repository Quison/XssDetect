# -*- coding: utf-8 -*-

import sys
sys.path.append(r"../comm")
import os
import threading
import thread
import time
import wx
from xss_check import XssCheck
from sqlite3worker import Sqlite3Worker

reload(sys)
sys.setdefaultencoding( "utf-8" )

class XssCheckThread(threading.Thread):
	
	def __init__(self, name, frame, lock):
		threading.Thread.__init__(self)
		self.name = name
		self.stoped = False
		self.frame = frame
		self.xss_check = XssCheck()
		self.lock = lock

	def run(self):
		while 1:
			spiderurl = None
			if CheckMain.stoped:
				break
			if len(CheckMain.spiderurls) <= 0:
				break
			else:
				# 注记得加锁
				self.lock.acquire()
				spiderurl = CheckMain.spiderurls.pop()
				self.lock.release()

			if spiderurl is not None:
				# 注spiderurl为method,url,param的一个元组
				method = spiderurl[0]
				url = spiderurl[1]
				param = spiderurl[2]
				self.frame.checking_url_staticText.SetLabel(unicode(url))

				# DOM XSS 检测
				for result_tuple in self.xss_check.do_dom_xss_check(url):
					self.print_result(result_tuple)

				# GET XSS 检测
				if method is not None and (method.lower() == 'get'):
					# 测试打印对接
					#self.print_result(spiderurl)

					for result_tuple in self.xss_check.do_xss_check(url):
						self.print_result(result_tuple)
				
				elif (method is not None) and (method.lower() == 'post'):
					# 测试打印对接
					#self.print_result(spiderurl)

					if param is None:
						locktinue
					for result_tuple in self.xss_check.do_xss_check(url, param):
						self.print_result(result_tuple)

	def print_result(self, result_tuple):
		result_list = [self.getName()]
		result_list.extend(list(result_tuple))
		if self.frame is not None:
			wx.CallAfter(self.frame.print_on_check_grid, result_list)
		else:
			print result_list


class CheckMain(object):
	"""
	检测多线程调度类
	"""
	def __init__(self, frame, thread_num):
		self.frame = frame
		self.thread_num = thread_num
		CheckMain.stoped = False
		self.threads = []
		self.lock = threading.Lock()

		# 从数据库中查数据
		self.sql_worker = Sqlite3Worker("../config/spiderurls.db")
		CheckMain.spiderurls = self.sql_worker.execute("SELECT method,url,param from spiderurls")

	def checking(self):
		for i in range(self.thread_num):
			t = XssCheckThread("Thread-"+str(i+1), self.frame, self.lock)
			self.threads.append(t)
			t.start()

		# 启动一个线程检测所有线程，当所有完成工作后提示
		thread.start_new_thread(self.check_done,())

	def stop(self):
		CheckMain.stoped = True

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
			self.frame.confirm_dialog(u"检测完成！")
			if self.frame.start_check_button.GetLabel() == u"暂停检测":
				self.frame.start_check_button.SetLabel(u"开始检测")
		else:
			print u"所有线程都完成工作。。。"

		# 睡眠三秒再关闭数据库连接，不然有些线程没写完会引发异常
		time.sleep(3)
		self.sql_worker.close()

if __name__ == '__main__':
	check_main = CheckMain(None, 2)
	check_main.checking()
