#_*_coding:utf-8_*_

import lxml.html
from lxml import etree
import requests
import string,random
from StringIO import StringIO

from lxml.html import fromstring, tostring
html = '''
<html>
<body>
    <form method="POST" name="form2" action="/bar">
        <input type="text" name="firstInput" />
        <input type="text" name="secondInput" />
        <input type="password" name="password">
        <input type="checkbox" name="Car">
        <select name="cars">
			<option value="volvo">Volvo</option>
			<option value="saab">Saab</option>
			<option value="fiat">Fiat</option>
		</select>
		<input type="radio" name="Sex" value="Female">
		<textarea name="content" id="content" ></textarea>
    </form>
</body>
</html>
'''
HTML = StringIO("""
<html>
<body>
    <form method="POST" name="form2" action="/bar">
        <input type="text" name="firstInput" />
        <input type="text" name="secondInput" />
        <input type="password" name="password">
        <input type="checkbox" name="Car">
        <select name="cars">
			<option value="volvo">Volvo</option>
			<option value="saab">Saab</option>
			<option value="fiat">Fiat</option>
		</select>
		<input type="radio" name="Sex" value="Female">
		<textarea name="content" id="content" ></textarea>
		<input type="submit" value="send">
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
			print field.style
			field_info = {} # 参数所有字段信息字典
			field_info['name'] = field.name
#			field_info['type'] = field.type
			postparameter.append(field_info)
		
		postdata['parameters'] = postparameter
		postdata_list.append(postdata)
	return postdata_list

url = "http://127.0.0.1/cms/message.php"
#qq = _post_new_urls(url,HTML)
#print qq

page = fromstring(html.lower().decode('utf-8'))
parameters = ""
for form in page.forms:
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
print parameters

#firstInput=222&secondInput=333&password=444&Car=on&cars=fiat&Sex=Female&content=555