#_*_coding:utf-8_*_

import re
import Queue

from spider_url import SpiderUrl


class UrlManager(object):
	# 待爬取的数据不限长度
	_new_urls = Queue.Queue(maxsize = -1)

	# url过滤器
	_url_filter = set()

	# 已爬取过的url
	_old_urls = set()

	_domain = None

	def __init__(self):
		pass

	@staticmethod
	def add_new_url(spider_url):
		"""
		将连接添加到带爬取队列中并设置过滤器
		"""
		if (UrlManager._domain is None) or (spider_url is None):
			return

		url_str = spider_url.get_url_str()
		new_domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",url_str,re.M|re.I)
		if url_str not in UrlManager._url_filter and new_domain and (new_domain.group()==UrlManager._domain):
			# 将url添加到带待爬取的url队列
			UrlManager._new_urls.put(spider_url)
			# 同时将url添加到过滤器
			UrlManager._url_filter.add(url_str)

	@staticmethod
	def add_new_urls(urls_str, depth):
		"""
		批量添加新链接
		"""
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
	def init_spider(root_url):
		"""
		初始化爬虫
		"""	
		UrlManager.add_new_url(SpiderUrl(root_url, 0))
		UrlManager._domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",root_url,re.M|re.I).group()
		print "初始化"

	@staticmethod
	def reset_spider():
		"""
		重置爬虫设置
		"""
		# 清空待爬取链接列表
		while not(UrlManager._new_urls.empty()):
			UrlManager._new_urls.get()

		# 重置过滤器
		UrlManager._url_filter.clear()
		# 清空已爬取的url队列
		UrlManager._old_urls.clear()