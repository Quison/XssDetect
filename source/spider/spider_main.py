#_*_coding:utf-8_*_

import url_manager
import html_downloader
import html_parser
import html_outputer
import threading
import sys  
import re

from url_manager import UrlManager
from spider_url import SpiderUrl

class SpiderMain(object):
	
	def __init__(self, crawl_depth):
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		self.crawl_depth = crawl_depth
		self.stoped = False
		self.timeout = 3
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

	def stop_crawl(self):
		self.stoped = True

		print "停-------->",self.stoped

	def craw(self):
		while 1:
			if not(UrlManager.has_new_url()) or self.stoped:
				break
				
			# 从队列中获取一个待爬取的新连接
			spider_url = UrlManager.get_new_url()

			url_str = spider_url.get_url_str()
			url_depth = spider_url.get_url_depth()

			# 如果url的深度超过或等于爬取的深度那么跳过爬下一个
			if url_depth > self.crawl_depth:
				continue

			yield "url:" + url_str + " depth:" + str(url_depth)
			html_cont = self.downloader.download(url_str,headers=self.headers,timeout=self.timeout)
				
			# 将解析得的url放入带爬取链接队列中深度+1
			new_urls_str = self.parser.parse(url_str,html_cont)

			UrlManager.add_new_urls(new_urls_str, url_depth+1)

			self.outputer.collect_urls(new_urls_str)

			

