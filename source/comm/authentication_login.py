# -*- encoding: utf-8 -*-
import requests
from PIL import Image
import os
from StringIO import StringIO

global LOGIN_SESSION

class Login(object):

	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
		self.timeout = 2

	# 
	def do_login(self,url_befor, data, url_after):
		req = requests.session()
		r = req.post(url_befor,data)
		global LOGIN_SESSION
		LOGIN_SESSION = req

		#r = requests.get(url_after)
		
		if r.status_code == requests.codes.ok:
			#return True
			# 返回cookie
			return requests.utils.dict_from_cookiejar(req.cookies)
		else:
			return r.status_code

	def modify_paramter(self,paramter):
		paramter_dict = {}
		paramter_list = paramter.split('&')
		map(lambda x:paramter_dict.setdefault(x.split('=')[0], x.split('=')[1]), paramter_list)
		return paramter_dict

	def save_vercode(self,url,payload=None):
		r = requests.get(url,payload,timeout=2)
		if r.status_code == requests.codes.ok:
			if os.path.exists('../gui/images/vercode.png'):
				os.remove('../gui/images/vercode.png')
			i = Image.open(StringIO(r.content))
			i.save('../gui/images/vercode.png')
			return requests.codes.ok
		else:
			return r.status_code

	#改变图片大小  http://blog.csdn.net/zhoujianghai/article/details/7974249
	def resize_img(self,img_path):  
		try:
			img = Image.open(img_path)
			(width,height) = img.size
			new_width = 200
			new_height = height * new_width / width
			out = img.resize((new_width,new_height),Image.ANTIALIAS)
			ext = os.path.splitext(img_path)[1]
			new_file_name = '%s%s' %('new_vercode',ext)
			out.save(new_file_name,quality=95)
		except Exception,e:
			print e 



'''
url = "http://127.0.0.1/cms/admin/login.action.php"
para = "username=admin&password=123456"


login = Login()
param = login.modify_paramter(para)
login.do_login(url,param)


r = LOGIN_SESSION.get("http://127.0.0.1/cms/admin/index.php")
print r.text

'''