#_*_coding:utf-8_*_

import Queue
from spider_url import SpiderUrl

class UrlManager(object):
	# 待爬取的数据不限长度
	_new_urls = Queue.Queue(maxsize = -1)

	# url过滤器
	_url_filter = set()

	# 已爬取过的url
	_old_urls = set()

	def __init__(self):
		pass
		#self.new_urls = set()
		#self.old_urls = set()
		
		#list 转换为set，保持原来的程序，转换方式为
		#
		#  l = [1,2,3,4,5,6,7,8]
		#  s = set(l)
		#  就这样类似强制类型转换。一旦数据量非常大的话，list索引就会很耗时
		#  这样子也不是很好，后面解析之后存储新的URL，也不是很好，所以还是用直接查询数据库的方式吧。

	@staticmethod
	def add_new_url(spider_url):
		if spider_url is None:
			return

		url_str = spider_url.get_url_str()
		if url_str not in UrlManager._url_filter:
			# 将url添加到带待爬取的url队列
			UrlManager._new_urls.put(spider_url)
			# 同时将url添加到过滤器
			UrlManager._url_filter.add(url_str)

	@staticmethod
	def add_new_urls(urls_str, depth):
		if urls_str is None or len(urls_str) == 0:
			return

		for url_str in urls_str:
			UrlManager.add_new_url(SpiderUrl(url_str, depth))

	@staticmethod
	def has_new_url():
		"""
		判断是否还有待爬取的链接
		"""
		return not(UrlManager._new_urls.empty())

	@staticmethod
	def get_new_url():
		# 获取带爬取的链接
		new_url = UrlManager._new_urls.get()

		# 将连接添加到已爬取的连接
		UrlManager._old_urls.add(new_url)

		return new_url

	@staticmethod
	def clear_all_data():
		# 清空待爬取链接列表
		while not(UrlManager._new_urls.empty()):
			UrlManager._new_urls.get()

		# 重置过滤器
		UrlManager._url_filter.clear()

		# 清空以爬取的url队列
		UrlManager._old_urls.clear()

	@staticmethod
	def init_spider(root_url):
		UrlManager.add_new_url(SpiderUrl(root_url, 0))