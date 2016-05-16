#! /usr/bin/env python
#_*_coding:utf-8_*_

from lxml import etree
import urlparse
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class HtmlParser(object):

	def __init__(self):
		pass
	#	self.domain = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?",root_url,re.M|re.I).group()


	def _get_new_urls(self,page_url,lxml_html):
		new_urls = set()

		url_node = lxml_html.xpath(u"//a/@href")
		for url in url_node:
			new_full_url = urlparse.urljoin(page_url,url)
			new_urls.add(new_full_url)

		return new_urls

	def parse(self, page_url, html_cont):	
		
		if page_url is None or html_cont is None:
			return

		lxml_html = etree.HTML(html_cont)
		new_urls = self._get_new_urls(page_url,lxml_html)

		return new_urls
