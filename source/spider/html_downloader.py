#_*_coding:utf-8_*_

import requests

class HtmlDownloader(object):

#	def __init__(self,headers):
#		self.headers = headers

	def download(self, spider_url, headers,timeout):
		url = spider_url.get_url()
		if url is None:
			return None
		try:
			r = requests.get(url,headers=headers,timeout=timeout)
			if r.status_code == requests.codes.ok:
				return r.content	
		except Exception, e:
			return None
		return None