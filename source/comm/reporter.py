# -*- coding: utf-8 -*-

import os
import time

class Reporter:
	"""
	用于报告输出，以当前时间为文件名，输出到report目录下
	"""
	def __init__(self):

		self.file_name = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
		self.report_path = "../report"
		self.file = open(os.path.join(self.report_path, self.file_name), "w")

	def write(self, result_tuple):
		self.file.write("\n***********************************************************\n")
		self.file.write("请求类型：{0[0]}\n存在漏洞的URL：{0[1]}\n存在漏洞的参数：{0[2]}".format(result_tuple))
		self.file.write("\n***********************************************************\n")

	def close_file(self):
		self.file.close()


if __name__ == '__main__':

	reporter = Reporter()
	result_tuple = ("POST", "http://www.baidu.com", "id")
	for i in range(10):
		reporter.write(result_tuple)

	reporter.close_file()



