# -*- coding: utf-8 -*- 

import sys

import requests

reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append(r"../util")

from file_helper import FileHelper
from common_util import CommonUtil

class Authentication:

	def __init__(self):
		pass

	def get_vercode(self, vercode_url):
		pass

	@staticmethod
	def login():
		"""
		读取配置信息登录
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

		r = requests.post(login_url, params = post_data)

		cookies = r.cookies

		print cookies