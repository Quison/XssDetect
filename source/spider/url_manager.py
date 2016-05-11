#_*_coding:utf-8_*_

class UrlManager(object):

	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()
		
		#list 转换为set，保持原来的程序，转换方式为
		#
		#  l = [1,2,3,4,5,6,7,8]
		#  s = set(l)
		#  就这样类似强制类型转换。一旦数据量非常大的话，list索引就会很耗时
		#  这样子也不是很好，后面解析之后存储新的URL，也不是很好，所以还是用直接查询数据库的方式吧。

	def add_new_url(self,url):
		if url is None:
			return

		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return

		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls)!= 0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)

		return new_url

