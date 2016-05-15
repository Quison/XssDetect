#_*_coding:utf-8_*_

#from spider import url_manager,html_downloader,html_parser,html_outputer
'''
	one url one process
'''

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

	
	

	def __init__(self):
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

		# 用于控制停止爬取
		self.is_end_crawl = False


	def set_end_crawl(self, aboolean):
		self.is_end_crawl = aboolean


	def craw(self, root_url,headers,timeout,crawl_depth):
		domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",root_url,re.M|re.I).group()
		while UrlManager.has_new_url() and not(self.is_end_crawl):
			try:
				# 从队列中获取一个待爬取的新连接
				spider_url = UrlManager.get_new_url()
				url_str = spider_url.get_url_str()
				url_depth = spider_url.get_url_depth()

				# 如果url的深度超过或等于爬取的深度那么跳过爬下一个
				if url_depth > crawl_depth:
					continue

				html_cont = self.downloader.download(url_str,headers=headers,timeout=timeout)
				
				# 将解析得的url放入带爬取链接队列中深度+1
				new_urls_str = self.parser.parse(url_str,html_cont,domain)
				UrlManager.add_new_urls(new_urls_str, url_depth+1)
				self.outputer.collect_urls(new_urls_str)

				yield "url:" + url_str + " depth:" + str(url_depth)

			except Exception, e:
				print 'craw failed '
				print e

		self.outputer.insert_get_data()

# if __name__ == '__main__':
# #	root_url = "https://docs.python.org/3/library/sqlite3.html"
# #	root_url = "http://192.168.204.242/cms/index.php"
# 	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
# 	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
# 	timeout = 3
# 	crawl_depth = 3    # 爬虫深度，最多爬取crawl_depth这么多个链接地址
# 	obj_spider = SpiderMain()
# 	obj_spider.craw(root_url,headers,timeout,crawl_depth)
# #	for x in range(5):
# #		t = threading.Thread(target=obj_spider.craw,args=(root_url,headers,timeout,crawl_depth))
# #		t.start()