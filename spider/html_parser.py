#! /usr/bin/env python
#_*_coding:utf-8_*_

from lxml import etree

class HtmlParser(object):

	def __init__(self):
		pass
	
	# get new urls (recommends)

	def _get_new_urls(self,page_url,lxml_html):
		new_urls = set()

		url_node = lxml_html.xpath(u"//a")
		for url in url_node:
			new_urls.add(url.attrib['href'])

		return new_urls

	# get data (url,name,year,score,type)
	def _get_new_data(self,page_url,lxml_html):

		res_data = {}
		res_data['url'] = page_url

		name_node = lxml_html.xpath(u"//*[@id='content']/h1/span")
		res_data['name'] = name_node[0].text
		res_data['year'] = name_node[1].text	

		score_node = lxml_html.xpath(u"//*[@id='interest_sectl']/div[1]/div[2]/strong")
		res_data['score'] = score_node[0].text

		return res_data


	def parse(self, page_url, html_cont):	
		
		if page_url is None or html_cont is None:
			return

		lxml_html = etree.HTML(html_cont)

		new_urls = self._get_new_urls(page_url,lxml_html)
		new_data = self._get_new_data(page_url,lxml_html)

		return new_urls,new_data
