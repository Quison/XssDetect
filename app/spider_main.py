#! /usr/bin/env python
#_*_coding:utf-8_*_

#from baike_spider import url_manager,html_downloader,html_parser,html_outputer
'''
	one url one process
'''

import url_manager
import html_downloader
import html_parser
import html_outputer
import sys  

class SpiderMain(object):

	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self,root_url,headers,timeout):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():

			try:
				new_url = self.urls.get_new_url()
				print 'craw  %d:%s' %(count,new_url)

				html_cont = self.downloader.download(new_url,headers=headers,timeout=timeout)

				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)

				if count == 25:
					break
				count = count + 1

			except Exception, e:
				print 'craw failed '
				print e

		self.outputer.output_html()



if __name__ == '__main__':
	root_url = "https://movie.douban.com/subject/1849031/"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
	timeout = 3
	obj_spider = SpiderMain()
	obj_spider.craw(root_url,headers,timeout)

