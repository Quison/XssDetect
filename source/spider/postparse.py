#_*_coding:utf-8_*_

import lxml.html
from lxml import etree
import requests

from StringIO import StringIO

HTML = StringIO("""
<html>
<body>
    <form method="POST" name="form1" action="/foo">
        <input name="uselessInput" type="text" />
    </form>
    <form method="POST" name="form2" action="/bar">
        <input name="firstInput" type="text" />
        <input name="secondInput" type="text" />
    </form>
</body>
</html>
""")


tree = lxml.html.parse(HTML)
root = tree.getroot()
for form in root.xpath('//form'):
	postdata = {}
	field_info = {}
	postparm = []

	postdata['method'] = form.method
	postdata['action'] = form.action
	for field in form.getchildren():
		field_info['name'] = field.name
		field_info['type'] = field.type
		postparm.append(field_info)
	postdata['parm'] = postparm
#	print postdata

def _post_new_urls(page_url,html_cont):
#	HTML = StringIO(html_cont)
	tree = lxml.html.parse(html_cont)
	root = tree.getroot()

	postdata = {} # 最后返回的整个字典
	
	for form in root.xpath('//form'):
		
		postparameter = [] # 参数list
		postdata['method'] = form.method
		postdata['action'] = form.action

		for field in form.getchildren():
			field_info = {} # 参数所有字段信息字典
			field_info['name'] = field.name
			field_info['type'] = field.type
			postparameter.append(field_info)
		
		postdata['parameters'] = postparameter
	print postdata
	return postdata

def _post_new_urls(page_url,HTML):
#	HTML = StringIO(html_cont)
	tree = lxml.html.parse(HTML)
	root = tree.getroot()

	#postdata = {} # 最后返回的整个字典
	postdata_list = []
	for form in root.xpath('//form'):
		postdata = {}
		postparameter = [] # 参数list
		postdata['method'] = form.method
		postdata['action'] = form.action

		for field in form.getchildren():
			field_info = {} # 参数所有字段信息字典
			field_info['name'] = field.name
			field_info['type'] = field.type
			postparameter.append(field_info)
		
		postdata['parameters'] = postparameter
		postdata_list.append(postdata)
	return postdata_list


url = "http://127.0.0.1/cms/message.php"
#r = requests.get("http://127.0.0.1/cms/message.php")
#html_cont = r.text
#print html_cont
qq = _post_new_urls(url,HTML)
print qq