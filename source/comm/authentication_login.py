# -*- encoding: utf-8 -*-
import requests
from PIL import Image
import os
from StringIO import StringIO

class Login(object):

	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
		self.timeout = 2
		self.login_session = requests.session()

	# 
	def do_login(self,url_befor, data, url_after):
		# 不管成不成功都会有一个只
		self.login_session.post(url_befor,data)

		r = self.login_session.get(url_after)
		
		# 登录成功则不处理
		if r.status_code == requests.codes.ok:
			self.login_session
			# 返回登录成功，且返回cookie
			return True,requests.utils.dict_from_cookiejar(self.login_session.cookies)
		else:
			#登录失败，把self.login_session设为None
			self.login_session = None
			# 返回失败，且返回错误码
			return False,r.status_code

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


	def get_login_session(self):
		return self.login_session;

	def do_logout(self):
		self.login_session = None



'''
url = "http://127.0.0.1/cms/admin/login.action.php"
para = "username=admin&password=123456"


login = Login()
param = login.modify_paramter(para)
login.do_login(url,param)


r = LOGIN_SESSION.get("http://127.0.0.1/cms/admin/index.php")
print r.text

'''