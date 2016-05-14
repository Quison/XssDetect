# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class CommonUtil:

	def __init__(self):
		pass

	@staticmethod
	def get_dict_value(adict, key):
		"""
		判断配置文件中是否存在key，
		如果存在着返回vlaue否则返回默认值
		"""
		if key in adict:
			return adict[key]
		else:
			return ""