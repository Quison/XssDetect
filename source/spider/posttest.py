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
qq = _post_new_urls(url,HTML)
print qq