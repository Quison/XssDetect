# -*- encoding: utf-8 -*-

import sqlite3
import requests
from lxml import etree
import lxml.html
import urlparse

'''
sql_worker = Sqlite3Worker('test.db')
sql_worker.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
sql_worker.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
sql_worker.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','RHAT',100,35.14)")

result = sql_worker.execute("select date from stocks")
print type(result)



l = [1,2,3,4,5,6,7,8]
s = set(l)
print s
print type(s)
if 3 in s:
	print "in"

'''

url = "http://192.168.204.242/cms/index.php"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
timeout = 3

r = requests.get(url,headers=headers,timeout=timeout)
if r.status_code == requests.codes.ok:
	html = r.text	

lxml_html = etree.HTML(html)

hrefs = lxml_html.xpath(u"//a/@href")
for new_url in hrefs:
	new_full_url = urlparse.urljoin(url,new_url)
	print new_full_url



#form = lxml_html.xpath(u"//form")
#for f in form:
#	print f[0].tag

#qq = etree.Element("form")
#print etree.SubElement
#	textarea 
#	input	type="radio"	type="button" type="text"	type="password"	type="checkbox"	type="radio"
#	select	option 

