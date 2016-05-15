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
	def get_vercode():
		r = requests.get("https://account.tophant.com/captcha")

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