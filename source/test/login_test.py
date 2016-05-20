# -*- coding: utf-8 -*-

import requests
import json
from PIL import Image
from StringIO import StringIO

class http_handler(object):

	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'}
		self.timeout = 2

	# payload = {'key1': 'value1', 'key2': 'value2'}  表示请求参数
	# http://httpbin.org/get?key2=value2&key1=value1  请求url
	# json.dumps(payload) 将直接吧dict作为参数，进行http请求
	def http_get(self,url,payload=None):
		r = requests.get(url,payload)
		if r.status_code == requests.codes.ok:
			i = Image.open(StringIO(r.content))
			i.save('jjj.jpg')

	#改变图片大小  http://blog.csdn.net/zhoujianghai/article/details/7974249
	def resize_img(self,img_path):  
		try:
			img = Image.open(img_path)
			(width,height) = img.size
			new_width = 200
			new_height = height * new_width / width
			out = img.resize((new_width,new_height),Image.ANTIALIAS)
			ext = os.path.splitext(img_path)[1]
			new_file_name = '%s%s' %('small',ext)
			out.save(new_file_name,quality=95)
		except Exception,e:
			print e 



	def http_post(self,url,data=None):
		r = requests.post(url,data,allow_redirects=False,timeout=self.timeout)
		if r.status_code == requests.codes.ok:
#			print r.url
#			print r.headers
#			print r.cookies
			print r.request.headers




#url = "http://192.168.14.44:88/kuc/kuc_validate?uuid=1463645441299-32000016"
url = "http://192.168.204.242/cms/admin/login.php"
data = {'username': 'admin', 'password': '111111','image.x':'41','image.y':'36'}
login_url = "http://192.168.204.242/cms/admin/index.php"

session = requests.Session()
session.post(url,data=data)

r = session.get(login_url)
print r
print r.cookies

#http = http_handler()
#http.http_post(url,data)

