#_*_coding:utf-8_*_

class SpiderUrl:
	"""
	爬虫的简单对象，存储url以及其对应的数据
	"""
	def __init__(self, url, depth, method='get', param=[]):
		self.__url = url
		self.__depth = depth
		self.__method = method
		self.__param = param

	def set_url(self, url):
		self.__url = url

	def get_url(self):
		return self.__url

	def set_depth(self, depth):
		self.__depth = depth

	def get_depth(self):
		return self.__depth

	def set_method(self, method):
		self.__method = method

	def get_method(self):
		return self.__method

	def set_param(self, param):
		self.__param = param

	def get_param(self):
		return self.__param

if __name__ == '__main__':
	spider_url = SpiderUrl("http://www.baidu.com", 2)
	print spider_url.get_url()
	print spider_url.get_depth()
	print spider_url.get_method()