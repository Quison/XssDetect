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

class SpiderMain(object):

	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self,root_url,headers,timeout,count=15):
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print 'craw  %d:%s' %(count,new_url)

				html_cont = self.downloader.download(new_url,headers=headers,timeout=timeout)
				new_urls = self.parser.parse(new_url,html_cont)
#				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_urls)
				count = count -1 
				if count == 0:
					break

			except Exception, e:
				print 'craw failed '
				print e

#		self.outputer.output_html()
#		print self.outputer.datas



if __name__ == '__main__':
#	root_url = "http://192.168.204.242/cms/"
	root_url = "http://192.168.204.242/cms/index.php"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
	timeout = 3
	obj_spider = SpiderMain()
	obj_spider.craw(root_url,headers,timeout)
#	for x in range(5):
#		t = threading.Thread(target=obj_spider.craw,args=(root_url,headers,timeout,))
#		t.start()