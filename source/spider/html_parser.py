#! /usr/bin/env python
#_*_coding:utf-8_*_

from lxml import etree
import lxml.html
from StringIO import StringIO
import urlparse
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class HtmlParser(object):

	def __init__(self):
		pass

	def _get_new_urls(self,page_url,lxml_html):
		new_urls = set()

		url_node = lxml_html.xpath(u"//a/@href")
		for url in url_node:
			new_full_url = urlparse.urljoin(page_url,url)
			new_urls.add(new_full_url)

		return new_urls

	# 函数对post表单form进行解析，返回url以及参数和类型
	def _post_new_urls(self,page_url,html_cont):
		HTML = StringIO(html_cont)
		tree = lxml.html.parse(HTML)
		root = tree.getroot()

		postdata = {} # 最后返回的整个字典

		for form in root.xpath('//form'):
			
			field_info = {} # 参数所有字段信息字典
			postparm = [] # 参数list

			postdata['method'] = form.method
			postdata['action'] = form.action
			for field in form.getchildren():
				field_info['name'] = field.name	#参数名称
				field_info['type'] = field.type	#参数类型，常见为input类型
				postparm.append(field_info)
			postdata['parm'] = postparm
			
		return postdata


	def parse(self, page_url, html_cont):	
		
		if page_url is None or html_cont is None:
			return

		lxml_html = etree.HTML(html_cont)
		new_urls = self._get_new_urls(page_url,lxml_html)
#		new_urls = self._post_new_urls(page_url,html_cont)
		return new_urls
