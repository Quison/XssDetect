# -*- encoding: utf-8 -*-
import requests
import sys
sys.path.append(r"../comm")

import authentication_login


class TestLogin(object):

	def __init__(self):
		pass

	def download(self,url):
		r = authentication_login.LOGIN_SESSION.get(url)
		print r.content
		

'''

url = "http://127.0.0.1/cms/admin/index.php"
a = TestLogin()
a.download(url)



'''
