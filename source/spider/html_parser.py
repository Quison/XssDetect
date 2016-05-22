#! /usr/bin/env python
#_*_coding:utf-8_*_

import sys
from lxml import etree
import string
import random

import urlparse

from lxml.html import fromstring, tostring
from spider_url import SpiderUrl


reload(sys)
sys.setdefaultencoding( "utf-8" )

class HtmlParser(object):

	def __init__(self):
		pass

	def _get_new_urls(self, spider_url, lxml_html):
		"""
		解析get类型的url
		"""
		spider_url_set = set()
		# 获取解析的url的链接和深度
		url_str = spider_url.get_url()
		url_depth = spider_url.get_depth()

		url_node = lxml_html.xpath(u"//a/@href")
		url_frame = lxml_html.xpath(u"//frame")
		if url_node:
			for url in url_node:
				new_url_str = urlparse.urljoin(url_str,url)

				# 创建一个spider_url，深度为原来的深度加1
				new_spider_url = SpiderUrl(new_url_str, url_depth+1, "get")
				spider_url_set.add(new_spider_url)

		if url_frame:
			for url in url_frame:
				new_url = url.get('src')
				new_url_str = urlparse.urljoin(url_str,new_url)
				new_spider_url = SpiderUrl(new_url_str, url_depth+1, "get")
				spider_url_set.add(new_spider_url)

		return spider_url_set

	# 函数对post表单form进行解析，返回url以及参数data
	# 注意 html_cont 传入的参数为requests请求的源码，应该为response.text
	def _post_new_urls(self, spider_url, html_cont):
		"""
		解析post类型的url
		"""
		
		spider_url_set = set()
		url_str = spider_url.get_url()
		url_depth = spider_url.get_depth()
		parameters = ""
		html_page = fromstring(html_cont.lower())
		for form in html_page.forms:
			new_url_str = urlparse.urljoin(url_str, form.action)
			url_method = form.method

			for element in form.iter():
				if element.tag == 'input':

					if element.type == 'text' or element.type == 'password':
						if element.name is not None:
							_input = element.name+'='+("".join(random.sample(string.ascii_lowercase, 5)))
							parameters = parameters + _input + '&'
					if element.type == 'checkbox':
						if element.name is not None:
							checkbox = element.name + '=' + 'on'
							parameters = parameters + checkbox + '&'
					if element.type == 'radio':
						radio = element.attrib['name'] + '=' + element.attrib['value']
						parameters = parameters + radio + '&'

				if element.tag == 'textarea':
					if element.name is not None:
						textarea = element.name+'='+("".join(random.sample(string.ascii_lowercase, 5)))
						parameters = parameters + textarea + '&'

				if element.tag == 'select':
					if element.name is not None:
						select = element.name
						for x in element.getchildren():
							pass
						parameters = parameters + select + '=' + x.attrib['value'] + '&'

				url_parameters = parameters[:-1]

			new_spider_url = SpiderUrl(new_url_str, url_depth+1, "post", url_parameters)

			spider_url_set.add(new_spider_url)

		return spider_url_set



	def parse(self, spider_url, html_cont):	
		
		if spider_url is None or html_cont is None:
			return

		lxml_html = etree.HTML(html_cont)
		get_spider_url_set = self._get_new_urls(spider_url,lxml_html)
		post_spider_url_set = self._post_new_urls(spider_url,html_cont)

		# 返回他们的并集
		return get_spider_url_set|post_spider_url_set

