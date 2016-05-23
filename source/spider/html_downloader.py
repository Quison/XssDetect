#_*_coding:utf-8_*_

import requests
import sys
sys.path.append(r"../comm")
import authentication_login

#测试请求成功
#a = authentication_login.LOGIN_SESSION
#print a.get("http://127.0.0.1/cms/admin/index.php").content

class HtmlDownloader(object):

	def __init__(self):
		pass


	def download(self, spider_url, headers, timeout, login_session=None):
		url = spider_url.get_url()
		if url is None:
			return None
		try:
			#如果登录的session为None则使用原库的requests请求
			r = None
			if login_session is None:
				r = requests.get(url,headers=headers,timeout=timeout)
			else:
				r = login_session.get(url,headers=headers,timeout=timeout)
			if r.status_code == requests.codes.ok:
				return r.content	
		except Exception, e:
			return None
		return None