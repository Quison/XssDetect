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

class SpiderMain(object):

	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self,root_url,headers,timeout,crawl_depth):
		domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",root_url,re.M|re.I).group()

		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				#print 'craw  %d:%s' %(crawl_depth,new_url)
				

				html_cont = self.downloader.download(new_url,headers=headers,timeout=timeout)
				new_urls = self.parser.parse(new_url,html_cont,domain)
#				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_urls(new_urls)

				crawl_depth = crawl_depth -1 
				if crawl_depth == 0:
					break
				
				yield new_url
			except Exception, e:
				print 'craw failed '
				print e

		self.outputer.insert_get_data()
#		print self.outputer.datas



if __name__ == '__main__':
#	root_url = "https://docs.python.org/3/library/sqlite3.html"
#	root_url = "http://192.168.204.242/cms/index.php"
	root_url = "http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
	timeout = 3
	crawl_depth = 15    # 爬虫深度，最多爬取crawl_depth这么多个链接地址
	obj_spider = SpiderMain()
#	obj_spider.craw(root_url,headers,timeout,crawl_depth)
	for x in range(5):
		t = threading.Thread(target=obj_spider.craw,args=(root_url,headers,timeout,crawl_depth))
		t.start()