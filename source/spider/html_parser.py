#! /usr/bin/env python
#_*_coding:utf-8_*_

from lxml import etree
#import lxml.html
import string
import random
from lxml.html import fromstring, tostring
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

	# 函数对post表单form进行解析，返回url以及参数data
	# 注意 html_cont 传入的参数为requests请求的源码，应该为response.text
	def _post_new_urls(self,page_url,html_cont):
		parameters = ""
		html_page = fromstring(html_cont.lower().decode('utf-8'))

		for form in html_page.forms:
			
			for element in form.iter():

				if element.tag == 'input':

					if element.type == 'text' or element.type == 'password':
						_input = element.name+'='+("".join(random.sample(string.ascii_lowercase, 5)))
						parameters = parameters + _input + '&'
					if element.type == 'checkbox':
						checkbox = element.name + '=' + 'on'
						parameters = parameters + checkbox + '&'
					if element.type == 'radio':
						radio = element.attrib['name'] + '=' + element.attrib['value']
						parameters = parameters + radio + '&'

				if element.tag == 'textarea':
					textarea = element.name+'='+("".join(random.sample(string.ascii_lowercase, 5)))
					parameters = parameters + textarea + '&'

				if element.tag == 'select':
					select = element.name
					for x in element.getchildren():
						pass
					parameters = parameters + select + '=' + x.attrib['value'] + '&'
		parameters = parameters[:-1]
		return page_url,parameters



	def parse(self, page_url, html_cont):	
		
		if page_url is None or html_cont is None:
			return

		lxml_html = etree.HTML(html_cont)
		new_urls = self._get_new_urls(page_url,lxml_html)
#		new_urls = self._post_new_urls(page_url,html_cont)
		return new_urls
