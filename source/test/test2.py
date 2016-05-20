# -*- encoding: utf-8 -*-
'''
登录模块
'''
import requests

LOGIN_SESSION = ""
#&image.x=68&image.y=37
#data = {"username":"admin","password":"123456"}
data = "username=admin&image.x=68&image.y=37&password=123456"
login_data = dict(username='admin',password='123456')
url = "http://192.168.204.242/cms/admin/login.action.php"

#http://192.168.204.242/cms/admin/index.php
s = requests.session()
s.post(url,data=login_data)

LOGIN_SESSION = s
r = LOGIN_SESSION.get("http://192.168.204.242/cms/admin/index.php")
print r.content

print type(s)
print type(LOGIN_SESSION)

class Login(object):
	def __init__(self):
		pass

	def do_login(self,url,data):
		pass