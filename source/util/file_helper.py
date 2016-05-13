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
	def write_payload(content_str):
		"""
		保存内容到payload配置文件
		"""
		with open(FileHelper._PAYLOAD_FILE, "w") as config_file:
			config_file.write(content_str)

	@staticmethod
	def read_payload():
		"""
		读取payload文件存放到列表中
		"""
		f = open(FileHelper._PAYLOAD_FILE)
		payload = []
		for line in f:
			payload.append(line.strip())
		f.close()
		return payload_content

	@staticmethod
	def write_setting_info(setting_info_dict):
		"""
		保存内容到config配置文件
		"""
		with open(FileHelper._CONFIG_FILE, "w") as setting_file:
			for key in setting_info_dict.keys():
				setting_file.write("{0}={1}\n".format(key, setting_info_dict[key]))


	@staticmethod
	def read_setting_info():
		"""
		读取配置文件属性放到字典中
		"""
		f = open(FileHelper._CONFIG_FILE)
		setting_info_dict = {}
		for line in f:
			lst = line.split("=")
			setting_info_dict[lst[0]] = lst[1].strip() if len(lst) == 2 else ""
		f.close()
		return setting_info_dict
