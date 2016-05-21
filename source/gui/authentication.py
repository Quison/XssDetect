# -*- coding: utf-8 -*- 

import sys

import requests

reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append(r"../comm")

from file_helper import FileHelper
from common_util import CommonUtil

class Authentication:

	def __init__(self):
		pass

	@staticmethod
	def get_vercode(url):
		r = requests.get(url)
		print r.text

	@staticmethod
	def login():
		"""
		读取配置信息登录返回cookie
		"""
		# 读取配置文件
		adict = FileHelper.read_setting_info()

		# 构造post的数据
		post_data = {}
		post_data[CommonUtil.get_dict_value(adict, "username_key")] = CommonUtil.get_dict_value(adict, "username_value")
		post_data[CommonUtil.get_dict_value(adict, "password_key")] = CommonUtil.get_dict_value(adict, "password_value")
		post_data[CommonUtil.get_dict_value(adict, "vercode_key")] = CommonUtil.get_dict_value(adict, "vercode_value")
		
		# 获取登录连接
		login_url = CommonUtil.get_dict_value(adict, "login_url")

		session = requests.session()
		r = session.post(login_url, data = post_data)

		# 如果请求成功则返回cookie的内容
		if r.status_code == requests.codes.ok:
			return requests.utils.dict_from_cookiejar(session.cookies)

		else:
			return r.status_code

'''
	def save_vercode(self,url,payload=None):
		if os.path.exists('vercode.jpg'):
			os.remove('vercode.jpg')

		r = requests.get(url,payload)
		if r.status_code == requests.codes.ok:
			i = Image.open(StringIO(r.content))
			i.save('vercode.jpg')

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


if __name__ == '__main__':
	url = "http://www.zhihu.com/captcha.gif?r=1463383349155&type=login"
	Authentication.get_vercode(url)