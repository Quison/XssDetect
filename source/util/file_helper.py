# -*- coding: utf-8 -*-


class FileHelper:
	"""
	文件操作工具类
	"""
	_CONFIG_FILE = "../config/config.properties"
	_PAYLOAD_FILE = "../config/payload.properties"

	def __init__(self):
		pass
	@staticmethod
	def save_payload(content_str):
		"""
		保存内容到payload配置文件
		"""
		with open(FileHelper._PAYLOAD_FILE, "w") as config_file:
			config_file.write(content_str)

	@staticmethod
	def save_setting_info(setting_info_dict):
		"""
		保存内容到config配置文件
		"""
		with open(FileHelper._CONFIG_FILE, "w") as setting_file:
			for key in setting_info_dict.keys():
				setting_file.write("{0}={1}\n".format(key, setting_info_dict[key]))

