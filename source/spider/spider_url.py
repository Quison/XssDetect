#_*_coding:utf-8_*_

class SpiderUrl:
	"""
	爬虫的简单对象，存储url以及其对应的深度
	"""
	def __init__(self, url_str, url_depth):
		self.url_str = url_str
		self.url_depth = url_depth

	def get_url_str(self):
		return self.url_str

	def set_url_str(self, url_str):
		self.url_str = url_str

	def get_url_depth(self):
		return self.url_depth

	def set_url_depth(self, url_depth):
		self.url_depth = url_depth